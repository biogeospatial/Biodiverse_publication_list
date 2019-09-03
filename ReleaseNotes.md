**Table of contents:**
* [Version 3.00](#version-300)
* [Version 2.99 dev series](#version-299-dev-series)
* [Version 2.1](#version-21)
* [Version 2.0](#version-20)
* [Version 1.99 dev series](#version-199-dev-series)
  * [Version 1.99_008](#version-199_008)
  * [Version 1.99_007](#version-199_007)
  * [Version 1.99_006](#version-199_006)
  * [Version 1.99_005](#version-199_005)
  * [Version 1.99_004](#version-199_004)
  * [Version 1.99_003](#version-199_003)
  * [Version 1.99_002](#version-199_002)
* [Version 1.1](#version-11)
* [Version 1](#version-1)
* [Version 0.99 dev series](#version-099-dev-series)
  * [Version 0.99_007](#version-099_007)
  * [Version 0.99_006](#version-099_006)
  * [Version 0.99_005](#version-099_005)
  * [Version 0.99_004](#version-099_004)
  * [Version 0.99_002](#version-099_002)
  * [Version 0.99_001](#version-099_001)
* [Version 0.19](#version-019)
* [Version 0.18](#version-018)
* [Version 0.17](#version-017)
* [Version 0.16](#version-016)
* [Version 0.15](#version-015)
* [Version 0.14](#version-014)
* [Version 0.13](#version-013)
* [Version 0.12](#version-012)
* [Version 0.11](#version-011)
* [Version 0.10](#version-010)
* [Version 0.9.1185](#version-091185)

# Version 3.00 #

For the full list of issues and changes leading to the 3.0 release, see https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=milestone%3ARelease_3

  * General
    * Unicode file names are now supported.  This was implemented across [several issues](https://github.com/shawnlaffan/biodiverse/projects/3).  [(A few) more details are in the blog post](https://biodiverse-analysis-software.blogspot.com/2019/05/unicode-file-names-on-windows.html)
    * The minimum perl version is now 5.22, to take advantage of some of the optimisation and general improvements in the language.  This is invisible to users of the exe versions, but users of the source code version need to ensure they use a perl version of 5.22 or later. Issues [#680](https://github.com/shawnlaffan/biodiverse/issues/680), [#705](https://github.com/shawnlaffan/biodiverse/issues/705), [#659](https://github.com/shawnlaffan/biodiverse/issues/659)
    * Exports to XML are no longer supported.  YAML and JSON do all that is needed here.  [Issue #736](https://github.com/shawnlaffan/biodiverse/issues/736)
    * Cluster outputs can be exported to shapefile format.  This gives polygons for each branch in the tree.  [Issue #161](https://github.com/shawnlaffan/biodiverse/issues/161). [More details are in the blog post](https://biodiverse-analysis-software.blogspot.com/2019/08/export-cluster-analyses-to-shapefiles.html)
  * BaseData 
    * Import of polygon and polyline shapefile data is now supported.  [More details are in the blog post](https://biodiverse-analysis-software.blogspot.com/2018/12/import-polygon-and-polyline-data.html). [Issue #697](https://github.com/shawnlaffan/biodiverse/issues/697).
    * The spatial resolution of BaseData objects can now be decreased.  [More details are in the blog post](https://biodiverse-analysis-software.blogspot.com/2019/04/reduce-spatial-resolution-of-your-data.html). [Issue #723](https://github.com/shawnlaffan/biodiverse/issues/723).
    * Axes can be dropped from label and group names, e.g. family:genus:species:population can be simplified to genus:species.  [More details in the blog post](https://biodiverse-analysis-software.blogspot.com/2019/05/drop-label-and-group-axes.html).  [Issue #722](https://github.com/shawnlaffan/biodiverse/issues/722).
  * Randomisations
    * These are now faster for large basedata sets.  A consequence is that the randomisations for a given PRNG seed value will differ from version 2.1 and earlier, so if exact replication is needed then ensure you use the same version as the analyses you are replicating.  [Issue #703](https://github.com/shawnlaffan/biodiverse/issues/703) 
  * Cluster and RegionGrower analyses
    * The internal index used for matrices now uses the C locale for numeric values.  Incorrect values could otherwise be returned in some locales where the comma is used as the radix character.  Biodiverse now throws an exception when it encounters indexes with commas in the values, recommending that the matrix be rebuilt.  [Issue #742](https://github.com/shawnlaffan/biodiverse/issues/742)
  * Trees
    * Tree exports to shapefile format are no longer supported.  The original purpose is better served exporting to newick with tree branch colours.  [Issue #735](https://github.com/shawnlaffan/biodiverse/issues/735)
  * GUI
    * The index lists in open analysis tabs are now updated when a randomisation completes.  Previously the tab had to be closed and re-opened.  [Issue #693](https://github.com/shawnlaffan/biodiverse/issues/693) 
    * Display statistics are updated when an analysis is re-run.  Previously the tab had to be closed and re-opened to ensure the correct ranges of values were used.  [Issue #714](https://github.com/shawnlaffan/biodiverse/issues/714) 
    * Spatial analyses can be exported to RGB GeoTIFF files.  This allows users to reconstruct in a GIS package the colour scheme used in Biodiverse.  [More details in the blog post](https://biodiverse-analysis-software.blogspot.com/2019/05/reproduce-spatial-plots-with-same.html). [Issue #375](https://github.com/shawnlaffan/biodiverse/issues/375).  


# Version 2.99 dev series #

This was a development release series, leading towards version 3.0.  The summary of changes is under the [Version 3.00 entry](#version-300)

For the full list of issues and changes leading to the 3.0 release, see https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=milestone%3ARelease_3



# Version 2.1 #

This version provides a small number of updates and improvements over the version 2.0 release.  

Highlights are:
  * GUI
    * The label list in the view labels tab is now correctly updated when multiple labels are deleted.  [Issue #700](https://github.com/shawnlaffan/biodiverse/issues/700) 
    *  The user defined colours in the cluster tab uses a 13 colour palette by default (it was 9).  [Issue #688](https://github.com/shawnlaffan/biodiverse/issues/688) 
  * Exports
    * Cluster and RegionGrower exports now support the export of a GeoTIFF of the map display with colours that match the tree branches.  [Issue #684](https://github.com/shawnlaffan/biodiverse/issues/684)  [There is also a blog post showing this in action](https://biodiverse-analysis-software.blogspot.com/2018/08/cluster-analyses-export-coloured.html).
    * Various minor export issues have been resolved. 
  * Randomisations
    * The structured randomisations are faster for larger data sets.  [Issue #685](https://github.com/shawnlaffan/biodiverse/issues/685)
  * Tree trimming 
    *  Tree trimming has been sped up for large trees.  [Issue #679](https://github.com/shawnlaffan/biodiverse/issues/679)
    * The trim trees tool has the option to trim to the last common ancestor, thereby removing a dangling root node.  [Issue #670](https://github.com/shawnlaffan/biodiverse/issues/670)

For the full list of issues and changes in the 2.1 release, see https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=milestone%3ARelease_2.1+

To see the full list of open issues or to report a bug or enhancement request, see https://github.com/shawnlaffan/biodiverse/issues

# Version 2.0 #

This is the 2.0 release.  It contains all of the changes in the [version 1.99 development series](#version-199).

This release contains several major changes to the underlying code-base, as well as the addition of several major new features.  They are not guaranteed to be backwards compatible with previous versions (1.1 and earlier, see this [blog post](http://biodiverse-analysis-software.blogspot.com.au/2016/08/new-more-efficient-file-format.html) for more details).  It can still use most Biodiverse files created using earlier versions, but files created using this version are not guaranteed to work with earlier versions.

  * The only change of note from the 1.99 series is that a serious memory leak in the Mac implementation has been fixed.  Details are in [Issue 671](https://github.com/shawnlaffan/biodiverse/issues/671).

For the full list of issues and changes leading to the 2.0 release, see https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=milestone%3ARelease_2.0+

To see the full list of open issues or to report a bug or enhancement request, see https://github.com/shawnlaffan/biodiverse/issues



# Version 1.99 dev series #

This is a development release series, leading towards version 2.0.

Collectively, these releases comprise several major changes to the underlying code-base, as well as the addition of a number of major new features.  They are not guaranteed to be backwards compatible with previous versions (1.1 and earlier).  They can still use most Biodiverse files created using earlier versions, but files created using this version are not guaranteed to work with earlier versions.

For the full list of issues and changes leading to the 2.0 release, see https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=milestone%3ARelease_2.0+

To see the full list of open issues or to report a bug or enhancement request, see https://github.com/shawnlaffan/biodiverse/issues

## Version 1.99_008 ##
  * GUI
    * Spatial tab: Indices that match tree branches can now be displayed on the tree.  [Issue #626](https://github.com/shawnlaffan/biodiverse/issues/626)  [See the blog post for more details](http://biodiverse-analysis-software.blogspot.com.au/2017/09/visualise-spatial-analysis-results-on.html).
    * View Labels tab: Users can now copy the full records for selected labels.  [Issue #667](https://github.com/shawnlaffan/biodiverse/issues/667), see also the [blog post](https://biodiverse-analysis-software.blogspot.com/2017/08/copy-selected-records-to-clipboard.html)
    * Label and group properties can be deleted [Issue 547](https://github.com/shawnlaffan/biodiverse/issues/547)
    *  Map colours can be log scaled in the Spatial, Cluster and View Labels tabs.  [Issue #301](https://github.com/shawnlaffan/biodiverse/issues/301)  [See more in the blog post](http://biodiverse-analysis-software.blogspot.com.au/2017/09/log-scale-your-map-displays.html)
  * Exports
    * Tree lists can be exported to Nexus formats. [Issue #503](https://github.com/shawnlaffan/biodiverse/issues/503) [See the blog post for more details](https://biodiverse-analysis-software.blogspot.com/2017/09/export-lists-to-newick-format.html).

## Version 1.99_007 ##
  * Big ticket items
    * Biodiverse now installs cleanly on Macintosh computers.  Look for the development release [download links here](https://purl.org/biodiverse/wiki/Download) and [installation instructions here](https://purl.org/biodiverse/wiki/Installation)
    * Biodiverse now provides a remap guesser to make it easier to match labels (e.g. taxa names) between basedata, trees, matrices and property tables.  See the [blog post](http://biodiverse-analysis-software.blogspot.com/2017/04/matching-spatial-tree-matrix-and.html) for more details.
  * GUI
    * Tree exports can now include the last-used branch colours.  [Issue 630](https://github.com/shawnlaffan/biodiverse/issues/630)
  * BaseData
    * Spreadsheet and shapefile imports now properly support DMS (degrees-minutes-seconds) group coordinates.  [Issue 627](https://github.com/shawnlaffan/biodiverse/issues/627)
  * Analyses
    * Randomisations now provide rank relative significance scores.  [Issue 607](https://github.com/shawnlaffan/biodiverse/issues/607).  More details in the [blog post](http://biodiverse-analysis-software.blogspot.com.au/2016/08/easier-to-use-randomisation-results.html)
  * Indices
    * The inter-event interval (IEI) indices have been removed from the main distribution.  If needed then they can be made available again.  [Issue 661](https://github.com/shawnlaffan/biodiverse/issues/661)
  * Exports
    * File exports now support definition queries.  This allows users to export only a subset of their data.  [Issue 599](https://github.com/shawnlaffan/biodiverse/issues/599)


## Version 1.99_006 ##
  * GUI
    * View Labels tab: Labels are sorted using a [natural sort order](https://en.wikipedia.org/wiki/Natural_sort_order).  [Issue 614](https://github.com/shawnlaffan/biodiverse/issues/614)
    * Groups with text axes also use a natural sort to determine the plotting coordinates.  [Issue 613](https://github.com/shawnlaffan/biodiverse/issues/613)

## Version 1.99_005 ##
  * GUI
    * Users can now control the colour of individual branches and their descendants in the Cluster analysis tab.  [Issue 600](shawnlaffan/biodiverse/issues/600).  [See the blog post for more details](http://biodiverse-analysis-software.blogspot.com.au/2016/09/new-selection-tool-in-cluster-analysis.html).
  * File formats
    * Some basedatas were not saving correctly when using the Sereal format.  This only affected users of the 1.99_004 release and was fixed in commit [a68eb20](https://github.com/shawnlaffan/biodiverse/commit/a68eb2021dbb14d3d550ccb0becbd6c75b725545) (which also made it consistent with the existing Storable approach). 

## Version 1.99_004 ##
  * File formats
    * The default file format now uses Sereal instead of Storable.  [Issue 358](shawnlaffan/biodiverse/issues/358).  See this [blog post](http://biodiverse-analysis-software.blogspot.com.au/2016/08/new-more-efficient-file-format.html) for more details.
  * Randomisations
    * Randomisation outputs can now be renamed.  [Issue 609](https://github.com/shawnlaffan/biodiverse/issues/609)
    * Randomisation scores are now automatically converted into rank-relative positions.  These can be more easily converted to significance scores.  [Issue 607](/shawnlaffan/biodiverse/issues/607).  See [this blog post](http://biodiverse-analysis-software.blogspot.com.au/2016/08/easier-to-use-randomisation-results.html) for more details.
  * Exports
    * JSON is now supported for table exports.  [Issue 593](/shawnlaffan/biodiverse/issues/593)

## Version 1.99_003 ##
  * GUI
    * The overlays system now warns you if the shapefile is unlikely to be visible, for example when the shapefile is in geographic coordinates but the BaseData file is in an Albers coordinate system.  [Issue 604](shawnlaffan/biodiverse/issues/604)
    * The randomisation tab has been restructured to be more compact.
  * Randomisations
    * New spatially structured randomisations are available.  More details in a forthcoming blog post.  [Issue 76](/shawnlaffan/biodiverse/issues/76)
    * Randomisation scores are now automatically categorised into significance thresholds.  [A blog post gives further details](http://biodiverse-analysis-software.blogspot.com.au/2016/08/biodiverse-now-categorises-your.html), [Issue 607](/shawnlaffan/biodiverse/issues/607)
  * Indices
    * A "central" variant of the RPE indices is now available and can be used with the [PE Central indices](https://purl.org/biodiverse/wiki/IndicesDevVersion#phylogenetic-endemism-central).  [A description is here](https://purl.org/biodiverse/wiki/IndicesDevVersion#relative-phylogenetic-endemism-central).  The calculation is the same as the non-central version, but the set of branches used are taken from the first neighbour set.
  * Trees
    * Biodiverse was hanging when trimming some trees to match the basedata.  [Commit ce678640d725d96078b7288833b52c97b9e46c4b](https://github.com/shawnlaffan/biodiverse/commit/ce678640d725d96078b7288833b52c97b9e46c4b)

## Version 1.99_002 ##

  * GUI
    * No more do we depend on Gtk2::GladeXML for the user interface, thus removing a dependency that has long been deprecated.  [Issue 413](/shawnlaffan/biodiverse/issues/413)
  * Indices
    * A set of species richness estimators are now supported [Issue 420](/shawnlaffan/biodiverse/issues/420) A blog post is [here](http://biodiverse-analysis-software.blogspot.com.au/2016/05/biodiverse-now-includes-species.html).
    * The range weighted turnover indices described in [Laffan et al. (2016)](http://dx.doi.org/10.1111/2041-210X.12513) are now included.  [Issue 577](https://github.com/shawnlaffan/biodiverse/issues/577).


# Version 1.1 #

This is a small-ish update to the 1.0 release, containing a few bug fixes and enhancements.

The main highlights are:

  * GUI
    * Groups can be renamed in the same way that labels are.  This is most useful when you have text based group names, not coordinate based names.  [Issue 553](https://github.com/shawnlaffan/biodiverse/issues/553)
    * Two basedatas can be merged, providing they have the same cell sizes and origins.  [Issue 493](https://github.com/shawnlaffan/biodiverse/issues/493)
    * View labels tab: Selected labels can be copied to the clipboard.  [Issue 557](https://github.com/shawnlaffan/biodiverse/issues/557)  [_Read the blog post_](http://biodiverse-analysis-software.blogspot.com.au/2015/06/copy-selected-labels-to-clipboard.html)
    * Trees can be ladderised so they plot child branches in order of the number of descendants. [Issue 530](https://github.com/shawnlaffan/biodiverse/issues/530)
  * Data import
    * Data can now be imported from spreadsheet formats.  [Issue 540](https://github.com/shawnlaffan/biodiverse/issues/540)  [_Read the blog post_](http://biodiverse-analysis-software.blogspot.com.au/2015/06/import-your-species-data-from.html)
  * Analyses
    * Randomisations [_(read the blog post)_](http://biodiverse-analysis-software.blogspot.com.au/2015/06/better-control-of-randomisations.html)
      * Randomisations can now be run for subsets of your data.  Specifying a definition query determines which groups are randomised, while specifying a spatial condition constrains the randomisation to stay within subsets.  In this way one can randomise labels such that they stay within, for example, the bioregion in which they are found.  [Issue 554](https://github.com/shawnlaffan/biodiverse/issues/554) 
      * Randomisations now allow users to specify a subset of labels which will be held constant, i.e. their distributions are not randomised.  This allows one to, for example, hold one clade in a tree constant, while randomising the remainder of the data.  [Issue 556](https://github.com/shawnlaffan/biodiverse/issues/556)
    * The spatial index is now used more effectively.  [Issue 550](https://github.com/shawnlaffan/biodiverse/issues/550), [Issue 545](https://github.com/shawnlaffan/biodiverse/issues/550), [Issue 551](https://github.com/shawnlaffan/biodiverse/issues/551)
    * Calculations and Indices
      * New calculation for phylogenetic abundance.  [Issue 559](https://github.com/shawnlaffan/biodiverse/issues/559)
    

For the full list of issues and changes leading to the 1.1 release, see https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=milestone%3ARelease_1.1+ and https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=milestone%3A%22Metadata+system+-+use+OO+not+bare+hashes%22+

To see the full list of open issues or to report a bug or enhancement request, see https://github.com/shawnlaffan/biodiverse/issues


# Version 1 #

This is the 1.0 release.  It contains all of the changes in the [version 0.99 development series](#version-099).

This release contains several major changes to the underlying code-base, as well as the addition of several major new features.  It is not backwards compatible with previous versions (0.19 and earlier) in several respects.  It can still use most Biodiverse files created using earlier versions, but files created using this version are not guaranteed to work with earlier versions.

For the full list of issues and changes leading to the 1.0 release, see https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=milestone%3ARelease_1.0+

To see the full list of open issues or to report a bug or enhancement request, see https://github.com/shawnlaffan/biodiverse/issues


# Version 0.99 dev series #

This is a development release series, leading towards version 1.0.

Collectively, these releases comprise several major changes to the underlying code-base, as well as the addition of a number of major new features.  They are not backwards compatible with previous versions (0.19 and earlier) in several respects.  They can still use most Biodiverse files created using earlier versions, but files created using this version are not guaranteed to work with earlier versions.

For the full list of issues and changes leading to the 1.0 release, see https://github.com/shawnlaffan/biodiverse/milestones/Release1.0

To see the full list of open issues or to report a bug or enhancement request, see https://github.com/shawnlaffan/biodiverse/issues

## Version 0.99_007 ##

This is the seventh phase of the development version leading towards version 1.0.

Main changes since the preceding version ([0.99_006](#version-099_006)) are below.  Issue numbers which are not crossed out are yet to be completed.

  * GUI
    * The label selection mode can now be set, so in addition to being able to create a new selection each time one of the grid, tree or matrix panes is clicked, users can now also add to or remove from the current selection.  This allows the selection of, for example, distinct clades on the tree.  These might then be deleted from the basedata using the deletion methods added in the previous development release.  [Issue 535](/shawnlaffan/biodiverse/issues/535)
    * Fixed a crash when a tree was trimmed and had no remaining branches, and a View Labels tab was open.  [Issue 534](/shawnlaffan/biodiverse/issues/534)


## Version 0.99_006 ##

This is the sixth phase of the development version leading towards version 1.0.

Main changes since the preceding version ([0.99_005](#version-099_005)) are below.  Issue numbers which are not crossed out are yet to be completed.

  * GUI
    * The new pan and zoom functionality now works consistently across all views (maps, trees and matrices).  [Issue 353](/shawnlaffan/biodiverse/issues/353)
    * New functions have been added to work with the selected labels.
      * Labels can be selected using partial text matches.  These use regular expressions, so can be as complex as is needed, but the simplest case is just a fragment of the label name.  Selections can optionally be added to or removed from.  [Issue 529](/shawnlaffan/biodiverse/issues/29)
      * Selected labels can be deleted from the basedata, or new basedatas can be created using the selected (or non-selected) labels.  [Issue 528](/shawnlaffan/biodiverse/issues/528).
      * The selected set can be switched (inverted) so all non-selected labels become the selected set.  [Issue 532](/shawnlaffan/biodiverse/issues/532)
      * The selected set (labels and the groups in which they occur) can be exported directly from the View Labels tab.  [Issue 414](/shawnlaffan/biodiverse/issues/414)

  * Export/import
    * Trees exported from Biodiverse now roundtrip properly when labels are quoted.  [Issue 270](/shawnlaffan/biodiverse/issues/270)
    * Sparse format matrix files can now be imported in the GUI.  [Issue 82](/shawnlaffan/biodiverse/issues/82)
    * Matrix exports now use a progress dialog to avoid a non-responsive GUI.  They also write direct to file to reduce memory overheads.  [Issue 517](/shawnlaffan/biodiverse/issues/517)
    * Basedata imports are now faster.  The effect is greatest for raster imports where there is no transform in place.  [Issue 527](/shawnlaffan/biodiverse/issues/527)

  * Analyses
    * In the spatial analyses, users can control the use of the spatial index across the whole analysis, or on a per-spatial condition level.  [Issue 205](/shawnlaffan/biodiverse/issues/205)
    * Control is also available for result and neighbour set recycling (the system detects these correctly in most cases, but it is useful to control it in falsely detected cases).  [Issue 205](/shawnlaffan/biodiverse/issues/205)

## Version 0.99_005 ##

This is the fifth phase of the development version leading towards version 1.0.

Main changes since the preceding version ([0.99_004](#version-099_004)) are below.  Issue numbers which are not crossed out are yet to be completed.

  * GUI
    * The colour of cells with undefined (nodata) values can now be set by the user.  So can the colour of cells which failed the definition query or were otherwise excluded.  [Issue 278](/shawnlaffan/biodiverse/issues/278)
    * An export menu is now visible in all output tabs so one does not need to go back to the outputs tab whenever one wishes to export them.  [Issue 273](/shawnlaffan/biodiverse/issues/273)
    * Progress bars are now displayed in all matrix exports.  This avoids periods of GUI non-responsiveness.  Matrices are also written directly file to reduce memory overheads for large matrices.  [Issue 517](/shawnlaffan/biodiverse/issues/517)


## Version 0.99_004 ##

This is the fourth phase of the development version leading towards version 1.0 (0.99_003 was only used for internal numbering).

Main changes since the preceding version ([0.99_002](#version-099_002)) are below.  Issue numbers which are not crossed out are yet to be completed.

  * GUI
    * The phylogenetic endemism and related indices are now in their own category (Phylogentic Endemism).  The Phylogenetic Indices category was getting too busy.  [Issue 499](/shawnlaffan/biodiverse/issues/499)
    * Cell outlines can now be turned off.  This is useful when cells are small and any outlines obscure the cell contents.  [Issue 311](/shawnlaffan/biodiverse/issues/311)
    * The legend can be hidden so it no longer overlaps with the grid.  [Issue 59](/shawnlaffan/biodiverse/issues/59)
    * Display cursors now change to match the selected mode (e.g. zoom in, pan, select).  [Issue 490](/shawnlaffan/biodiverse/issues/490)
    * A warning is now shown at startup when extensions cannot be loaded.  This was previously only sent to the console window.  [Issue 500](/shawnlaffan/biodiverse/issues/500)
    * The width of tree branches can now be controlled.  The default value of zero will let the system choose a value based on the sparseness of the terminal branches.  [Issue 505](/shawnlaffan/biodiverse/issues/505)

  * Analyses
    * Analyses are now run as temporary objects and then copied across on success.  This means that many of the optimisations where neighbours and matrices are recycled can apply more often since the originals are not replaced until the analysis completes successfully.  [Issue 444](/shawnlaffan/biodiverse/issues/444)

  * Indices
    * New calculations are now available to calculate the label sample count percentiles across a sample, as well as the rank relative abundance of the labels in the processing group relative to all other groups in the neighbour sets.  [Issue 507](/shawnlaffan/biodiverse/issues/507)

  * Imports
    * Basedata imports now ignore records with a value of NA.  This makes it easier to work with data exported from R as no special processing is needed.  [Issue 489](/shawnlaffan/biodiverse/issues/489)
    * Basedata imports now have an option to control the number of decimal places used in the group axis calculation.  The default is currently 7.  [Issue 488](/shawnlaffan/biodiverse/issues/488)

  * Exports
    * Tree exports to nexus format can optionally not use the translate block.  This means internal nodes can be named and the read.nexus function in ape will still be able to read the file.  [Issue 502](/shawnlaffan/biodiverse/issues/502)


## Version 0.99_002 ##

This is the second phase of the development version leading towards version 1.0.

Main changes since the preceding version ([0.99_001](#version-099_001)) are below.  Issue numbers which are not crossed out are yet to be completed.


  * GUI
    * The pan and zoom interface has been rewritten to be more like other tools and to present a cleaner interface.  [Issue 353](/shawnlaffan/biodiverse/issues/353)
    * Tree plots now grey-out non-highlighted branches.  This makes it much easier to see which branches are selected.  [Issue 464](/shawnlaffan/biodiverse/issues/464)
    * The Spatial and Matrix tabs now have a tree panel which plots the tree used in the analysis, or the tree selected at the project level.  This works similarly to the View Labels tab in that branches are highlighted as cells are hovered over, and cells are highlighted as branches are hovered over.  [Issue 409](/shawnlaffan/biodiverse/issues/409)
    * A popup message is now shown when a basedata has more than two axes, as this could cause overplotting of groups.  [Issue 461](/shawnlaffan/biodiverse/issues/461)
    * Trees can now be converted to their equal branch length form.  [Issue 504](/shawnlaffan/biodiverse/issues/04) (see also [Issue 482](/shawnlaffan/biodiverse/issues/482))

  * Analyses
    * The rand_structured randomisation is now considerably faster.  [Issue 487](/shawnlaffan/biodiverse/issues/487)

  * Indices and Calculations
    * The relative phylogenetic indices used in the CANAPE process have now been added (see http://dx.doi.org/10.1038/ncomms5473 ).  [Issue 482](/shawnlaffan/biodiverse/issues/482)
    * Users can now calculate the phylogenetic endemism analogous to the Endemism Central calculation, such that the set of branches considered are those in neighbour set 1 but the local ranges come from across neighbour sets 1 and 2.  [Issue 460](/shawnlaffan/biodiverse/issues/460)

  * Trees
    * Tree imports are now considerably faster.  For example, the Open Tree of Life tree with ~2.5 million nodes takes 3 minutes (note that it needs 6.5GB RAM and the GUI is unlikely to be able to plot it). [Issue 483](/shawnlaffan/biodiverse/issues/483)
    * Tree trimming is now considerably faster.  [Issue 470](/shawnlaffan/biodiverse/issues/470)



## Version 0.99_001 ##

This is the first phase of the development version leading towards version 1.0.

Main changes since the previous version (0.19) are below.  Issue numbers which are not crossed out are yet to be completed.

  * Analyses
    * The RegionGrower analyses now stop once the maximum optimisation criterion is reached and delete singleton nodes by default.  This leaves a smaller tree consisting only of those elements required to optimise the index.  [Issue  451](/shawnlaffan/biodiverse/issues/451), [Issue 448](/shawnlaffan/biodiverse/issues/448)
    * The Cluster and RegionGrower tie breakers are now optional and are faster and less memory intensive.  If they are turned off then the pre-0.19 tie-breaker approach is used.  [Issue 427](/shawnlaffan/biodiverse/issues/427)

  * Indices and calculations
    * The NRI and NTI indices from PhyloCom are now supported.  Note that these reverse the sign compared to PhyloCom, so positive values are dispersed and negative are clustered.  This is consistent with the picante package in R.  [Issue 442](/shawnlaffan/biodiverse/issues/442)
    * New indices are now available for per-node contributions to the PD and PE indices, including their ancestral components.  [Issue 434](/shawnlaffan/biodiverse/issues/434)
    * Kulczynski 2 is now supported.  [Issue 445](/shawnlaffan/biodiverse/issues/445)
    * A range weighted Gi`*` index of label properties is now available.  [Issue 402](/shawnlaffan/biodiverse/issues/402)
    * The count of terminal nodes used in the neighbour sets can now be obtained.  [Issue 265](/shawnlaffan/biodiverse/issues/265)
    * The endemism and rarity calculations now return an undefined value when the relevant neighbour set contains no labels (consists only of empty groups).  Previously it returns zero.  [Issue 458](/shawnlaffan/biodiverse/issues/458)

  * Spatial Conditions
    * sp_box() function is now available.  [Issue 159](/shawnlaffan/biodiverse/issues/159)

  * GUI
    * Exclusions dialogue.  Empty groups and labels can optionally not be deleted.  This allows the geographic extent to be consistent before and after exclusions are run.  [Issue 423](/shawnlaffan/biodiverse/issues/423)
    * The progress dialogues are now unified into a single window, greatly reducing the number of popup windows generated in several analyses.  [Issue 295](/shawnlaffan/biodiverse/issues/295)
    * The label range and sample counts can now be added as label properties.  This is useful when one wants to subset a data set using the Exclusions dialogue, but retain their original ranges and abundances.  This is accessed via the basedata menu.  [Issue 412](/shawnlaffan/biodiverse/issues/412)

  * Imports
    * Basedata
      * Raster data files can now be imported directly.  Any file format [supported by GDAL](http://www.gdal.org/formats_list.html) can be used.  [Issue 408](/shawnlaffan/biodiverse/issues/408)
      * Shapefiles can now be imported (point formats only).  [Issue 408](/shawnlaffan/biodiverse/issues/408)
      * When multiple files are selected they can now optionally be assigned to separate Basedatas.  [Issue 378](/shawnlaffan/biodiverse/issues/378)
    * Trees
      * The tabular tree formats can now be imported.  [Issue 322](/shawnlaffan/biodiverse/issues/322)
    * Matrices
      * Sparse matrices can be imported (but not yet in the GUI).  [Issue 82](/shawnlaffan/biodiverse/issues/82)

  * Exports
    * BaseStructs (groups, labels and spatial outputs).
      * Shapefile format (polygons and points) is now supported.  [Issue 419](/shawnlaffan/biodiverse/issues/419)
      * GeoTIFF is now supported.  [Issue 447](/shawnlaffan/biodiverse/issues/447)
      * The ER-Mapper exports are no longer offset by half a cell.  [Issue 453](/shawnlaffan/biodiverse/issues/453)
    * Trees
      * Export to shapefile format is now supported.      [Issue 410](/shawnlaffan/biodiverse/issues/410)


# Version 0.19 #

This was released on 28-Oct-2013.  It is a stable release and contains all changes from the 0.18 development series.  See the list [here](#version-018).

To see the full list of issues and changes in this release, see https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=label%3AMilestone-Release0.18+

To see the list of open issues or to report a bug or enhancement request, see https://github.com/shawnlaffan/biodiverse/issues


# Version 0.18 #

This was a development version, with periodic releases of test versions.

The last development version was 0.18_008

Main changes since previous version (0.17) are:
  * Analyses
    * Cluster and Region Grower analyses now have user-controllable tie-breaker options.  Previously the system would choose a pair at random when there was a choice of two or more pairs.  Now users can opt to maximise or minimise any of the indices available for cluster or region grower analyses, in addition to a random selection.  For example, one might wish to choose the pair that maximises the weighted endemism score, and if that still results in  tie then choose a pair at random.  Note that this change also involved changes to the internals of the clustering algorithm, so analyses with the new method will not result in the same set of clusters as before, even if the same PRNG seed is set.  However, randomisations of cluster analyses built using the old system will still follow the old approach so they will be valid.  [Issue #116](/shawnlaffan/biodiverse/issues/116)
    * Cluster analyses: Users can now control the pseudo-random number generator (PRNG) sequence by specifying the PRNG seed.  This means that, when a random tie-breaker is used, one can guarantee the same order each time the analysis is run (but see [the FAQ](FAQ#why-do-i-get-different-randomisation-results-on-a-64-and-32-bit)).  [Issue #356](/shawnlaffan/biodiverse/issues/356)
    * Cluster analyses:  Analyses using more than one spatial condition now work properly.  Previously the clusters would bleed across boundaries they should not.  [Issue #397](/shawnlaffan/biodiverse/issues/397)
    * The big memory leak in the randomisations has finally been tracked down and fixed.  [Issue #5](/shawnlaffan/biodiverse/issues/5)
    * Randomisations:  New options to perturb the trees and group properties.  [Issue #388](/shawnlaffan/biodiverse/issues/388), [Issue #389](/shawnlaffan/biodiverse/issues/389)
  * Indices and Calculations
    * Add new calculation to obtain the list of labels that occur on the tree.  [Issue #319](/shawnlaffan/biodiverse/issues/319)
    * The phylogenetic diversity and phylogenetic endemism measures now use only the labels on the tree.  The main change for users is that the PD_per_taxon index will now divide PD by the number of labels in the sample that are on the tree, not the species richness of the sample.  Previously, if your sample contained labels not on the tree then the values returned were too low.  [Issue #320](/shawnlaffan/biodiverse/issues/320).
    * calc_pd_node_list returns a hash with the node lengths (index PD_INCLUDED_NODE_LIST).  Previously it just had values of 1.  [Issue #321](/shawnlaffan/biodiverse/issues/321).
    * The PE_WE index is now undefined when no tree branches occur in the neighbour sets.
    * New calculations have been added to replicate some of the analyses in PhyloCom.  These are available under the PhyloCom category in the calculations lists.  [Issue #331](/shawnlaffan/biodiverse/issues/331) and [Issue #332](/shawnlaffan/biodiverse/issues/332).
    * New calculation to obtain a list of the nodes not on the selected tree.  [Issue #334](/shawnlaffan/biodiverse/issues/334)
    * The AED and related indices are now calculated correctly.  [Issue #206](/shawnlaffan/biodiverse/issues/206)
    * New indices for corrected weighted phylogenetic endemism and rarity (PE_CWE and PHYLO_RARITY_CWR).  These are phylogenetic analogues of the corrected weighted endemism index and can be interpreted as the degree to which the ranges or abundances of branches found in a neighbour set are restricted to that neighbour set.  A value of 1 is completely restricted, values approaching zero have very little restriction.
    * The taxonomic and matrix overlap calculations have been removed.  They never worked properly in any case.  [Issue #400](/shawnlaffan/biodiverse/issues/400)
  * Spatial conditions
    * The `sp_match_text()` and `sp_match_regex()` conditions now match against the whole label by default.  Specifying the axis argument will make them behave as in previous releases.  [Issue #325](/shawnlaffan/biodiverse/issues/325)
    * New condition `sp_select_element()` which will match only one element (group).  This is the same as sp_match_text() but has been optimised to make it considerably faster since it can only ever match one element.  [Issue #326](/shawnlaffan/biodiverse/issues/326)
    * Analyses using point in polygon conditions for neighbour sets 1 & 2 now work correctly.  Previously no groups were identified in neighbour set 2.  [Issue #380](/shawnlaffan/biodiverse/issues/380)
    * The assessment of spatial conditions is now considerably faster.  This will substantially speed up analyses with complex conditions.  (But note that analyses using `sp_self_only()` will not show any difference because the system knows it does not need to run any comparisons, thus avoiding needless computation).  [Issue #381](/shawnlaffan/biodiverse/issues/381)
  * GUI
    * Trees can be rescaled so the branch lengths are divided by their ranges on the selected BaseData.  This will help when interpreting the various phylogenetic endemism indices.  [Issue #385](/shawnlaffan/biodiverse/issues/385)
    * Label and group properties can now be attached after the data are imported.  [Issue #327](/shawnlaffan/biodiverse/issues/327)
    * Labels can be renamed after import.  [Issue #349](/shawnlaffan/biodiverse/issues/349)
    * The run exclusions dialogue now supports additional exclusions criteria.  These include:
      * Labels can be deleted using a list from a file ([issue #348](/shawnlaffan/biodiverse/issues/348)) or using a text match ([issue #347](/shawnlaffan/biodiverse/issues/347)).
      * Groups can be excluded using a definition query, using the same syntax as for a spatial analysis ([issue #370](/shawnlaffan/biodiverse/issues/370)).
  * Exports
    * Delimited text exports for BaseStruct objects (groups, labels, spatial analyses) now write directly to file, avoiding large memory usage.  [Issue #350](/shawnlaffan/biodiverse/issues/350)
    * All tree nodes can now be optionally exported when using the Table Grouped type.  [Issue #312](/shawnlaffan/biodiverse/issues/312)
  * Data structures
    * The matrices are now less memory hungry.  Previously matrices with many unique values would require large amounts of storage due to the value indexing used.  This was a particular problem for phylogenetic turnover measures.  [Issue #328](/shawnlaffan/biodiverse/issues/328)

To see the full list of issues and changes in the 0.18_00x versions, see https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=label%3AMilestone-Release0.18+

To see the list of open issues or to report a bug or enhancement request, see https://github.com/shawnlaffan/biodiverse/issues



# Version 0.17 #

This version was released on 06Jul2012.

Main changes since the previous version (0.16) are:

  * GUI
    * Shapefile overlays are selected as soon as they are opened.  This ensures they are plotted by default.  [Issue #293](/shawnlaffan/biodiverse/issues/293)
    * View labels: numeric label data sets are sorted numerically.  [Issue #260](/shawnlaffan/biodiverse/issues/260)
  * Analyses
    * Calculations for cluster nodes can now be done after the event.  The system no longer needs to completely rebuild the tree.  [Issue #289](/shawnlaffan/biodiverse/issues/289)
  * Calculations and indices
    * Added absolute endemism.  [Issue #144](/shawnlaffan/biodiverse/issues/144).
    * Added PD Endemism (absolute phylogenetic endemism).  [Issue #292](/shawnlaffan/biodiverse/issues/292).
    * Completed indices to summarise label and group properties.  [Issue #207](/shawnlaffan/biodiverse/issues/207), [Issue #212](/shawnlaffan/biodiverse/issues/212), [Issue #216](/shawnlaffan/biodiverse/issues/216).
  * Spatial conditions
    * Added sp_point_in_poly_shape() to use polygons from a shapefile.  [Issue #226](/shawnlaffan/biodiverse/issues/226)
    * Added optimisation for conditions that always return the same result.  [Issue #304](/shawnlaffan/biodiverse/issues/304)
    * Added sp_get_spatial_output_list_value() to allow access to other outputs in the same BaseData.  This allows one to, for example, restrict analyses to groups with an endemism score above some threshold.  [Issue #233](/shawnlaffan/biodiverse/issues/233)
  * Exports
    * Users can now add plot coords to the tabular tree exports.  This allows reconstruction of the tree in, for example, a GIS.  [Issue 281](/shawnlaffan/biodiverse/issues/81)
    * NA is now an option for nodata.  This improves compatibility with R.  [Issue #271](/shawnlaffan/biodiverse/issues/271)
    * Raster exports now work for all cases (was getting errors for some cell sizes).  [Issue #294](/shawnlaffan/biodiverse/issues/294)
  * Imports
    * Tree imports now work when there are duplicate node names.  Any duplicates have `__dup$i` appended to the name, where `$i` is an integer that is incremented from 1.  For a node called `node`, any duplicates are called `node__dup1`, `node__dup2`, etc.  [Issue #302](/shawnlaffan/biodiverse/issues/302)

To see the full list of issues and changes in this version, see https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=label%3AMilestone-Release0.17+

To see the list of open issues or to report a bug or enhancement request, see https://github.com/shawnlaffan/biodiverse/issues

# Version 0.16 #

This version was a series of beta releases.

Main changes since the previous version (0.15) are:

  * General
    * Groups and spatial outputs can now be exported direct to DIVAGIS raster formats.  [Issue #220](/shawnlaffan/biodiverse/issues/220).
  * GUI
    * Matrices generated by cluster analyses are now added to the project and can be visualised as a spatial plot.  Click on an element (cell) in the plot to see its dissimilarity with every other element used in the matrix (the index element is coloured grey).  This is very useful when used in conjunction with tools like Generalised Dissimilarity Modelling and when interpreting correlograms of species turnover.  [Issue #199](/shawnlaffan/biodiverse/issues/199).
    * Grey scale shading is now supported.  [Issue #32](/shawnlaffan/biodiverse/issues/32).
    * Users can now switch between tabs using control-tab and shift-control-tab keys. [Issue #196](/shawnlaffan/biodiverse/issues/196).
    * The colour of the shapefile overlay can be changed.  [Issue #75](/shawnlaffan/biodiverse/issues/75).
    * Outputs tab - the output type is listed next to each output.  [Issue #201](/shawnlaffan/biodiverse/issues/201).
    * Colour stretches can be adjusted using percentile values (2.5, 5, 95, 97.5).  [Issue #244](/shawnlaffan/biodiverse/issues/244).
    * View labels tab
      * Element properties with a value of nodata are displayed as -99999.  [Issue #189](/shawnlaffan/biodiverse/issues/189).
      * System no longer intermittently hangs when control clicking.  [Issue #194](/shawnlaffan/biodiverse/issues/194).
      * Labels list is now stable when sorting by a column with tied values.  [Issue #246](/shawnlaffan/biodiverse/issues/246).
      * Label and group axes can be re-ordered after import.  This is useful when you have forgotten to reorder them at import and, for example, your data file contains a field for latitude before longitude.  [Issue #188](/shawnlaffan/biodiverse/issues/188).
  * Analyses
    * New analysis type of RegionGrower.  It is an extension to the cluster analyses that uses any scalar metric that lumps two neighbour sets together when calculated.  One can also merge those pairs that either maximise or minimise the selected index.  When used with indices like richness it is effectively a one-pass complementarity analysis.  (Its matrices can also be displayed spatially since it is just a variant on the cluster analyses - see [issue #199](/shawnlaffan/biodiverse/issues/199)).  [Issue #204](/shawnlaffan/biodiverse/issues/204).
    * Cluster matrices can be written to file as they are built.  These are not added to the GUI, thus saving memory and allowing extremely large matrices to be built for use in external applications.  [Issue #186](/shawnlaffan/biodiverse/issues/186).
    * More efficient cluster matrix construction and use.  [Issue #185](/shawnlaffan/biodiverse/issues/185), [Issue #210](/shawnlaffan/biodiverse/issues/210), [Issue #234](/shawnlaffan/biodiverse/issues/234)
    * Better handling of empty groups.  [Issue #180](/shawnlaffan/biodiverse/issues/180), [Issue #181](/shawnlaffan/biodiverse/issues/181), [Issue #228](/shawnlaffan/biodiverse/issues/228), [Issue #234](/shawnlaffan/biodiverse/issues/234).
  * Calculations and indices
    * NEST_RESULTANT index is now correctly calculated.  [Issue #182](/shawnlaffan/biodiverse/issues/182).
    * Added phylogenetic nearest taxon distance indices.  [Issue #225](/shawnlaffan/biodiverse/issues/225).
    * Indices for phylogenetic dissimilarity are now available.  [Issue #215](/shawnlaffan/biodiverse/issues/215).  [Issue #240](/shawnlaffan/biodiverse/issues/240).
    * Added AED, BED and related indices.  [Issue #206](/shawnlaffan/biodiverse/issues/206).
    * Added indices for numeric label dissimilarity.  [Issue #223](/shawnlaffan/biodiverse/issues/223).
  * Spatial conditions.
    * sp_select_sequence() now works as a definition query.  [Issue #190](/shawnlaffan/biodiverse/issues/190).
    * sp_is_left_of(), sp_is_right_of() and sp_in_line_with() identify if the element is to one side of a vector or on it.  [Issue #202](/shawnlaffan/biodiverse/issues/202).
    * sp_select_block () for block subsampling.  [Issue #218](/shawnlaffan/biodiverse/issues/218).
    * sp_point_in_polygon().  [Issue #221](/shawnlaffan/biodiverse/issues/221).
    * sp_group_not_empty() - does the group have any labels?  See [Issue #234](/shawnlaffan/biodiverse/issues/234).

To see the full list of issues and changes, see https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=label%3AMilestone-Release0.16+

# Version 0.15 #

Main changes since the previous version (0.14) are:

  * Calculations and Indices
    * The PD node list has been moved to its own calculation ([issue #130](/shawnlaffan/biodiverse/issues/130))
    * The Phylogenetic Endemism (PE) lists have been moved to their own sub ([issue #131](/shawnlaffan/biodiverse/issues/131))
  * Exporting data
    * Exporting groups to raster formats now works properly ([issue #129](/shawnlaffan/biodiverse/issues/129))
    * Exporting matrices from a cluster analyses now works ([issue #142](/shawnlaffan/biodiverse/issues/142))
    * Exporting to ER-Mapper files now works properly, with some caveats (see [issue #135](/shawnlaffan/biodiverse/issues/135) and the [FAQ](FAQ#my_er-mapper-bil-file-is-offset-by-half-a-pixel))
  * Importing data
    * Column numbers are now displayed when importing data ([issue #128](/shawnlaffan/biodiverse/issues/128))
    * Tree imports now use the same quotes character as BaseData imports ([issue #152](/shawnlaffan/biodiverse/issues/152))
  * Spatial Conditions
    * sp_ellipse() works properly now ([issue #150](/shawnlaffan/biodiverse/issues/150))
  * Randomisations
    * Ties are now counted ([issue #146](/shawnlaffan/biodiverse/issues/146))
  * Visualisation
    * User defined properties are now displayed in the view labels tab ([issue #155](/shawnlaffan/biodiverse/issues/155)).
  * Under the bonnet
    * User defined properties are now imported properly in the GUI ([issue #154](/shawnlaffan/biodiverse/issues/154))
    * Neighbour set recycling works properly now ([issue #127](/shawnlaffan/biodiverse/issues/127) & [issue #145](/shawnlaffan/biodiverse/issues/145))
    * Module Statistics::Descriptive2 is now deprecated.  It has been replaced by Biodiverse::Statistics which depends explicitly on Statistics::Descriptive ([issue #139](/shawnlaffan/biodiverse/issues/139))

To see the full list of changes, see https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=label%3AMilestone-Release0.15+


# Version 0.14 #

Main changes since the previous version (0.13) are:

  * GUI (and general)
    * The naming errors with saving basedata, tree, and matrix files to the biodiverse native format have been corrected.  ([Issue #104](/shawnlaffan/biodiverse/issues/104))
    * Reading a tree file from biodiverse format works again.  ([Issue #105](/shawnlaffan/biodiverse/issues/105))
    * The GUI now recognises R style tables for import (as exported using the write.table() function in R).  ([Issue #20](/shawnlaffan/biodiverse/issues/20))
    * Tree and matrix objects can be renamed.  ([Issue #72](/shawnlaffan/biodiverse/issues/72))
    * Users can now describe the selected basedata, tree and matrix.  Results are printed to both a popup and to the log window (from where they can be more easily copied).  ([Issue #93](/shawnlaffan/biodiverse/issues/93))
    * The parameters sections of the Spatial and Cluster tabs can be hidden to free up real estate when selecting calculations to run.  Click on the Parameters button at the top left of the tab to apply it.  ([Issue #68](/shawnlaffan/biodiverse/issues/68))
    * Trees and matrices embedded in basedata objects can be added to the project.  ([Issue #71](/shawnlaffan/biodiverse/issues/71))
    * Labels in a basedata object can be deleted using the nodes/elements in the selected tree or matrix.  The converse can also be done, where those BaseData labels not in the matrix or tree are deleted.  ([issue #74](/shawnlaffan/biodiverse/issues/74)).
  * Calculations and indices:
    * The count calculations have each been seperated into one calculation for the lists and one for the summary stats.  This applies to the local ranges, local sample counts and element lists.
    * Metadata for the indices now includes formulae.  These are displayed in the online help, but are not displayed in the GUI.  http://purl.org/biodiverse/wiki/Indices
    * Added new index, NEST_RESULTANT (nestedness-resultant, [Indices#Nestedness-resultant](Indices#nestedness-resultant)) from Baselga (2010) Glob Ecol Biogeog.  http://dx.doi.org/10.1111/j.1466-8238.2009.00490.x ([issue #92](/shawnlaffan/biodiverse/issues/92))
    * Added binary and sample weighted taxonomic distinctness and variation from Clarke & Warwick (2001) Mar Ecol Progr Ser. http://dx.doi.org/10.3354/meps216265 (note that these are beta level implemenations and need user testing) ([issue #102](/shawnlaffan/biodiverse/issues/102))
    * The Endemism and Rarity calculations are now listed under their own headings.
    * Added new list calculations to enable hierarchical partitioning of the endemism results (the ENDC`_`HPART`_` and ENDW`_`HPART`_` lists).  ([Issue #99](/shawnlaffan/biodiverse/issues/99))
    * The Bray-Curtis calculation ([Indices#Bray-Curtis_non-metric](Indices#bray-curtis-non-metric)) now also returns the A, B and W values used in the calculations. ([Issue #124](/shawnlaffan/biodiverse/issues/124))
    * Added new calculation for Bray-Curtis values normalised by the neighbourhood group counts ([Indices#Bray-Curtis_non-metric,_group_count_normalised](Indices#bray-curtis-non-metric-group-count-normalised)).  Resultant indices are the BRAY_CURTIS_NORM and associated A, B and W values. ([Issue #126](/shawnlaffan/biodiverse/issues/126))
  * Spatial Conditions
    * New condition `sp_match_regex` which allows the user to match using arbitrary regular expressions.  For example, to match any group where the neighbour's third axis starts with the processing group's third axis, use `sp_match_regex (re => qr/^$coord[2]/, axis => 2, type => 'nbr')`.  ([Issue #101](/shawnlaffan/biodiverse/issues/101))
  * Randomisations
    * The randomisations now compare against all lists, not just those in SPATIAL_RESULTS.  One consequence of this is that the resulting list names have changed.  To enable users to keep track of the results across multiple lists, the results are now named using the randomisation name, followed by `>>`, followed by the original list name.  For example, for a randomisation called `Rand1`, one could have resulting lists called `Rand1>>SPATIAL_RESULTS` and `Rand1>>ENDC_WTLIST`.  The naming scheme for the list contents has not changed (see [AnalysisTypes#Randomisations](AnalysisTypes#randomisations)).  The code is not backwards compatible, so previously run randomisations cannot be extended cleanly using this method.  This is because the SPATIAL_RESULTS comparisons will be divided across two lists in an output, e.g. `Rand1` and `Rand1>>SPATIAL_RESULTS`.  Re-running the randomisation from scratch is recommended.  Alternately, one can manually sum the `C_` and `Q_` values across the two result sets and from them calculate the updated `P_` values. ([Issue 100](/shawnlaffan/biodiverse/issues/100))
    * The swapping algorithm has been rewritten so it converges more efficiently  for large data sets.  (Swapping is used to reach richness targets in the rand_structured randomisation).  A consequence of this is that structured randomisations will not produce the same result between versions 0.13 and 0.14 if the seed value is specified.  This is because the random values are used in a different order and so will produce different results if given the same sequence of random values. As with the previous change, the simple solution to this is to start any randomisations afresh after upgrading rather than continuing any existing randomisations.  Continuing randomisations created in BaseData objects prior to version 0.14 will result in mixed algorithms, thus making reproduction of results difficult.  ([Issue #103](/shawnlaffan/biodiverse/issues/103))
    * The comparison algorithm used when comparing spatial analyses now uses recycled results, resulting in a smaller memory footprint.  Recycling occurs when results are the same across the neighbourhood, as occurs with block and zone type spatial conditions.  In these cases one can generate one set of results and apply them across the neighbourhood rather than having multiple sets of identical results.  ([Issue #107](/shawnlaffan/biodiverse/issues/107))
  * Under the bonnet
    * Several optimisations have been added where the system can use recycled results (those where the results are the same for all groups in a neighbourhood).


To see the full list of changes, see https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=label%3AMilestone-Release0.14+

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
    * Newick files are now supported for import (see [issue #79](/shawnlaffan/biodiverse/issues/79)).
    * When displaying the cluster dendrogram, the user can choose not to use the slider bar to select nodes to plot on the map (access via the dendrogram Options menu).
  * Group coordinates can be specified as Degree, Minutes, Seconds within a single column.  (Note: this is currently a beta level implementation).  See [issue #61](/shawnlaffan/biodiverse/issues/61).
  * The system now warns if the user attempts to create a new output, or rename an existing output, using a name that is already in use for that output type (see [issue #62](/shawnlaffan/biodiverse/issues/62)).
  * The randomisation list results are now accessible (see [issue #45](/shawnlaffan/biodiverse/issues/45)).
  * See also https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=label%3AMilestone-Release0.13+

  * For the list of current issues, or to submit a bug report or enhancement request then please see https://github.com/shawnlaffan/biodiverse/issues

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
  * The MXO_WARD and TXO_WARD metrics have been removed.  Use the new ["Compare dissimilarity matrix values"](Indices#compare-dissimilarity-matrix-values) analysis instead.
  * Matrix elements (labels) can be remapped on import, as well as excluded/included using the properties table.
  * The scree plot below the dendrogram is minimised to begin with.  It can be pulled up when needed.

  * See also https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=label%3AMilestone-Release0.12+


# Version 0.11 #

06Nov2009

Main changes since previous version (0.10).  This is a cleanup and bug fix release with no new features.

  * Improved feedback and error trapping when running analyses.  If the system fails then a popup window will tell you what went wrong and where.  This information is still printed to the log window so you can access it after closing the popup.
  * The error trapping also corrects issues where users are unable to close a tab if an analysis fails.
  * Basedata imports fail with a warning when they reach a record with an undefined or non-numeric value to be used for the groups (unless it is a text group).  The user can set an option to skip these records (this is on by default).
  * System warns user when trying to export a randomisation output.  These cannot currently be exported (although the PRNG state would be useful).  The results can be exported from the relevant spatial or cluster output.  See [KeyConcepts#Randomisations](KeyConcepts#randomisations)
  * Exports for spatial outputs, groups and labels now have an option to specify the type of file instead of relying on the file extension for this.  This does not change the possibilities, but does make them clearer.



# Version 0.10 #

21Oct2009

Main changes since previous version (0.9.1185)

  * Phylogenetic endemism indices are now in the main distribution.  For the theory and some examples, see [Rosauer, Laffan et al. (2009) Molecular Ecology](http://dx.doi.org/10.1111/j.1365-294X.2009.04311.x)
  * Basedata objects now import from matrix format files, eg site by species matrices.  These are a common data format for specimen data.
  * Documentation is moving to the Google Code wiki site.  http://code.google.com/p/biodiverse/w/list
  * Renaming of basedata and outputs is now possible in the GUI
  * Users can now specify a definition query to control the groups used in an analysis.  This uses the same syntax as the spatial neighbourhoods.  See http://purl.org/biodiverse/wiki/KeyConcepts#definition-queries
  * Option to show/hide the spatial neighbour and definition query edit boxes in the spatial and cluster tabs.  This frees up screen real estate but does not disable them.
  * Spatial parameters:
    * sp_circle now has an axes argument to control the axes used (default is still to use all axes)
    * New subroutine `sp_match_text (text => 'blah', axis => 0, type => 'proc')`
    * New subroutine `sp_annulus (inner_radius => 100000, outer_radius => 300000)`
    * See http://purl.org/biodiverse/wiki/SpatialConditions for examples.
  * The Biodiverse icon is now used in all versions (previously was only the exe version)
  * The version numbering system now excludes the SVN revision number.
  * Numerous bug fixes - see https://github.com/shawnlaffan/biodiverse/issues?utf8=%E2%9C%93&q=label%3AMilestone-Release0.10+
  * Some minor speed-ups and smaller memory footprint in some cases

  * For the full issues list and to report a bug or request an enhancement, visit https://github.com/shawnlaffan/biodiverse/issues



# Version 0.9.1185 #

Main changes since previous release (version 0.9.1127)

  * Installation instructions updated, particularly for the Mac installs.
  * Fixed bug in tree reading module.  Now correctly reads nexus format files, including those exported from Biodiverse.
  * Documentation updated.
  * Example files added to distribution (data folder)
  * BaseData import now handles text with embedded newlines (these occur occasionally in plant and other data bases, usually in the collection descriptions).
  * Statistics::Descriptive2 now included in the distribution (under the lib folder)
  * Fixed issue where saved project file is given the name "1.bps"