# Standard Basedata Import (continued) #

This Page follows on from the Import data Page **(Check Name)**

**Step 3**  If you specified that your data **were not** in matrix format in step 2, the following Choose columns dialogue box will appear.

![http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step3.png](http://biodiverse.googlecode.com/svn/wiki/screenshots/import_basedata_step3.png)

At least one Group and one Label column must be set from the "Type" drop-down menu, but more than one of each may be chosen where appropriate.  For example:

  * Both a "species" column and a "genus" column (if separated in your file) may be set as one combined label for your data points; or
  * In order to specify a Cartesian grid both the x-coordinate and y-coordinate columns in a file need to be set as "Group" (specifying only an "x" column or "y" column as the Group would result in a one-dimensional analysis of the data across that group's domain).

Selection of a Group column gives the option to define cell size (in the same units as the group data is stored) and origin. Please note that the default cell size is 100,000.00 and default origin is 0.00, these values may need to be adjusted to suit the data being imported.  The origin option allows alignment of the imported data with a non-zero origin when necessary (e.g. when using coarse resolution climate data in a related analysis to ensure the resulting cell boundaries align exactly between data sets).

The "Data in degrees?" combo box allows the importation of data in degrees minutes seconds formats, as well as determining if the values are in the valid range (the latter works for both DMS and decimal degrees formats). Specify is\_lat for latitude and is\_lon for longitude. Examples of valid formats are:

```
Latitude,Longitude
S23°32'09.567", E149°23'18.009"
23°32'09.567"S, 149°23'18.009"E
-23 32 9.567, +149 23 18.009
-23.535991, 149.388336
```

The _Type_ drop-down menu also allows filtering of data rows by assigning the column types "Include\_columns" and "Exclude\_columns".  There is no limit on the number of these column types that can be assigned.  If one or more inclusion column is specified, only those data rows with non-zero values in at least one of these columns will be imported. If one or more exclusion column is specified, only those data rows with a value of zero in all of these columns will be imported (ie. any non-zero value will trigger a row to be excluded).

If a file contains columns that are irrelevant to the analysis, these columns should be set to "Ignore".

**Click OK.**

Next Page – **Step 4 Click here to go to the next Import Basedata page**