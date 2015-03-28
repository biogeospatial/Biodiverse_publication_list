# Step 3 - Importing Matrix Format Basedata #

This page follows on from step 2 of importing Basedata

**Step 3**  If you specified that your data **were** in matrix format, the following dialogue window will appear.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step3_matrix_format.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step3_matrix_format.png)

At least one column must be set to "Group" using the Type drop-down menu. Selection of a Group column gives the option to define cell size (in the same units as the group data is stored) and origin. Please note that the default cell size is 100,000.00 and default origin is 0.00, these values may need to be adjusted to suit the data being imported.  The origin option allows alignment of the imported data with a non-zero origin when necessary (e.g. when using coarse resolution climate data in a related analysis to ensure the resulting cell boundaries align exactly between data sets).

The "Data in degrees?" combo box allows the importation of data in degrees minutes seconds formats, as well as determining if the values are in the valid range (the latter works for both DMS and decimal degrees formats). Specify is\_lat for latitude and is\_lon for longitude. Examples of valid formats are:
```
Latitude,Longitude
S23°32'09.567", E149°23'18.009"
23°32'09.567"S, 149°23'18.009"E
-23 32 9.567, +149 23 18.009
-23.535991, 149.388336
```

Matrix import differs from the standard import process in that there is no Label option in the drop-down menu.  Instead the options "Label\_start\_col" and "Label\_end\_col" denote which column headers to use for the Labels.

**Label\_start\_col** must be assigned to at least one column.

**Label\_end\_col** is optional. If not specified then the system will use all columns after the "label\_start\_col".

If more than one start and/or end column is specified then the system will use the first start\_col and last end\_col (see [issue #164](https://code.google.com/p/biodiverse/issues/detail?id=#164)).

If one or more "label" columns precede the group column/sthe file will need to be edited and the column moved so it is after the Groups.  The system currently only allows one option per column so it cannot be both start and end.

The Type drop-down menu also allows filtering of data rows by assigning the column types "Include\_columns" and "Exclude\_columns". There is no limit on the number of these column types that can be assigned. If one or more inclusion column is specified, only those data rows with non-zero values in at least one of these columns will be imported. If one or more exclusion column is specified, only those data rows with a value of zero in all of these columns will be imported (ie. any non-zero value will trigger a row to be excluded).

Take care not to specify a column in the Label range as “include” or “exclude” as it may negatively impact on your results (although it is a valid selection in some circumstances, for example if presence of a species should be used to exclude a sample row).

Columns marked as “ignore” but between a label\_start\_col and label\_end\_col will be imported (“ignore” is the default setting).  To skip columns between the label start and end columns it is recommended that an exclude column be set in a label remap file.

Remember that the values for each row of a matrix are the sample counts To view presence/absence data per group ensure that you have selected the “Convert sample counts to binary” option on the preceding Import options window.

Finally, use a [label remap/property table](DataStructures#Element_property_tables.md) to change the column names, for example to separate genus and species into separate axes for analysis.

Click OK.

**Next Page – Step 4 Click here to go to the next Import Basedata page**