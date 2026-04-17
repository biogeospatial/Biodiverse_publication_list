# Publication Website Link

https://biogeospatial.github.io/Biodiverse_publication_list/

# Publication List Explained

This repository includes a collection of scripts designed to generate an HTML publication list from data stored in a CSV file.

Biodiverse publication Workflow (Visualisation of CICD, also can be replicated locally if required. Instructions down further below):

![Biodiverse publication workflow](process-flowchart.png)

The csv file `publication-list.csv` is the source of where the DOIs come from. If this is changed, a script `generate_publication_bib_list.py` is automatically run to produce a `publication-list-biodiverse.bib` file. This script is derived from the `publist-wrangle.ipynb` notebook file. The notebook uses the `bibtexparser` library to parse the `publication-list.csv` to create the .bib file.

After this, quarto is run to produce a html file. Github expects a folder to publish from (`site/` in this case). This is why in the yml file, it creates a `site/` folder and moves the html to that folder.

The last script run is a additional file "add_pub_headers.py" which creates the headers that appear in the final HTML output file.

# Important information

### Updating the csv file `publication-list.csv`:

To add new DOIs, just add the doi as a new line entry into the `publication-list.csv` file. It does not matter what order you add the entry to in the file (Quarto uses Pandoc under the hood to handle citations and bibliography ordering), as long as each DOI entry is on its own line.

#### Column Order:

The CSV file must follow this exact column order:
`doi,note`
It is important you follow this order, where each value is separated by a comma (,). The doi field is required, the note field is optional. If there is no note, just end the line with a comma. An api is called that fetches all the information related to the doi. Hence, there is no manual work required to add all the other information in the csv file. Just the doi is necessary.

#### Missing Values (No note):

If a DOI (or any entry) does not have a value for a particular column, leave that column empty. For example:

`10.1234/abc,`

Here, there is no note field for this entry.

#### Handling Commas in Entries:

If a value itself contains a comma, enclose it in double quotation marks. For example:

`10.1234/abc,"Comma, inbetween"`

#### Signifying a DOI as either a "in press" or "preprint" option

The csv file has a column named note. Add either option "in press" or "preprint" to this column.

### What happens if CICD Automation fails

There is two options to this:

#### 1. Manually triggering CICD

The `render-publications.yml` workflow has included: `workflow_dispatch: {}`. This allows you to manually trigger the workflow button in the Actions tab anytime you want without commiting anything.

#### 2. Running Locally

Running it locally should always work. Make sure you have the following prerequisites files:

```
- "publication-list.csv"
- "generate_publication_bib_list.py"
- "publication-list.qmd"
- "global-ecology-and-biogeography.csl"
- "add_pub_headers.py"
```

Make sure correct dependencies are installed:

```
Sudo apt install python3-pip

pip install mistune pandas bibtexparser requests
```

Then run:

```
python3 generate_publication_bib_list.py
```

to generate the `publication-list-biodiverse.bib` bib file.

Then:

```
quarto render publication-list.qmd --to html
```

to create the `publication-list.html` html file. You should then be able to view this file as intended.

Finally run:

```
python add_pub_headers.py site/publication-list.html
```

This adds headers to the final HTML file.

## Dependencies

- Python 3.8+
- Quarto
- pandoc

This filter was created following [Quarto's documentation](https://quarto.org/docs/extensions/filters.html#filter-extensions).
