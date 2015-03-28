

# Introduction #

This is an overview of the data structures used in Biodiverse.

All structures store a set of parameters in addition to one or more other types of data.  The parameters are used to record any property needed by the system, as well as other objects such as arguments passed to an analysis.


# Projects #

Projects consist of a set of any number of BaseData, Tree and Matrix objects.  They are self contained as they have no links to essential external files and thus provide a convenient means of keeping a set of related analyses in one location.

The only external data currently linked are shapefiles used as overlays in plotting, and these can be repaired or ignored when plotting data.

Note that saving a BaseData, Tree or Matrix to their own native Biodiverse format elsewhere on disk makes a duplicate copy of that object.  Any changes to that object in the project will have no effect on the separately saved version, and vice versa.  See also the [file naming scheme](#File_naming_scheme.md)

# Elements #

Elements are one of the basic units used in Biodiverse.  Each element has a unique identifier and stores one or more lists, for example the SPATIAL\_RESULTS lists of a moving window analysis.  They are also used in the matrices, in which case one element stores only the value for one matrix cell.

# BaseStructs #

A BaseStruct object consists of a set of [elements](#Elements.md).  It is the storage system used for, amongst other things, the [groups](#Groups.md), [labels](#Labels.md), spatial outputs, and [element property tables](#Element_property_tables.md).

# BaseData #

A BaseData object is the primary storage object used in Biodiverse.  It consists of one Groups object, one Labels object, a set of parameters, and one or more cluster, moving window and randomisation outputs.

One potentially useful function you can perform on the BaseData is to transpose it, causing the labels to be groups and vice versa. To do so, select _Basedata->Transpose_ from the main menu. This will produce a new, transposed BaseData object which you can view and analyse.

## Labels ##

A labels object is a special type of BaseStruct, with the labels being a special type of [element](#Element.md).  Typically they represent species, but in reality they can be any named entity that is then collected and aggregated into a group.  Their unique identifier (name) can consist of any number of axes, allowing the representation of taxonomic order or some other hierarchy within the labels.

## Groups ##

A groups object is also a special type of BaseStruct object, with groups also being a special type of [element](#Element.md).  Typically groups are square cells into which the labels are aggregated (binned), but can represent any number of axes with differing cell sizes and numeric and text types.  These are plotted in the map outputs and used for the spatial components of the moving window, cluster and randomisation analyses.

Groups are analogous to bins in other systems, for example [UniFrac](http://bmf2.colorado.edu/unifrac/index.psp).

Group coordinates: For numerical coordinates, such as X,Y, the group location is given by the centre of the group.  For example, for a cell size of 1, with no offset, the coordinates would each end in .5

## Spatial outputs ##

These are a BaseStruct object and used to store the results of a moving window analysis.  They are also used in the cluster analyses to determine which neighbours should be considered for each of the cluster matrices, as this is just a spatial analysis with no actual analyses, just the neighbour sets for each [element](#Element.md).

More details are (or will be) given in [AnalysisTypes#Spatial\_analyses](AnalysisTypes#Spatial_analyses.md) and [SampleSession#Running\_a\_spatial\_(moving\_window)\_analysis](SampleSession#Running_a_spatial_(moving_window)_analysis.md).

## Cluster outputs ##

These are a tree object, but also store the matrices used in their construction.  The terminal nodes have the name of the relevant [group](#Group.md) (element) from the BaseData object, and this is used to link the data in the display.

More detals are (or will be) given in [AnalysisTypes#Clustering](AnalysisTypes#Clustering.md) and [SampleSession#Running\_a\_Cluster\_Analysis](SampleSession#Running_a_Cluster_Analysis.md).

## Randomisation outputs ##

The randomisation outputs do not themselves store any results (see [AnalysisTypes#Randomisations](AnalysisTypes#Randomisations.md)).  In addition to the arguments used in their creation, they store the PRNG's current state, as well as that used to start the PRNG stream.

See also [SampleSession#Running\_a\_randomisation](SampleSession#Running_a_randomisation.md).

# Matrices #

These are matrices of numeric values representing some relationship between a set of [elements](#Element.md).  They should normally be square, but the system does not impose that requirement.  Normally they are linked to the labels of a BaseData object and used in the visualisation and analyses.  They are also used in the cluster analyses, and if so they can be exported via the cluster outputs.

Previous uses include genetic similarities ([Bickford et al. 2004](http://dx.doi.org/10.1111/j.1365-2699.2004.01127.x)), but any numeric value can be used.  It is up to the user to ensure it is sensible (the system does not stop the user from doing something stupid, just in case it turns out to be really useful).

Matrices in Biodiverse are stored with a high degree of redundancy, so do use a large amount of memory for large matrices.  This is to allow fast access of attributes such as the smallest and largest values, or counts of rows and columns, or how many defined values each row has.  The storage approach may change in the future if a more efficient structure is on offer that retains the aspects of speed.


# Trees #

These are typicaly phylogenies but can be any form of hierarchical tree structure, for example taxonomies or word roots.  Trees are a collection of nodes, with the hierarchy inferred based on links to and from parent and cild nodes.

## Tree Nodes ##

These are the individual units of the trees.  They are analogous to [elements](#Elements.md) in a BaseStruct in that analysis result lists can be stored in them, but they also store links to their parents and to their children.

The node length values are the distance from them to their parent node.  These lengths can be negative in some cases, for example when one or more spatial constraints exclude some more similar elements and/or nodes from the initial clustering.  When these are considered in a subsequent matrix (i.e. for a less constrictive spatial constraint) then
the nodes can be negative for such linkages.  Alternately negative lengths can occur when using the Recalculation Linkage function as a consequence of recalculating the linkages as if the two nodes are single aggregated [elements](#Element.md) instead of a weighted function of their respective elements.  This will occur for the cluster indices that do not use sample counts.

Each node must have a unique name.  In the case of those that link to an [element](#Element.md) (e.g. a [group](#Groups.md) or [label](#Labels.md)) this is straightforward and can use the same name.  Internal nodes are slightly different, and are assigned a unique value followed by three underscore characters (, e.g. `18___`).  This is done on the basis that it is unlikely for an element name to have three trailing underscores.  Using three trailing underscores for non-internal names will cause unpredictable behaviour as Biodiverse uses the name to determine if a node is internal or not.

# Remap tables #

These are [element property tables](#Element_property_tables.md).

# Element property tables #

As with so many objects in Biodiverse, element property tables are also special type of BaseStruct object (making BaseStruct a relevant name).

The primary purpose of these tables is to remap (change) names on import so that one data set will properly match another, for example where one needs to alter a set of labels in a tree to match those used in a BaseData object, or vice versa.  One can also use them to keep a single file with taxonomic aggregations rather than editing one's source data (obviously it will not work for divisions, though).  They can also be used to set arbitrary properties for data set elements for use in subsequent analyses and calculations.  Species ranges and sample counts are two examples that are currently supported.  Others still need to be implemented, but they can be displayed in the View Labels tab as of version 0.15 ([issue #155](https://code.google.com/p/biodiverse/issues/detail?id=#155)).

Note that label and group properties are assigned at the time of import.  Subsequent changes are not currently supported.

One can also use these tables to set element properties such as label or group sample counts or label ranges on import.

One can also exclude or include on a per-label or per-group basis. If one or more include columns are specified then the effect on BaseData and matrix imports is that only elements with at least one import column value that returns true will be included.  If one or more exclude columns are specified then the effect is to exclude any element for which the exclude column is true.  Note that matrices are symmetric so excluding an element will remove all pairs of which it is part.

If the table has more than one entry for the same element name then it will use the last property encountered for that element.  Remapping of element names are chained such that the last one is used.  For example, the table might remap species1 to species2 and then to species3.  In this case any occurrences of elements 'species1' and 'species2' are assigned directly to 'species3', with the final name taking properties set for 'species3' and not 'species1' or 'species2'.  An exception to this is the include and exclude flags.  These are applied to the original element name (although this might change in future).

Label property tables will perhaps be used more often than group property tables, since locations don't change but names do.  However, it can be useful to add additional axis properties to a group based on its location (for example biome and distance from some key feature).  In this way the properties can be defined once instead of being listed for every single row in the input data set (consider the repetition for data set of 2,000,000 input records with only two possible biomes...).

## Importing element property data ##

The import process is similar to that for a BaseData set, in that one must select the file, choose the field separator and quotes characters, and then tell the system what rows and columns represent what.  The meaning of the different options are as follows.  If more than one column is given for the range, sample\_count and Use\_field\_name options then the GUI will take the last one specified.  If used in a script then no order is guaranteed, so take care to specify one column only for those options.  Note that you currently cannot re-order the input or remapped element columns in the GUI so these will need to be in the same order as in the BaseData set.

  * **Input\_element**:  This column will be used to form part of the label or group name.  Select as many of these as you have axes in the BaseData set, otherwise they will not match and the table will have no effect.
  * **Remapped\_element**:  This column will be used to form part of the remapped element name.
  * **Include**:  Control the inclusion of elements.  A value of 1 means it will be included.  More than one of these can be specified (see above for the effect).
  * **Exclude**:  Control the exclusion of elements.  A value of 1 means it will be excluded.  More than one of these can be specified (see above for the effect).
  * **range**:  This value will be used as the label range instead of counting the number of groups in which the label occurs.  This affects the [endemism](Indices#Endemism.md) calculations.
  * **sample\_count**:  This value will be used as the sample count value instead of counting the number of samples at import.  This affects the [rarity](Indices#Rarity.md) calculations.
  * **Use\_field\_name**:  A property will be set for each element that has the name of the field and the value of each row.  Use this to import additional properties for a set of labels or groups.

## The table file ##

The element property (remap) table file is simply a table that has two or more columns that allow you to match the labels used in your tree or matrix to the labels used in your BaseData (or in any of the other directions, as appropriate).  The system uses exact matches to link the BaseData, trees and matrices so this is often a necessary step.

As an example, say you have labels in your BaseData which are made up from two axes (derived from columns for genus and species, e.g. "Pultenaea:obstreperus"), while your tree or matrix has names with only one axis (e.g. "P\_obstreperus").  To make them match in Biodiverse you need to map one to the other.

The first few lines of an example remap table would look like this:

```
Genus,Species,Tree_name
Pultenaea,obstreperus,P_obstreperus
Pultenaea,intransigentus,P_intransigentus
```

When you import the tree and choose to remap the names on the tree, select the remap table file, and then set the columns such that Genus is a remapped\_element, Species is a remapped\_element, Tree\_name is an input\_element.

Note that the field names can be anything.  The fields in the header row are only used for column selection in the GUI.

When remapped, the input\_element column(s) are changed to the combined remapped\_elements.  As noted above, you need to specify as many input\_element and remapped\_element columns as you are using in your respective tree and basedata (or matrix, as appropriate).  For the example above where a tree is being remapped to match the basedata, the basedata uses two axes so the remap table needs to have to remapped\_element columns. The tree names are only one axis (the norm for nexus format trees) so there is only one input\_element column.

Take care with spaces.  Biodiverse uses an exact matching system, so any excess whitespace will cause a non-match to occur.  This is both at the remapping stage and when visualising the data. Basically, " Rhynchospora\_crinipes" is not the same as "Rhynchospora\_crinipes", and the same applies for " Rhynchospora crinipes" and "Rhynchospora crinipes".  Both case have a space at the start of the first of the pair.


# File naming scheme #

The naming system is a “b” for Biodiverse, followed by a letter for the object type, and then an “s” or “y” to denote if it is in a Storable or YAML format. The Storable version is preferred.  The YAML format requires more time to parse in and out and uses more memory.  It is deprecated and will be removed in a future release, but will be supported for export as it is sometimes useful to interrogate the internal data structure using a text editor.

BPS/BPY is a Biodiverse project file. This stores a set of BaseData, Matrix and Phylogeny objects and any display parameters.  Note that it stores copies of these objects, so changes made to any of the separate or original versions have no effect, and vice versa.

BDS/BDY is a Biodiverse BaseData object.

BTS/BTY is a Tree object.

BMS/BMY is a matrix object.

The BaseData objects and their cluster and spatial outputs contain references to any matrix or phylogeny arguments to enable the randomisations to function effectively. These references mean that copies of the matrices and phylogenies will be stored with the BaseData object if it is exported separately from a project, but will not be visible if the BaseData object is subsequently loaded into a new project.  Use the _BaseData->Extract embedded matrices_ and _BaseData->Extract embedded tree_ menu options to make them available to the project.

Note that it is not possible to directly save a cluster, spatial or randomisation analysis from the GUI because the object needs its links to the parent BaseData object.  The reference system used means that the BaseData object will be folded into the analysis object through its reference, thus making the separation unnecessary and complex to unravel on subsequent import.