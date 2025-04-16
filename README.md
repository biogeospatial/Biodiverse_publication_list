# publist

This repository contains various scripts to produce a publication list from a .bib file. 

This `publication-list-biodiverse.bib` file was generated from using the `publist-wrangle.ipynb` notebook. The notebook uses the `bibtexparser` library to parse the `PublicationsList.mq` to create the .bib file.

## Dependencies
- Python 3.8+
- Quarto
- pandoc

The workflow for future publications repository is as follows:

1. Manually update the publication-list-biodiverse.bib, this does not need to be in any specific order. This step can also be automated in the future.

2. Using the `publication-list.qmd`, we can generate a .html of publication list.  Behind the scenes, Quarto uses pandoc to convert the .qmd file to .html. 

3. The `publication-list.qmd` file uses the `publication-list-biodiverse.bib` file to generate the publication list. The .qmd file is a Quarto document that uses the `pandoc-csl` filter to format the bibliography using a citation style language (CSL) file. The CSL used here is based on the Global Ecology and Biogeography (GEB) journal style with some modifications. 

4. The .csl contains modications to print out "(in press)" or "(preprint)" after the year for each reference. This are commented inside the .csl within the <bibliography> tag.

5. The .csl will also group references first by "in press" and then by "preprint". This is done by using the `sort` tag in the .csl file. The `sort` tag is set to "in press" and "preprint" to group the references accordingly

## Room for improvement
It is possible to create a header for "In Press", "Preprints", "Published"  using a .lua filter. Lua filters can be called within the Quarto doc using the `filters:` field in the yaml header. 

I've tried my best to implement this but with no luck. The actua lua filter is in `groupbib/_extensions/filters/groupbib.lua` 

This filter was created following [Quarto's documentation](https://quarto.org/docs/extensions/filters.html#filter-extensions). 