import re
import os
import pandas as pd
import bibtexparser
import requests

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
curr_progress_count = 0

# === Step 3: Process each DOI ===
for index, row in df.iterrows():
    doi = str(row["doi"]).strip()
    note_value = (
        str(row["note"]).strip() if has_notes and not pd.isna(row["note"]) else ""
    )

    if not doi:
        continue

    try:
        response = requests.get(
            doi_url_base + doi, headers={"Accept": "application/x-bibtex"}, timeout=15
        )
        response.raise_for_status()
        raw_entry = response.text.strip()

        m = re.match(r"@(\w+)\s*{\s*([^,]+),", raw_entry)
        if m:
            entry_type = m.group(1)
            entry_id = m.group(2)
        else:
            entry_type = "article"
            entry_id = doi.replace("/", "_")

        fields = re.findall(r'(\w+)\s*=\s*[{"]([^}"]+)[}"],?', raw_entry)

        # Normalize formatting
        field_lines = []
        existing_keys = set()
        for key, value in fields:
            key = key.lower().strip()
            value = value.strip().replace("\n", " ")
            existing_keys.add(key)

            if key == "title":
                value = "{" + value + "}"

            field_lines.append(f"  {key:<10}= {{{value}}},")

        if note_value and "note" not in existing_keys:
            field_lines.append(f"  note       = {{{note_value}}},")

        if field_lines:
            field_lines[-1] = field_lines[-1].rstrip(",")

        formatted_entry = (
            f"@{entry_type}{{{entry_id},\n" + "\n".join(field_lines) + "\n}"
        )
        bibtex_entries.append(formatted_entry)

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
