import re
import os
from pathlib import Path
from shutil import copyfile
import pandas as pd
import bibtexparser
import requests
import subprocess

INPUT_CSV = "publication-list.csv"
OUTPUT_BIB = "publication-list-biodiverse.bib"

current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

# === Step 1: Load CSV ===
if not os.path.exists(INPUT_CSV):
    print(f"CSV file not found: {INPUT_CSV}")
    exit(1)

df = pd.read_csv(INPUT_CSV)
if "doi" not in df.columns:
    print("The CSV file must have a 'doi' column.")
    exit(1)

has_notes = "note" in df.columns
dois = df["doi"].dropna().astype(str).tolist()
print(f"----- Found {len(dois)} DOIs in {INPUT_CSV} -----")

# === Step 2: Prepare output directory ===
output_dir = os.path.join(current_directory)
os.makedirs(output_dir, exist_ok=True)

doi_url_base = "https://doi.org/"
bibtex_entries = []
entry_ids = []
curr_progress_count = 0

bib_by_year = {}

# === Step 3: Process each DOI ===
for index, row in df.iterrows():
    doi = str(row["doi"]).strip()
    note_value = (
        str(row["note"]).strip() if has_notes and not pd.isna(row["note"]) else ""
    )

    if not doi:
        continue
        
    #  skip commented lines
    if doi.startswith("#"):
        curr_progress_count += 1
        continue

    #  strip commented notes
    if note_value.startswith('#'):
        note_value = ""

    try:
        if doi.startswith("10."):
            response = requests.get(
                doi_url_base + doi, headers={"Accept": "application/x-bibtex"}, timeout=15
            )
            response.raise_for_status()
            raw_entry = response.text.strip()
        else:
            bib_no_doi = Path("bib_no_doi", doi + ".bib")
            with open(bib_no_doi, "r", encoding="utf-8") as bib:
                raw_entry = bib.read().strip()

        m = re.match(r"@(\w+)\s*{\s*([^,]+),", raw_entry)
        if m:
            entry_type = m.group(1)
            entry_id = m.group(2)
        else:
            entry_type = "article"
            entry_id = doi.replace("/", "_")

        if entry_id in entry_ids:
            entry_id = entry_id + "_" + str(entry_ids.count(entry_id))

        fields = re.findall(r'(\w+)\s*=\s*[{"]([^}"]+)[}"],?', raw_entry)
        
        #print (raw_entry)
        year_tag = ""

        # Normalize formatting
        field_lines = []
        existing_keys = set()
        for key, value in fields:
            key = key.lower().strip()
            value = value.strip().replace("\n", " ")
            existing_keys.add(key)

            if key == "title":
                value = "{" + value + "}"
            if key == "year":
                if note_value == "":
                    if value <= "2011":
                        year_tag = "2011_and_earlier"
                    else:
                        year_tag = value
                else:
                    year_tag = note_value.replace(" ", "_")

            field_lines.append(f"  {key:<10}= {{{value}}},")

        if note_value and "note" not in existing_keys:
            field_lines.append(f"  note       = {{{note_value}}},")

        if field_lines:
            field_lines[-1] = field_lines[-1].rstrip(",")

        formatted_entry = (
            f"@{entry_type}{{{entry_id},\n" + "\n".join(field_lines) + "\n}"
        )
        entry_ids.append(entry_id)

        bibtex_entries.append(formatted_entry)
        if not year_tag in bib_by_year:
            bib_by_year[year_tag] = []
        bib_by_year[year_tag].append (formatted_entry)

        curr_progress_count += 1
        print(f"✅ Processed DOI {doi} [{curr_progress_count}/{len(dois)}]")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Failed to retrieve BibTeX for {doi}: {e}")

# === Step 4: Write all entries to file ===
with open(OUTPUT_BIB, "w", encoding="utf-8") as bibfile:
    for entry in bibtex_entries:
        bibfile.write(entry + "\n\n")

print(f"All BibTeX entries saved to '{OUTPUT_BIB}'")

# === Step 5: Count entries ===
with open(OUTPUT_BIB, "r", encoding="utf-8") as bibfile:
    bib_database = bibtexparser.load(bibfile)

num_entries = len(bib_database.entries)
print(f"The number of entries in {OUTPUT_BIB}: {num_entries}")
print(f"The number of DOIs processed: {len(dois)}")


qmd_template = """
---
title: "YEAR GOES HERE"
bibliography: YEAR_GOES_HERE.bib
csl: global-ecology-and-biogeography.csl
nocite: |
  @*
---

::: {#refs}
:::
"""

#  work in a new dir so the config file has less impact
wd = "bib_by_year"
if not Path(wd).exists():
    Path.mkdir(wd)
os.chdir(wd) 
csl_fname = "global-ecology-and-biogeography.csl"
if not Path(csl_fname).exists():
    copyfile (Path("..", csl_fname), csl_fname)

for year in bib_by_year:
    #  we copy this file below but it needs to exist for the first render step
    Path("..", year + ".qmd").touch()

#  now dump to one file per year (or note)
for year, data in bib_by_year.items():
    if len(data) == 0:
        continue
    
    qmd_fname = year + ".qmd"
    qmd_fname_updir = Path("..", qmd_fname)

    bib_name = year + ".bib"
    with open(bib_name, "w", encoding="utf-8") as bibfile:
        for entry in data:
            bibfile.write(entry + "\n\n")
    
    _fname = "_" + year + ".qmd"
    with open (_fname, "w", encoding="utf-8") as qmdfile:
        text = qmd_template.replace("YEAR_GOES_HERE", year)
        text = text.replace("YEAR GOES HERE", year.replace("_", " "))
        qmdfile.write(text)

    #  convert to html
    cmd = ["quarto", "render", _fname, "--to", "html"]
    print (cmd)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print ("system call failed: " + str(result.returncode))
        print (result.stdout)
        print (result.stderr)
    
    #  now back to qmd
    htm_fname = "_" + year + ".html"
    cmd = ["pandoc", "-f", "html", "-t", "markdown", "-o", qmd_fname, htm_fname]
    print (cmd)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print ("system call failed: " + str(result.returncode))
        print (result.stdout)
        print (result.stderr)
    
    lines = []
    with open (qmd_fname, "r", encoding="utf-8") as f:
        for line in f:
            line = line.replace(r" {#section .title}", "")
            if not line.startswith(":::"):
                lines.append(line)

    with open (qmd_fname, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(f"{line}")

    copyfile (qmd_fname, qmd_fname_updir)
    