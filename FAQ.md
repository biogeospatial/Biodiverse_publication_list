This is a list of questions that might be frequently asked.  It will be extended as more questions come to light.




# General Questions #

## I have a question about how to use the software ##

Check the help pages on the wiki (HelpOverview or http://code.google.com/p/biodiverse/w/list).  If it is not covered there then please contact the developers, or join the Biodiverse-Users google group and post a question there.  http://groups.google.com/group/biodiverse-users

## Where can I get sample data to experiment with? ##

Sample data are distributed with the software.  Look in the data folder.  The Readme.txt file explains what they represent.

You can download other geolocated data from a variety of sources, for example [GBIF](http://data.gbif.org/) or [Australia's Virtual Herbarium](http://www.ersa.edu.au/avh/).  There are also many sources for trees, e.g. the [Tree of Life](http://tolweb.org/tree/).


## I have found a bug ##

Please submit bugs via the Issues list at http://code.google.com/p/biodiverse/issues/list

## I would like a new feature to be added to Biodiverse ##

These are also submitted via the issues list.  Just specify the type label as Type-Enhancement (click on the _Type-Defect_ box to open the menu containing this option).  http://code.google.com/p/biodiverse/issues/list

## Does it only work on Australian data? ##

No, we just use Australian data for the examples.  It will work on any data you give it.

## Will it work with non-geographic data? ##

Yes, Biodiverse is essentially ignorant of geography.  It will work on any data you give it.  (Whether the analysis is appropriate or not is a different issue).

## What are groups and labels? ##

See [DataStructures#BaseData](DataStructures#BaseData.md)

## What are labels without groups? ##

These are the label version of the empty groups.  They allow the system to consider additional labels in analyses, for example where labels are not in your data set but still need to be considered in an analysis using a tree.  One can set label properties for these, such as label ranges, and they will be considered in any analyses.  An example might be a phylogenetic endemism calculation for Australia, where the phylogeny includes species from outside of Australia.  (Please note that this needs to be tested more thoroughly than it has thus far).

# Data import #

## I imported my data and it only has one cell ##

Make sure your cell size is appropriate for your data.  It needs to be in the same units, as Biodiverse knows nothing about where your data come from and cannot compensate.  For example, if you are using latitude/longitude data then the default cell size of 100,000 will wrap around the planet many times.  Use a size of 0.25, for example, to produce quarter degree cells.  If you are using data in a projected coordinate system with metres as the units, then use 25000 to obtain a 25 km cell size.  If your data are in millimetres, e.g. from a petri dish, then a cell size of 10 will result in each cell being one square centimetre.

## My species list has been provided as a site by species matrix.  How do I import it? ##

Turn on the checkbox next to _Data are in matrix form?_ when importing.  See [SampleSession#BaseData](SampleSession#BaseData.md).

## Can I skip a subset of species when importing data? ##

Yes.  Use an Element Property table for this purpose, specifying one or more exclude and/or include columns.  See [DataStructures#Element\_property\_tables](DataStructures#Element_property_tables.md).  From version 0.18003 you can also exclude (delete) some labels after you have imported them.

## Where is the menu option to load an element properties table? ##

There isn't one at the moment.  Properties tables are loaded as part of the [BaseData import process](SampleSession#BaseData.md).  If you are [importing multiple files into the same BaseData object](SampleSession#Adding_to_an_existing_data_set.md) then unfortunately you will need to import the properties table each time.

## Can I import more than one file at a time? ##

Yes, for BaseData objects.  Note that this requires that each input file has the same column order (the headings can differ, but the contents must have the same meaning).

It is possible to do this for a standard import.  Importing from matrix format files needs to be tested.

If your input files do not have common headings then you can import them sequentially into an existing BaseData object.  See [SampleSession#Adding\_to\_an\_existing\_data\_set](SampleSession#Adding_to_an_existing_data_set.md).


# Analyses #

## What is the difference between the central and whole endemism calculations? ##

The underlying calculations are the same between the two calculations.  The only difference between them is the set of labels (e.g. species) used in the calculations.  In the endemism whole calculations (those indices starting with ENDW) the list of species and their local ranges are taken from both neighbour sets, effectively treating the two neighbour sets as a single combined neighbour set.  In the central calculations (those indices starting with ENDC) the list of species is taken from the first neighbour set but the local ranges used in the numerator are taken across both neighbour sets.

In essence, the difference is in the question asked.  For the ENDW calculations it is "to what degree are the labels in my neighbour sets endemic to the area defined by neighbour sets 1 and 2", whereas for the ENDC calculations it is "to what degree are the labels in neighbour set 1 endemic to the area defined by neighbour sets 1 and 2".

If you have only one neighbour set then the two calculations will produce identical results.

## What neighbourhood size should I use? ##

The choice of neighbourhood size is one of those hoary old chestnuts that affects all spatial analyses.  Neighbourhood size is analogous to a spatially moving MAUP ([modifiable areal unit problem](http://en.wikipedia.org/wiki/Modifiable_areal_unit_problem), of which [gerrymandering](http://en.wikipedia.org/wiki/Gerrymandering) is a good example).  See Chapter 2 of [O'Sullivan and Unwin, 2010, Geographic Information Analysis](http://dx.doi.org/10.1002/9780470549094) for a good introduction to this and other general issues of spatial analysis.

One approach to neighbourhood selection is to approach them from the perspective of "At what neighbourhood size is my analysis result optimised?"  In the case of endemism, one looks for the size of neighbourhood that maximises endemism, possibly also assessing the rate of change of endemism with increasing neighbourhood size (see for example [Laffan and Crisp, 2003](http://www3.interscience.wiley.com/journal/118882020/abstract)).  This principle applies to any spatial analysis, though (see [Bickford et al., 2004](http://dx.doi.org/10.1111/j.1365-2699.2004.01127.x), [Laffan, 2006](http://dx.doi.org/10.1111/j.1365-3180.2006.00491.x)).  One can also develop neighbourhoods based on the assumed controlling process and compare them with other simpler neighbourhoods ([Laffan, 2002](http://dx.doi.org/10.1080/13658810110099107)).

One can also use the cluster analyses to define neighbourhoods based on the data themselves.  Simply choose a set of calculations to run at the bottom of the cluster window (see [SampleSession#Running\_calculations\_for\_each\_node](SampleSession#Running_calculations_for_each_node.md)).  (Note that this method will only run those analyses that require a minimum of one neighbour set, so indices such as those that measure dissimilarity between two sets of neighbours cannot be calculated).

## How does the system use the spatial conditions when clustering? ##

The way it works is that every group pair that satisfies the first condition is clustered together.  Once there are no more of these to cluster it starts to use those that satisfy the second condition.  If there is anything left over that did not satisfy either condition then all of the nodes are lumped together under a single root node, taking the node with the longest total length as the position of the root.

One benefit of this approach is if one has an axis that represents a region.  One can set a condition to consider only within-region group-pairs (e.g. `sp_match_text()` or `sp_match_regex()`), followed by one that considers all pairs.

In most cases one would set the second condition to use all pairs (`sp_select_all()`), which is the same as reverting to a non-spatial clustering.  However, sometimes one might wish to use to increasing spatial lag distances.  The GUI currently only supports two conditions but any number can be specified through a script.


## Why do I get different randomisation results on a 64 and 32 bit machines? ##

This is due to the pseudo-random number generator (PRNG) library the system uses.  For a given seed value it generates a vector of integers as the starting state for the PRNG sequence.  On 32 bit machines these are 32 bit vectors, while on 64 bit machines these are 64 bit integers, thus differing between architectures.  To avoid confusion, the system will throw an exception if you try to continue a randomisation analysis on one architecture which you started on the other architecture.


## I want to analyse environmental data ##

Biodiverse supports the analysis and aggregation of environmental variables but these need to be imported into their own basedata object (preferably using the same cell size and origin as the species data).  You can use the [numeric labels](Indices#Numeric_Labels.md) calculations to get summaries of their distributions.  The species and environmental data can be combined afterwards in a stats package, database or spreadsheet and then analysed for correlations and the like.  One can also import environmental data as label or group properties, for which calculations will be part of version 0.16 ([issue #212](https://code.google.com/p/biodiverse/issues/detail?id=#212), [issue #207](https://code.google.com/p/biodiverse/issues/detail?id=#207) and [issue #214](https://code.google.com/p/biodiverse/issues/detail?id=#214)).  Label properties can be viewed in the [View Labels](SampleSession#Visualising_data.md) tab in version 0.15, though.

## My structured randomisations do not have constant richness scores ##

The rand\_structured randomisation function with arguments rand\_multiplier=1 and rand\_addition=0 is only guaranteed to keep the species richness constant in each group.  If your neighbourhood includes more than one group then the randomly assigned richness will not be constant across the neighbourhood.  While it is constant per group, the randomised assemblages in neighbouring groups differ, and thus the richness across the neighbour set will differ from that of the original.  This effect will be most noted in the endemism and richness calculations.

Consider an example where a neighbour set of two groups has four distinct labels, with Group 1 containing three (labels A, B & C) and Group 2 containing three also (labels B, C & D).  In the randomised version each of Groups 1 and 2 will have three labels, but this could be a distribution where Group 1 has labels C, D & E while Group 2 has labels X, Y & Z.  This is an aggregate richness across the neighbour set of six.

Is there a cure?  Not really.  It is more of a feature since the randomisation is operating as designed.  If you want to reduce the effect then you will need to wait for the spatially constrained randomisations to be implemented ([issue #76](https://code.google.com/p/biodiverse/issues/detail?id=#76) and [issue #160](https://code.google.com/p/biodiverse/issues/detail?id=#160)).  While these will not be guaranteed to make the richness of each neighbour set constant, they will be closer since they will assign labels in a spatially clustered fashion (depending on the spatial constraint specified, and also on the spatial clustering of labels in the original data set).

## My phylogenetic analyses have empty results ##

This is likely caused by the BaseData and tree having non-matching labels and node names, respectively.  The way to correct it is to use a [properties table](DataStructures#Element_property_tables.md) on import to remap the names of one to match the other.  Which one to remap depends on your circumstances.  If multiple BaseData labels are represented by a single node on the tree then it is probably best to remap the BaseData.  If you wish to run other analyses that use the hierarchies implied by a label name (e.g. Family::Genus::Species in the [hierarchical labels](Indices#Hierarchical_Labels.md) and [endemism partitioning](Indices#Endemism_central_hierarchical_partition.md)) then remap the tree node names to match the BaseData.  In cases where neither is needed then it will probably not matter.

The way to test if the BaseData labels match the tree node names is to use the [View Labels](SampleSession#Visualising_data.md) tab.  If they match then the appropriate labels and nodes will be selected in each pane.

## Why aren't there analysis results everywhere? ##

By default, Biodiverse only stores groups with data in them.  The effect of this is that, when you run your analysis, it will only consider those groups in the data set.

This approach is useful for two reasons.  First, it restricts calculations to those locations that have data and therefore reduces the smoothing effects that can occur if all neighbouring locations are used (this can sometimes give a misleading impression of data continuity).  Second, it makes for smaller data sets, thus saving a bit of memory (albeit that's less important than accuracy).

All of that said, it's up to the user to decide how they want to run their analysis.  If you want to include empty cells in your analyses then these need to be enabled at the time of import by checking the "Allow empty groups?" check box in the import properties.  You will need to provide a data set of cell coordinates for Biodiverse to use, or include them in the original import file.  Go to [SampleSession#BaseData](SampleSession#BaseData.md) and look for the second screen shot and the subsequent para starting with 'Both the _empty groups_ and...'.  (Note that this is broken in version 0.15 - see [issue #180](https://code.google.com/p/biodiverse/issues/detail?id=#180)).

## What is length vs total length in the cluster analyses? ##

Length is the length of the node clicked on.  Total length is the length from that node to the tip of the tree (and should probably be renamed).

## What are total\_length\_gui and `_`y in the cluster analyses? ##

These are display parameters used by the system and can be ignored.

# Exported data #

## What coordinate system are my data in? ##

Biodiverse knows nothing about coordinate systems and does no transformation of coordinates except to snap them to the group coordinates using the cellsize you set at import.  This means that the results are in whatever coordinate system your input data were in.

The good news here is that, in your GIS software, you can then define the coordinate system for any exported files to be the same as for your input data.

Once that is done then software that does on-the-fly projections for display will be able to plot any other data over your Biodiverse results.  The reverse is also true.

If your GIS software does not support on-the-fly projections then you can project the other data to the same coordinate system as your Biodiverse data.  Note that projecting the Biodiverse results can result in resampling distortions which might be undesirable in subsequent analyses.

Note that there is one known issue with ER-Mapper files ([listed below](#My_ER-Mapper_BIL_file_is_offset_by_half_a_pixel.md)).


## How do I export as a raster? ##

Use the ER-Mapper BIL file, ArcInfo Asciigrid or ArcInfo Floatgrid options.  From version 1 you can also use GeoTIFF.

These are currently not supported for the cluster analyses (see [issue #161](https://code.google.com/p/biodiverse/issues/detail?id=#161)).  In that case, export to delimited text and then import this as a point data source and convert to raster.  It is probably best to use the grouped option for this, as it will not have overlapping node ranges.  Alternately, select each node in turn and create a separate raster using its terminal nodes (this will need a scripting approach).


## Results exported to ER-Mapper BIL files do not display properly in ArcMap ##

You will need to calculate statistics for the image for it to display properly (before displaying it).  This can be done in ArcCatalog by right clicking on the file and choosing Calculate Statistics, or by using the _Calculate Statistics_ tool in ArcToolbox.

If you calculate statistics while displaying the image in ArcMap then it will not work properly.   This is possibly because it does so for only the subset of bands being displayed, and then cannot save the file correctly.  Doing the whole file using the approach above gets around this.

## My ER-Mapper BIL file is offset by half a pixel ##

Note that this will no longer apply in Biodiverse Version 1.  Users of ArcGIS 9 will need to correct it using the Shift tool in ArcToolbox.  See [issue 453](https://code.google.com/p/biodiverse/issues/detail?id=453).

The ER-Mapper file export is written to work with ArcMap 9.  However, ArcMap 9 seems to use the centre of the registration cell as the location of the registration coordinate.  This results in an offset of 0.5 pixels to the north and west when it is plotted using some other system like Erdas or ER-Mapper.  The solution is to edit the header file and change these two lines:
```
RegistrationCellX  = 0
RegistrationCellY  = 0
```
to be
```
RegistrationCellX  = 0.5
RegistrationCellY  = 0.5
```

The system behaviour was set for ArcMap 9 under the assumption that more people were using it for display.

## Why do my exported raster files have strange characters like %3A in the names? ##

This applies to version 0.15 and later.

The operating systems do not normally allow certain characters in filenames, for example colons, quotes or backslashes.  If these characters are used in the filenames then exports of groups to the single band raster formats like geotiff, ascii and floatgrid formats will fail, as the file names cannot use the actual names (the colon is a separator, and quotes are often used to obey CSV rules).  Changing the characters to the URI escaped forms gets around this (see [issue #129](https://code.google.com/p/biodiverse/issues/detail?id=#129)).  For a list of the characters and their escaped forms, see http://www.december.com/html/spec/esccodes.html


# Known issues #

See also the Issues list http://code.google.com/p/biodiverse/issues/list

## Biodiverse crashes and disappears without any message ##

This is most likely an [out of memory error](#I_get_an_Out_of_memory_error.md).

## I get an Out of memory error ##

In some cases the system will use up all the available memory, following which it will crash.  Specific cases are the randomisations (see [issue #5](https://code.google.com/p/biodiverse/issues/detail?id=#5), fixed in version 0.19) and when one is using a 32 bit system to work with a large BaseData object (e.g. >100,000 groups and ~60 labels) and tries to save the data set while also displaying several outputs.

On most 32-bit operating systems the maximum memory allocated to a process is 2GB. On Linux it is 3GB, and server versions of Windows can be configured for 3GB.  If more than this is needed then the system will crash.  There is also the issue that Perl's memory management system is not perfect, and also does not free memory to the system under the assumption it will need it again later for a pience of code.  For large processes the system runs out of available memory and crashes.

Closing Biodiverse and restarting it will clear any memory no longer needed, but does not solve all cases involving large data sets.  In this case one should close any open tabs in the GUI before exporting or saving, as the memory used for the GUI section is freed and returned properly.  One can also subdivide the analyses and run them separately (i.e. a small number of analyses per duplicate BaseData).  Randomisations for these duplicates can be reproduced by specifying the same starting seed and parameters.

If that does not not work then the next solution is to move to a 64 bit system which allows more memory per process.  Make sure Perl and GTK are both 64 bit, as 32 bit implementations still have the 2GB memory limitation on these systems.  Note that the issue will still affect 64 bit systems, but that one can get much further before crashing.

An alternate solution, if a 64 bit system is not available, is to subdivide the BaseData object into tiles before analysis.  This works well for most moving window analyses, but cluster and randomisation analyses will not produce correct results as the groups and labels they use will be restricted to each tile.  One must also ensure the tiles have overlapping boundaries to ensure the moving window analyses have the correct neighbour sets (the degree of overlap depends on the neighbour set used).  Indices that use global statistics, such as the global range used in the endemism indices, also need some care.  Global ranges and global sample counts can be set using an Element Properties table when importing the BaseData (see [DataStructures#Element\_property\_tables](DataStructures#Element_property_tables.md)).  This can be constructed from the whole data set by calculating the endemism and rarity lists with a spatial condition set to `sp_select_all()`, and then extracted by control clicking on the displayed results to see the lists, from which the values can be copied into a spreadsheet or other program.  (This assumes you can display the results without the crash.   If not then a script is the only way to extract the data).

For the randomisations we have also developed a command line tool that runs the randomisations a small number of iterations at a time and then restarts the process (load\_and\_randomise\_wrapper).  This was released in version 0.14, and documentation are at the LoadAndRandomise page.  Note that, since [issue 5](https://code.google.com/p/biodiverse/issues/detail?id=5) was fixed, this has been superseded by the run\_randomisation utility (see the RunRandomisation page).

## Opening the help system on Linux does not return focus to Biodiverse ##

This seems to be an issue with the command used to open the browser, or possibly the operating system.  The solution is to open the browser outside Biodiverse before accessing the help.