

# Overview #

This serves as the main interface to the help system.  Eventually it will consist of a set of links to other pages.  It is very much a work in progress at the moment.

The key point to keep in mind when using Biodiverse is that it has been developed first for spatial analyses. This includes the Moving Window, Clustering and Randomisations. All of the code has been written under this framework. Any other analysis that can be conducted is in some senses incidental. This does not mean it is invalid, just that it needs to be cast in a spatial framework to run.

# Data Structures #

See DataStructures.

# Analyses #

See AnalysisTypes.

# Spatial conditions #

See the SpatialConditions page.

# Colour schemes #

## Hue and saturation modes ##

Numerically continuous analysis results can be displayed using either Hue or Saturation modes.

The hue mode uses colours from light blue through green and yellow to red.  It is the default for spatial results.

The saturation mode assigns colours as different levels of saturation for a single colour, the default being red.  (This is the scheme used in the view labels tab).  You can select an alternate colour using the colour button to the right of the chooser.  Note that greyscale is currently not supported (at version 0.12), and the system only uses the hue setting, ignoring any saturation and value settings.  See [issue #32](https://code.google.com/p/biodiverse/issues/detail?id=#32).

If you are unsure of how visible your results will be to the colour blind then take a screen shot and put it through the Daltonizer at http://www.vischeck.com/daltonize/ .  Saturation mode should be better than hue in these cases.


## Contrasting colour scheme ##

Cluster analyses can be displayed as aggregates of nodes using the contrasting colour scheme.

The contrasting colour scheme is restricted to a maximum of 13 colours, with a different colour scheme used for 9 or fewer. The schemes are derived from http://www.colorbrewer.org, but with the addition of a mid-grey to the 12 colour scheme. We have experimented with more colours, but found them difficult to distinguish (which is pretty much as recommended on the ColorBrewer web site...).

# Map overlays #

You can display a feature (vector) data set in the group grid pane as a background to make it easier to identify groups, especially if they are geographically related.  An example might be a map of national borders or of bioregions.

Overlays are available when a map is displayed, for example when viewing labels or displaying the results of a cluster or spatial analysis (see [SampleSession#The\_Group\_Grid](SampleSession#The_Group_Grid.md), [SampleSession#Viewing\_the\_cluster\_results](SampleSession#Viewing_the_cluster_results.md) and [SampleSession#Viewing\_the\_spatial\_results](SampleSession#Viewing_the_spatial_results.md)).

To plot an overlay, select the Overlays button in the panel. A list of the currently available overlays will be displayed. To add a new overlay, click Add, and select the desired overlay file.  Your selected file will be added to the list of available overlays. To display it in the group grid, select it and click Ok. It may take a few seconds for the overlay to appear. To remove the currently displayed overlay, open the Overlays menu again and click the Clear button. Note: clicking Delete in the Overlays window will delete the shapefile from the list, but will not remove it from the display if it is currently being displayed. You must click Clear as well. Using an overlay may result in noticeably slower display processing (e.g. when highlighting groups), particularly with more detailed shapefiles. This is due to the amount of display refreshing that must be done.

Only shapefiles are supported at the moment. They also need to be polyline or polygon. Points are not plotted, but you could buffer your points by a small distance and plot the resulting polygons.

Several data sets can be loaded but only one can be displayed (see [issue #48](https://code.google.com/p/biodiverse/issues/detail?id=#48)).  If you wish to plot more than one set of features then combine them into a new data set using a GIS.

The system also ignores any vertices that are beyond the bounds of the BaseData groups, so you cannot zoom out any further than the BaseData extent.


# Using the spatial index #

A spatial index can only be set if there is a selected BaseData object.  It is saved as part of the BaseData object it is related to.

The spatial index speeds up processing by reducing the number of comparisons that need to be made when assessing if a group is a neighbour of the processing goup.  Exactly how much of a speed up is a function of the index resolution and the spatial condition specified (larger neighbourhoods take longer as they use more index blocks and therefore the system must make more comparisons).

As an example of the speed up, an analysis of approximately 20,000 groups took ~3600 seconds for a four cell radius circular neighbourhood without the index. With the index it took 30 seconds. Similarly, an analysis with a radius of one cell also took ~3600 seconds without the index and 12 seconds with it.

The reason for the speed-up is that the system no longer needs to assess every other group in the BaseData as a possible neighbour, and instead focusses only on those groups that occur within the indexed blocks that satisfy the spatial condition. Think of the search through the index returning a coarse first approximation to the neighbours, with a second search refining the solution to the actual set of neighbours.

Most spatial conditions one will use are likely to be simple and use the available functions.  In these cases the system can precalculate which index bocks (elements) to search.  However, if you are using complex spatial conditions then it must search the index to determine which index blocks should be assessed as containing possible neighbours in the analysis.  This can take some time when using a fine resolution index as it must assess each corner of the index extents, and every one of each corner block's immediate neighbours, against every other possible index block.  This results in `(m^2 * 3^m * n)` comparisons, where `n` is the number of index blocks and `m` is the number of axes (dimensions) used.  This works out to `4*9n = 36n` for a data set with two group axes.  The final analysis should still be faster for most calculations, though.

The system will ignore the spatial index if the spatial conditions used specify it must be ignored, for example with the text matching conditions.  It can also be turned off (deleted) if needed by using the _Analyses->Index_ menu.

The optimal size of the spatial index is a function of the spatial conditions specified.  The default is twice the resolution of each axis, and this will work reasonably well for most analyses.  For analyses where the spatial conditions do not involve user defined conditions then setting the index to the same size as the BaseData group resolutions should be fastest.  For cell sizes of zero you should start with an index resolution similar to the analyses being run and experiment from there.  For cases where the system must search the index to find possible neighbours then the optimal size is a trade-off between the initial search and the number of subsequent searches (think of this in terms of the pay-off in the shorter analysis time given the investment in the initial index search).

Note that the index can be deleted and rebuilt at any time, and these changes affect only subsequent analyses, not those that preceded any change.

It is also worth noting that the spatial analyses are optimised to skip searching for neighbours in cases where an analysis is using the same spatial conditions and definition query as another spatial analysis in that BaseData.  In such cases, the analysis copies the neighbour sets across from the other BaseData.  This can substantially increase the speed of any analyses, but will obviously affect any comparison between index size experiments suggested above.  In such cases you should delete the analysis output before re-running with a different index configuration.

# NoData #

NoData represents an unknown or undefined value.  It is commonly used in geospatial analysis software.

NoData will occur in certain analyses when no reasonable value can result, for example where there is a division by zero or where there are no valid labels in a neighbourhood, e.g. a matrix analysis was run, but there are no labels in the neighbourhood that are listed in the matrix and therefore no value can be assigned that is a function of the matrix.  It is a bad idea to use zero in these cases, as it often has a meaning of its own, for example 0 for a Jaccard dissimilarity means the two sets of neighbours are identical. Hence the use of NoData.

Groups with a value of NoData are plotted as white.  (Black means the group was not included in the analysis, and is typically the case in a cluster analysis if a neighbourhood or definition query is specified).

NoData in Biodiverse is stored internally using Perl's special `undef` value (meaning undefined).  The NoData value can be changed on export if needed, and for the raster outputs is set to -9999 by default.  A value of zero is possible but, as explained above, it not a good choice in most cases.  Typically it is best to leave the nodata value as `undef` and let the system change it if needed (which it does for the raster exports).


# Other topics #

## Calculations ##

These are the collections of indices that are run in the moving window and cluster analyses.  They are actually a type of analysis, but the terminology would then clash with that used for the cluster and moving window analyses.


## Specifying extensions ##

_Need to explain the specification of extensions and how to load them._


## The ABC lists ##

These lists appear in the popup windows. They might look odd at first, and are in some senses left over from the early system development when most indices depended on some function of A, B and C.

These are based on the fundamental components used for the dissimilarity metrics. **A** is the count of shared labels, **B** is the count of labels found only in the first group, **C** is the count found only in the second group.

**ABC2** also keeps track of how many groups each label occurs in for the set of groups specified, while **ABC3** reports the number of samples. **ABC2** is used in, for example, endemism calculations while **ABC3** is used for those needing counts, for example redundancy.

## Scree plot ##

The scree plot below a tree indicates how many nodes occur at each level of, for example, dissimilarity.

## Selecting tree nodes ##

See [SampleSession#The\_Tree](SampleSession#The_Tree.md) and [SampleSession#Viewing\_the\_cluster\_results](SampleSession#Viewing_the_cluster_results.md).


## Negative length nodes ##

Negative length nodes (those that go backwards) often occur when using link\_recalculate clustering or when switching from spatial to non-spatial clustering. In the latter case this is because the two most similar clusters may not be within the spatial neighbourhood specified, and so the similarity of the non-spatial clusters will be closer to zero than the final spatial clusters. In the former case, the recalculation weights each label equally (for most similarity metrics), so the merging of two clusters may actually reduce their joint dissimilarity with the other clusters in the system.  The end result is a nodel linkage that moves towards zero instead of away from it.

See [this image](http://biodiverse.googlecode.com/svn/wiki/screenshots/cluster_analysis_results_page_recalc_linkage.png) for an example.

If the negative nodes make interpretation difficult then change the display [to plot by depth](http://biodiverse.googlecode.com/svn/wiki/screenshots/cluster_analysis_results_page_recalc_linkage_plot_by_depth.png).

## Cluster Linkages ##

See [SampleSession#Cluster\_parameters](SampleSession#Cluster_parameters.md).


## Supported file types ##

### Import ###

BaseData and Matrix objects can import from text files such as CSV or TXT. They currently guess the field separator by default,
but this can be specified as an argument if guesswork is unsuccessful.

Trees can be imported from Nexus files. NeXML support is planned.

Matrices do not care if the matrix is upper right, lower left, both, or any combination of the above.
They will store the last defined value for an element pair (reading left to right, top to bottom).

### Export ###

Spatial and cluster objects can be exported to table formats. Supported formats include delimited text (txt & csv), html table (htm), XML and YAML.  The latter two are probably not as useful as the others.

Exports to shapefiles are not supported due to a fatal error in the library we are using, and also due to DBF field name limitations (see below).  They can, however, be recreated from the other formats after import to a GIS or by using a suitable library.

BaseData objects that use square cells and have only two axes can be exported to raster formats.  Currently the system supports Arc/Info asciigrid and floatgrid format, as well as ER-Mapper ERS format.  Note that the first two options will produce multiple files with the index name inserted before any specified file extension (e.g. fred.asc can result in `fred_ENDC_CWE.asc` and `fred_ENDC_WE.asc`).  The ER-Mapper export produces `fred` (the data file in Band Interleaved by Line, or BIL, format) and `fred.ers` (the header file).  Note that the ERS file does not include band statistics so these need to be calculated for them to plot properly in ArcMap (see [the FAQ](FAQ#Results_exported_to_ER-Mapper_BIL_files_do_not_display_properly.md)).  Exporting labels with more than one column could cause issues with the .flt and .asc files, as the colon used to separate the columns is a protected character as far as Windows filenames are concerned (and probably other operating systems).  This has been addressed in version 0.15 (see [the FAQ](FAQ#Why_do_my_asciigrid_or_floatgrid_files_have_strange_characters_l.md)).

Cluster objects can also be exported to the Newick and Nexus formats (Nexus actually uses the Newick format for trees).

_Note:_ The DBF format only allows field names of ten characters.  This is not long enough for many of the index field names so DBF export has been disabled.

_Note:_ If you are exporting an asymmetric array list as a symmetric structure then the system will use the array elements as the field names and insert a 1 in each of the columns where that column element is in the list for that row element. This is because it does not have any values associated with it. If it did then it would be stored as a hash, which is a series of key/value pairs where each key is unique.  Array lists are just a sequence of values and can contain repeated values.  They are used for some of the numerical label statistics and also randomisation results for the cluster trees.

## Using the tree exported to a table ##

### Tabular tree ###

The tree structure is a table allows the storage of the tree's topology in an RDBMS or other structure, including other list data such as from a spatial analysis run for each node of a cluster tree.  These cannot currently be exported using the Newick format.  (It should be possible by repeating the tree for each list element with the values stored as the bootstrap values for each node, but this is potentially very messy).

_Need to add an example table._

### Table grouped ###

This is a means of exporting the tree to an RDBMS format but retaining a classification as used for displaying clusters (see [SampleSession#Viewing\_the\_cluster\_results](SampleSession#Viewing_the_cluster_results.md), but a few images down).  One can choose two types.  First, one can cut the tree along a line at a specified depth or length.  This is a means of exporting the result of a slider bar display.  Second, one can specify a number of clusters are to be selected below the root node.  This approach is the same as colouring using a mouse click on the root node.

_Need to add an example table._