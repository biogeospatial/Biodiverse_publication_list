import re
import mistune
import os
import pandas as pd
import bibtexparser
import requests

current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

# Specify the path to your .md file
file_path = "PublicationsList.md"

# Define output directory for BibTeX files
output_dir = os.path.join(current_directory, "generated_bib_lists")
os.makedirs(output_dir, exist_ok=True)

# Read the markdown file
with open(file_path, "r", encoding="utf-8") as md_file:
    content = md_file.read()

print(content)

# Parse Markdown content (not really used further, but kept here)
markdown = mistune.create_markdown()
parsed = markdown(content)
print(parsed)

# Extract DOIs from the markdown
urls = re.findall(r"https:\/\/doi\.org\/[0-9.]+\/[a-zA-Z0-9.]+", content)
print(urls)

urls_2 = re.findall(
    r"https:\/\/doi\.org\/[0-9.]+\/[a-zA-Z0-9.-]+(?:\/[a-zA-Z0-9.-]+)?", content
)

df = pd.DataFrame(urls_2, columns=["doi"])
print(df)

# Remove the URL part
dois = [re.findall(r"https:\/\/doi\.org\/([a-zA-Z0-9./-]+)", url) for url in urls_2]
dois = [item[0] for item in dois if item]  # Flatten and clean
print(dois)

# Base URL for DOI requests
doi_url_base = "https://doi.org/"

# Fetch and save BibTeX for each DOI (individual files)
# for doi in dois:
#     try:
#         response = requests.get(
#             doi_url_base + doi, headers={"Accept": "application/x-bibtex"}
#         )
#         response.raise_for_status()

#         bibtex_str = response.text
#         bibtex_data = bibtexparser.loads(bibtex_str)  # parses but not really used here

#         # Save individual BibTeX file
#         filename = os.path.join(output_dir, f"{doi.replace('/', '_')}.bib")
#         with open(filename, "w") as bibfile:
#             bibfile.write(bibtex_str)

#         print(f"Saved BibTeX for {doi} to {filename}")

#     except requests.exceptions.RequestException as e:
#         print(f"Failed to retrieve BibTeX for {doi}: {e}")
#     except Exception as e:
#         print(f"Failed to parse BibTeX for {doi}: {e}")

# Collect all BibTeX entries into one file
bibtex_entries = []
for doi in dois:
    try:
        response = requests.get(
            doi_url_base + doi, headers={"Accept": "application/x-bibtex"}
        )
        response.raise_for_status()
        bibtex_entries.append(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve BibTeX for {doi}: {e}")

all_entries_file = os.path.join(output_dir, "all_entries.bib")
with open(all_entries_file, "w") as bibfile:
    for entry in bibtex_entries:
        bibfile.write(entry + "\n\n")

print(f"All BibTeX entries saved to '{all_entries_file}'")

# Load and count entries
with open(all_entries_file) as bibfile:
    bib_database = bibtexparser.load(bibfile)

num_entries = len(bib_database.entries)
print(f"The number of entries in all_entries.bib is: {num_entries}")

num_doi = len(dois)
print(f"The number of DOIs from the markdown is: {num_doi}")
