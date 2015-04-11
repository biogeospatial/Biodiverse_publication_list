# Indices available in Biodiverse #
_Generated GMT Tue Oct 29 03:40:34 2013 using build_indices_table.pl, Biodiverse version 0.19._


This is a listing of the indices available in Biodiverse,
ordered by the calculations used to generate them.
It is generated from the system metadata and contains all the
information visible in the GUI, plus some additional details.

Most of the headings are self-explanatory.  For the others:
  * The **Subroutine** is the name of the subroutine used to call the function if you are using Biodiverse through a script.
  * The **Index** is the name of the index in the SPATIAL_RESULTS list, or if it is its own list then this will be its name.  These lists can contain a variety of values, but are usually lists of labels with some value, for example the weights used in an endemism calculation.  The names of such lists typically end in "LIST", "ARRAY", "HASH" or "LABELS".
  * **Valid cluster metric** is whether or not the index can be used as a clustering metric.  A blank value means it cannot.
  * The **Minimum number of neighbour sets** dictates whether or not a calculation or index will be run.  If you specify only one neighbour set then all those calculations that require two sets will be dropped from the analysis.  (This is always the case for calculations applied to cluster nodes as there is only one neighbour set, defined by the set of groups linked to the terminal nodes below a cluster node).  Note that many of the calculations lump neighbour sets 1 and 2 together.  See the SpatialConditions page for more details on neighbour sets.

