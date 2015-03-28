<a href='Hidden comment: The source of this document is the Sample_session.pdf file distributed with versions 0.11 and earlier.  This was converted from !OpenOffice to wiki format, via html.
'></a>


This is the main source of documentation for the GUI.  It needs further development, and much of the content will move into the other wiki pages over time, with this document being shortened and serving the purpose of an overview.

If you find parts of it need to be clarified, or material is missing, then please add a comment at the end of the page or submit an issue (http://code.google.com/p/biodiverse/issues).  If you would like to contribute to the documentation then please submit changes as diff/patch format files if possible as these make it easier to review and apply the changes.  If you aren't sure what those are then plain text will do just as well.



# A sample session #

There are seven main components in a full session.

  1. Open or import data into a project (BasaData, matrices and trees)
  1. Visualise the data (view labels)
  1. Exclude some of the data
  1. Build a spatial index
  1. Run a cluster analysis
  1. Run a moving window analysis
  1. Run a randomisation to assess the quality of the results
  1. Export or save the data and results

We suggest you read this in conjunction with the KeyConcepts and DataStructures documents. Much additional information can be found within the application itself, for example by hovering the mouse over various buttons and menu items to view their associated tooltips.

If you wish to experiment with these options then use the Example\_site\_data.csv file for species sample data, Example\_matrix.txt file for matrix data and Example\_tree.nex file for tree data. These are under the Biodiverse/data folder in the distribution. Note that these are fictional data so the results have no meaning beyond example purposes.

Note also that these instructions apply to version 0.14 and later.

## A word of warning ##

Perl is able to handle different numeric locales, however there are some consequences for the analyses.  If your language settings use a comma as the radix (decimal place marker) then several of the comparisons will either fail or will silently not work as expected.  Randomisations are a particular issue here.  The problem is due to how Perl handles strings (text) converted to numbers.  A string representing a number such as '0,5', which might be perfectly valid in your locale, will be quietly converted by perl to 0 when needed for numeric operations.  '0.5' will work as expected.

**How to avoid this problem:**  Use a locale that uses a "." as the radix character (e.g. one of the English locales), or modify your settings to use the "." as the radix.  It is also safer to not mix your locales between Biodiverse sessions (i.e. do not import data using one locale and then analyse it using another).  A fix has been implemented for version 0.14 to avoid this problem (see [issue #81](https://code.google.com/p/biodiverse/issues/detail?id=#81)), but it needs to be tested on non-English locales.


# Opening/importing data #

## Opening Data ##

Data can be loaded into a project if they have previously been saved as separate files on disk.  Use the  _Open_ options under the respective menus, or click on the open folder icon from the selected object bar (tooltip "open from native format").  The filename extensions for each object type are given at [DataStructures#File\_naming\_scheme](DataStructures#File_naming_scheme.md).

Change the name in the textbox at the top if you want to list them by a different name.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/open_existing_object.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/open_existing_object.png)

Note the common “Places” in the left panel of the window. This is the bookmark system used by Gtk (the window system we use), and is persistent across sessions.  You can also select a folder in the right panel and click the _Add_ button to permanently add this folder to the Places panel for convenient access in the future. Likewise, you can remove added (but not default) directories with the _Remove_ button.  You should also be able to drag and drop folders onto the place section.


## Importing Data ##

BaseData, Matrix, and Tree object data can be imported by clicking on their respective import buttons (plus signs) in the main toolbar or through their respective menus. Either an existing data set can be extended with the import (obviously, the new file must contain data of a similar format to the BaseData being extended), or a new one can be created.

BaseData and Matrix objects can be imported from text files. Currently, only delimited text files are supported (e.g. CSV, comma separated variable). They should contain columns for one or more labels (e.g. names such as genus and species) and groups (e.g. x and y coordinates of a data point). The columns of data in your file don't have to be separated by commas, and a prompt allows you to specify the separator used (or simply to have the system make an "educated" guess for tabs, commas, spaces etc.) along with various other import options.

Biodiverse does not care if a matrix being imported is upper right, lower left, both, or any combination of the above. They will store the last valid value for an element pair.

Tree data can be imported from nexus format files (file extension .nex or .tre).

The import options allow you to use a label and/or group properties table for the data you are importing (e.g. to remap label names so they match ther data sets or set their sample counts). A properties file should be a delimted text file with a column or columns containing the current labels of the data you are importing and a column or columns with the new labels they will be mapped to (a subsequent window will allow you to specify which column is which). Any unmapped labels will simply retain their original names when imported.

For BaseData and tree object types the import process involves selecting your data file and a label/group properties file (if desired). A file-browsing window will show your Biodiverse directory by default, and will list several common directories you can search through, such as the C: drive and Desktop on Windows.  Matrices do not yet have remapping, but it is planned (see [issue #16](https://code.google.com/p/biodiverse/issues/detail?id=#16)).

### BaseData ###

There are two types of data supported for import.  In the first case you might have a list where you have one record per observation, for example a list with one line for each species/coordinate combination.  This is the more common data format.  The second format is where you have a matrix of data, with coordinates as the rows and species as the columns, for example a sites by species matrix.  The value of each field is the count of observations for that site/species (group/label) pair.  Examples of each format are in the example data, see Example\_site\_data.csv and Example\_site\_data\_matrix\_form.csv.

Most of the import process is common for both, but the specification of groups and labels differs.

#### Common (pt1) ####

From the BaseData import dialogue window you can select your data file or files. The text box at the top right of the window allows you to name the BaseData object that will be produced (as opposed to the default file name). Once you are finished, click Next.  Multiple files can be imported in the one process so long as they all share the same column order and meaning (the column names do not matter, only the contents).  If you have several files that do not share column orders then import each one separately into the same BaseData.  If your data were generated in R using the write.table() function then from version 0.14 the system will detect this and allow for the missing column header for the row names (see [issue #20](https://code.google.com/p/biodiverse/issues/detail?id=#20)).

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step1.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step1.png)

You will then see a window with various options you can set for the import, such as whether remapping tables are to be used.  If you specify that remapping will be used, you will be able to select your remapping file(s) after you set the parameters for the main BaseData import.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step2.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step2.png)

The set label/group properties and remap check boxes allow you to specify properties for the labels and groups.  See [DataStructures#Element\_property\_tables](DataStructures#Element_property_tables.md).

Allowing labels with no groups lets you include labels in the analyses which are not assigned to a group.  An example might be where you wish to include species that occur outside your study area when comparing a local region with a broader region.

Allowing empty groups lets you have groups that are considered for analysis, but that have no labels themselves.  This is useful when you wish to have moving window analyses extend beyond the sampled data to give a smoother result (it is up to the user to ensure such smoothness is valid), or you want a randomisation to assign labels to more groups than just those containing labels.  (Note that this is broken in version 0.15 - see [issue #180](https://code.google.com/p/biodiverse/issues/detail?id=#180)).

Both the _empty groups_ and _labels with no groups_ options are implemented by setting a sample\_count column in the input file, with the appropriate records given a value of 0.  If no such column is given or the value is blank then a count of 1 is assumed, rendering these options redundant (and the imported data set possibly erroneous).  It is probably easiest to import these as separate files rather than "pollute" your sample data.  See [#Adding\_to\_an\_existing\_data\_set](#Adding_to_an_existing_data_set.md) for details of how to do this.

The "Skip lines with undef groups" check box allows you to ignore records (lines) where a group field is either undefined or non-numeric.  This can occur where you do not know the coordinates for a sample, if you choose the wrong column to use for the groups, or if you have a series of lines with no data at the end of a file (a common issue with exporting from spreadsheet programs).  If turned off and such a line is encountered then the import will fail when it reaches that line.  The alternative is to remove these lines from the input file before import, a sometimes tedious and involved task.  This issue does not affect text groups, as an undefined value is treated as a zero length string - "".

The "Convert sample counts to binary" option converts any non-zero sample count value to a 1.  This is per-record, not per-group.

The next window allows you to specify how the columns in your file will be treated.  The available options are determined by your selection of the "Data are in matrix form?" check box.

#### Data are not in matrix format ####

If you specify that your data **are not** in matrix form then the next window will look like this (explanation below).

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step3.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step3.png)

You must set at least one Group and one Label column, but more than one of each may be chosen. For example, you may typically wish to use both a "species" column and a "genus" column (if separated in your file) as one combined label for your data points, or to specify both the x-coordinate and y-coordinate columns in a file as "Group", to specify a Cartesian grid (specifying only an "x" column or "y" column as the Group would result in a one-dimensional analysis of the data across that group's domain).  When a Group column has been set you will be given the option to select its cell size (in the same units as the group data is stored) and origin.  These default to 100,000.00 and 0.00, respectively so make sure they are appropriate to your data.  The origin allows you to align your imported data with a non-zero origin, e.g. you are using some coarse resolution climate data in a related analysis and you wish to ensure the resulting cell boundaries align exactly between data sets.

You can filter which data rows to use by assigning column types as “Include\_columns” and “Exclude\_columns” via the Type drop-down menu. You can have any number of each type of column. If one or more inclusion columns is specified, only those data rows with non-zero values in _at least one_ of these columns will be imported. If one or more exclusion columns is specified, only those data rows with a value of zero in _all_ of these columns will be imported (ie. any non-zero value will trigger a row to be excluded).

All columns in your file that are irrelevant to the analysis should be set to “Ignore”.


You can also specify if the group data are degrees using the _Degrees?_ comboboxes.  This allows the importation of data in degrees minutes seconds formats, as well as some validation of data to determine if the value is in the valid range (the latter works for both DMS and decimal degrees formats).  Specify _is\_lat_ for latitude and _is\_lon_ for longitude.  Examples of valid formats are:
```
Latitude,Longitude
S23°32'09.567", E149°23'18.009"
23°32'09.567"S, 149°23'18.009"E
-23 32 9.567, +149 23 18.009
-23.535991, 149.388336
```


#### Data are in matrix format ####

If you specify that your data **are** in matrix form then the next window will look like this (explanation below).

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step3_matrix_format.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step3_matrix_format.png)

The group options for the matrix imports are the same as for the non-matrix imports.

The key difference from the non-matrix import are the label\_start\_col and label\_end\_col column options (the Label option is also not available).  These denote which column headers to use for the labels.  The label\_end\_col is optional.  If not specified then the system will use all columns after the label\_start\_col.  If more than one start and/or end column is specified then the system will use the first start col and last end col (see [issue #164](https://code.google.com/p/biodiverse/issues/detail?id=#164)).  If you have a single label column before the groups are specified then you will need to edit the file so it is after the groups, as the system currently only allows one option per column so it cannot be both start and end.  Include and exclude columns apply as before, so take care not to specify a label column as include or exclude as it might not do what you want (although it is possible that it will, for example if presence of a species should be used to exclude a sample row).  If you want to skip columns between the label start and end columns then set an exclude column in a label remap file.  Remember also that the values for each row are the sample counts - set the "Convert sample counts to binary" option in the preceding window if you only want presence/absence data per group.  Finally, use a [label remap/property table](DataStructures#Element_property_tables.md) to change the column names, for example to separate genus and species into separate axes for analysis.

Those columns marked as ignore but between a label\_start\_col and label\_end\_col will be imported.

Click OK.

#### Common (pt2) ####

The next window allows you to order your labels and groups for the desired view. In the example data set, placing “genus” above “species” produces labels named with the species name concatenated after the genus name, and placing “y” above “x” makes the y column data the first dimension of a group's coordinates and x the second (this is useful if you have a file where latitude precedes longitude in the file's column order).

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step4.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step4.png)

Note: once the data are imported and opened, the first group axis will be displayed along a horizontal axis and the second (if one exists) on a vertical axis. Biodiverse does not currently support a graphical view for more than two group axes, although they can still be imported and analysed.  Any data set containing more than two axes will be displayed using the first two axes.

Once you have accepted the label and group ordering, and if you had previously specified that you wished to set label and/or group properties and remap, you are brought to a final set of windows where you can select the element property table file and its respective parameters (one each for labels and groups if you selected both).  If you did not specify that any properties were to be set then this step is skipped.  The set of windows is the same for group and label properties, although the column options differ between them.  (See also [DataStructures#Element\_property\_tables](DataStructures#Element_property_tables.md) for details about importing other properties).

![http://biodiverse.googlecode.com/svn/wiki/screenshots/remap_labels_screen1.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/remap_labels_screen1.png)

![http://biodiverse.googlecode.com/svn/wiki/screenshots/remap_labels_screen2.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/remap_labels_screen2.png)

![http://biodiverse.googlecode.com/svn/wiki/screenshots/remap_labels_screen3.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/remap_labels_screen3.png)


If you decide you don't want to select a remap file after all, simply click Cancel. The system will now import your data into a BaseData object. A status bar appears showing progress. When the import is complete, you are free to visualise and analyse the data. The Outputs tab shows all currently imported BaseData objects and associated analyses that you can work with.

#### Adding to an existing data set ####

The process described above will create a new BaseData object in the Biodiverse session. Alternatively, if you have an existing BaseData object in your project and wish to add more data you can do so by following the normal import process, but in the dialogue window where you select the file to be imported, uncheck the “New” box at the top and select the existing BaseData set to import into from the drop-down menu.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_into_existing.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_into_existing.png)

Data being appended to an existing BaseData object should have group data in the same coordinate system or numeric range as the existing BaseData (for example, 'x' and 'y' columns of decimal degree geographic coordinates if the existing data were so), otherwise the results will be unpredictable.  Labels are more flexible, and can be comprised of more or fewer components (columns) than the data being appended to.

You may also create a new BaseData object as a duplicate of the currently selected BaseData by the _Basedata->Duplicate_ menu option.  This will also duplicate any analyses performed on the BaseData. To duplicate the BaseData only, select _Basedata->Duplicate without outputs_.

Note that any spatial index will need to be rebuilt if new data are imported (unless no new groups are added).  See [KeyConcepts#Using\_the\_spatial\_index](KeyConcepts#Using_the_spatial_index.md).

### Matrices ###

Matrix data can be imported at any time, although it can only be viewed with an existing (and selected) basedata object.

When importing matrix data, you will first be asked to specify the matrix data file in the same way as for basedata objects.  As with BaseData files, if your data were generated in R using the write.table() function then from version 0.14 the system will detect this and allow for the missing column header for the row names (see [issue #20](https://code.google.com/p/biodiverse/issues/detail?id=#20)).

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_matrix_step1.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_matrix_step1.png)

The next window asks how the columns in the matrix file should be read.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_matrix_step2.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_matrix_step2.png)

You must select at least one label column, and one (and only one) “Matrix start” column. Any other columns in the file should be set to “Ignore”. Click Ok. Your matrix has now been imported, and should appear in the drop-down menu in the matrix toolbar at the top of the screen. It will be displayed the next time you visualise basedata (though keep in mind it will only produce a useful display if the matrix and basedata objects share some labels).

Remapping and explicit inclusion/exclusion of matrix elements is done using an element properties table, the same as for a BaseData import.  You will be given the option to use an element properties table after the matrix file and its columns have been specified.  Choosing cancel will stop the whole import.

### Trees ###

As with matrices, trees can be imported at any time, but can only be visualized once a (any) basedata object has been imported and visualized as well. Again, a tree is most useful if the basedata being displayed shares labels with it.

A tree must be in a nexus format (`*`.nex or `*`.tre extension). All trees in a nexus file will be imported and added to the project.  To import, select the import button in the Tree toolbar. A window will appear for you to select your file.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_tree_step1.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_tree_step1.png)

Select your file and click Ok. You will then have the option of choosing a label remap file.  This is often needed so the node names match the relevant BaseData labels (see FAQ#My\_phylogenetic\_analyses\_have\_empty\_results).

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_tree_step2.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_tree_step2.png)

If you don't wish to remap labels, simply click Cancel and the system will import the tree.  If you do then click OK and then you will be prompted to select a properties (remap) file, followed by an option to specify a column separator and quote character, and then the column types.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_tree_step3.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_tree_step3.png)

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_tree_step4.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_tree_step4.png)

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_tree_step5.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_tree_step5.png)

Note that you need to specify as many input\_element columns as the tree labels have (this will be one for nexus files, but will increase if we ever import tabular trees) and then as many remapped\_element columns as your BaseData object has label columns.  This is so they match correctly.


Alternatively to importing a tree from a file, you can also derive one at any time during your session if you already have a basedata and/or matrix object selected. This can be done by selecting the “Create tree from labels” or “Convert matrix to tree” options under the BaseData and Matrix menus, respectively. When generating a tree from the basedata labels, labels are treated as taxonomic names, and thus are primarily useful for a tree if they have at least 2 components (e.g. genus and species); ie. at least 2 columns representing labels in the original data file or if singular labels are remapped to multi-part labels. The tree hierarchy is then based on the ordering of the label components (see the previous section for how to choose label and group ordering during the basedata import process). A tree generated from a matrix simply reflects the matrix relationships based on the values of its cells.

# Visualising data #

Often the first step you will take once you have imported the data into a BaseData object is to view the data to visualize the relationship between the groups and labels. This is done through the _Basedata->View Labels_ menu option. Alternatively, you can view the data from the Outputs tab by double-clicking on the basedata object or by selecting it and clicking the _Show_ button on the right side of the window.

Once this is done, you should see four panes, as below (the two panes on the right-hand side may be appear differently depending on whether a matrix or tree is currently selected in their respective dropdown menus in the toolbar at the top of the screen).

![http://biodiverse.googlecode.com/svn/wiki/screenshots/view_labels1.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/view_labels1.png)

The top left contains two lists of the labels in the selected basedata object. Each list can be sorted by any of the columns. The top right contains a grid of the selected matrix elements (it is blank if no matrix is selected). The bottom left contains a grid of the groups in the current basedata object. The bottom right contains the currently selected tree (blank if none selected).

The sizes of the panes can be changed by clicking and dragging the dividing bars between them.  These are no visible for the GTK MS-Windows theme but can be located by moving the mouse over them and observing where the mouse icon changes.

Essentially, the system provides a simple linked visualisation system so that the selection (labels, groups, matrix cells or tree nodes) in one pane is reflected in the other three. If more than one label is contained in the selection in any pane, the groups in the group grid are coloured with a hue of red according to the number of the selected labels they contain (dark red for more, lighter red for less, white for none).

If at any time you wish to deselect any currently selected/highlighted labels, hold the control key and click on them in the label lists or simply click on any nongroup location in the group grid pane to deselect all.

Interaction with each of the panes is now described.

## The Label Lists ##

Interaction with the labels is similar to many lists you will encounter.

Click on any row in the list to highlight a single label. Hold the shift key down to select a contiguous block, and the control key to select (or deselect) non-contiguous labels. The main use for a second list is to be able to select labels from each list to highlight specific cells – or blocks of cells – in the matrix pane, if a matrix is currently selected. The first (top) label list represents matrix rows, while the second (bottom) label list represents matrix columns.  The second list is only visible if the project has a selected matrix.

Sorting the label lists is done by clicking on the column headers. Subsequent clicks on column headers sort the data by that column in ascending, descending, and default order. The default order is by label, in alphabetical order. Re-ordering of these lists also re-orders the matrix plot.  The current selection in the lists is updated whenever you select elements in one of the other panes.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/view_labels2_one_label_selected.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/view_labels2_one_label_selected.png)

At version 0.14 there are five or six columns: the Label (the name of the label), Variety, Samples, Redundancy and Selected.  The "Col selected" column is only visible if the project has a selected matrix.  From version 0.15 there are also columns for any user specified properties imported using an element properties table ([DataStructures#Element\_property\_tables](DataStructures#Element_property_tables.md)).

The Variety column shows the number of groups the label occurs in. This is analogous to the range unless one is set separately on import using the _set label remap and properties_ option.

The Samples column lists number of times this label occurs across all groups. Groups can have many samples of the same label.  It does not include the value set by the _set label remap and properties_ option.

The Redundancy column shows the sample redundancy for each label. This is calculated as (1 – variety / samples). A value close to one represents a good overall sample of a label relative to the number of groups it occurs in (many redundant samples). A value of zero means that there is, on average, close to one sample per group the label occurs in, and it is therefore not well sampled.

The selection columns have a value of 1 when that label is selected, allowing the user to raise the selected set to the top of the list.  The "Selected col" value is 1 only when one selects a matrix column, either through the lower Label List or on the matrix itself.

## The Group Grid ##

The group grid is a spatial display of the groups. Normally this is a map of the data (e.g. if your group data consists of some form of geographic coordinates), but there is no reason that you are restricted to using geographic locations as your groups. So long as the data have numerical coordinates, everything will be fine and dandy.  If your data use text group axes then the system will assign them to cells on a grid based on an alphabetical sorting.  This can be difficult to interpret, but the remember system is fundamentally a tool for spatial analysis.

Hovering over a group will highlight in bold the nodes in the tree corresponding to the labels it contains, if a tree has been selected.

Left-clicking on a group will highlight it in dark red. Other groups may also be highlighted depending on the number of labels they share with the selected group (darker red for more shared labels, lighter red for less, white for no labels in common). Similarly, you can click and drag a box around multiple groups. Groups will then be highlighted according to the number of labels they have in common with the selected group. Labels in selected groups will also be highlighted in the top label list (although the list does not automatically jump to them).  Drawing a box over the grid with the left mouse button selects labels from all the groups in the box, allocating the hue based on the species richness of the selection rather than a single group.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/view_labels2_one_group_selected.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/view_labels2_one_group_selected.png)

While holding the control key down, click on a group to display a pop-up window that allows you to see a list of the labels it contains and the sample size in that group for each label. Note: this will also select that group (and change highlighting as appropriate). To bring up any group's detailed information without changing current highlighting, use the middle/wheel mouse button to select a group.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/view_labels3_popup_group.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/view_labels3_popup_group.png)

The title of this window indicates the group being examined. To re-use the same window to display another group's data, check the _Re-use_ box. If this box is unchecked, data for subsequently selected groups will be displayed in new windows. This is useful when making comparisons between label presence and sampling among different groups. The _Copy_ button in the group info window makes a copy of the group coordinates and all labels with their sample size to the clipboard for use elsewhere.

You can also display a shapefile (a map of a country's border lines, for example) in the group grid pane as a background to make it easier to identify groups, especially if they are geographically related. See [KeyConcepts#Map\_overlays](KeyConcepts#Map_overlays.md) for how.

The group grid display extent (zoom level) can also be changed by using the three zoom buttons in the bottom left of the pane. If you are at a zoom level that does not display all groups at once, you can navigate using the scroll bars or by right-clicking (or clicking the middle/wheel mouse button) and dragging.  You can also pan by clicking on a part of the plot without a group and dragging.

## The Matrix Grid ##

![http://biodiverse.googlecode.com/svn/wiki/screenshots/view_labels2_matrix_subset_selected.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/view_labels2_matrix_subset_selected.png)

The top right pane displays a grid of the currently selected matrix. Each cell represents a pair of labels from the label lists, coloured according to the pair's matrix value, with a colour scale for these values on the right of the matrix.

Cells in the matrix grid are only coloured if both labels they represent are present in the basedata label list. If one or both of its labels are not present in the basedata, a cell remains white.

The system lists which element you are hovering over at the top of the pane, indicating the label pair and its matrix value.

The ordering of the matrix rows matches the current ordering of the upper label list in the label list pane, while the ordering of the matrix columns matches that of the lower label list. Changes in the ordering of either label list will automatically be reflected in the matrix.

Click on a single element (cell) to select one pair of labels. The two label lists will automatically adjust to show these two (the top list highlighting the label corresponding to the matrix row, the bottom list highlighting the label corresponding to the matrix column).  All cells in the group grid containing those labels will be highlighted in red as per the groups, as will the relevant nodes on the tree.

Similarly, you can click and drag the left mouse button to select a rectangular region in the matrix. This will highlight the selected labels in the other panes, adjusting the label lists to reflect the new selection.

The matrix grid view can also be customised by using the three zoom buttons in the bottom left of the pane. If you are at a zoom level that does not display the whole matrix at once, you can navigate using the scroll bars or by right-clicking (or clicking the middle/wheel mouse button) and dragging.

## The Tree ##

![http://biodiverse.googlecode.com/svn/wiki/screenshots/view_labels2_one_clade_selected.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/view_labels2_one_clade_selected.png)

The tree is generally a representation of the phylogenetic similarities between labels, although it could be used for anything that uses such a structure. In this pane, you should see two sections (assuming a tree object is selected in the main toolbar at the top of the window). The upper section displays the relationship between labels as a dendrogram, while the bottom section displays a simple graph of the proportion of nodes present to the left of a vertical cut through the tree above (known as the [scree plot](KeyConcepts#Scree_plot.md)). If this plot is not immediately visible, it may be “hidden” at the bottom. Move the mouse toward the bottom of the tree pane until it indicates a bar that you can click on and drag upward to reveal the graph.  Use this bar to reduce the size of the scree plot if it is too large.

The dendrogram can be plotted by node depth or length via the _Options_ button at the bottom of the pane. This menu also allows you to change highlighting settings.

Hovering over a tree node highlights the groups containing the node's labels in the group grid. It does this using a circular symbol. Right click on the node to fix the highlights until the next mouse click in the tree pane.

Left-clicking on a branch node selects all labels in terminal descendants (single-label nodes) of that node in the tree that are also in the label lists. Any nodes containing a label that is not present in the basedata will remain black in the tree.

Control-click on a node to display a pop-up window from which you can access lists of the labels, groups and node characteristics (length, name, etc). General interaction with this pop-up is the same as that for the group info pop-up described [above](#The_Group_Grid.md).

![http://biodiverse.googlecode.com/svn/wiki/screenshots/view_labels3_popup_clade.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/view_labels3_popup_clade.png)

You should notice a blue vertical sliding bar on the right side of the tree pane. Sometimes it can disappear off the side under the scroll bar, in which case use the zoom controls to zoom out and locate it, or find it in the scree plot. Hovering the mouse over this bar will display three numbers. The first two numbers indicate the quantity and percentage of nodes present to the right of the bar. If the tree is plotted by node depth, the third number indicates the depth at the current bar position. If the plot is by node length, the third number indicates the distance from the bar position to the most distant (left-most) leaf node.

The tree view can also be customised by using the three zoom buttons in the bottom left of the pane. If you are at a zoom level that does not display the whole tree at once, you can navigate using the scroll bars or by holding down the right mouse button and dragging.


# Excluding Data #

Once you have looked at the labels, or even before if you are confident, you can begin to remove groups and labels that you consider redundant, irrelevant, or even just wrong.  This is on the basis of their properties, and not on the basis of the labels.  Excluding labels or groups based on their names is done at the time of import using include and exclude fields in the data or in an [element properties table](DataStructures#Element_property_tables.md).

To run the exclusions on the currently selected basedata object, open menu option _Basedata -> Run Exclusions_. You should see a window similar to the one below.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/run_exclusions_checked.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/run_exclusions_checked.png)

There are currently four group properties and three label properties that can be assessed, setting maximum or minimum values by which to exclude them. These characteristics are _variety_, _samples_ and _redundancy_ for both labels and groups as well as _range_ for labels. The _variety_ of a group is the number of different labels it contains (the same as the richness). A group's _samples_ is the total number of samples of all labels it contains. A group's _redundancy_ is the complement of the ratio of the number labels to the number of samples in that group (i.e. a group with 2 labels having a total of 8 labels will have a redundancy of 0.75).  For labels, _variety_ is the number of groups it occurs in.  The _samples_ is the number of samples of that label across all groups.  The _redundancy_ is analogous to that used for groups, except it is a function of the ratio of the group count to the sample count for that label.  The label _range_ is the _variety_ unless it has been specified using label properties at the time of import.

In the screen shot above, any label with a range of 50 or more will be removed (excluded) from the BaseData object, as will any group with a variety of 6 or fewer labels, or 10 or fewer samples across all labels it contains.  (All tests are evaluated using conditions of "less than or equal to" or "greater than or equal to", as appropriate).

If you already have the BaseData displayed when you run the exclusions then any display will not be updated. Close the display and re-open it to see the changes.

Prior to version 0.15 you will also need to manually rebuild any spatial index if groups were deleted, as this will contain references to deleted groups and any subsequent analysis will fail (see [issue #171](https://code.google.com/p/biodiverse/issues/detail?id=#171)).

**_A word of warning_**: Running the exclusions multiple times is not a good idea. The remaining groups and labels are updated each time, thus recalculating their various scores. For example, if you delete a group on the basis of its redundancy then you will reduce the diversity of any of its labels by one. This means that for analyses that use it you will reduce the variety of that label, and the range if one is not set using an [element properties table](DataStructures#Element_property_tables.md) at import.

It is also a bad idea to run the exclusions after you have run any of the cluster or spatial analyses. These analyses will no longer properly relate to their parent BaseData object if you do this.  Any linking back to elements deleted from the BaseData, such as for display or interrogation of labels in groups, will cause an error.  For this reason the system will stop you from doing this.  If you do need to run further exclusions then delete all the outputs or duplicate the BaseData without outputs and work on that (menu _Basedata -> Duplicate without outputs_).

# Building a spatial index #

A spatial index will make the spatial analyses run faster, although users should note that not all spatial conditions will work with the index (typically those with complex user-defined conditions).  To set this use the menu option _Analyses -> Build Spatial Index_.  The index can be deleted and rebuilt at any time, and these changes affect only subsequent analyses, not those that preceded any change.

See [KeyConcepts#Using\_the\_spatial\_index](KeyConcepts#Using_the_spatial_index.md) for more details about the choice of settings and how it works.

# Running a Cluster Analysis #

Cluster analyses are used to identify clusters in the data.  Biodiverse supports agglomerative clustering of the groups based on their labels, or some function of their labels such as the values of a linked matrix or tree.

Note that clusters are often called groups, but the term is not used here as it could cause confusion with [BaseData groups](DataStructures#Groups.md) (although one could make the case that they are similar).

To run a cluster analysis on the currently selected basedata object, open menu option _Analyses->Cluster_.

The cluster tab has two main sections where you can set options. The upper section (_Parameters_) determines the parameters used in the clustering to generate a tree. The lower (_Spatial calculations to run for each cluster node_) determines what subsequent calculations will be run for each node in this tree using the groups it contains to define the spatial sample.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/cluster_analysis_first_page.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/cluster_analysis_first_page.png)

Click on the _Go_ button (or use the keyboard shortcut Control-G) once you have specified your parameters and any desired calculations (see details below). The system will first build the dissimilarity matrices, then run the clustering using these matrices, and then any spatial calculations you have selected for each node. One or more progress bars (depending on your options) let you know how things are progressing. Once complete, a prompt asks if you would like to display the results. If so, a display pane comes up showing you the results. You can pull the pane down (via an invisible slider bar at the top of the white pane) to see the options you used; for example, to change them and recalculate an analysis. If you don't wish to view the results at this time, they may be accessed later from the _Outputs_ tab. In this tab, analyses are automatically placed and indented below the basedata object they were performed on.

## Cluster parameters ##

The _Name_ option is the name used in the system for that analysis. By default, the name of an analysis is the name of the basedata object (e.g. “sampledata”) followed by an underscore, “Cluster” and a digit (e.g. “sampledata\_Cluster0”). Numbering starts at 0 and any subsequent analyses created for that basedata object create a similar name with the number incremented by 1. However, you can give an analysis any name you want, but if one with that name already exists, you will be notified that the original analysis will be overwritten if you continue. (Note: naming conflicts only arise for different analyses on the same basedata object.)

The _Metric_ option specifies the dissimilarity metric that will be used to compare groups. It is from this function that the matrices of dissimilarities are built.  See the [Indices](Indices.md) page for specific details about each index.

The _Linkage_ option determines how the similarities of newly formed cluster nodes to other nodes (elements) in the matrix are calculated.
  * link\_average uses the average value of the merged groups, weighted by the number of terminal nodes they each include.  In this way a merger between node A with 10 terminal nodes and node B with 1 terminal node will not be biased towards the labels in node B.
  * link\_average\_unweighted uses the average, but does not weight by terminal nodes.
  * link\_maximum uses the maximum value of the merged nodes.  For a dissimilarity matrix this has the effect of taking the most dissimilar value amongst each successive merger.
  * link\_minimum uses the minimum value of the merged nodes.  For a dissimilarity matrix this has the effect of taking the least dissimilar value amongst each successive merger.
  * link\_recalculate has the effect of combining the terminal nodes under each node and treating them as an aggregate group.  This can be useful in cases where there are sampling biases and well sampled labels would swamp the signal from poorly sampled labels.  See [Bickford et al. (2004)](http://dx.doi.org/10.1111/j.1365-2699.2004.01127.x) for an example of this.  This method will cause reversals (negative node lengths) in the tree as new labels enter the calculations for the dissimilarity metrics based on presence/absence.  However, there should be no difference between link\_average and link\_recalculate for indices that use sample counts (e.g. [BRAY\_CURTIS](http://code.google.com/p/biodiverse/wiki/Indices#Bray-Curtis_non-metric)).


The _Spatial conditions_text boxes allow you to enter a set of spatial constraints for the clustering (see the SpatialConditions page for details on how to specify these). If specified, the analysis will only cluster those groups or clusters with other groups satisfy the spatial constraints (relative to the processing group). If the clustering process runs out of neighbours then it switches to the next matrix in the list and continues clustering with that matrix. _Prior to version 0.14, if the union of the matrices (the `shadow matrix`) is not symmetric then the clustering will stop with multiple root nodes and the system will not worked as hoped.  This is why it is a good idea to specify `sp_always_true()` as the final spatial condition for clustering to ensure all works properly (or use some other condition that will give a symmetric matrix).  From version 0.14 this constraint has been removed to allow calculations with larger data sets where clustering everything is not practical.  Note, however, that a root node is added to the tree such that all nodes line up when plotted.  The linkages of the right-most nodes with this root node are denoted as JOIN\_NOT\_METRIC in the NODE\_VALUES list._  The _Verify_ button (the one with the big tick on it) lets you know if the spatial conditions are syntactically valid. It does not check if the conditions do what you want, but this is hardly unusual for a computer program.

The _Definition Query_ text box allows the exclusion of groups from the clustering process (as opposed to controlling which neighbour groups a processing group can be clustered with).   See the SpatialConditions page for more details.

## Running calculations for each node ##

Use the check boxes to select which sets of calculations are to be performed, and therefore which indices will be calculated. Press the plus buttons next to each set to select specific analyses. Press the plus button again to see which indices each one calculates. Text at each level tells you about the calculations and what they do.

Not all these calculations or indices are valid for clusters, and the system strips out the ones that are not before any calculations are performed. If a spatial analysis is selected, indices resulting in single values will be stored within a list called SPATIAL\_RESULTS in each cluster tree node. Those that are lists will be stored in each node at the same level as SPATIAL\_RESULTS. This will become more clear when you run a cluster analysis and view the results.


## Viewing the cluster results ##

There are three sub-panes within the display pane. On the left is the group grid, on the upper right is the tree representing the clustering, and on the lower right is the scree plot for the tree. Prior to version 0.12 you will likely need to pull the bottom of the tree pane down to reduce the scree plot's vertical extent and expand the tree so it can be viewed properly.  From version 0.12 you will need to pull the scree plot up to see it.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/cluster_analysis_results_page.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/cluster_analysis_results_page.png)


As with the visualisation of basedata/matrix/tree objects described earlier, the system is linked, and interactions in the group grid or tree of the cluster display are generally reflected in the other. Hovering the mouse over a node in the tree highlights the groups (in the group grid) that are contained in that node. Likewise, hovering the mouse over a group in the group grid will highlight the path (set of nodes/clusters) in the tree to which that group belongs. Right click on a tree node to fix a colour to the subclusters (descendant nodes in the tree). These clusters are split into a number of coloured groupings based on the “Clusters to colour” parameter at the bottom of the pane. Note that some leaf nodes in the tree may have a length of zero (indicated by vertical bars at the leftmost side of the tree, longer bars indicating more zero-length leaf nodes). Thus, if any such nodes occur under (to the left of) the node you have selected, their colouring will not be apparent if you are using “Plot by Length” mode. These nodes, along with their colouring (if selected) can be made apparent by switching to “Plot by Depth” mode under the tree options button.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/cluster_analysis_results_page_coloured_and_highlighted_nodes.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/cluster_analysis_results_page_coloured_and_highlighted_nodes.png)

The blue sliding bar in the tree pane can be dragged across the tree to colour the nodes and groups at that level. The bar also displays the number of nodes it is crossing when the mouse is focused on it. Note that the maximum number of contrasting colours the system will display is 13. If the slider bar crosses more than 13 nodes, all nodes will be uniformly coloured red instead, and groups in the group grid will not be coloured.

Note that, from version 0.13, the user can set the slider bar to not affect the colouring.  This is accessed via the _Options_ menu under the dendrogram.

Groups contained in selected clusters will be coloured in the group grid. The colouring for these groups are assigned according to the hue/sat scheme selected (see the bottom of the groups grid pane) and are based on the value of each group for the index selected.


![http://biodiverse.googlecode.com/svn/wiki/screenshots/cluster_analysis_results_page_coloured_by_slider.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/cluster_analysis_results_page_coloured_by_slider.png)

![http://biodiverse.googlecode.com/svn/wiki/screenshots/cluster_analysis_results_plot_by_depth_page_coloured_by_slider.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/cluster_analysis_results_plot_by_depth_page_coloured_by_slider.png)

The choice of which index to show in the group grid is made in the selection boxes beneath the grid. The one on the left is the list of calculations (e.g. SPATIAL\_RESULTS or [ABC2\_LABELS\_SET1](Indices#Ranges.md)) and the one on the right shows which index or list element (group or label) to display from that analysis. The default is the special _Cluster_ list, which colours the clusters using a contrasting colour scheme (Brewer, Cynthia A., (2005), _Designing Better Maps: A Guide for GIS Users_, ESRI Press, Redlands CA, 203 pp. [www.colorbrewer.org](http://www.colorbrewer.org/)). Note: the right-hand lists of indices/elements to display only appears once an analysis other than the default Cluster is selected from the left-hand list. In addition to the contrast and continuous colour schemes, white groups in the grid are those that are not in the selected clusters. Black means they are in the selected clusters, but are not relevant to the index and/or elements (group/label) selected from the drop-down menus in the group grid pane.

Holding down the control key while clicking on a group in the grid produces (as usual) a pop-up with a list of the labels in that group. If the group is in a selected cluster, other information and indices pertaining to the group and its cluster can also be accessed from this pop-up. Similarly, you can control-click on a node in the tree to see a pop-up with indices for individual labels and groups contained in the node, indices for the collection of groups/labels in the node (SPATIAL\_RESULTS), and characteristics of that node (NODE\_VALUES). These are accessed from the _Data_ drop-down menu in the pop-up window.



You can customize the tree display via the _Option_ button below the scree plot. You can determine (1) whether the tree will be plotted by the length or depth of each node, and (2) whether the cluster grouping that is done when clicking on a node uses length or depth. Normally length for both is good enough, but when you have non-monotonic linkages and reversals then the overlaps and negative lengths make it easier to plot by depth and group by length.  Compare the two images below.


![http://biodiverse.googlecode.com/svn/wiki/screenshots/cluster_analysis_results_page_recalc_linkage.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/cluster_analysis_results_page_recalc_linkage.png)

![http://biodiverse.googlecode.com/svn/wiki/screenshots/cluster_analysis_results_page_recalc_linkage_plot_by_depth.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/cluster_analysis_results_page_recalc_linkage_plot_by_depth.png)

Vector overlays can be plotted using the “overlays” interface at the bottom of the screen (see [KeyConcepts#Map\_overlays](KeyConcepts#Map_overlays.md)).

# Running a spatial (moving window) analysis #

Now that you have been amazed by the functionality in the cluster tab, you will probably want to try your hand at one of the spatial analyses.

Spatial analyses are used to identify spatial patterns in the data. Generally it is treated as a moving window analysis, where the neighbourhoods are evaluated for each group in the basedata object, but the flexibility of the spatial [neighbourhood definitions](SpatialConditions.md) means moving window is not always the correct term.

To run a spatial analysis on the currently selected basebata object, open menu option _Analyses -> Spatial_.

The Spatial tab has two main sections where you can set options (see below), and this process is very similar to that of a cluster analysis. The upper section (_Parameters_) determines the parameters used in defining the two neighbour sets used in the spatial analysis. The lower (_Calculations to run for each neighbourhood_) determines the subsequent calculations that will be run for the set of neighbours related to each group. You can select any number of calculations to perform.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/spatial_analysis_first_page.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/spatial_analysis_first_page.png)

Unless you have specified a complex spatial neighbourhood that causes errors in the neighbours then you should turn the [spatial index](KeyConcepts#Using_the_spatial_index.md) on (menu option _Analyses -> Build Spatial Index_) (see also [#Building\_a\_spatial\_index](#Building_a_spatial_index.md)). The best resolution to use depends on your data set, but a good start is twice the cell size. If you have a cell size of zero then make it approximately the same as the extent of your neighbourhood definition.

Click on the _Go_ button (or use the shortcut Ctl-G) once you have specified your parameters and selected which calculations you want to run for each processing group (see below for how). The system will then run the selected spatial analyses. The progress bar lets you know how things are progressing (as the name suggests).  Once the analysis is complete, it pulls up a display pane and shows you a map of the results. Pull the pane down to view the options you used, for example to change them and re-run the analysis.  You will be warned about overwriting an existing analysis.

## Spatial analysis options ##

The _Name_ option is the name used in the system. Analyses within a given BaseData may not have the same name.

The _Neighbour set 1_ and _Neighbour set 2_text boxes allow you to define the neighbour sets used for the calculations (see SpatialConditions for how). There is no requirement to include the processing group in any of the neighbour sets, and both neighbour sets may be arbitrarily defined independently of each other. It is up to the user to identify what is most appropriate for the analysis at hand. You are also not obliged to specify a second neighbourhood.  The use of these neighbourhoods varies by analysis. Some aggregate the neighbourhoods into a single set (e.g. [endemism\_whole](http://code.google.com/p/biodiverse/wiki/Indices#Endemism_and_Rarity)), others compare the labels in the first neighbour set with those in the second (e.g. [Jaccard and other dissimilarity indices](http://code.google.com/p/biodiverse/wiki/Indices#Taxonomic_Dissimilarity_and_Comparison)), while others use the first set to define the list of labels to use but then consider distributions across both neighbour sets (e.g. [endemism\_central](http://code.google.com/p/biodiverse/wiki/Indices#Endemism_and_Rarity)).

The _Definition query_ text box allows the analysis to be applied to only a subset of groups (those which satisfy the criteria).  All groups are still considered as neighours though (see [SpatialConditions#Definition\_Queries](SpatialConditions#Definition_Queries.md)).

The _Verify_ buttons (big green ticks to the right of the neighbour set and definition query text boxes) let you know if the spatial conditions entered are syntactically valid. The system does not check if the conditions do what you want but, as was noted in the clustering section, this is hardly unusual for a computer program.

<a href='Hidden comment: THIS HAS BEEN REMOVED FROM THE GUI FOR NOW:
The _Plus_ button allows you to specify additional arguments if specified by the calculations, although this is not really used much yet.
'></a>

## Running analyses for the neighbour sets ##

This is the same as in the cluster tab. Use the check boxes to select which sets of calculations are to be used, and therefore which indices will be calculated. Press the plus buttons next to each set to expand or reduce the tree. Depending on the level, expanding the tree will either show which anlayses are available under a category (top level), or  shows a list of the indices each one calculates with an explanation for each (lower level). This information is also available from the [Indices](Indices.md) page.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/spatial_analysis_selected_analyses.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/spatial_analysis_selected_analyses.png)

Indices which result in single (scalar) values are collected and stored in a list called SPATIAL\_RESULTS in each element (group). Those that are lists are stored in each element  at the same level as SPATIAL\_RESULTS.

Those calculations or indices that require two neighbourhoods (such as Jaccard or Sorensen dissimilarity) will not be created if a second neighbourhood is not specified.

## Viewing the spatial results ##

The results are displayed as a map in a single pane within the tab.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/spatial_analysis_showing_map.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/spatial_analysis_showing_map.png)

The colour scheme can be changed to one based on intensity of a single hue if needed.  See [KeyConcepts#Colour\_schemes](KeyConcepts#Colour_schemes.md).  Currently the full range of colours is assigned to the index values using linear scaling between the minimum and maximum values.  Changing this is for a future release, or the data can be exported and plotted using a GIS or other package.

Hovering over a group will highlight the groups used in the calculations – a solid circle for those in the first neighbourhood and a dash for those in the second neighbourhood. Right click on a group to keep the highlighting at that group until the mouse is left clicked on any group.  You can control whether these are displayed, or just display one set, by using the _Neighbours_ selection below the map.

The specific index that is displayed is determined using the two selection boxes at the bottom left of the window. The default is SPATIAL\_RESULTS. This interface excludes lists that are not numeric hashes, so any result that is an array of numbers (such as [IEI\_DATA\_ARRAY](http://code.google.com/p/biodiverse/wiki/Indices#Inter-event_interval_statistics_data)) cannot be displayed this way.

Holding the control key while clicking on a group, or clicking on a group with the middle mouse button, produces a pop-up list with all the results in it, including those that cannot be displayed spatially. It also includes lists of the elements (groups) in each neighbour set (Elements set1, set2 and all) and of the labels in these neighbour sets (Labels set1, set2 and all). “All” is the union of neighbour sets 1 and 2.

Vector overlays can be plotted using the “overlays” interface at the bottom of the screen (see [KeyConcepts#Map\_overlays)).

The interpretation of some of the list results can take some thought.  Consider the [ENDC\_WTLIST](http://code.google.com/p/biodiverse/wiki/Indices#Endemism_central) result.  The set of groups that have a result (are coloured) are those that contained that label in their neighbour set.  This is not the same as the set of groups that contain that label (unless a condition was used that only uses the processing group, e.g. `sp_self_only()` or `$D==0`).  The main advantage of plotting these sorts of lists is that one can visualise where a specific label has a large or small effect.  In terms of weighted endemism, which is an additive calculation, one can also conduct further calculations outside of Biodiverse to determine which labels are contributing the most to the [ENDC\_WE](http://code.google.com/p/biodiverse/wiki/Indices#Endemism_central) or [ENDW\_WE](http://code.google.com/p/biodiverse/wiki/Indices#Endemism_whole) scores for each group's neighbour set.  This can be done by Control-clicking to open the popup list window and then copying and pasting, or [exporting](KeyConcepts#Export.md) the data to a different format.

# Running a randomisation #

The randomisation analyses are a means of assessing the significance of the analysis results against one or more hypotheses of alternate random structure. At this stage the system only supports randomisation of the BaseData but future developments could also randomise, for example, the nodes on a tree.

To run a randomisation analysis on the currently selected basebata object, open menu option _Analyses -> Randomisation_.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/randomisation_analysis_page.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/randomisation_analysis_page.png)

The Randomisation tab has two main sections where you can set options. The upper section (_Setup_) determines the main setup parameters used in the randomisation, for example the randomisation function and the PRNG seed if you want to reproduce a sequence of random values between randomisations. The second (_Parameters_) are function specific options. At this stage only three randomisations are supported: rand\_csr\_by\_group, rand\_nochange and rand\_structured.

  * _rand\_csr\_by\_group_ randomly reallocates each group with all of its labels to another group's position. The csr stands for Complete Spatial Randomness, although the "complete" is somewhat of a misnomer since the internal structure of the groups stays the same regardless of where they are moved.
  * _rand\_nochange_ merely duplicates the BaseData object. It is useful if you are just plain paranoid and want to test the system.  (Note that cluster results are not guaranteed to be the same in version 0.15 and earlier.  See [issue #253](https://code.google.com/p/biodiverse/issues/detail?id=#253)).
  * _rand\_structured_ allows the replication of richness patterns from the original basedata in the randomised basedata, within some tolerances (as an additive offset and a multiplier). The addition of spatial structure is planned. Complete spatial randomness, where labels are allocated without any structure at all, can be achieved by specifying a richness\_addition parameter larger than the largest richness value amongst the groups.  (Some might think it odd that the most unstructured randomisation is under the structured function, but one should view it as an end-point of a continuum of outputs that this function allows.)

Note that none of these methods will relocate groups to locations that are not part of the BaseData.  Allow and specify [empty groups](SampleSession#BaseData.md) when you import the data if you want to increase the set of locations groups or their labels can be randomly allocated to.

Be careful in your selection of the randomisation function, as each specifies a different null model. Each also has a varying “degree of difficulty”. For example, it is easy for an analysis to be more spatially structured than a completely random reallocation of labels to groups, as the randomisation destroys any spatial structure. It is more difficult to be “better” than a randomisation that replicates other structural features such as species richness.  See for example [Laffan and Crisp (2003)](http://www3.interscience.wiley.com/journal/118882020/abstract).

Once you have specified your parameters, click on the _Randomise_ button (or Control-G on the keyboard). The system will then repeat the randomisation algorithm for the specified number of iterations. As usual, the progress bar lets you know how things are progressing. Once it is completed you are left back at the tab. You can either run more iterations or open the relevant analyses to view the results (see below). If you do run more iterations then it will warn you that any changes to the parameters, except the number of iterations, are ignored. This is to avoid chaos and mayhem in the interpretation of the results -– if you want to assess different parameters then create a new randomisation and run it separately.

All of the spatial and cluster outputs within a BaseData are compared with their randomised versions. Prior to version 0.12 the system does not check to see if new analyses are conducted after a randomisation.  From version 0.12 the user is warned if this is the case.  The reason for this is to avoid (reduce) confusion between outputs.  For example, one could have the case where some analyses in a BaseData have undergone 999 iterations of the randomisation while others were created immediately after the 899th iteration and thus their randomisation results are based on only 100 iterations.


## Interpreting the results ##

See [AnalysisTypes#Randomisations](AnalysisTypes#Randomisations.md) for an explanation of what the randomisation results mean.


# Exporting and saving #

Exporting an entire project is done through the _File_ menu using _Save_ or _Save As_. This preserves all existing basedata, matrix and tree objects – along with their associated analyses – as a “.bps” file. Exporting of the currently selected basedata, matrix and tree objects (as “.bds”, “.bms” and “.bts” files, respectively) is done through their respective menus or through the “save” icons on the toolbar.

Exporting a cluster or spatial analysis is done through the Outputs tab. Select the appropriate output and choose export.

A window will appear to allow the selection of the output format and file type.  The second window allows the specification of the file name and any relevant parameters.


The key options for the table exports are which list to export and whether to force asymmetric lists to be symmetric. One example use of a symmetric table is to generate a matrix of neighbours when using the Element List calculations.  Forcing lists to be symmetric produces larger file sizes but allows for easier import of some results into database programs.  The size difference will be trivial in many cases, but the system can run out of memory for large files (e.g. exporting 100,000 groups with 30+ labels).

The key option when exporting a cluster analysis is whether to use a table, nexus or newick format. Most of the other options relate to the tabular formats (hover the mouse above the values to see the tooltip explanations). For tables, one needs to decide which list values to include (if any), how many cluster groups are needed or whether to specify a length or depth to determine the groups (analogous to the slider bar). See [KeyConcepts#Using\_the\_tree\_exported\_to\_a\_table](KeyConcepts#Using_the_tree_exported_to_a_table.md).