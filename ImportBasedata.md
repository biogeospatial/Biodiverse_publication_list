Table of contents:



This page explains the steps involved in importing Base Data into Biodiverse (up to step 2).

# Importing Base Data #
Biodiverse can import BaseData in one of two data formats, spreadsheet format or matrix format.  Examples of each format are provided in the data folder included with the Biodiverse download.

**Standard or spreadsheet format** is the more common data format.  An example is a dataset with one observation per row made up of columns for species and coordinates.  See Example\_site\_data.csv.

**Matrix format** is a matrix of data, with coordinates as the rows and species as the columns.  For example in a site by species matrix the value of each field is the count of observations for that site/species (group/label) pair.  See Example\_site\_data\_matrix\_form.csv.

Most of the import process is common for both data formats, but the specification of groups and labels differs.

**N.B.**  The Biodiverse sample data will be used throughout this tutorial.

## Importing a new BaseData object ##
This process will create a new Basedata object in the Biodiverse session.  To extend an existing dataset, see **Adding to an existing dataset.**

**Step 1**  Open Biodiverse.  Got to the Basedata menu or use the icons in the Basedata toolbar at the top of the screen.  Select ‘Import’ from the menu or the ‘add’ symbol from the ribbon.  The Import Data dialogue window will appear.  Select the file or files to be imported.  The text box at the top right of the window allows you to name the BaseData object that will be produced (as opposed to the default file name).

Once you are finished, click **Next**.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step1.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step1.png)

**N.B.**  Multiple files can be imported in the one process so long as they all share the same column order and meaning (the column names do not matter, only the contents).  If you have several files with different column orders then import each one separately into the same BaseData. If the data **were/was?** generated in R using the write.table() function then the system will detect this and allow for the missing column header for the row names.

**Step 2** The Import options dialogue window will then appear.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step2.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step2.png)

## Import Options ##
**Set label/group properties and remap:**  Allows properties to be specified for the labels and groups (see [DataStructures#Element\_property\_tables](DataStructures#Element_property_tables.md)).  If this option is selected you will be able to select your remapping file(s) after the parameters for the main Basedata import have been set.

**Allow labels with no groups:**  Permits the inclusion of labels in the analyses which are not assigned to a group. An example might be where you wish to include species that occur outside your study area when comparing a local region with a broader region.

**Allow empty groups:**  Permits groups that are considered for analysis, but that have no labels themselves. This is useful when you wish to have moving window analyses extend beyond the sampled data to give a smoother result (it is up to the user to ensure such smoothness is valid), or you want a randomisation to assign labels to more groups than just those containing labels.

Both the "empty groups" and "labels with no groups" options are implemented by setting a sample\_count column in the input file, with the appropriate records given a value of 0. If no such column is given or the value is blank then a count of 1 is assumed, rendering these options redundant (and the imported data set possibly erroneous). It is probably easiest to import these as separate files rather than "pollute" your sample data (See Adding\_to\_an\_existing\_data\_set for details of how to do this).

**Data are in matrix form:**  Used if the data are not in standard format.  **The process of importing data differs if this box is checked** (See **Import Matrix Basedata**).

**Skip lines with undef groups:**  Allows records (lines) to be ignored where a group field is either undefined or non-numeric. This can occur where the coordinates for a sample are unknown, if the wrong column is chosen for the groups, or if a file contains a series of lines with no data at its end (a common issue when exporting from spreadsheet programs).  If this option is not selected and such a line is encountered the import will fail when it reaches that line.  The alternative is to remove these lines from the input file before importing, a sometimes tedious and involved task. This issue does not affect text groups, as an undefined value is treated as a zero length string.

**Convert sample counts to binary:**  Converts any non-zero sample count value to a 1.  This is per record, not per group.

Once you have made your selections, click **Next**.

The next dialogue window allows you to specify how the columns in your file will be treated.  The available options depend on if you selected the 'Data are in matrix form' checkbox.

If your data are in spreadsheet format go to **Import Standard Basedata**.

If your data are in matrix format go to **Import Matrix Basedata**.