Note that calculations can provide different numbers of indices depending on the nature of the BaseData set used.
This currently applies to the hierarchically partitioned endemism calculations (both [central](#Endemism_central_hierarchical_partition) and [whole](#Endemism_whole_hierarchical_partition)) and [hierarchical labels](#Hierarchical_Labels).

Table of contents:


## Element Properties ##




> ### Group property Gi* statistics ###

**Description:**   List of Getis-Ord Gi* statistics for each group property across both neighbour sets

**Subroutine:**   calc_gpprop_gistar

**Reference:**   Getis and Ord (1992) Geographical Analysis. http://dx.doi.org/10.1111/j.1538-4632.1992.tb00261.x


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 1 | GPPROP_GISTAR_LIST | List of Gi* scores|   | 1 |







> ### Group property data ###

**Description:**   Lists of the groups and their property values used in the group properties calculations

**Subroutine:**   calc_gpprop_lists

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 2 | GPPROP_STATS_EXAMPLE_GPROP1_DATA |   |   | 1 |
| 3 | GPPROP_STATS_EXAMPLE_GPROP2_DATA |   |   | 1 |







> ### Group property hashes ###

**Description:**   Hashes of the groups and their property values used in the group properties calculations. Hash keys are the property values, hash values are the property value frequencies.

**Subroutine:**   calc_gpprop_hashes

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 4 | GPPROP_STATS_EXAMPLE_GPROP1_HASH |   |   | 1 |
| 5 | GPPROP_STATS_EXAMPLE_GPROP2_HASH |   |   | 1 |







> ### Group property quantiles ###

**Description:**   Quantiles for each group property across both neighbour sets

**Subroutine:**   calc_gpprop_quantiles

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 6 | GPPROP_QUANTILE_LIST | List of quantiles for the label properties (05 10 20 30 40 50 60 70 80 90 95) |   | 1 |







> ### Group property summary stats ###

**Description:**   List of summary statistics for each group property across both neighbour sets

**Subroutine:**   calc_gpprop_stats

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 7 | GPPROP_STATS_LIST | List of summary statistics (count mean min max median sum sd iqr) |   | 1 |







> ### Label property Gi**statistics ###**

**Description:**   List of Getis-Ord Gi**statistic for each label property across both neighbour sets**

**Subroutine:**   calc_lbprop_gistar

**Reference:**   Getis and Ord (1992) Geographical Analysis. http://dx.doi.org/10.1111/j.1538-4632.1992.tb00261.x


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 8 | LBPROP_GISTAR_LIST | List of Gi**scores**|   | 1 |







> ### Label property data ###

**Description:**   Lists of the labels and their property values used in the label properties calculations

**Subroutine:**   calc_lbprop_data

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 9 | LBPROP_STATS_EXAMPLE_PROP1_DATA |   |   | 1 |
| 10 | LBPROP_STATS_EXAMPLE_PROP2_DATA |   |   | 1 |







> ### Label property hashes ###

**Description:**   Hashes of the labels and their property values used in the label properties calculations. Hash keys are the property values, hash values are the property value frequencies.

**Subroutine:**   calc_lbprop_hashes

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 11 | LBPROP_STATS_EXAMPLE_PROP1_HASH |   |   | 1 |
| 12 | LBPROP_STATS_EXAMPLE_PROP2_HASH |   |   | 1 |







> ### Label property lists ###

**Description:**   Lists of the labels and their property values within the neighbour sets

**Subroutine:**   calc_lbprop_lists

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 13 | LBPROP_LIST_EXAMPLE_PROP1 |   |   | 1 |
| 14 | LBPROP_LIST_EXAMPLE_PROP2 |   |   | 1 |







> ### Label property quantiles ###

**Description:**   List of quantiles for each label property across both neighbour sets


**Subroutine:**   calc_lbprop_quantiles

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 15 | LBPROP_QUANTILES | List of quantiles for the label properties: (05 10 20 30 40 50 60 70 80 90 95) |   | 1 |







> ### Label property summary stats ###

**Description:**   List of summary statistics for each label property across both neighbour sets


**Subroutine:**   calc_lbprop_stats

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 16 | LBPROP_STATS | List of summary statistics (count mean min max median sum skewness kurtosis sd iqr) |   | 1 |


## Endemism ##




> ### Absolute endemism ###

**Description:**   Absolute endemism scores.


**Subroutine:**   calc_endemism_absolute

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 17 | END_ABS1 | Count of labels entirely endemic to neighbour set 1 |   | 1 |
| 18 | END_ABS1_P | Proportion of labels entirely endemic to neighbour set 1 |   | 1 |
| 19 | END_ABS2 | Count of labels entirely endemic to neighbour set 2 |   | 1 |
| 20 | END_ABS2_P | Proportion of labels entirely endemic to neighbour set 2 |   | 1 |
| 21 | END_ABS_ALL | Count of labels entirely endemic to neighbour sets 1 and 2 combined |   | 1 |
| 22 | END_ABS_ALL_P | Proportion of labels entirely endemic to neighbour sets 1 and 2 combined |   | 1 |







> ### Absolute endemism ###

**Description:**   Lists underlying the absolute endemism scores.


**Subroutine:**   calc_endemism_absolute_lists

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 23 | END_ABS1_LIST | List of labels entirely endemic to neighbour set 1 |   | 1 |
| 24 | END_ABS2_LIST | List of labels entirely endemic to neighbour set 1 |   | 1 |
| 25 | END_ABS_ALL_LIST | List of labels entirely endemic to neighbour sets 1 and 2 combined |   | 1 |







> ### Endemism central ###

**Description:**   Calculate endemism for labels only in neighbour set 1, but with local ranges calculated using both neighbour sets

**Subroutine:**   calc_endemism_central

**Reference:**   Crisp et al. (2001) J Biogeog. http://dx.doi.org/10.1046/j.1365-2699.2001.00524.x ; Laffan and Crisp (2003) J Biogeog. http://www3.interscience.wiley.com/journal/118882020/abstract


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** | **Reference** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|:--------------|
| 26 | ENDC_CWE | Corrected weighted endemism |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \frac{ENDC_WE}{ENDC_RICHNESS}%.png' title='= \frac{ENDC_WE}{ENDC_RICHNESS}' />  |   |
| 27 | ENDC_RICHNESS | Richness used in ENDC_CWE (same as index RICHNESS_SET1) |   | 1 |   |   |
| 28 | ENDC_SINGLE | Endemism unweighted by the number of neighbours. Counts each label only once, regardless of how many groups in the neighbourhood it is found in.   Useful if your data have sampling biases and best applied with a small window. |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \sum_{t \in T} \frac {1} {R_t}%.png' title='= \sum_{t \in T} \frac {1} {R_t}' /> where <img src='http://latex.codecogs.com/png.latex?t%.png' title='t' /> is a label (taxon) in the set of labels (taxa) <img src='http://latex.codecogs.com/png.latex?T%.png' title='T' /> in neighbour set 1, and <img src='http://latex.codecogs.com/png.latex?R_t%.png' title='R_t' /> is the global range of label <img src='http://latex.codecogs.com/png.latex?t%.png' title='t' /> across the data set (the number of groups it is found in, unless the range is specified at import).  | Slatyer et al. (2007) J. Biogeog http://dx.doi.org/10.1111/j.1365-2699.2006.01647.x |
| 29 | ENDC_WE | Weighted endemism |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \sum_{t \in T} \frac {r_t} {R_t}%.png' title='= \sum_{t \in T} \frac {r_t} {R_t}' /> where <img src='http://latex.codecogs.com/png.latex?t%.png' title='t' /> is a label (taxon) in the set of labels (taxa) <img src='http://latex.codecogs.com/png.latex?T%.png' title='T' /> in neighbour set 1, <img src='http://latex.codecogs.com/png.latex?r_t%.png' title='r_t' /> is the local range (the number of elements containing label <img src='http://latex.codecogs.com/png.latex?t%.png' title='t' /> within neighbour sets 1 & 2, this is also its value in list ABC2_LABELS_ALL), and <img src='http://latex.codecogs.com/png.latex?R_t%.png' title='R_t' /> is the global range of label <img src='http://latex.codecogs.com/png.latex?t%.png' title='t' /> across the data set (the number of groups it is found in, unless the range is specified at import).  |   |







> ### Endemism central hierarchical partition ###

**Description:**   Partition the endemism central results based on the taxonomic hierarchy inferred from the label axes. (Level 0 is the highest).

**Subroutine:**   calc_endemism_central_hier_part

**Reference:**   Laffan et al. (2013) J Biogeog. http://dx.doi.org/10.1111/jbi.12001


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 30 | ENDC_HPART_0 | List of the proportional contribution of labels to the endemism central calculations, hierarchical level 0 |   | 1 |
| 31 | ENDC_HPART_1 | List of the proportional contribution of labels to the endemism central calculations, hierarchical level 1 |   | 1 |
| 32 | ENDC_HPART_C_0 | List of the proportional count of labels to the endemism central calculations (equivalent to richness per hierarchical grouping), hierarchical level 0 |   | 1 |
| 33 | ENDC_HPART_C_1 | List of the proportional count of labels to the endemism central calculations (equivalent to richness per hierarchical grouping), hierarchical level 1 |   | 1 |
| 34 | ENDC_HPART_E_0 | List of the expected proportional contribution of labels to the endemism central calculations (richness per hierarchical grouping divided by overall richness), hierarchical level 0 |   | 1 |
| 35 | ENDC_HPART_E_1 | List of the expected proportional contribution of labels to the endemism central calculations (richness per hierarchical grouping divided by overall richness), hierarchical level 1 |   | 1 |
| 36 | ENDC_HPART_OME_0 | List of the observed minus expected proportional contribution of labels to the endemism central calculations , hierarchical level 0 |   | 1 |
| 37 | ENDC_HPART_OME_1 | List of the observed minus expected proportional contribution of labels to the endemism central calculations , hierarchical level 1 |   | 1 |







> ### Endemism central lists ###

**Description:**   Lists used in endemism central calculations

**Subroutine:**   calc_endemism_central_lists

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 38 | ENDC_RANGELIST | List of ranges for each label used in the endemism central calculations |   | 1 |
| 39 | ENDC_WTLIST | List of weights for each label used in the endemism central calculations |   | 1 |







> ### Endemism central normalised ###

**Description:**   Normalise the WE and CWE scores by the neighbourhood size.
(The number of groups used to determine the local ranges).


**Subroutine:**   calc_endemism_central_normalised

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|
| 40 | ENDC_CWE_NORM | Corrected weighted endemism normalised by groups |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \frac{ENDC_CWE}{EL_COUNT_ALL}%.png' title='= \frac{ENDC_CWE}{EL_COUNT_ALL}' />  |
| 41 | ENDC_WE_NORM | Weighted endemism normalised by groups |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \frac{ENDC_WE}{EL_COUNT_ALL}%.png' title='= \frac{ENDC_WE}{EL_COUNT_ALL}' />  |







> ### Endemism whole ###

**Description:**   Calculate endemism using all labels found in both neighbour sets

**Subroutine:**   calc_endemism_whole

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** | **Reference** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|:--------------|
| 42 | ENDW_CWE | Corrected weighted endemism |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \frac{ENDW_WE}{ENDW_RICHNESS}%.png' title='= \frac{ENDW_WE}{ENDW_RICHNESS}' />  |   |
| 43 | ENDW_RICHNESS | Richness used in ENDW_CWE (same as index RICHNESS_ALL) |   | 1 |   |   |
| 44 | ENDW_SINGLE | Endemism unweighted by the number of neighbours. Counts each label only once, regardless of how many groups in the neighbourhood it is found in.   Useful if your data have sampling biases and best applied with a small window. |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \sum_{t \in T} \frac {1} {R_t}%.png' title='= \sum_{t \in T} \frac {1} {R_t}' /> where <img src='http://latex.codecogs.com/png.latex?t%.png' title='t' /> is a label (taxon) in the set of labels (taxa) <img src='http://latex.codecogs.com/png.latex?T%.png' title='T' /> across neighbour sets 1 & 2, and <img src='http://latex.codecogs.com/png.latex?R_t%.png' title='R_t' /> is the global range of label <img src='http://latex.codecogs.com/png.latex?t%.png' title='t' /> across the data set (the number of groups it is found in, unless the range is specified at import).  | Slatyer et al. (2007) J. Biogeog http://dx.doi.org/10.1111/j.1365-2699.2006.01647.x |
| 45 | ENDW_WE | Weighted endemism |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \sum_{t \in T} \frac {r_t} {R_t}%.png' title='= \sum_{t \in T} \frac {r_t} {R_t}' /> where <img src='http://latex.codecogs.com/png.latex?t%.png' title='t' /> is a label (taxon) in the set of labels (taxa) <img src='http://latex.codecogs.com/png.latex?T%.png' title='T' /> across both neighbour sets, <img src='http://latex.codecogs.com/png.latex?r_t%.png' title='r_t' /> is the local range (the number of elements containing label <img src='http://latex.codecogs.com/png.latex?t%.png' title='t' /> within neighbour sets 1 & 2, this is also its value in list ABC2_LABELS_ALL), and <img src='http://latex.codecogs.com/png.latex?R_t%.png' title='R_t' /> is the global range of label <img src='http://latex.codecogs.com/png.latex?t%.png' title='t' /> across the data set (the number of groups it is found in, unless the range is specified at import).  |   |







> ### Endemism whole hierarchical partition ###

**Description:**   Partition the endemism whole results based on the taxonomic hierarchy inferred from the label axes. (Level 0 is the highest).

**Subroutine:**   calc_endemism_whole_hier_part

**Reference:**   Laffan et al. (2013) J Biogeog. http://dx.doi.org/10.1111/jbi.12001


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 46 | ENDW_HPART_0 | List of the proportional contribution of labels to the endemism whole calculations, hierarchical level 0 |   | 1 |
| 47 | ENDW_HPART_1 | List of the proportional contribution of labels to the endemism whole calculations, hierarchical level 1 |   | 1 |
| 48 | ENDW_HPART_C_0 | List of the proportional count of labels to the endemism whole calculations (equivalent to richness per hierarchical grouping), hierarchical level 0 |   | 1 |
| 49 | ENDW_HPART_C_1 | List of the proportional count of labels to the endemism whole calculations (equivalent to richness per hierarchical grouping), hierarchical level 1 |   | 1 |
| 50 | ENDW_HPART_E_0 | List of the expected proportional contribution of labels to the endemism whole calculations (richness per hierarchical grouping divided by overall richness), hierarchical level 0 |   | 1 |
| 51 | ENDW_HPART_E_1 | List of the expected proportional contribution of labels to the endemism whole calculations (richness per hierarchical grouping divided by overall richness), hierarchical level 1 |   | 1 |
| 52 | ENDW_HPART_OME_0 | List of the observed minus expected proportional contribution of labels to the endemism whole calculations , hierarchical level 0 |   | 1 |
| 53 | ENDW_HPART_OME_1 | List of the observed minus expected proportional contribution of labels to the endemism whole calculations , hierarchical level 1 |   | 1 |







> ### Endemism whole lists ###

**Description:**   Lists used in the endemism whole calculations

**Subroutine:**   calc_endemism_whole_lists

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 54 | ENDW_RANGELIST | List of ranges for each label used in the endemism whole calculations |   | 1 |
| 55 | ENDW_WTLIST | List of weights for each label used in the endemism whole calculations |   | 1 |







> ### Endemism whole normalised ###

**Description:**   Normalise the WE and CWE scores by the neighbourhood size.
(The number of groups used to determine the local ranges).


**Subroutine:**   calc_endemism_whole_normalised

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|
| 56 | ENDW_CWE_NORM | Corrected weighted endemism normalised by groups |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \frac{ENDW_CWE}{EL_COUNT_ALL}%.png' title='= \frac{ENDW_CWE}{EL_COUNT_ALL}' />  |
| 57 | ENDW_WE_NORM | Weighted endemism normalised by groups |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \frac{ENDW_WE}{EL_COUNT_ALL}%.png' title='= \frac{ENDW_WE}{EL_COUNT_ALL}' />  |


## Hierarchical Labels ##




> ### Ratios of hierarchical labels ###

**Description:**   Analyse the diversity of labels using their hierarchical levels.
The A, B and C scores are the same as in the Label Counts analysis (calc_label_counts)
but calculated for each hierarchical level, e.g. for three axes one could have
A0 as the Family level, A1 for the Family:Genus level,
and A2 for the Family:Genus:Species level.
The number of indices generated depends on how many axes are used in the labels.
In this case there are 2.  Axes are numbered from zero
as the highest level in the hierarchy, so level 0 is the top level
of the hierarchy.


**Subroutine:**   calc_hierarchical_label_ratios

**Reference:**   Jones and Laffan (2008) Trans Philol Soc http://dx.doi.org/10.1111/j.1467-968X.2008.00209.x


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 58 | HIER_A0 | A score for level 0 |   | 2 |
| 59 | HIER_A1 | A score for level 1 |   | 2 |
| 60 | HIER_ARAT1_0 | Ratio of A scores, (HIER_A1 / HIER_A0) |   | 2 |
| 61 | HIER_ASUM0 | Sum of shared label sample counts, level 0 |   | 2 |
| 62 | HIER_ASUM1 | Sum of shared label sample counts, level 1 |   | 2 |
| 63 | HIER_ASUMRAT1_0 | 1 - Ratio of shared label sample counts, (HIER_ASUM1 / HIER_ASUM0) | cluster metric | 2 |
| 64 | HIER_B0 | B score  for level 0 |   | 2 |
| 65 | HIER_B1 | B score  for level 1 |   | 2 |
| 66 | HIER_BRAT1_0 | Ratio of B scores, (HIER_B1 / HIER_B0) |   | 2 |
| 67 | HIER_C0 | C score for level 0 |   | 2 |
| 68 | HIER_C1 | C score for level 1 |   | 2 |
| 69 | HIER_CRAT1_0 | Ratio of C scores, (HIER_C1 / HIER_C0) |   | 2 |


## Inter-event Interval Statistics ##




> ### Inter-event interval statistics ###

**Description:**   Calculate summary statistics from a set of numeric labels that represent event times.
Event intervals are calculated within groups, then aggregated across the neighbourhoods, and then summary stats are calculated.

**Subroutine:**   calc_iei_stats

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 70 | IEI_CV | Coefficient of variation (IEI_SD / IEI_MEAN) |   | 1 |
| 71 | IEI_GMEAN | Geometric mean |   | 1 |
| 72 | IEI_KURT | Kurtosis |   | 1 |
| 73 | IEI_MAX | Maximum value (100th percentile) |   | 1 |
| 74 | IEI_MEAN | Mean | cluster metric | 1 |
| 75 | IEI_MIN | Minimum value (zero percentile) |   | 1 |
| 76 | IEI_N | Number of samples |   | 1 |
| 77 | IEI_RANGE | Range (max - min) |   | 1 |
| 78 | IEI_SD | Standard deviation |   | 1 |
| 79 | IEI_SKEW | Skewness |   | 1 |







> ### Inter-event interval statistics data ###

**Description:**   The underlying data used for the IEI stats.

**Subroutine:**   calc_iei_data

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 80 | IEI_DATA_ARRAY | Interval data in array form.  Multiple occurrences are repeated  |   | 1 |
| 81 | IEI_DATA_HASH | Interval data in hash form where the  interval is the key and number of occurrences is the value |   | 1 |


## Lists and Counts ##




> ### Element counts ###

**Description:**   Counts of elements used in neighbour sets 1 and 2.


**Subroutine:**   calc_elements_used

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 82 | EL_COUNT_ALL | Count of elements in both neighbour sets |   | 2 |
| 83 | EL_COUNT_SET1 | Count of elements in neighbour set 1 |   | 1 |
| 84 | EL_COUNT_SET2 | Count of elements in neighbour set 2 |   | 2 |







> ### Element lists ###

**Description:**   Lists of elements used in neighbour sets 1 and 2.
These form the basis for all the spatial calculations.

**Subroutine:**   calc_element_lists_used

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 85 | EL_LIST_ALL | List of elements in both neighour sets |   | 2 |
| 86 | EL_LIST_SET1 | List of elements in neighbour set 1 |   | 1 |
| 87 | EL_LIST_SET2 | List of elements in neighbour set 2 |   | 2 |







> ### Label counts ###

**Description:**   Counts of labels in neighbour sets 1 and 2.
These form the basis for the Taxonomic Dissimilarity and Comparison indices.

**Subroutine:**   calc_abc_counts

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 88 | ABC_A | Count of labels common to both neighbour sets |   | 2 |
| 89 | ABC_ABC | Total label count across both neighbour sets (same as RICHNESS_ALL) |   | 2 |
| 90 | ABC_B | Count of labels unique to neighbour set 1 |   | 2 |
| 91 | ABC_C | Count of labels unique to neighbour set 2 |   | 2 |







> ### Label counts not in sample ###

**Description:**   Count of basedata labels not in either neighbour set (shared absence)
Used in some of the dissimilarity metrics.

**Subroutine:**   calc_d

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 92 | ABC_D | Count of labels not in either neighbour set (D score) |   | 1 |







> ### Local range lists ###

**Description:**   Lists of labels with their local ranges as values.
The local ranges are the number of elements in which each label is found in each neighour set.

**Subroutine:**   calc_local_range_lists

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 93 | ABC2_LABELS_ALL | List of labels in both neighbour sets |   | 2 |
| 94 | ABC2_LABELS_SET1 | List of labels in neighbour set 1 |   | 1 |
| 95 | ABC2_LABELS_SET2 | List of labels in neighbour set 2 |   | 2 |







> ### Local range summary statistics ###

**Description:**   Summary stats of the local ranges within neighour sets.

**Subroutine:**   calc_local_range_stats

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 96 | ABC2_MEAN_ALL | Mean label range in both element sets |   | 1 |
| 97 | ABC2_MEAN_SET1 | Mean label range in neighbour set 1 |   | 1 |
| 98 | ABC2_MEAN_SET2 | Mean label range in neighbour set 2 |   | 2 |
| 99 | ABC2_SD_ALL | Standard deviation of label ranges in both element sets |   | 2 |
| 100 | ABC2_SD_SET1 | Standard deviation of label ranges in neighbour set 1 |   | 1 |
| 101 | ABC2_SD_SET2 | Standard deviation of label ranges in neighbour set 2 |   | 2 |







> ### Redundancy ###

**Description:**   Ratio of labels to samples.
Values close to 1 are well sampled while zero means
there is no redundancy in the sampling


**Subroutine:**   calc_redundancy

**Reference:**   Garcillan et al. (2003) J Veget. Sci. http://dx.doi.org/10.1111/j.1654-1103.2003.tb02174.x


**Formula:**
> <img src='http://latex.codecogs.com/png.latex?= 1 - \frac{richness}{sum\ of\ the\ sample\ counts}%.png' title='= 1 - \frac{richness}{sum\ of\ the\ sample\ counts}' />

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|
| 102 | REDUNDANCY_ALL | for both neighbour sets |   | 1 | <img src='http://latex.codecogs.com/png.latex?= 1 - \frac{RICHNESS_ALL}{ABC3_SUM_ALL}%.png' title='= 1 - \frac{RICHNESS_ALL}{ABC3_SUM_ALL}' />   |
| 103 | REDUNDANCY_SET1 | for neighour set 1 |   | 1 | <img src='http://latex.codecogs.com/png.latex?= 1 - \frac{RICHNESS_SET1}{ABC3_SUM_SET1}%.png' title='= 1 - \frac{RICHNESS_SET1}{ABC3_SUM_SET1}' />   |
| 104 | REDUNDANCY_SET2 | for neighour set 2 |   | 2 | <img src='http://latex.codecogs.com/png.latex?= 1 - \frac{RICHNESS_SET2}{ABC3_SUM_SET2}%.png' title='= 1 - \frac{RICHNESS_SET2}{ABC3_SUM_SET2}' />   |







> ### Richness ###

**Description:**   Count the number of labels in the neighbour sets

**Subroutine:**   calc_richness

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 105 | RICHNESS_ALL | for both sets of neighbours |   | 1 |
| 106 | RICHNESS_SET1 | for neighbour set 1 |   | 1 |
| 107 | RICHNESS_SET2 | for neighbour set 2 |   | 2 |







> ### Sample count lists ###

**Description:**   Lists of sample counts for each label within the neighbour sets.
These form the basis of the sample indices.

**Subroutine:**   calc_local_sample_count_lists

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 108 | ABC3_LABELS_ALL | List of labels in both neighbour sets with their sample counts as the values. |   | 2 |
| 109 | ABC3_LABELS_SET1 | List of labels in neighbour set 1. Values are the sample counts.   |   | 1 |
| 110 | ABC3_LABELS_SET2 | List of labels in neighbour set 2. Values are the sample counts. |   | 2 |







> ### Sample count summary stats ###

**Description:**   Summary stats of the sample counts across the neighbour sets.


**Subroutine:**   calc_local_sample_count_stats

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 111 | ABC3_MEAN_ALL | Mean of label sample counts across both element sets. |   | 2 |
| 112 | ABC3_MEAN_SET1 | Mean of label sample counts in neighbour set1. |   | 1 |
| 113 | ABC3_MEAN_SET2 | Mean of label sample counts in neighbour set 2. |   | 2 |
| 114 | ABC3_SD_ALL | Standard deviation of label sample counts in both element sets. |   | 2 |
| 115 | ABC3_SD_SET1 | Standard deviation of sample counts in neighbour set 1. |   | 1 |
| 116 | ABC3_SD_SET2 | Standard deviation of label sample counts in neighbour set 2. |   | 2 |
| 117 | ABC3_SUM_ALL | Sum of the label sample counts across both neighbour sets. |   | 2 |
| 118 | ABC3_SUM_SET1 | Sum of the label sample counts across both neighbour sets. |   | 1 |
| 119 | ABC3_SUM_SET2 | Sum of the label sample counts in neighbour set2. |   | 2 |


## Matrix ##




> ### Compare dissimilarity matrix values ###

**Description:**   Compare the set of labels in one neighbour set with those in another using their matrix values. Labels not in the matrix are ignored. This calculation assumes a matrix of dissimilarities and uses 0 as identical, so take care).

**Subroutine:**   calc_compare_dissim_matrix_values

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 120 | MXD_COUNT | Count of comparisons used. |   | 2 |
| 121 | MXD_LIST1 | List of the labels used from neighbour set 1 (those in the matrix). The list values are the number of times each label was used in the calculations. This will always be 1 for labels in neighbour set 1. |   | 2 |
| 122 | MXD_LIST2 | List of the labels used from neighbour set 2 (those in the matrix). The list values are the number of times each label was used in the calculations. This will equal the number of labels used from neighbour set 1. |   | 2 |
| 123 | MXD_MEAN | Mean dissimilarity of labels in set 1 to those in set 2. | cluster metric | 2 |
| 124 | MXD_VARIANCE | Variance of the dissimilarity values, set 1 vs set 2. | cluster metric | 2 |







> ### Matrix statistics ###

**Description:**   Calculate summary statistics of matrix elements in the selected matrix for labels found across both neighbour sets.
Labels not in the matrix are ignored.

**Subroutine:**   calc_matrix_stats

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 125 | MX_KURT | Kurtosis |   | 1 |
| 126 | MX_LABELS | List of the matrix labels in the neighbour sets |   | 1 |
| 127 | MX_MAXVALUE | Maximum value |   | 1 |
| 128 | MX_MEAN | Mean |   | 1 |
| 129 | MX_MEDIAN | Median |   | 1 |
| 130 | MX_MINVALUE | Minimum value |   | 1 |
| 131 | MX_N | Number of samples (matrix elements, not labels) |   | 1 |
| 132 | MX_PCT05 | 5th percentile value |   | 1 |
| 133 | MX_PCT25 | First quartile (25th percentile) |   | 1 |
| 134 | MX_PCT75 | Third quartile (75th percentile) |   | 1 |
| 135 | MX_PCT95 | 95th percentile value |   | 1 |
| 136 | MX_RANGE | Range (max-min) |   | 1 |
| 137 | MX_SD | Standard deviation |   | 1 |
| 138 | MX_SKEW | Skewness |   | 1 |
| 139 | MX_VALUES | List of the matrix values |   | 1 |







> ### Rao's quadratic entropy, matrix weighted ###

**Description:**   Calculate Rao's quadratic entropy for a matrix weights scheme.
BaseData labels not in the matrix are ignored

**Subroutine:**   calc_mx_rao_qe

**Formula:**
> <img src='http://latex.codecogs.com/png.latex?= \sum_{i \in L} \sum_{j \in L} d_{ij} p_i p_j%.png' title='= \sum_{i \in L} \sum_{j \in L} d_{ij} p_i p_j' /> where <img src='http://latex.codecogs.com/png.latex?p_i%.png' title='p_i' /> and <img src='http://latex.codecogs.com/png.latex?p_j%.png' title='p_j' /> are the sample counts for the i'th and j'th labels, <img src='http://latex.codecogs.com/png.latex?d_{ij}%.png' title='d_{ij}' /> is the matrix value for the pair of labels <img src='http://latex.codecogs.com/png.latex?ij%.png' title='ij' /> and <img src='http://latex.codecogs.com/png.latex?L%.png' title='L' /> is the set of labels across both neighbour sets that occur in the matrix.

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 140 | MX_RAO_QE | Matrix weighted quadratic entropy |   | 1 |
| 141 | MX_RAO_TLABELS | List of labels and values used in the MX_RAO_QE calculations |   | 1 |
| 142 | MX_RAO_TN | Count of comparisons used to calculate MX_RAO_QE |   | 1 |


## Numeric Labels ##




> ### Numeric label data ###

**Description:**   The underlying data used for the numeric labels stats, as an array.
For the hash form, use the ABC3_LABELS_ALL index from the 'Sample count lists' calculation.

**Subroutine:**   calc_numeric_label_data

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 143 | NUM_DATA_ARRAY | Numeric label data in array form.  Multiple occurrences are repeated based on their sample counts. |   | 1 |







> ### Numeric label dissimilarity ###

**Description:**   Compare the set of numeric labels in one neighbour set with those in another.

**Subroutine:**   calc_numeric_label_dissimilarity

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|
| 144 | NUMD_ABSMEAN | Mean absolute dissimilarity of labels in set 1 to those in set 2. | cluster metric | 2 | <img src='http://latex.codecogs.com/png.latex?= \frac{\sum_{l_{1i} \in L_1} \sum_{l_{2j} \in L_2} abs (l_{1i} - l_{2j})(w_{1i} \times w_{2j})}{n_1 \times n_2}%.png' title='= \frac{\sum_{l_{1i} \in L_1} \sum_{l_{2j} \in L_2} abs (l_{1i} - l_{2j})(w_{1i} \times w_{2j})}{n_1 \times n_2}' /> where<img src='http://latex.codecogs.com/png.latex?L1%.png' title='L1' /> and <img src='http://latex.codecogs.com/png.latex?L2%.png' title='L2' /> are the labels in neighbour sets 1 and 2 respectively, and <img src='http://latex.codecogs.com/png.latex?n1%.png' title='n1' /> and <img src='http://latex.codecogs.com/png.latex?n2%.png' title='n2' /> are the sample counts in neighbour sets 1 and 2  |
| 145 | NUMD_COUNT | Count of comparisons used. |   | 2 | <img src='http://latex.codecogs.com/png.latex?= n1 * n2%.png' title='= n1 * n2' /> where values are as for <img src='http://latex.codecogs.com/png.latex?NUMD_ABSMEAN%.png' title='NUMD_ABSMEAN' />  |
| 146 | NUMD_VARIANCE | Variance of the dissimilarity values (mean squared deviation), set 1 vs set 2. | cluster metric | 2 | <img src='http://latex.codecogs.com/png.latex?= \frac{\sum_{l_{1i} \in L_1} \sum_{l_{2j} \in L_2} (l_{1i} - l_{2j})^2(w_{1i} \times w_{2j})}{n_1 \times n_2}%.png' title='= \frac{\sum_{l_{1i} \in L_1} \sum_{l_{2j} \in L_2} (l_{1i} - l_{2j})^2(w_{1i} \times w_{2j})}{n_1 \times n_2}' /> where values are as for <img src='http://latex.codecogs.com/png.latex?NUMD_ABSMEAN%.png' title='NUMD_ABSMEAN' />  |







> ### Numeric label harmonic and geometric means ###

**Description:**   Calculate geometric and harmonic means for a set of numeric labels.


**Subroutine:**   calc_numeric_label_other_means

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 147 | NUM_GMEAN | Geometric mean |   | 1 |
| 148 | NUM_HMEAN | Harmonic mean |   | 1 |







> ### Numeric label quantiles ###

**Description:**   Calculate quantiles from a set of numeric labels.
Weights by samples so multiple occurrences are accounted for.


**Subroutine:**   calc_numeric_label_quantiles

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 149 | NUM_Q005 | 5th percentile |   | 1 |
| 150 | NUM_Q010 | 10th percentile |   | 1 |
| 151 | NUM_Q015 | 15th percentile |   | 1 |
| 152 | NUM_Q020 | 20th percentile |   | 1 |
| 153 | NUM_Q025 | 25th percentile |   | 1 |
| 154 | NUM_Q030 | 30th percentile |   | 1 |
| 155 | NUM_Q035 | 35th percentile |   | 1 |
| 156 | NUM_Q040 | 40th percentile |   | 1 |
| 157 | NUM_Q045 | 45th percentile |   | 1 |
| 158 | NUM_Q050 | 50th percentile |   | 1 |
| 159 | NUM_Q055 | 55th percentile |   | 1 |
| 160 | NUM_Q060 | 60th percentile |   | 1 |
| 161 | NUM_Q065 | 65th percentile |   | 1 |
| 162 | NUM_Q070 | 70th percentile |   | 1 |
| 163 | NUM_Q075 | 75th percentile |   | 1 |
| 164 | NUM_Q080 | 80th percentile |   | 1 |
| 165 | NUM_Q085 | 85th percentile |   | 1 |
| 166 | NUM_Q090 | 90th percentile |   | 1 |
| 167 | NUM_Q095 | 95th percentile |   | 1 |







> ### Numeric label statistics ###

**Description:**   Calculate summary statistics from a set of numeric labels.
Weights by samples so multiple occurrences are accounted for.


**Subroutine:**   calc_numeric_label_stats

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 168 | NUM_CV | Coefficient of variation (NUM_SD / NUM_MEAN) |   | 1 |
| 169 | NUM_KURT | Kurtosis |   | 1 |
| 170 | NUM_MAX | Maximum value (100th quantile) |   | 1 |
| 171 | NUM_MEAN | Mean |   | 1 |
| 172 | NUM_MIN | Minimum value (zero quantile) |   | 1 |
| 173 | NUM_N | Number of samples |   | 1 |
| 174 | NUM_RANGE | Range (max - min) |   | 1 |
| 175 | NUM_SD | Standard deviation |   | 1 |
| 176 | NUM_SKEW | Skewness |   | 1 |







> ### Numeric labels Gi**statistic ###**

**Description:**   Getis-Ord Gi**statistic for numeric labels across both neighbour sets**

**Subroutine:**   calc_num_labels_gistar

**Reference:**   Getis and Ord (1992) Geographical Analysis. http://dx.doi.org/10.1111/j.1538-4632.1992.tb00261.x


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 177 | NUM_GISTAR | List of Gi**scores**|   | 1 |


## PhyloCom Indices ##




> ### Phylogenetic and Nearest taxon distances, abundance weighted ###

**Description:**   Distance stats from each label to the nearest label along the tree.  Compares with all other labels across both neighbour sets. Weighted by sample counts (which currently must be integers)

**Subroutine:**   calc_phylo_mpd_mntd3

**Reference:**   Webb et al. (2008) http://dx.doi.org/10.1093/bioinformatics/btn358


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 178 | PMPD3_MAX | Maximum of pairwise phylogenetic distances |   | 1 |
| 179 | PMPD3_MEAN | Mean of pairwise phylogenetic distances |   | 1 |
| 180 | PMPD3_MIN | Minimum of pairwise phylogenetic distances |   | 1 |
| 181 | PMPD3_N | Count of pairwise phylogenetic distances |   | 1 |
| 182 | PMPD3_RMSD | Root mean squared pairwise phylogenetic distances |   | 1 |
| 183 | PNTD3_MAX | Maximum of nearest taxon distances |   | 1 |
| 184 | PNTD3_MEAN | Mean of nearest taxon distances |   | 1 |
| 185 | PNTD3_MIN | Minimum of nearest taxon distances |   | 1 |
| 186 | PNTD3_N | Count of nearest taxon distances |   | 1 |
| 187 | PNTD3_RMSD | Root mean squared nearest taxon distances |   | 1 |







> ### Phylogenetic and Nearest taxon distances, local range weighted ###

**Description:**   Distance stats from each label to the nearest label along the tree.  Compares with all other labels across both neighbour sets. Weighted by sample counts

**Subroutine:**   calc_phylo_mpd_mntd2

**Reference:**   Webb et al. (2008) http://dx.doi.org/10.1093/bioinformatics/btn358


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 188 | PMPD2_MAX | Maximum of pairwise phylogenetic distances |   | 1 |
| 189 | PMPD2_MEAN | Mean of pairwise phylogenetic distances |   | 1 |
| 190 | PMPD2_MIN | Minimum of pairwise phylogenetic distances |   | 1 |
| 191 | PMPD2_N | Count of pairwise phylogenetic distances |   | 1 |
| 192 | PMPD2_RMSD | Root mean squared pairwise phylogenetic distances |   | 1 |
| 193 | PNTD2_MAX | Maximum of nearest taxon distances |   | 1 |
| 194 | PNTD2_MEAN | Mean of nearest taxon distances |   | 1 |
| 195 | PNTD2_MIN | Minimum of nearest taxon distances |   | 1 |
| 196 | PNTD2_N | Count of nearest taxon distances |   | 1 |
| 197 | PNTD2_RMSD | Root mean squared nearest taxon distances |   | 1 |







> ### Phylogenetic and Nearest taxon distances, unweighted ###

**Description:**   Distance stats from each label to the nearest label along the tree.  Compares with all other labels across both neighbour sets.

**Subroutine:**   calc_phylo_mpd_mntd1

**Reference:**   Webb et al. (2008) http://dx.doi.org/10.1093/bioinformatics/btn358


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 198 | PMPD1_MAX | Maximum of pairwise phylogenetic distances |   | 1 |
| 199 | PMPD1_MEAN | Mean of pairwise phylogenetic distances |   | 1 |
| 200 | PMPD1_MIN | Minimum of pairwise phylogenetic distances |   | 1 |
| 201 | PMPD1_N | Count of pairwise phylogenetic distances |   | 1 |
| 202 | PMPD1_RMSD | Root mean squared pairwise phylogenetic distances |   | 1 |
| 203 | PNTD1_MAX | Maximum of nearest taxon distances |   | 1 |
| 204 | PNTD1_MEAN | Mean of nearest taxon distances |   | 1 |
| 205 | PNTD1_MIN | Minimum of nearest taxon distances |   | 1 |
| 206 | PNTD1_N | Count of nearest taxon distances |   | 1 |
| 207 | PNTD1_RMSD | Root mean squared nearest taxon distances |   | 1 |


## Phylogenetic Indices ##




> ### Corrected weighted phylogenetic endemism ###

**Description:**   What proportion of the PD is range-restricted to this neighbour set?

**Subroutine:**   calc_phylo_corrected_weighted_endemism

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** | **Reference** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|:--------------|
| 208 | PE_CWE | Corrected weighted endemism.  This is the phylogenetic analogue of corrected weighted endemism. |   | 1 | <img src='http://latex.codecogs.com/png.latex?PE_WE / PD%.png' title='PE_WE / PD' />  |   |







> ### Corrected weighted phylogenetic rarity ###

**Description:**   What proportion of the PD is abundance-restricted to this neighbour set?

**Subroutine:**   calc_phylo_corrected_weighted_rarity

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** | **Reference** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|:--------------|
| 209 | PHYLO_RARITY_CWR | Corrected weighted phylogenetic rarity.  This is the phylogenetic rarity analogue of corrected weighted endemism. |   | 1 | <img src='http://latex.codecogs.com/png.latex?AED_T / PD%.png' title='AED_T / PD' />  |   |







> ### Evolutionary distinctiveness ###

**Description:**   Evolutionary distinctiveness metrics (AED, ED, ES)
Label values are constant for all neighbourhoods in which each label is found.

**Subroutine:**   calc_phylo_aed

**Reference:**   Cadotte & Davies (2010) http://dx.doi.org/10.1111/j.1472-4642.2010.00650.x


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Reference** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:--------------|
| 210 | PHYLO_AED_LIST | Abundance weighted ED per terminal label |   | 1 | Cadotte & Davies (2010) http://dx.doi.org/10.1111/j.1472-4642.2010.00650.x |
| 211 | PHYLO_ED_LIST | "Fair proportion" partitioning of PD per terminal label |   | 1 | Isaac et al. (2007) http://dx.doi.org/10.1371/journal.pone.0000296 |
| 212 | PHYLO_ES_LIST | Equal splits partitioning of PD per terminal label |   | 1 | Redding & Mooers (2006) http://dx.doi.org/10.1111%2Fj.1523-1739.2006.00555.x |







> ### Evolutionary distinctiveness per site ###

**Description:**   Site level evolutionary distinctiveness

**Subroutine:**   calc_phylo_aed_t

**Reference:**   Cadotte & Davies (2010) http://dx.doi.org/10.1111/j.1472-4642.2010.00650.x


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Reference** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:--------------|
| 213 | PHYLO_AED_T | Abundance weighted ED_t (sum of values in PHYLO_AED_LIST times their abundances). This is equivalent to a phylogenetic rarity score (see phylogenetic endemism) |   | 1 | Cadotte & Davies (2010) http://dx.doi.org/10.1111/j.1472-4642.2010.00650.x |







> ### Evolutionary distinctiveness per terminal taxon per site ###

**Description:**   Site level evolutionary distinctiveness per terminal taxon

**Subroutine:**   calc_phylo_aed_t_wtlists

**Reference:**   Cadotte & Davies (2010) http://dx.doi.org/10.1111/j.1472-4642.2010.00650.x


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Reference** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:--------------|
| 214 | PHYLO_AED_T_WTLIST | Abundance weighted ED per terminal taxon (the AED score of each taxon multiplied by its abundance in the sample) |   | 1 | Cadotte & Davies (2010) http://dx.doi.org/10.1111/j.1472-4642.2010.00650.x |
| 215 | PHYLO_AED_T_WTLIST_P | Proportional contribution of each terminal taxon to the AED_T score |   | 1 | Cadotte & Davies (2010) http://dx.doi.org/10.1111/j.1472-4642.2010.00650.x |







> ### Labels not on tree ###

**Description:**   Create a hash of the labels that are not on the tree

**Subroutine:**   calc_labels_not_on_tree

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 216 | PHYLO_LABELS_NOT_ON_TREE | A hash of labels that are not found on the tree, across both neighbour sets |   | 1 |
| 217 | PHYLO_LABELS_NOT_ON_TREE_N | Number of labels not on the tree |   | 1 |
| 218 | PHYLO_LABELS_NOT_ON_TREE_P | Proportion of labels not on the tree |   | 1 |







> ### Labels on tree ###

**Description:**   Create a hash of the labels that are on the tree

**Subroutine:**   calc_labels_on_tree

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 219 | PHYLO_LABELS_ON_TREE | A hash of labels that are found on the tree, across both neighbour sets |   | 1 |







> ### PD-Endemism ###

**Description:**   Absolute endemism analogue of PE.  It is the sum of the branch lengths restricted to the neighbour sets.

**Subroutine:**   calc_pd_endemism

**Reference:**   See Faith (2004) Cons Biol.  http://dx.doi.org/10.1111/j.1523-1739.2004.00330.x


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 220 | PD_ENDEMISM | Phylogenetic Diversity Endemism |   | 1 |
| 221 | PD_ENDEMISM_WTS | Phylogenetic Diversity Endemism weights per node found only in the neighbour set |   | 1 |







> ### Phylo Jaccard ###

**Description:**   Jaccard phylogenetic dissimilarity between two sets of taxa, represented by spanning sets of branches


**Subroutine:**   calc_phylo_jaccard

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|
| 222 | PHYLO_JACCARD | Phylo Jaccard score | cluster metric | 2 | <img src='http://latex.codecogs.com/png.latex?= 1 - (A / (A + B + C))%.png' title='= 1 - (A / (A + B + C))' /> where A is the length of shared branches, and B and C are the length of branches found only in neighbour sets 1 and 2  |







> ### Phylo S2 ###

**Description:**   S2 phylogenetic dissimilarity between two sets of taxa, represented by spanning sets of branches


**Subroutine:**   calc_phylo_s2

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|
| 223 | PHYLO_S2 | Phylo S2 score | cluster metric | 2 | <img src='http://latex.codecogs.com/png.latex?= 1 - (A / (A + min (B, C)))%.png' title='= 1 - (A / (A + min (B, C)))' /> where A is the length of shared branches, and B and C are the length of branches found only in neighbour sets 1 and 2  |







> ### Phylo Sorenson ###

**Description:**   Sorenson phylogenetic dissimilarity between two sets of taxa, represented by spanning sets of branches


**Subroutine:**   calc_phylo_sorenson

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|
| 224 | PHYLO_SORENSON | Phylo Sorenson score | cluster metric | 2 | <img src='http://latex.codecogs.com/png.latex?1 - (2A / (2A + B + C))%.png' title='1 - (2A / (2A + B + C))' /> where A is the length of shared branches, and B and C are the length of branches found only in neighbour sets 1 and 2  |







> ### Phylogenetic ABC ###

**Description:**   Calculate the shared and not shared branch lengths between two sets of labels

**Subroutine:**   calc_phylo_abc

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 225 | PHYLO_A | Length of branches shared by labels in nbr sets 1 and 2 |   | 2 |
| 226 | PHYLO_ABC | Length of all branches associated with labels in nbr sets 1 and 2 |   | 2 |
| 227 | PHYLO_B | Length of branches unique to labels in nbr set 1 |   | 2 |
| 228 | PHYLO_C | Length of branches unique to labels in nbr set 2 |   | 2 |







> ### Phylogenetic Diversity ###

**Description:**   Phylogenetic diversity (PD) based on branch lengths back to the root of the tree.
Uses labels in both neighbourhoods.

**Subroutine:**   calc_pd

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** | **Reference** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|:--------------|
| 229 | PD | Phylogenetic diversity |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \sum_{c \in C} L_c%.png' title='= \sum_{c \in C} L_c' /> where <img src='http://latex.codecogs.com/png.latex?C%.png' title='C' /> is the set of branches in the minimum spanning path joining the labels in both neighbour sets to the root of the tree,<img src='http://latex.codecogs.com/png.latex?c%.png' title='c' /> is a branch (a single segment between two nodes) in the spanning path <img src='http://latex.codecogs.com/png.latex?C%.png' title='C' /> , and <img src='http://latex.codecogs.com/png.latex?L_c%.png' title='L_c' /> is the length of branch <img src='http://latex.codecogs.com/png.latex?c%.png' title='c' /> .  | Faith (1992) Biol. Cons. http://dx.doi.org/10.1016/0006-3207(92)91201-3 |
| 230 | PD_P | Phylogenetic diversity as a proportion of total tree length |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \frac { PD }{ \sum_{c \in C} L_c }%.png' title='= \frac { PD }{ \sum_{c \in C} L_c }' /> where terms are the same as for PD, but <img src='http://latex.codecogs.com/png.latex?c%.png' title='c' /> , <img src='http://latex.codecogs.com/png.latex?C%.png' title='C' /> and <img src='http://latex.codecogs.com/png.latex?L_c%.png' title='L_c' /> are calculated for all nodes in the tree.  |   |
| 231 | PD_P_per_taxon | Phylogenetic diversity per taxon as a proportion of total tree length |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \frac { PD_P }{ RICHNESS_ALL }%.png' title='= \frac { PD_P }{ RICHNESS_ALL }' />  |   |
| 232 | PD_per_taxon | Phylogenetic diversity per taxon |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \frac { PD }{ RICHNESS_ALL }%.png' title='= \frac { PD }{ RICHNESS_ALL }' />  |   |







> ### Phylogenetic Diversity node list ###

**Description:**   Phylogenetic diversity (PD) nodes used.

**Subroutine:**   calc_pd_node_list

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 233 | PD_INCLUDED_NODE_LIST | List of tree nodes included in the PD calculations |   | 1 |







> ### Phylogenetic Diversity terminal node list ###

**Description:**   Phylogenetic diversity (PD) terminal nodes used.

**Subroutine:**   calc_pd_terminal_node_list

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 234 | PD_INCLUDED_TERMINAL_NODE_LIST | List of tree terminal nodes included in the PD calculations |   | 1 |







> ### Phylogenetic Endemism ###

**Description:**   Phylogenetic endemism (PE).Uses labels in both neighbourhoods and trims the tree to exclude labels not in the BaseData object.

**Subroutine:**   calc_pe

**Reference:**   Rosauer et al (2009) Mol. Ecol. http://dx.doi.org/10.1111/j.1365-294X.2009.04311.x


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 235 | PE_WE | Phylogenetic endemism |   | 1 |
| 236 | PE_WE_P | Phylogenetic weighted endemism as a proportion of the total tree length |   | 1 |







> ### Phylogenetic Endemism lists ###

**Description:**   Lists used in the Phylogenetic endemism (PE) calculations.

**Subroutine:**   calc_pe_lists

**Reference:**   Rosauer et al (2009) Mol. Ecol. http://dx.doi.org/10.1111/j.1365-294X.2009.04311.x


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 237 | PE_LOCAL_RANGELIST | Local node ranges used in PE calculations (number of groups in which a node is found) |   | 1 |
| 238 | PE_RANGELIST | Node ranges used in PE calculations |   | 1 |
| 239 | PE_WTLIST | Node weights used in PE calculations |   | 1 |







> ### Phylogenetic Endemism single ###

**Description:**   PE scores, but not weighted by local ranges.

**Subroutine:**   calc_pe_single

**Reference:**   Rosauer et al (2009) Mol. Ecol. http://dx.doi.org/10.1111/j.1365-294X.2009.04311.x


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 240 | PE_WE_SINGLE | Phylogenetic endemism unweighted by the number of neighbours. Counts each label only once, regardless of how many groups in the neighbourhood it is found in. Useful if your data have sampling biases. Better with small sample windows. |   | 1 |
| 241 | PE_WE_SINGLE_P | Phylogenetic endemism unweighted by the number of neighbours as a proportion of the total tree length. Counts each label only once, regardless of how many groups in the neighbourhood it is found. Useful if your data have sampling biases. |   | 1 |







> ### Taxonomic/phylogenetic distinctness ###

**Description:**   Taxonomic/phylogenetic distinctness and variation. THIS IS A BETA LEVEL IMPLEMENTATION.

**Subroutine:**   calc_taxonomic_distinctness

**Reference:**   Warwick & Clarke (1995) Mar Ecol Progr Ser. http://dx.doi.org/10.3354/meps129301 ; Clarke & Warwick (2001) Mar Ecol Progr Ser. http://dx.doi.org/10.3354/meps216265


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 242 | TD_DENOMINATOR | Denominator from TD_DISTINCTNESS calcs |   | 1 |
| 243 | TD_DISTINCTNESS | Taxonomic distinctness |   | 1 |
| 244 | TD_NUMERATOR | Numerator from TD_DISTINCTNESS calcs |   | 1 |
| 245 | TD_VARIATION | Variation of the taxonomic distinctness |   | 1 |







> ### Taxonomic/phylogenetic distinctness, binary weighted ###

**Description:**   Taxonomic/phylogenetic distinctness and variation using presence/absence weights.  THIS IS A BETA LEVEL IMPLEMENTATION.

**Subroutine:**   calc_taxonomic_distinctness_binary

**Reference:**   Warwick & Clarke (1995) Mar Ecol Progr Ser. http://dx.doi.org/10.3354/meps129301 ; Clarke & Warwick (2001) Mar Ecol Progr Ser. http://dx.doi.org/10.3354/meps216265


| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|
| 246 | TDB_DENOMINATOR | Denominator from TDB_DISTINCTNESS |   | 1 |   |
| 247 | TDB_DISTINCTNESS | Taxonomic distinctness, binary weighted |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \frac{\sum \sum_{i \neq j} \omega_{ij}}{s(s-1))}%.png' title='= \frac{\sum \sum_{i \neq j} \omega_{ij}}{s(s-1))}' /> where <img src='http://latex.codecogs.com/png.latex?\omega_{ij}%.png' title='\omega_{ij}' /> is the path length from label <img src='http://latex.codecogs.com/png.latex?i%.png' title='i' /> to the ancestor node shared with <img src='http://latex.codecogs.com/png.latex?j%.png' title='j' />  |
| 248 | TDB_NUMERATOR | Numerator from TDB_DISTINCTNESS |   | 1 |   |
| 249 | TDB_VARIATION | Variation of the binary taxonomic distinctness |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \frac{\sum \sum_{i \neq j} \omega_{ij}^2}{s(s-1))} - \bar{\omega}^2%.png' title='= \frac{\sum \sum_{i \neq j} \omega_{ij}^2}{s(s-1))} - \bar{\omega}^2' /> where <img src='http://latex.codecogs.com/png.latex?\bar{\omega} = \frac{\sum \sum_{i \neq j} \omega_{ij}}{s(s-1))} \equiv TDB_DISTINCTNESS%.png' title='\bar{\omega} = \frac{\sum \sum_{i \neq j} \omega_{ij}}{s(s-1))} \equiv TDB_DISTINCTNESS' />  |


