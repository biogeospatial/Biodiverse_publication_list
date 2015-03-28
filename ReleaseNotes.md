

# Version 0.99 #

This is a development release series, leading towards version 1.0.

Collectively, these releases comprise several major changes to the underlying code-base, as well as the addition of a number of major new features.  They are not backwards compatible with previous versions (0.19 and earlier) in several respects.  They can still use most Biodiverse files created using earlier versions, but files created using this version are not guaranteed to work with earlier versions.

For the full list of issues and changes leading to the 1.0 release, see http://code.google.com/p/biodiverse/issues/list?can=1&q=label%3AMilestone-Release1.0

To see the full list of open issues or to report a bug or enhancement request, see http://code.google.com/p/biodiverse/issues/

## Version 0.99\_007 ##

This is the seventh phase of the development version leading towards version 1.0.

Main changes since the preceding version ([0.99\_006](#Version_0.99_006.md)) are below.  Issue numbers which are not crossed out are yet to be completed.

  * GUI
    * The label selection mode can now be set, so in addition to being able to create a new selection each time one of the grid, tree or matrix panes is clicked, users can now also add to or remove from the current selection.  This allows the selection of, for example, distinct clades on the tree.  These might then be deleted from the basedata using the deletion methods added in the previous development release.  [Issue 535](https://code.google.com/p/biodiverse/issues/detail?id=535)
    * Fixed a crash when a tree was trimmed and had no remaining branches, and a View Labels tab was open.  [Issue 534](https://code.google.com/p/biodiverse/issues/detail?id=534)


## Version 0.99\_006 ##

This is the sixth phase of the development version leading towards version 1.0.

Main changes since the preceding version ([0.99\_005](#Version_0.99_005.md)) are below.  Issue numbers which are not crossed out are yet to be completed.

  * GUI
    * The new pan and zoom functionality now works consistently across all views (maps, trees and matrices).  [Issue 353](https://code.google.com/p/biodiverse/issues/detail?id=353)
    * New functions have been added to work with the selected labels.
      * Labels can be selected using partial text matches.  These use regular expressions, so can be as complex as is needed, but the simplest case is just a fragment of the label name.  Selections can optionally be added to or removed from.  [Issue 529](https://code.google.com/p/biodiverse/issues/detail?id=529)
      * Selected labels can be deleted from the basedata, or new basedatas can be created using the selected (or non-selected) labels.  [Issue 528](https://code.google.com/p/biodiverse/issues/detail?id=528).
      * The selected set can be switched (inverted) so all non-selected labels become the selected set.  [Issue 532](https://code.google.com/p/biodiverse/issues/detail?id=532)
      * The selected set (labels and the groups in which they occur) can be exported directly from the View Labels tab.  [Issue 414](https://code.google.com/p/biodiverse/issues/detail?id=414)

  * Export/import
    * Trees exported from Biodiverse now roundtrip properly when labels are quoted.  [Issue 270](https://code.google.com/p/biodiverse/issues/detail?id=270)
    * Sparse format matrix files can now be imported in the GUI.  [Issue 82](https://code.google.com/p/biodiverse/issues/detail?id=82)
    * Matrix exports now use a progress dialog to avoid a non-responsive GUI.  They also write direct to file to reduce memory overheads.  [Issue 517](https://code.google.com/p/biodiverse/issues/detail?id=517)
    * Basedata imports are now faster.  The effect is greatest for raster imports where there is no transform in place.  [Issue 527](https://code.google.com/p/biodiverse/issues/detail?id=527)

  * Analyses
    * In the spatial analyses, users can control the use of the spatial index across the whole analysis, or on a per-spatial condition level.  [Issue 205](https://code.google.com/p/biodiverse/issues/detail?id=205)
    * Control is also available for result and neighbour set recycling (the system detects these correctly in most cases, but it is useful to control it in falsely detected cases).  [Issue 205](https://code.google.com/p/biodiverse/issues/detail?id=205)

## Version 0.99\_005 ##

This is the fifth phase of the development version leading towards version 1.0.

Main changes since the preceding version ([0.99\_004](#Version_0.99_004.md)) are below.  Issue numbers which are not crossed out are yet to be completed.

  * GUI
    * The colour of cells with undefined (nodata) values can now be set by the user.  So can the colour of cells which failed the definition query or were otherwise excluded.  [Issue 278](https://code.google.com/p/biodiverse/issues/detail?id=278)
    * An export menu is now visible in all output tabs so one does not need to go back to the outputs tab whenever one wishes to export them.  [Issue 273](https://code.google.com/p/biodiverse/issues/detail?id=273)
    * Progress bars are now displayed in all matrix exports.  This avoids periods of GUI non-responsiveness.  Matrices are also written directly file to reduce memory overheads for large matrices.  [Issue 517](https://code.google.com/p/biodiverse/issues/detail?id=517)


## Version 0.99\_004 ##

This is the fourth phase of the development version leading towards version 1.0 (0.99\_003 was only used for internal numbering).

Main changes since the preceding version ([0.99\_002](#Version_0.99_002.md)) are below.  Issue numbers which are not crossed out are yet to be completed.

  * GUI
    * The phylogenetic endemism and related indices are now in their own category (Phylogentic Endemism).  The Phylogenetic Indices category was getting too busy.  [Issue 499](https://code.google.com/p/biodiverse/issues/detail?id=499)
    * Cell outlines can now be turned off.  This is useful when cells are small and any outlines obscure the cell contents.  [Issue 311](https://code.google.com/p/biodiverse/issues/detail?id=311)
    * The legend can be hidden so it no longer overlaps with the grid.  [Issue 59](https://code.google.com/p/biodiverse/issues/detail?id=59)
    * Display cursors now change to match the selected mode (e.g. zoom in, pan, select).  [Issue 490](https://code.google.com/p/biodiverse/issues/detail?id=490)
    * A warning is now shown at startup when extensions cannot be loaded.  This was previously only sent to the console window.  [Issue 500](https://code.google.com/p/biodiverse/issues/detail?id=500)
    * The width of tree branches can now be controlled.  The default value of zero will let the system choose a value based on the sparseness of the terminal branches.  [Issue 505](https://code.google.com/p/biodiverse/issues/detail?id=505)

  * Analyses
    * Analyses are now run as temporary objects and then copied across on success.  This means that many of the optimisations where neighbours and matrices are recycled can apply more often since the originals are not replaced until the analysis completes successfully.  [Issue 444](https://code.google.com/p/biodiverse/issues/detail?id=444)

  * Indices
    * New calculations are now available to calculate the label sample count percentiles across a sample, as well as the rank relative abundance of the labels in the processing group relative to all other groups in the neighbour sets.  [Issue 507](https://code.google.com/p/biodiverse/issues/detail?id=507)

  * Imports
    * Basedata imports now ignore records with a value of NA.  This makes it easier to work with data exported from R as no special processing is needed.  [Issue 489](https://code.google.com/p/biodiverse/issues/detail?id=489)
    * Basedata imports now have an option to control the number of decimal places used in the group axis calculation.  The default is currently 7.  [Issue 488](https://code.google.com/p/biodiverse/issues/detail?id=488)

  * Exports
    * Tree exports to nexus format can optionally not use the translate block.  This means internal nodes can be named and the read.nexus function in ape will still be able to read the file.  [Issue 502](https://code.google.com/p/biodiverse/issues/detail?id=502)


## Version 0.99\_002 ##

This is the second phase of the development version leading towards version 1.0.

Main changes since the preceding version ([0.99\_001](#Version_0.99_001.md)) are below.  Issue numbers which are not crossed out are yet to be completed.


  * GUI
    * The pan and zoom interface has been rewritten to be more like other tools and to present a cleaner interface.  [Issue 353](https://code.google.com/p/biodiverse/issues/detail?id=353)
    * Tree plots now grey-out non-highlighted branches.  This makes it much easier to see which branches are selected.  [Issue 464](https://code.google.com/p/biodiverse/issues/detail?id=464)
    * The Spatial and Matrix tabs now have a tree panel which plots the tree used in the analysis, or the tree selected at the project level.  This works similarly to the View Labels tab in that branches are highlighted as cells are hovered over, and cells are highlighted as branches are hovered over.  [Issue 409](https://code.google.com/p/biodiverse/issues/detail?id=409)
    * A popup message is now shown when a basedata has more than two axes, as this could cause overplotting of groups.  [Issue 461](https://code.google.com/p/biodiverse/issues/detail?id=461)
    * Trees can now be converted to their equal branch length form.  [Issue 504](https://code.google.com/p/biodiverse/issues/detail?id=504) (see also [Issue 482](https://code.google.com/p/biodiverse/issues/detail?id=482))

  * Analyses
    * The rand\_structured randomisation is now considerably faster.  [Issue 487](https://code.google.com/p/biodiverse/issues/detail?id=487)

  * Indices and Calculations
    * The relative phylogenetic indices used in the CANAPE process have now been added (see http://dx.doi.org/10.1038/ncomms5473 ).  [Issue 482](https://code.google.com/p/biodiverse/issues/detail?id=482)
    * Users can now calculate the phylogenetic endemism analogous to the Endemism Central calculation, such that the set of branches considered are those in neighbour set 1 but the local ranges come from across neighbour sets 1 and 2.  [Issue 460](https://code.google.com/p/biodiverse/issues/detail?id=460)

  * Trees
    * Tree imports are now considerably faster.  For example, the Open Tree of Life tree with ~2.5 million nodes takes 3 minutes (note that it needs 6.5GB RAM and the GUI is unlikely to be able to plot it). [Issue 483](https://code.google.com/p/biodiverse/issues/detail?id=483)
    * Tree trimming is now considerably faster.  [Issue 470](https://code.google.com/p/biodiverse/issues/detail?id=470)



## Version 0.99\_001 ##

This is the first phase of the development version leading towards version 1.0.

Main changes since the previous version (0.19) are below.  Issue numbers which are not crossed out are yet to be completed.

  * Analyses
    * The RegionGrower analyses now stop once the maximum optimisation criterion is reached and delete singleton nodes by default.  This leaves a smaller tree consisting only of those elements required to optimise the index.  [Issue  451](https://code.google.com/p/biodiverse/issues/detail?id=451), [Issue 448](https://code.google.com/p/biodiverse/issues/detail?id=448)
    * The Cluster and RegionGrower tie breakers are now optional and are faster and less memory intensive.  If they are turned off then the pre-0.19 tie-breaker approach is used.  [Issue 427](https://code.google.com/p/biodiverse/issues/detail?id=427)

  * Indices and calculations
    * The NRI and NTI indices from PhyloCom are now supported.  Note that these reverse the sign compared to PhyloCom, so positive values are dispersed and negative are clustered.  This is consistent with the picante package in R.  [Issue 442](https://code.google.com/p/biodiverse/issues/detail?id=442)
    * New indices are now available for per-node contributions to the PD and PE indices, including their ancestral components.  [Issue 434](https://code.google.com/p/biodiverse/issues/detail?id=434)
    * Kulczynski 2 is now supported.  [Issue 445](https://code.google.com/p/biodiverse/issues/detail?id=445)
    * A range weighted Gi`*` index of label properties is now available.  [Issue 402](https://code.google.com/p/biodiverse/issues/detail?id=402)
    * The count of terminal nodes used in the neighbour sets can now be obtained.  [Issue 265](https://code.google.com/p/biodiverse/issues/detail?id=265)
    * The endemism and rarity calculations now return an undefined value when the relevant neighbour set contains no labels (consists only of empty groups).  Previously it returns zero.  [Issue 458](https://code.google.com/p/biodiverse/issues/detail?id=458)

  * Spatial Conditions
    * sp\_box() function is now available.  [Issue 159](https://code.google.com/p/biodiverse/issues/detail?id=159)

  * GUI
    * Exclusions dialogue.  Empty groups and labels can optionally not be deleted.  This allows the geographic extent to be consistent before and after exclusions are run.  [Issue 423](https://code.google.com/p/biodiverse/issues/detail?id=423)
    * The progress dialogues are now unified into a single window, greatly reducing the number of popup windows generated in several analyses.  [Issue 295](https://code.google.com/p/biodiverse/issues/detail?id=295)
    * The label range and sample counts can now be added as label properties.  This is useful when one wants to subset a data set using the Exclusions dialogue, but retain their original ranges and abundances.  This is accessed via the basedata menu.  [Issue 412](https://code.google.com/p/biodiverse/issues/detail?id=412)

  * Imports
    * Basedata
      * Raster data files can now be imported directly.  Any file format [supported by GDAL](http://www.gdal.org/formats_list.html) can be used.  [Issue 408](https://code.google.com/p/biodiverse/issues/detail?id=408)
      * Shapefiles can now be imported (point formats only).  [Issue 408](https://code.google.com/p/biodiverse/issues/detail?id=408)
      * When multiple files are selected they can now optionally be assigned to separate Basedatas.  [Issue 378](https://code.google.com/p/biodiverse/issues/detail?id=378)
    * Trees
      * The tabular tree formats can now be imported.  [Issue 322](https://code.google.com/p/biodiverse/issues/detail?id=322)
    * Matrices
      * Sparse matrices can be imported (but not yet in the GUI).  [Issue 82](https://code.google.com/p/biodiverse/issues/detail?id=82)

  * Exports
    * BaseStructs (groups, labels and spatial outputs).
      * Shapefile format (polygons and points) is now supported.  [Issue 419](https://code.google.com/p/biodiverse/issues/detail?id=419)
      * GeoTIFF is now supported.  [Issue 447](https://code.google.com/p/biodiverse/issues/detail?id=447)
      * The ER-Mapper exports are no longer offset by half a cell.  [Issue 453](https://code.google.com/p/biodiverse/issues/detail?id=453)
    * Trees
      * Export to shapefile format is now supported.      [Issue 410](https://code.google.com/p/biodiverse/issues/detail?id=410)


# Version 0.19 #

This was released on 28-Oct-2013.  It is a stable release and contains all changes from the 0.18 development series.  See the list [here](#Version_0.18.md).

To see the full list of issues and changes in this release, see http://code.google.com/p/biodiverse/issues/list?can=1&q=label%3AMilestone-Release0.18

To see the list of open issues or to report a bug or enhancement request, see http://code.google.com/p/biodiverse/issues/


# Version 0.18 #

This was a development version, with periodic releases of test versions.

The last development version was 0.18\_008

Main changes since previous version (0.17) are:
  * Analyses
    * Cluster and Region Grower analyses now have user-controllable tie-breaker options.  Previously the system would choose a pair at random when there was a choice of two or more pairs.  Now users can opt to maximise or minimise any of the indices available for cluster or region grower analyses, in addition to a random selection.  For example, one might wish to choose the pair that maximises the weighted endemism score, and if that still results in  tie then choose a pair at random.  Note that this change also involved changes to the internals of the clustering algorithm, so analyses with the new method will not result in the same set of clusters as before, even if the same PRNG seed is set.  However, randomisations of cluster analyses built using the old system will still follow the old approach so they will be valid.  [Issue #116](https://code.google.com/p/biodiverse/issues/detail?id=#116)
    * Cluster analyses: Users can now control the pseudo-random number generator (PRNG) sequence by specifying the PRNG seed.  This means that, when a random tie-breaker is used, one can guarantee the same order each time the analysis is run (but see [the FAQ](FAQ#Why_do_I_get_different_randomisation_results_on_a_64_and_32_bit.md)).  [Issue #356](https://code.google.com/p/biodiverse/issues/detail?id=#356)
    * Cluster analyses:  Analyses using more than one spatial condition now work properly.  Previously the clusters would bleed across boundaries they should not.  [Issue #397](https://code.google.com/p/biodiverse/issues/detail?id=#397)
    * The big memory leak in the randomisations has finally been tracked down and fixed.  [Issue #5](https://code.google.com/p/biodiverse/issues/detail?id=#5)
    * Randomisations:  New options to perturb the trees and group properties.  [Issue #388](https://code.google.com/p/biodiverse/issues/detail?id=#388), [Issue #389](https://code.google.com/p/biodiverse/issues/detail?id=#389)
  * Indices and Calculations
    * Add new calculation to obtain the list of labels that occur on the tree.  [Issue #319](https://code.google.com/p/biodiverse/issues/detail?id=#319)
    * The phylogenetic diversity and phylogenetic endemism measures now use only the labels on the tree.  The main change for users is that the PD\_per\_taxon index will now divide PD by the number of labels in the sample that are on the tree, not the species richness of the sample.  Previously, if your sample contained labels not on the tree then the values returned were too low.  [Issue #320](https://code.google.com/p/biodiverse/issues/detail?id=#320).
    * calc\_pd\_node\_list returns a hash with the node lengths (index PD\_INCLUDED\_NODE\_LIST).  Previously it just had values of 1.  [Issue #321](https://code.google.com/p/biodiverse/issues/detail?id=#321).
    * The PE\_WE index is now undefined when no tree branches occur in the neighbour sets.
    * New calculations have been added to replicate some of the analyses in PhyloCom.  These are available under the PhyloCom category in the calculations lists.  [Issue #331](https://code.google.com/p/biodiverse/issues/detail?id=#331) and [Issue #332](https://code.google.com/p/biodiverse/issues/detail?id=#332).
    * New calculation to obtain a list of the nodes not on the selected tree.  [Issue #334](https://code.google.com/p/biodiverse/issues/detail?id=#334)
    * The AED and related indices are now calculated correctly.  [Issue #206](https://code.google.com/p/biodiverse/issues/detail?id=#206)
    * New indices for corrected weighted phylogenetic endemism and rarity (PE\_CWE and PHYLO\_RARITY\_CWR).  These are phylogenetic analogues of the corrected weighted endemism index and can be interpreted as the degree to which the ranges or abundances of branches found in a neighbour set are restricted to that neighbour set.  A value of 1 is completely restricted, values approaching zero have very little restriction.
    * The taxonomic and matrix overlap calculations have been removed.  They never worked properly in any case.  [Issue #400](https://code.google.com/p/biodiverse/issues/detail?id=#400)
  * Spatial conditions
    * The `sp_match_text()` and `sp_match_regex()` conditions now match against the whole label by default.  Specifying the axis argument will make them behave as in previous releases.  [Issue #325](https://code.google.com/p/biodiverse/issues/detail?id=#325)
    * New condition `sp_select_element()` which will match only one element (group).  This is the same as sp\_match\_text() but has been optimised to make it considerably faster since it can only ever match one element.  [Issue #326](https://code.google.com/p/biodiverse/issues/detail?id=#326)
    * Analyses using point in polygon conditions for neighbour sets 1 & 2 now work correctly.  Previously no groups were identified in neighbour set 2.  [Issue #380](https://code.google.com/p/biodiverse/issues/detail?id=#380)
    * The assessment of spatial conditions is now considerably faster.  This will substantially speed up analyses with complex conditions.  (But note that analyses using `sp_self_only()` will not show any difference because the system knows it does not need to run any comparisons, thus avoiding needless computation).  [Issue #381](https://code.google.com/p/biodiverse/issues/detail?id=#381)
  * GUI
    * Trees can be rescaled so the branch lengths are divided by their ranges on the selected BaseData.  This will help when interpreting the various phylogenetic endemism indices.  [Issue #385](https://code.google.com/p/biodiverse/issues/detail?id=#385)
    * Label and group properties can now be attached after the data are imported.  [Issue #327](https://code.google.com/p/biodiverse/issues/detail?id=#327)
    * Labels can be renamed after import.  [Issue #349](https://code.google.com/p/biodiverse/issues/detail?id=#349)
    * The run exclusions dialogue now supports additional exclusions criteria.  These include:
      * Labels can be deleted using a list from a file ([issue #348](https://code.google.com/p/biodiverse/issues/detail?id=#348)) or using a text match ([issue #347](https://code.google.com/p/biodiverse/issues/detail?id=#347)).
      * Groups can be excluded using a definition query, using the same syntax as for a spatial analysis ([issue #370](https://code.google.com/p/biodiverse/issues/detail?id=#370)).
  * Exports
    * Delimited text exports for BaseStruct objects (groups, labels, spatial analyses) now write directly to file, avoiding large memory usage.  [Issue #350](https://code.google.com/p/biodiverse/issues/detail?id=#350)
    * All tree nodes can now be optionally exported when using the Table Grouped type.  [Issue #312](https://code.google.com/p/biodiverse/issues/detail?id=#312)
  * Data structures
    * The matrices are now less memory hungry.  Previously matrices with many unique values would require large amounts of storage due to the value indexing used.  This was a particular problem for phylogenetic turnover measures.  [Issue #328](https://code.google.com/p/biodiverse/issues/detail?id=#328)

To see the full list of issues and changes in the 0.18\_00x versions, see http://code.google.com/p/biodiverse/issues/list?can=1&q=label%3AMilestone-Release0.18

To see the list of open issues or to report a bug or enhancement request, see http://code.google.com/p/biodiverse/issues/



# Version 0.17 #

This version was released on 06Jul2012.

Main changes since the previous version (0.16) are:

  * GUI
    * Shapefile overlays are selected as soon as they are opened.  This ensures they are plotted by default.  [Issue #293](https://code.google.com/p/biodiverse/issues/detail?id=#293)
    * View labels: numeric label data sets are sorted numerically.  [Issue #260](https://code.google.com/p/biodiverse/issues/detail?id=#260)
  * Analyses
    * Calculations for cluster nodes can now be done after the event.  The system no longer needs to completely rebuild the tree.  [Issue #289](https://code.google.com/p/biodiverse/issues/detail?id=#289)
  * Calculations and indices
    * Added absolute endemism.  [Issue #144](https://code.google.com/p/biodiverse/issues/detail?id=#144).
    * Added PD Endemism (absolute phylogenetic endemism).  [Issue #292](https://code.google.com/p/biodiverse/issues/detail?id=#292).
    * Completed indices to summarise label and group properties.  [Issue #207](https://code.google.com/p/biodiverse/issues/detail?id=#207), [Issue #212](https://code.google.com/p/biodiverse/issues/detail?id=#212), [Issue #216](https://code.google.com/p/biodiverse/issues/detail?id=#216).
  * Spatial conditions
    * Added sp\_point\_in\_poly\_shape() to use polygons from a shapefile.  [Issue #226](https://code.google.com/p/biodiverse/issues/detail?id=#226)
    * Added optimisation for conditions that always return the same result.  [Issue #304](https://code.google.com/p/biodiverse/issues/detail?id=#304)
    * Added sp\_get\_spatial\_output\_list\_value() to allow access to other outputs in the same BaseData.  This allows one to, for example, restrict analyses to groups with an endemism score above some threshold.  [Issue #233](https://code.google.com/p/biodiverse/issues/detail?id=#233)
  * Exports
    * Users can now add plot coords to the tabular tree exports.  This allows reconstruction of the tree in, for example, a GIS.  [Issue 281](https://code.google.com/p/biodiverse/issues/detail?id=281)
    * NA is now an option for nodata.  This improves compatibility with R.  [Issue #271](https://code.google.com/p/biodiverse/issues/detail?id=#271)
    * Raster exports now work for all cases (was getting errors for some cell sizes).  [Issue #294](https://code.google.com/p/biodiverse/issues/detail?id=#294)
  * Imports
    * Tree imports now work when there are duplicate node names.  Any duplicates have `__dup$i` appended to the name, where `$i` is an integer that is incremented from 1.  For a node called `node`, any duplicates are called `node__dup1`, `node__dup2`, etc.  [Issue #302](https://code.google.com/p/biodiverse/issues/detail?id=#302)

To see the full list of issues and changes in this version, see http://code.google.com/p/biodiverse/issues/list?can=1&q=label%3AMilestone-Release0.17

To see the list of open issues or to report a bug or enhancement request, see http://code.google.com/p/biodiverse/issues/

# Version 0.16 #

This version was a series of beta releases.

Main changes since the previous version (0.15) are:

  * General
    * Groups and spatial outputs can now be exported direct to DIVAGIS raster formats.  [Issue #220](https://code.google.com/p/biodiverse/issues/detail?id=#220).
  * GUI
    * Matrices generated by cluster analyses are now added to the project and can be visualised as a spatial plot.  Click on an element (cell) in the plot to see its dissimilarity with every other element used in the matrix (the index element is coloured grey).  This is very useful when used in conjunction with tools like Generalised Dissimilarity Modelling and when interpreting correlograms of species turnover.  [Issue #199](https://code.google.com/p/biodiverse/issues/detail?id=#199).
    * Grey scale shading is now supported.  [Issue #32](https://code.google.com/p/biodiverse/issues/detail?id=#32).
    * Users can now switch between tabs using control-tab and shift-control-tab keys. [Issue #196](https://code.google.com/p/biodiverse/issues/detail?id=#196).
    * The colour of the shapefile overlay can be changed.  [Issue #75](https://code.google.com/p/biodiverse/issues/detail?id=#75).
    * Outputs tab - the output type is listed next to each output.  [Issue #201](https://code.google.com/p/biodiverse/issues/detail?id=#201).
    * Colour stretches can be adjusted using percentile values (2.5, 5, 95, 97.5).  [Issue #244](https://code.google.com/p/biodiverse/issues/detail?id=#244).
    * View labels tab
      * Element properties with a value of nodata are displayed as -99999.  [Issue #189](https://code.google.com/p/biodiverse/issues/detail?id=#189).
      * System no longer intermittently hangs when control clicking.  [Issue #194](https://code.google.com/p/biodiverse/issues/detail?id=#194).
      * Labels list is now stable when sorting by a column with tied values.  [Issue #246](https://code.google.com/p/biodiverse/issues/detail?id=#246).
      * Label and group axes can be re-ordered after import.  This is useful when you have forgotten to reorder them at import and, for example, your data file contains a field for latitude before longitude.  [Issue #188](https://code.google.com/p/biodiverse/issues/detail?id=#188).
  * Analyses
    * New analysis type of RegionGrower.  It is an extension to the cluster analyses that uses any scalar metric that lumps two neighbour sets together when calculated.  One can also merge those pairs that either maximise or minimise the selected index.  When used with indices like richness it is effectively a one-pass complementarity analysis.  (Its matrices can also be displayed spatially since it is just a variant on the cluster analyses - see [issue #199](https://code.google.com/p/biodiverse/issues/detail?id=#199)).  [Issue #204](https://code.google.com/p/biodiverse/issues/detail?id=#204).
    * Cluster matrices can be written to file as they are built.  These are not added to the GUI, thus saving memory and allowing extremely large matrices to be built for use in external applications.  [Issue #186](https://code.google.com/p/biodiverse/issues/detail?id=#186).
    * More efficient cluster matrix construction and use.  [Issue #185](https://code.google.com/p/biodiverse/issues/detail?id=#185), [Issue #210](https://code.google.com/p/biodiverse/issues/detail?id=#210), [Issue #234](https://code.google.com/p/biodiverse/issues/detail?id=#234)
    * Better handling of empty groups.  [Issue #180](https://code.google.com/p/biodiverse/issues/detail?id=#180), [Issue #181](https://code.google.com/p/biodiverse/issues/detail?id=#181), [Issue #228](https://code.google.com/p/biodiverse/issues/detail?id=#228), [Issue #234](https://code.google.com/p/biodiverse/issues/detail?id=#234).
  * Calculations and indices
    * NEST\_RESULTANT index is now correctly calculated.  [Issue #182](https://code.google.com/p/biodiverse/issues/detail?id=#182).
    * Added phylogenetic nearest taxon distance indices.  [Issue #225](https://code.google.com/p/biodiverse/issues/detail?id=#225).
    * Indices for phylogenetic dissimilarity are now available.  [Issue #215](https://code.google.com/p/biodiverse/issues/detail?id=#215).  [Issue #240](https://code.google.com/p/biodiverse/issues/detail?id=#240).
    * Added AED, BED and related indices.  [Issue #206](https://code.google.com/p/biodiverse/issues/detail?id=#206).
    * Added indices for numeric label dissimilarity.  [Issue #223](https://code.google.com/p/biodiverse/issues/detail?id=#223).
  * Spatial conditions.
    * sp\_select\_sequence() now works as a definition query.  [Issue #190](https://code.google.com/p/biodiverse/issues/detail?id=#190).
    * sp\_is\_left\_of(), sp\_is\_right\_of() and sp\_in\_line\_with() identify if the element is to one side of a vector or on it.  [Issue #202](https://code.google.com/p/biodiverse/issues/detail?id=#202).
    * sp\_select\_block () for block subsampling.  [Issue #218](https://code.google.com/p/biodiverse/issues/detail?id=#218).
    * sp\_point\_in\_polygon().  [Issue #221](https://code.google.com/p/biodiverse/issues/detail?id=#221).
    * sp\_group\_not\_empty() - does the group have any labels?  See [Issue #234](https://code.google.com/p/biodiverse/issues/detail?id=#234).

To see the full list of issues and changes, see http://code.google.com/p/biodiverse/issues/list?can=1&q=label%3AMilestone-Release0.16

# Version 0.15 #

Main changes since the previous version (0.14) are:

  * Calculations and Indices
    * The PD node list has been moved to its own calculation ([issue #130](https://code.google.com/p/biodiverse/issues/detail?id=#130))
    * The Phylogenetic Endemism (PE) lists have been moved to their own sub ([issue #131](https://code.google.com/p/biodiverse/issues/detail?id=#131))
  * Exporting data
    * Exporting groups to raster formats now works properly ([issue #129](https://code.google.com/p/biodiverse/issues/detail?id=#129))
    * Exporting matrices from a cluster analyses now works ([issue #142](https://code.google.com/p/biodiverse/issues/detail?id=#142))
    * Exporting to ER-Mapper files now works properly, with some caveats (see [issue #135](https://code.google.com/p/biodiverse/issues/detail?id=#135) and the [FAQ](FAQ#My_ER-Mapper_BIL_file_is_offset_by_half_a_pixel.md))
  * Importing data
    * Column numbers are now displayed when importing data ([issue #128](https://code.google.com/p/biodiverse/issues/detail?id=#128))
    * Tree imports now use the same quotes character as BaseData imports ([issue #152](https://code.google.com/p/biodiverse/issues/detail?id=#152))
  * Spatial Conditions
    * sp\_ellipse() works properly now ([issue #150](https://code.google.com/p/biodiverse/issues/detail?id=#150))
  * Randomisations
    * Ties are now counted ([issue #146](https://code.google.com/p/biodiverse/issues/detail?id=#146))
  * Visualisation
    * User defined properties are now displayed in the view labels tab ([issue #155](https://code.google.com/p/biodiverse/issues/detail?id=#155)).
  * Under the bonnet
    * User defined properties are now imported properly in the GUI ([issue #154](https://code.google.com/p/biodiverse/issues/detail?id=#154))
    * Neighbour set recycling works properly now ([issue #127](https://code.google.com/p/biodiverse/issues/detail?id=#127) & [issue #145](https://code.google.com/p/biodiverse/issues/detail?id=#145))
    * Module Statistics::Descriptive2 is now deprecated.  It has been replaced by Biodiverse::Statistics which depends explicitly on Statistics::Descriptive ([issue #139](https://code.google.com/p/biodiverse/issues/detail?id=#139))

To see the full list of changes, see http://code.google.com/p/biodiverse/issues/list?can=1&q=label%3AMilestone-Release0.15


# Version 0.14 #

Main changes since the previous version (0.13) are:

  * GUI (and general)
    * The naming errors with saving basedata, tree, and matrix files to the biodiverse native format have been corrected.  ([Issue #104](https://code.google.com/p/biodiverse/issues/detail?id=#104))
    * Reading a tree file from biodiverse format works again.  ([Issue #105](https://code.google.com/p/biodiverse/issues/detail?id=#105))
    * The GUI now recognises R style tables for import (as exported using the write.table() function in R).  ([Issue #20](https://code.google.com/p/biodiverse/issues/detail?id=#20))
    * Tree and matrix objects can be renamed.  ([Issue #72](https://code.google.com/p/biodiverse/issues/detail?id=#72))
    * Users can now describe the selected basedata, tree and matrix.  Results are printed to both a popup and to the log window (from where they can be more easily copied).  ([Issue #93](https://code.google.com/p/biodiverse/issues/detail?id=#93))
    * The parameters sections of the Spatial and Cluster tabs can be hidden to free up real estate when selecting calculations to run.  Click on the Parameters button at the top left of the tab to apply it.  ([Issue #68](https://code.google.com/p/biodiverse/issues/detail?id=#68))
    * Trees and matrices embedded in basedata objects can be added to the project.  ([Issue #71](https://code.google.com/p/biodiverse/issues/detail?id=#71))
    * Labels in a basedata object can be deleted using the nodes/elements in the selected tree or matrix.  The converse can also be done, where those BaseData labels not in the matrix or tree are deleted.  ([issue #74](https://code.google.com/p/biodiverse/issues/detail?id=#74)).
  * Calculations and indices:
    * The count calculations have each been seperated into one calculation for the lists and one for the summary stats.  This applies to the local ranges, local sample counts and element lists.
    * Metadata for the indices now includes formulae.  These are displayed in the online help, but are not displayed in the GUI.  http://code.google.com/p/biodiverse/wiki/Indices
    * Added new index, NEST\_RESULTANT (nestedness-resultant, [Indices#Nestedness-resultant](Indices#Nestedness-resultant.md)) from Baselga (2010) Glob Ecol Biogeog.  http://dx.doi.org/10.1111/j.1466-8238.2009.00490.x ([issue #92](https://code.google.com/p/biodiverse/issues/detail?id=#92))
    * Added binary and sample weighted taxonomic distinctness and variation from Clarke & Warwick (2001) Mar Ecol Progr Ser. http://dx.doi.org/10.3354/meps216265 (note that these are beta level implemenations and need user testing) ([issue #102](https://code.google.com/p/biodiverse/issues/detail?id=#102))
    * The Endemism and Rarity calculations are now listed under their own headings.
    * Added new list calculations to enable hierarchical partitioning of the endemism results (the ENDC`_`HPART`_` and ENDW`_`HPART`_` lists).  ([Issue #99](https://code.google.com/p/biodiverse/issues/detail?id=#99))
    * The Bray-Curtis calculation ([Indices#Bray-Curtis\_non-metric](Indices#Bray-Curtis_non-metric.md)) now also returns the A, B and W values used in the calculations. ([Issue #124](https://code.google.com/p/biodiverse/issues/detail?id=#124))
    * Added new calculation for Bray-Curtis values normalised by the neighbourhood group counts ([Indices#Bray-Curtis\_non-metric,\_group\_count\_normalised](Indices#Bray-Curtis_non-metric,_group_count_normalised.md)).  Resultant indices are the BRAY\_CURTIS\_NORM and associated A, B and W values. ([Issue #126](https://code.google.com/p/biodiverse/issues/detail?id=#126))
  * Spatial Conditions
    * New condition `sp_match_regex` which allows the user to match using arbitrary regular expressions.  For example, to match any group where the neighbour's third axis starts with the processing group's third axis, use `sp_match_regex (re => qr/^$coord[2]/, axis => 2, type => 'nbr')`.  ([Issue #101](https://code.google.com/p/biodiverse/issues/detail?id=#101))
  * Randomisations
    * The randomisations now compare against all lists, not just those in SPATIAL\_RESULTS.  One consequence of this is that the resulting list names have changed.  To enable users to keep track of the results across multiple lists, the results are now named using the randomisation name, followed by `>>`, followed by the original list name.  For example, for a randomisation called `Rand1`, one could have resulting lists called `Rand1>>SPATIAL_RESULTS` and `Rand1>>ENDC_WTLIST`.  The naming scheme for the list contents has not changed (see [AnalysisTypes#Randomisations](AnalysisTypes#Randomisations.md)).  The code is not backwards compatible, so previously run randomisations cannot be extended cleanly using this method.  This is because the SPATIAL\_RESULTS comparisons will be divided across two lists in an output, e.g. `Rand1` and `Rand1>>SPATIAL_RESULTS`.  Re-running the randomisation from scratch is recommended.  Alternately, one can manually sum the `C_` and `Q_` values across the two result sets and from them calculate the updated `P_` values. ([Issue 100](https://code.google.com/p/biodiverse/issues/detail?id=100))
    * The swapping algorithm has been rewritten so it converges more efficiently  for large data sets.  (Swapping is used to reach richness targets in the rand\_structured randomisation).  A consequence of this is that structured randomisations will not produce the same result between versions 0.13 and 0.14 if the seed value is specified.  This is because the random values are used in a different order and so will produce different results if given the same sequence of random values. As with the previous change, the simple solution to this is to start any randomisations afresh after upgrading rather than continuing any existing randomisations.  Continuing randomisations created in BaseData objects prior to version 0.14 will result in mixed algorithms, thus making reproduction of results difficult.  ([Issue #103](https://code.google.com/p/biodiverse/issues/detail?id=#103))
    * The comparison algorithm used when comparing spatial analyses now uses recycled results, resulting in a smaller memory footprint.  Recycling occurs when results are the same across the neighbourhood, as occurs with block and zone type spatial conditions.  In these cases one can generate one set of results and apply them across the neighbourhood rather than having multiple sets of identical results.  ([Issue #107](https://code.google.com/p/biodiverse/issues/detail?id=#107))
  * Under the bonnet
    * Several optimisations have been added where the system can use recycled results (those where the results are the same for all groups in a neighbourhood).


To see the full list of changes, see http://code.google.com/p/biodiverse/issues/list?can=1&q=label%3AMilestone-Release0.14

# Version 0.13 #

01Feb2010.

Main changes since the previous version (0.12) are:

  * Analyses, Calculations and Indices.
    * The use of the term "analyses" in the documentation is now clearer.  Analyses can be one of Cluster, Spatial or Randomisation.  The term "calculation" is now used to describe the collection of indices that are calculated together, e.g. for the groups under a cluster node or within a spatial neighbourhood.  An analysis can apply several calculations to generate some number of indices.
    * The endemism calculations have been subdivided.  The list indices are now in their own calculations, and need to be called explicitly if needed.
    * Two new rarity calculations have been added to generate the lists of weights and sample counts for each label used, as per the endemism calculations.
  * View labels tab:
    * The view labels lists now have additional columns to allow sorting based on the selections (i.e. to promote the selected set to the top of the list).  Note that the list order changes dynamically according to the sort options.  This means that the list will be reordered if the label selection is changed and there is a sort in place using one or both of these columns.
    * The second view labels list is only shown if there is a selected matrix.  This is because it is used to show the matrix column selection and control their sort order.
    * The map legend is now shown in the view labels map pane.  This allows easier interpretation of the mapped values.
  * Trees
    * Nexus file import is now more flexible in the characters it accepts in names (anything that has no special meaning in nexus files), and also numeric formats used for lengths.
    * Newick files are now supported for import (see [issue #79](https://code.google.com/p/biodiverse/issues/detail?id=#79)).
    * When displaying the cluster dendrogram, the user can choose not to use the slider bar to select nodes to plot on the map (access via the dendrogram Options menu).
  * Group coordinates can be specified as Degree, Minutes, Seconds within a single column.  (Note: this is currently a beta level implementation).  See [issue #61](https://code.google.com/p/biodiverse/issues/detail?id=#61).
  * The system now warns if the user attempts to create a new output, or rename an existing output, using a name that is already in use for that output type (see [issue #62](https://code.google.com/p/biodiverse/issues/detail?id=#62)).
  * The randomisation list results are now accessible (see [issue #45](https://code.google.com/p/biodiverse/issues/detail?id=#45)).
  * See also http://code.google.com/p/biodiverse/issues/list?can=1&q=label%3AMilestone-Release0.13

  * For the list of current issues, or to submit a bug report or enhancement request then please see http://code.google.com/p/biodiverse/issues/list

# Version 0.12 #

07Dec2009

Main changes since the previous version (0.11) are:

  * The Windows version comes bundled with updated GTK libraries, and the executable version does not require any additional downloads.  (We are still working on an easy Mac install).
  * The export interface has been revamped to use two windows.  The first allows the selection of the output format and the second has parameters specific to that format.  This makes the parameter choices clearer as irrelevant parameters are not displayed.
  * Feedback to GUI does not contain the line numbers for the code.  They are still printed to the log window, though.
  * Allow native format BaseData, matrix and tree files to be loaded on startup (previous versions only allowed a project file to be loaded as an argument on startup).
  * User is warned if they try to add a new spatial or cluster output to a BaseData and it has one or more randomisations.
  * Randomisation outputs can now be deleted.
  * Randomisation outputs now have export methods to generate text files of their initial and current pseudo-random number generator (PRNG) state.
  * The MXO\_WARD and TXO\_WARD metrics have been removed.  Use the new ["Compare dissimilarity matrix values"](http://code.google.com/p/biodiverse/wiki/Indices#Compare_dissimilarity_matrix_values) analysis instead.
  * Matrix elements (labels) can be remapped on import, as well as excluded/included using the properties table.
  * The scree plot below the dendrogram is minimised to begin with.  It can be pulled up when needed.

  * See also http://code.google.com/p/biodiverse/issues/list?can=1&q=label%3AMilestone-Release0.12


# Version 0.11 #

06Nov2009

Main changes since previous version (0.10).  This is a cleanup and bug fix release with no new features.

  * Improved feedback and error trapping when running analyses.  If the system fails then a popup window will tell you what went wrong and where.  This information is still printed to the log window so you can access it after closing the popup.
  * The error trapping also corrects issues where users are unable to close a tab if an analysis fails.
  * Basedata imports fail with a warning when they reach a record with an undefined or non-numeric value to be used for the groups (unless it is a text group).  The user can set an option to skip these records (this is on by default).
  * System warns user when trying to export a randomisation output.  These cannot currently be exported (although the PRNG state would be useful).  The results can be exported from the relevant spatial or cluster output.  See [KeyConcepts#Randomisations](KeyConcepts#Randomisations.md)
  * Exports for spatial outputs, groups and labels now have an option to specify the type of file instead of relying on the file extension for this.  This does not change the possibilities, but does make them clearer.



# Version 0.10 #

21Oct2009

Main changes since previous version (0.9.1185)

  * Phylogenetic endemism indices are now in the main distribution.  For the theory and some examples, see [Rosauer, Laffan et al. (2009) Molecular Ecology](http://dx.doi.org/10.1111/j.1365-294X.2009.04311.x)
  * Basedata objects now import from matrix format files, eg site by species matrices.  These are a common data format for specimen data.
  * Documentation is moving to the Google Code wiki site.  http://code.google.com/p/biodiverse/w/list
  * Renaming of basedata and outputs is now possible in the GUI
  * Users can now specify a definition query to control the groups used in an analysis.  This uses the same syntax as the spatial neighbourhoods.  See http://code.google.com/p/biodiverse/wiki/KeyConcepts#Definition_Queries
  * Option to show/hide the spatial neighbour and definition query edit boxes in the spatial and cluster tabs.  This frees up screen real estate but does not disable them.
  * Spatial parameters:
    * sp\_circle now has an axes argument to control the axes used (default is still to use all axes)
    * New subroutine `sp_match_text (text => 'blah', axis => 0, type => 'proc')`
    * New subroutine `sp_annulus (inner_radius => 100000, outer_radius => 300000)`
    * See http://code.google.com/p/biodiverse/wiki/SpatialConditions for examples.
  * The Biodiverse icon is now used in all versions (previously was only the exe version)
  * The version numbering system now excludes the SVN revision number.
  * Numerous bug fixes - see http://code.google.com/p/biodiverse/issues/list?can=1&q=label%3A%27release0.10%27
  * Some minor speed-ups and smaller memory footprint in some cases

  * For the full issues list and to report a bug or request an enhancement, visit http://code.google.com/p/biodiverse/issues/list



# Version 0.9.1185 #

Main changes since previous release (version 0.9.1127)

  * Installation instructions updated, particularly for the Mac installs.
  * Fixed bug in tree reading module.  Now correctly reads nexus format files, including those exported from Biodiverse.
  * Documentation updated.
  * Example files added to distribution (data folder)
  * BaseData import now handles text with embedded newlines (these occur occasionally in plant and other data bases, usually in the collection descriptions).
  * Statistics::Descriptive2 now included in the distribution (under the lib folder)
  * Fixed issue where saved project file is given the name "1.bps"