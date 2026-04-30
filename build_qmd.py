import re
import os
from pathlib import Path
from shutil import copyfile
import pandas as pd
import bibtexparser  #  !!!! v1 API needed at the moment
import subprocess
import yaml
from datetime import date

INPUT_CSV = "publication-list.csv"
OUTPUT_BIB = "publication-list-biodiverse.bib"

with open(OUTPUT_BIB, "r", encoding="utf-8") as bibfile:
    bib_database = bibtexparser.load(bibfile)

print(f"Loaded {len(bib_database.entries)} entries from {OUTPUT_BIB}")

df = pd.read_csv(INPUT_CSV)
has_notes = "note" in df.columns

csv_key_to_note = {}
for _, row in df.iterrows():
    key = str(row["doi"]).strip()
    if not key or key.startswith("#"):
        continue
    note_value = (
        str(row["note"]).strip() if has_notes and not pd.isna(row["note"]) else ""
    )
    if note_value.startswith("#"):
        note_value = ""
    csv_key_to_note[key] = note_value

bib_by_year = {}
for entry in bib_database.entries:
    entry_doi = entry.get("doi", "")
    note_value = csv_key_to_note.get(entry_doi) or csv_key_to_note.get(entry["ID"], "")

    year_val = entry.get("year", "").strip()
    if note_value == "":
        year_tag = "2011_and_earlier" if year_val <= "2011" else year_val
    else:
        year_tag = note_value.replace(" ", "_")

    db = bibtexparser.bibdatabase.BibDatabase()
    db.entries = [entry]
    formatted_entry = bibtexparser.dumps(db).strip()

    if year_tag not in bib_by_year:
        bib_by_year[year_tag] = []
    bib_by_year[year_tag].append(formatted_entry)

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

quarto_chapters = ["index.qmd"]

wd = "bib_by_year"
if not Path(wd).exists():
    Path(wd).mkdir()
os.chdir(wd)
csl_fname = "global-ecology-and-biogeography.csl"
if not Path(csl_fname).exists():
    copyfile(Path("..", csl_fname), csl_fname)

for year in bib_by_year:
    Path("..", year + ".qmd").touch()

for year, data in bib_by_year.items():
    if len(data) == 0:
        continue

    qmd_fname = year + ".qmd"
    qmd_fname_updir = Path("..", qmd_fname)

    quarto_chapters.append(qmd_fname)

    bib_name = year + ".bib"
    with open(bib_name, "w", encoding="utf-8") as bibfile:
        for entry in data:
            bibfile.write(entry + "\n\n")

    _fname = "_" + year + ".qmd"
    with open(_fname, "w", encoding="utf-8") as qmdfile:
        text = qmd_template.replace("YEAR_GOES_HERE", year)
        text = text.replace("YEAR GOES HERE", year.replace("_", " "))
        qmdfile.write(text)

    cmd = ["quarto", "render", _fname, "--to", "html"]
    # print(cmd)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("system call failed: " + str(result.returncode))
        print(result.stdout)
        print(result.stderr)

    htm_fname = "_" + year + ".html"
    cmd = ["pandoc", "-f", "html", "-t", "markdown", "-o", qmd_fname, htm_fname]
    # print(cmd)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("system call failed: " + str(result.returncode))
        print(result.stdout)
        print(result.stderr)

    lines = []
    with open(qmd_fname, "r", encoding="utf-8") as f:
        for line in f:
            line = line.replace(r" {#section .title}", "")
            if not line.startswith(":::"):
                lines.append(line)

    with open(qmd_fname, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(f"{line}")

    copyfile(qmd_fname, qmd_fname_updir)


def qmd_ch_processor(x):
    if x.startswith("index"):
        return "0"
    elif x.startswith("in_press"):
        return "1"
    elif x.startswith("preprint"):
        return "2"
    elif re.match(r"\d{4}", x):
        return str(3000 - int(x[0:4]))
    else:
        return x


quarto_config_f = Path("..", "_quarto.yml")
with open(quarto_config_f, "r", encoding="utf-8") as f:
    quarto_config = yaml.safe_load(f)

decorated = [(qmd_ch_processor(i), i) for i in quarto_chapters]
decorated.sort()
quarto_chapters = [v for k, v in decorated]
print(quarto_chapters)

quarto_config["book"]["date"] = str(date.today())
quarto_config["book"]["chapters"] = quarto_chapters
with open(quarto_config_f, "w", encoding="utf-8") as f:
    f.write(yaml.dump(quarto_config))