## Rarity ##




> ### Rarity central ###

**Description:**   Calculate rarity for species only in neighbour set 1, but with local sample counts calculated from both neighbour sets.
Uses the same algorithm as the endemism indices but weights by sample counts instead of by groups occupied.

**Subroutine:**   calc_rarity_central

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|
| 250 | RAREC_CWE | Corrected weighted rarity |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \frac{RAREC_WE}{RAREC_RICHNESS}%.png' title='= \frac{RAREC_WE}{RAREC_RICHNESS}' />  |
| 251 | RAREC_RICHNESS | Richness used in RAREC_CWE (same as index RICHNESS_SET1). |   | 1 |   |
| 252 | RAREC_WE | Weighted rarity |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \sum_{t \in T} \frac {s_t} {S_t}%.png' title='= \sum_{t \in T} \frac {s_t} {S_t}' /> where <img src='http://latex.codecogs.com/png.latex?t%.png' title='t' /> is a label (taxon) in the set of labels (taxa) <img src='http://latex.codecogs.com/png.latex?T%.png' title='T' /> across neighbour set 1, <img src='http://latex.codecogs.com/png.latex?s_t%.png' title='s_t' /> is sum of the sample counts for <img src='http://latex.codecogs.com/png.latex?t%.png' title='t' /> across the elements in neighbour sets 1 & 2 (its value in list ABC3_LABELS_ALL), and <img src='http://latex.codecogs.com/png.latex?S_t%.png' title='S_t' /> is the total number of samples across the data set for label <img src='http://latex.codecogs.com/png.latex?t%.png' title='t' /> (unless the total sample count is specified at import).  |







> ### Rarity central lists ###

**Description:**   Lists used in rarity central calculations

**Subroutine:**   calc_rarity_central_lists

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 253 | RAREC_RANGELIST | List of ranges for each label used in the rarity central calculations |   | 1 |
| 254 | RAREC_WTLIST | List of weights for each label used in therarity central calculations |   | 1 |







> ### Rarity whole ###

**Description:**   Calculate rarity using all species in both neighbour sets.
Uses the same algorithm as the endemism indices but weights
by sample counts instead of by groups occupied.


**Subroutine:**   calc_rarity_whole

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|
| 255 | RAREW_CWE | Corrected weighted rarity |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \frac{RAREW_WE}{RAREW_RICHNESS}%.png' title='= \frac{RAREW_WE}{RAREW_RICHNESS}' />  |
| 256 | RAREW_RICHNESS | Richness used in RAREW_CWE (same as index RICHNESS_ALL). |   | 1 |   |
| 257 | RAREW_WE | Weighted rarity |   | 1 | <img src='http://latex.codecogs.com/png.latex?= \sum_{t \in T} \frac {s_t} {S_t}%.png' title='= \sum_{t \in T} \frac {s_t} {S_t}' /> where <img src='http://latex.codecogs.com/png.latex?t%.png' title='t' /> is a label (taxon) in the set of labels (taxa) <img src='http://latex.codecogs.com/png.latex?T%.png' title='T' /> across both neighbour sets, <img src='http://latex.codecogs.com/png.latex?s_t%.png' title='s_t' /> is sum of the sample counts for <img src='http://latex.codecogs.com/png.latex?t%.png' title='t' /> across the elements in neighbour sets 1 & 2 (its value in list ABC3_LABELS_ALL), and <img src='http://latex.codecogs.com/png.latex?S_t%.png' title='S_t' /> is the total number of samples across the data set for label <img src='http://latex.codecogs.com/png.latex?t%.png' title='t' /> (unless the total sample count is specified at import).  |







> ### Rarity whole lists ###

**Description:**   Lists used in rarity whole calculations

**Subroutine:**   calc_rarity_whole_lists

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 258 | RAREW_RANGELIST | List of ranges for each label used in the rarity whole calculations |   | 1 |
| 259 | RAREW_WTLIST | List of weights for each label used in therarity whole calculations |   | 1 |


## Taxonomic Dissimilarity and Comparison ##




> ### Beta diversity ###

**Description:**   Beta diversity between neighbour sets 1 and 2.


**Subroutine:**   calc_beta_diversity

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|
| 260 | BETA_2 | The other beta | cluster metric | 2 | <img src='http://latex.codecogs.com/png.latex?= \frac{A + B + C}{max((A+B), (A+C))} - 1%.png' title='= \frac{A + B + C}{max((A+B), (A+C))} - 1' /> where <img src='http://latex.codecogs.com/png.latex?A%.png' title='A' /> is the count of labels found in both neighbour sets, <img src='http://latex.codecogs.com/png.latex?B%.png' title='B' /> is the count unique to neighbour set 1, and <img src='http://latex.codecogs.com/png.latex?C%.png' title='C' /> is the count unique to neighbour set 2. Use the [Label counts](#label-counts) calculation to derive these directly.  |







> ### Bray-Curtis non-metric ###

**Description:**   Bray-Curtis dissimilarity between two sets of labels.
Reduces to the Sorenson metric for binary data (where sample counts are 1 or 0).

**Subroutine:**   calc_bray_curtis

**Formula:**
> <img src='http://latex.codecogs.com/png.latex?= 1 - \frac{2W}{A + B}%.png' title='= 1 - \frac{2W}{A + B}' /> where <img src='http://latex.codecogs.com/png.latex?A%.png' title='A' /> is the sum of the sample counts in neighbour set 1, <img src='http://latex.codecogs.com/png.latex?B%.png' title='B' /> is the sum of sample counts in neighbour set 2, and <img src='http://latex.codecogs.com/png.latex?W=\sum^n_{i=1} min(sample_count_label_{i_{set1}},sample_count_label_{i_{set2}})%.png' title='W=\sum^n_{i=1} min(sample_count_label_{i_{set1}},sample_count_label_{i_{set2}})' /> (meaning it sums the minimum of the sample counts for each of the <img src='http://latex.codecogs.com/png.latex?n%.png' title='n' /> labels across the two neighbour sets),

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 261 | BC_A | The A factor used in calculations (see formula) |   | 2 |
| 262 | BC_B | The B factor used in calculations (see formula) |   | 2 |
| 263 | BC_W | The W factor used in calculations (see formula) |   | 2 |
| 264 | BRAY_CURTIS | Bray Curtis dissimilarity | cluster metric | 2 |







> ### Bray-Curtis non-metric, group count normalised ###

**Description:**   Bray-Curtis dissimilarity between two neighbourhoods,
where the counts in each neighbourhood are divided
by the number of groups in each neighbourhood to correct
for unbalanced sizes.


**Subroutine:**   calc_bray_curtis_norm_by_gp_counts

**Formula:**
> <img src='http://latex.codecogs.com/png.latex?= 1 - \frac{2W}{A + B}%.png' title='= 1 - \frac{2W}{A + B}' /> where <img src='http://latex.codecogs.com/png.latex?A%.png' title='A' /> is the sum of the sample counts in neighbour set 1 normalised (divided) by the number of groups, <img src='http://latex.codecogs.com/png.latex?B%.png' title='B' /> is the sum of the sample counts in neighbour set 2 normalised by the number of groups, and <img src='http://latex.codecogs.com/png.latex?W = \sum^n_{i=1} min(sample_count_label_{i_{set1}},sample_count_label_{i_{set2}})%.png' title='W = \sum^n_{i=1} min(sample_count_label_{i_{set1}},sample_count_label_{i_{set2}})' /> (meaning it sums the minimum of the normalised sample counts for each of the <img src='http://latex.codecogs.com/png.latex?n%.png' title='n' /> labels across the two neighbour sets),

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 265 | BCN_A | The A factor used in calculations (see formula) |   | 2 |
| 266 | BCN_B | The B factor used in calculations (see formula) |   | 2 |
| 267 | BCN_W | The W factor used in calculations (see formula) |   | 2 |
| 268 | BRAY_CURTIS_NORM | Bray Curtis dissimilarity normalised by groups | cluster metric | 2 |







> ### Jaccard ###

**Description:**   Jaccard dissimilarity between the labels in neighbour sets 1 and 2.

**Subroutine:**   calc_jaccard

**Formula:**
> <img src='http://latex.codecogs.com/png.latex?= 1 - \frac{A}{A + B + C}%.png' title='= 1 - \frac{A}{A + B + C}' /> where <img src='http://latex.codecogs.com/png.latex?A%.png' title='A' /> is the count of labels found in both neighbour sets, <img src='http://latex.codecogs.com/png.latex?B%.png' title='B' /> is the count unique to neighbour set 1, and <img src='http://latex.codecogs.com/png.latex?C%.png' title='C' /> is the count unique to neighbour set 2. Use the [Label counts](#label-counts) calculation to derive these directly.

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 269 | JACCARD | Jaccard value, 0 is identical, 1 is completely dissimilar | cluster metric | 2 |







> ### Nestedness-resultant ###

**Description:**   Nestedness-resultant index between the labels in neighbour sets 1 and 2.

**Subroutine:**   calc_nestedness_resultant

**Reference:**   Baselga (2010) Glob Ecol Biogeog.  http://dx.doi.org/10.1111/j.1466-8238.2009.00490.x


**Formula:**
> <img src='http://latex.codecogs.com/png.latex?=\frac{ \left | B - C \right | }{ 2A + B + C } \times \frac { A }{ A + min (B, C) }= SORENSON - S2%.png' title='=\frac{ \left | B - C \right | }{ 2A + B + C } \times \frac { A }{ A + min (B, C) }= SORENSON - S2' /> where <img src='http://latex.codecogs.com/png.latex?A%.png' title='A' /> is the count of labels found in both neighbour sets, <img src='http://latex.codecogs.com/png.latex?B%.png' title='B' /> is the count unique to neighbour set 1, and <img src='http://latex.codecogs.com/png.latex?C%.png' title='C' /> is the count unique to neighbour set 2. Use the [Label counts](#label-counts) calculation to derive these directly.

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 270 | NEST_RESULTANT | Nestedness-resultant index | cluster metric | 2 |







> ### Rao's quadratic entropy, taxonomically weighted ###

**Description:**   Calculate Rao's quadratic entropy for a taxonomic weights scheme.
Should collapse to be the Simpson index for presence/absence data.

**Subroutine:**   calc_tx_rao_qe

**Formula:**
> <img src='http://latex.codecogs.com/png.latex?= \sum_{i \in L} \sum_{j \in L} d_{ij} p_i p_j%.png' title='= \sum_{i \in L} \sum_{j \in L} d_{ij} p_i p_j' /> where <img src='http://latex.codecogs.com/png.latex?p_i%.png' title='p_i' /> and <img src='http://latex.codecogs.com/png.latex?p_j%.png' title='p_j' /> are the sample counts for the i'th and j'th labels, <img src='http://latex.codecogs.com/png.latex?d_{ij}%.png' title='d_{ij}' /> is a value of zero if <img src='http://latex.codecogs.com/png.latex?i = j%.png' title='i = j' /> , and a value of 1 otherwise. <img src='http://latex.codecogs.com/png.latex?L%.png' title='L' /> is the set of labels across both neighbour sets.

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 271 | TX_RAO_QE | Taxonomically weighted quadratic entropy |   | 1 |
| 272 | TX_RAO_TLABELS | List of labels and values used in the TX_RAO_QE calculations |   | 1 |
| 273 | TX_RAO_TN | Count of comparisons used to calculate TX_RAO_QE |   | 1 |







> ### S2 ###

**Description:**   S2 dissimilarity between two sets of labels


**Subroutine:**   calc_s2

**Reference:**   Lennon et al. (2001) J Animal Ecol.  http://dx.doi.org/10.1046/j.0021-8790.2001.00563.x


**Formula:**
> <img src='http://latex.codecogs.com/png.latex?= 1 - \frac{A}{A + min(B, C)}%.png' title='= 1 - \frac{A}{A + min(B, C)}' /> where <img src='http://latex.codecogs.com/png.latex?A%.png' title='A' /> is the count of labels found in both neighbour sets, <img src='http://latex.codecogs.com/png.latex?B%.png' title='B' /> is the count unique to neighbour set 1, and <img src='http://latex.codecogs.com/png.latex?C%.png' title='C' /> is the count unique to neighbour set 2. Use the [Label counts](#label-counts) calculation to derive these directly.

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 274 | S2 | S2 dissimilarity index | cluster metric | 2 |







> ### Simpson and Shannon ###

**Description:**   Simpson and Shannon diversity metrics using samples from all neighbourhoods.


**Subroutine:**   calc_simpson_shannon

**Formula:**
> For each index formula, <img src='http://latex.codecogs.com/png.latex?p_i%.png' title='p_i' /> is the number of samples of the i'th label as a proportion of the total number of samples <img src='http://latex.codecogs.com/png.latex?n%.png' title='n' /> in the neighbourhoods.

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** | **Formula** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|:------------|
| 275 | SHANNON_E | Shannon's evenness (H / HMAX) |   | 1 | <img src='http://latex.codecogs.com/png.latex?Evenness = \frac{H}{HMAX}%.png' title='Evenness = \frac{H}{HMAX}' />  |
| 276 | SHANNON_H | Shannon's H |   | 1 | <img src='http://latex.codecogs.com/png.latex?H = - \sum^n_{i=1} (p_i \cdot ln (p_i))%.png' title='H = - \sum^n_{i=1} (p_i \cdot ln (p_i))' />  |
| 277 | SHANNON_HMAX | maximum possible value of Shannon's H |   | 1 | <img src='http://latex.codecogs.com/png.latex?HMAX = ln(richness)%.png' title='HMAX = ln(richness)' />  |
| 278 | SIMPSON_D | Simpson's D. A score of zero is more similar. |   | 1 | <img src='http://latex.codecogs.com/png.latex?D = 1 - \sum^n_{i=1} p_i^2%.png' title='D = 1 - \sum^n_{i=1} p_i^2' />  |







> ### Sorenson ###

**Description:**   Sorenson dissimilarity between two sets of labels.
It is the complement of the (unimplemented) Czechanowski index, and numerically the same as Whittaker's beta.

**Subroutine:**   calc_sorenson

**Formula:**
> <img src='http://latex.codecogs.com/png.latex?= 1 - \frac{2A}{2A + B + C}%.png' title='= 1 - \frac{2A}{2A + B + C}' /> where <img src='http://latex.codecogs.com/png.latex?A%.png' title='A' /> is the count of labels found in both neighbour sets, <img src='http://latex.codecogs.com/png.latex?B%.png' title='B' /> is the count unique to neighbour set 1, and <img src='http://latex.codecogs.com/png.latex?C%.png' title='C' /> is the count unique to neighbour set 2. Use the [Label counts](#label-counts) calculation to derive these directly.

| **Index #** | **Index** | **Index description** | **Valid cluster metric?** | **Minimum number of neighbour sets** |
|:------------|:----------|:----------------------|:--------------------------|:-------------------------------------|
| 279 | SORENSON | Sorenson index | cluster metric | 2 |


<img src='http://www.codecogs.com/images/poweredbycc.gif' alt='Powered by CodeCogs' border='0' width='102' height='34' />
http://www.codecogs.com