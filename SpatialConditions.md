

# Introduction #

Spatial conditions are core to the Biodiverse system.  They are used to specify both neighbourhoods used in the analyses, and also the definition queries used to restrict the calculations to a subset of groups.

# Uses for spatial conditions #

Spatial conditions are used both to define the neighbourhoods of the spatial analyses and the definition queries used to constrain the set of groups used in the analyses.

> ## Neighbourhoods ##

Neighbourhoods are essential for any spatial analysis, as it is through these that one can define the set of groups to be considered in an analysis.  In the moving window analyses these determine which groups are compared with which other groups.  In the cluster analyses they determine which groups are considered candidates to be clustered together.  It is also possible to define neighbourhoods for spatially constrained randomisations (see [Laffan and Crisp, 2003, J Biogeog](http://www3.interscience.wiley.com/journal/118882020/abstract)), although this is yet to be implemented (see [issue #76](https://code.google.com/p/biodiverse/issues/detail?id=#76)).

Before we describe the process, some definitions are needed.  The **processing group** is the group being considered in the analysis at some iteration, and to which the results for that iteration are assigned.  A group is a member of the processing group's set of neighbours (is a **neighbouring group**) if the spatial condition evaluates to true.

A [spatial analysis](AnalysisTypes#Spatial_analyses.md) progressively iterates over each group that passes the definition query, assessing every other group for membership in neighbour set 1 or 2.  The selected indices are then calculated using the groups that occur in neighbour sets 1 and 2 (and their labels and other properties as required by the [calculations](KeyConcepts#Calculations.md)).

> ## Definition Queries ##

These differ from neighbourhoods as they assess only the processing group to determine if calculations should be run for it or not.  They use the same syntax as for neighbourhoods, but the system will commonly complain if a condition requiring a neighbouring group is used.

Note that groups that fail the definition query are still considered for membership of neighbour sets of those that pass.  Use a definition query in conjunction with an appropriate neighbourhood definition if you want to exclude some groups from neighbour sets as well.  For example, you could use `sp_match_text (axis => 2, text => 'fred', type => 'proc')` for the definition query and `sp_match_text (axis => 2, text => 'fred', type => 'nbr')` for the neighbourhood.  This will restrict calculations to those groups with a third axis of 'fred', and also exclude any group without fred in the third axis from the neighbour sets of those groups processed.

# Some details #

As with any system, there must be compromises between ease of use and system flexibility. In this case we have opted for system flexibility by direct use of Perl syntax. This means you can use arbitrarily complex functions to define neighbourhoods, including loops and other multiple variable conditions. This may be horrifying to non-perlers, as one of the main complaints about perl is its complex grammar and syntax. To alleviate this we are encapsulating many of the common conditions in subroutines that can be called by name with a set of arguments.  We have also provided examples below to assist.

The neighbourhood and definition query interfaces have a syntax verification button to check that the syntax is valid. This does not, however, guarantee your parameters will work, only that it is valid Perl code. (The reality here is that we will just evaluate the parameter statement with some default values and warn you if the system raises some sort of error or exception).

# Evaluation #

This is a brief description of the evaluation process used to determine the set of neighbours for a group.

Currently the system operates on boolean membership of the set of neighbours, so a group either is or is not a neighbour of the processing group.  If no spatial index is used then every group's membership of the processing cell's neighbour set is considered in turn.  If a spatial index is used then only a subset of neighbours is considered (those within the relevant spatial index blocks).  This is why processing times are usually shorter when using an index (see [KeyConcepts#Using\_the\_spatial\_index](KeyConcepts#Using_the_spatial_index.md)).

Spatial conditions need not return symmetric sets.  In this way group _i_ can be in group _j_'s neighbour set, but _j_ need not be in _i_'s neighbour set.  This is not an issue for moving window analyses, but can cause asymmetric dissimilarity matrices if used to run a spatially constrained cluster analysis.  This is why it is generally a good idea in these cases to set the second neighbourhood to be `sp_always_true()` or `1` (which is the same thing).

In the calculations, groups in neighbour set 1 are excluded from neighbour set 2 so there are no overlaps that would violate the comparison calculations.

The conditions are specified using some combination of pre-defined functions, pre-specified variables, and/or user defined variables and functions.  These are now described.


# Functions #

Functions are the easiest way to specify conditions as one does not need to wrestle with variables.  Functions also set metadata to tell the system how to use the spatial index.  The spatial index saves considerable processing time for large data sets as the system does not need to test many pairs of index blocks to determine which to use (see [KeyConcepts#Using\_the\_spatial\_index](KeyConcepts#Using_the_spatial_index.md)).  If you use a function for which an index will produce erroneous results then the system sets a flag to ignore it.

The available functions in version 0.17 are:
  * sp\_self\_only
  * sp\_select\_all
  * sp\_circle
  * sp\_circle\_cell
  * sp\_square
  * sp\_square\_cell
  * sp\_block
  * sp\_ellipse
  * sp\_annulus
  * sp\_match\_text
  * sp\_match\_regex
  * sp\_select\_sequence
  * sp\_is\_left\_of
  * sp\_is\_right\_of
  * sp\_in\_line\_with
  * sp\_point\_in\_poly
  * sp\_point\_in\_poly\_shape


> ## Examples using functions ##

```
#  radius of 100,000 map units, uses all axes so will 
#    be a circle for two dimensions, a sphere for three dimensions, 
#    and a hypersphere for more
sp_circle (radius => 100000)

# a circle using the second and fourth group axes
sp_circle (radius => 100000, axes => [1,3]) 

# circle of two cell radius
sp_circle_cell (radius => 2) 

#  an overlapping square, cube or hypercube depending on the number of axes
#    note - you cannot yet specify which axes to use 
#    so it will be square on all sides
sp_square (size => 300000)

#  non-overlapping square block (hypercube), size 3 map units on a side
#    (non-overlapping means each group is a member of only one neighbour set
#    so this is a good way of simulating coarser resolutions)
sp_block (size => 3)

#  rectangular block, ignores second axis
sp_block (size => [3, undef, 5])

#  northwards oriented ellipse using first two axes
sp_ellipse (
    major_radius => 300000, 
    minor_radius => 100000, 
    axes         => [0,1], 
    rotate_angle => 1.5714
)  

#  an annulus assessed against all axes
sp_annulus (inner_radius => 2000000, outer_radius => 4000000)

#  an annulus assessed against axes 0 and 1
sp_annulus (
    inner_radius => 2000000,
    outer_radius => 4000000, 
    axes         => [0,1]
)

#  select every group, including the processing group
sp_select_all()

#  two ways to select every group, excluding the processing group
sp_select_all() && ! sp_self_only()
sp_select_all() and not sp_self_only()


#  only use the processing group
sp_self_only() 

#  use any group where the first axis has value of 'type1'
sp_match_text (text => 'type1', axis => 0, type => 'nbr')

#  two ways to use any group where the first axis has value that is _not_ 'type1'
! sp_match_text (text => 'type1', axis => 0, type => 'nbr')
not sp_match_text (text => 'type1', axis => 0, type => 'nbr')

# match only when the third group axis is the same 
#   as the processing group's third axis
sp_match_text (text => $coord[2], axis => 2, type => 'nbr') 

# Set a definition query to only use groups with 'NK' as the third axis
sp_match_text (text => 'NK', axis => 2, type => 'proc') 

#  use any neighbour where the first axis includes the text 'type1'
sp_match_regex (re => qr'type1', axis => 0, type => 'nbr')

# match only when the third neighbour axis starts with
# the processing group's second axis
sp_match_regex (re => qr/^$coord[2]/, axis => 2, type => 'nbr')

# Set a definition query to only use groups where the
# third axis ends in 'park' (case insensitive)
sp_match_regex (text => qr{park$}i, axis => 2, type => 'proc')

# Select every tenth group 
# (note that groups are first sorted alphabetically in versions prior to 0.16, and south-west to north-east from 0.16)
sp_select_sequence (frequency => 10)

#  Select every tenth group, starting from the third
sp_select_sequence (frequency => 10, first_offset => 2)

#  Select every tenth group, starting from the third last and working backwards
sp_select_sequence (frequency => 10, first_offset => 2, reverse_order => 1)


###############################
#  Available from version 0.16.

#  Match when the neighbour is to the left of a vector radiating out from the processing group.
#  The angle is measured anticlockwise from east.
sp_is_left_of (vector_angle => 1.5707963267949)  #  angle in radians
sp_is_left_of (vector_angle_deg => 90)           #  angle in degrees


###############################
#  Available from version 0.17.

#  Match when the neighbour is to the right of a vector radiating out from the processing group
#  from the processing group.  The angle is measured anticlockwise from east.
sp_is_right_of (vector_angle => 1.5707963267949)  #  angle in radians
sp_is_right_of (vector_angle_deg => 90)           #  angle in degrees

#  Match when the neighbour is in line with a vector radiating from the processing group
sp_in_line_with (vector_angle => 1.5707963267949)  #  angle in radians
sp_in_line_with (vector_angle_deg => 90)           #  angle in degrees


#  Is the neighbour coord in a square polygon?  (edit the coords to fit your data)
sp_point_in_poly (polygon => [[0,0],[0,1],[1,1],[1,0],[0,0]], point => \@nbrcoord)

#  You can omit the point argument to automatically assess the neighbour when it is 
#  in a spatial condition and the processing group in a definition query
sp_point_in_poly (polygon => [[0,0],[0,1],[1,1],[1,0],[0,0]])

#  Is the coord in any polygon in a shapefile?
sp_point_in_poly_shape (file => '/path/to/shapefile.shp')

#  Is the coord in a specific polygon in a shapefile?
#  This is the FID field in ArcGIS, but note that the library we use counts from 1 whereas ArcGIS counts from 0.
#  If you are using ArcGIS to find the polygon ID you need then remember to add 1.
sp_point_in_poly_shape (file => '/path/to/shapefile.shp', field_val => 1)

#  Is the neighbour coord inside any polygon with a value of NSW for the field STATE_NAME?
#  Make sure you give the correct name and path to the shapefile.  
sp_point_in_poly_shape (
    file       => '/path/to/shapefile.shp',
    field_name => 'STATE_NAME', 
    field_val  => 'NSW',
)

#  Is the neighbour coord inside a specific biome (if you have the relevant shapefile)?
#  Note that the values must match exactly.
sp_point_in_poly_shape (
    shape      => '/path/to/biome_shapefile.shp', 
    field_name => 'BIOME', 
    field_val  => 'Tropical and subtropical dry broadleaf forests',
)

```

# Variables #

There are several different sets of variables implemented that the system recognises. Any undeclared variable you use that does not occur in this list will be treated as a zero or as undefined (depending on where it is used), which means it will probably not behave as you expect. An example declaring variables is given below.

As a general rule, uppercase letters denote absolute values, lower case letters denote signed values (positive or negative). Positive values are north, east, above, or to the right. Negative values are south, west, below or to the left.

`$D` is the absolute euclidean distance from the processing group to a candidate neighbour group across all dimensions.

`$D[0]`, `$D[1]` are the absolute euclidean distances in dimension 0 and 1. In most cases `$D[0]` will be the X (longitude) dimension, `$D[1]` will be the Y (latitude) dimension. The library functions can actually handle more dimensions than this (eg `$D[2]` for altitude or depth), but the GUI is not set up to display them (it will plot the data using the first two axes, so only the first of any overlapping groups will be visible).

`$d[0]`, `$d[1]` and so forth are the signed euclidean distance in dimension 0, 1 etc. This allows us to extract all groups within some distance in some direction. As with standard Cartesian plots, negative values are to the left or below (west or south), positive values to the right or above (east or north). As with `$D[0]`, `$d[0]` will normally be the X dimension, `$d[1]` will be the Y dimension.

Note that using `abs($d[1])` is the same as using `$D[1]`.

`$C`, `$C[0]`, `$C[1]`, `$c[0]`, `$c[1]` are the same as the euclidean distance variables (`$D` etc) but operate directly in group (cell) units. If your groups were imported using a cellsize of 100,000, then `$D[1] < 100000` is the same as `$C[1] < 1`. Note, however, that if you used a different resolution in each dimension, then the map and cell distances are not directly comparable.  For example, if cell sizes of 100 and 200 were used for axes 0 and 1 then `$C<1` is the same as `sqrt($C[0]**2 + $C[1]**2) < 1` which is `sqrt(($D[0]/100)**2 + ($D[1]/200)**2) < 1`, and _not_ `$D<100`.

`$coord_id1` is the name of the processing coord, `$coord_id2` is the name of the neighbour coord.  _(Available from version 0.16)._

`$coord[0]`, `$coord[1]` are the coordinate values of the processing group in the first and second dimensions. As per the above, think of these as X and Y, except that `$coord[5]` will also work if your groups have six or more dimensions. Note that the `$coord[]` variables do not necessarily work properly with the spatial index, so you might need to turn the index off when using them.

`$nbrcoord[0]` etc are analogous to `$coord[0]` etc, except that they are the coordinates for the current neighbour group.

Non-programmers need to note that the array index starts from zero, so `$coord[1]` is the second coordinate axis and not the first.  This differs from systems like R and AWK, but is consistent with many other programming languages like C and Python.


> ## Examples using variables ##

  * Set the neighbours to be those groups where the absolute distance from the processing group is less than 100,000.

```
$D <= 100000
```

  * Select all groups to the west of the processing group.

```
$d[0] < 0
```

  * Select all groups to the north-east of the processing group.

```
$d[0] > 0 && $d[1] > 0
```

  * The absolute distance in the first (eg x) dimension is less than 100,000 AND the signed distance is greater than 100,000. This will result in a neighbourhood that is a column of groups 200,000 map units east-west, and including all groups 100,000 map units north of the processing group. Not that you would normally want a neighbourhood like this...

```
$D[0] <= 100000 && $d[1] >= 100000
```

  * Select everything north of 6000000 (e.g. if using UTM coordinates as axes 0 and 1).  This is an example that could be used as a definition query, and will not work well as a neighbourhood (use `$nbr_y` instead of `$y` for that).

```
$y > 6000000
```

  * Select everything within a rectangle.  This is another useful definition query.

```
$y > 6000000 && $y <= 6100000 && $x > 580000 && $x <= 600000
```

  * Select a specific processing coord (`495:595`), useful as a definition query to use only one group.  Note the use of the `eq` operator - this matches text.  _(Not available before version 0.16)_
```
$coord_id1 eq '495:595'
```



# Declaring variables and using more complex functions #

Variable declaration is done as per Perl syntax. For example:

```
my $some_var = 10;
return ($D / $some_var) <= 100;
```

This trivial example evaluates to true if the absolute distance divided by 10 (the value in variable `$some_var`) is less than 100. The semicolon denotes a separation of statements to be processed in sequence, such that this example could be written on one line. The result of the last statement is what is returned to the analysis to determine if the group is part of the neighbourhood or not. It is evaluated as true or false.  The word `return` is not actually needed in this case, but does make things clearer when there are multiple lines of code.

A more complex function might involve an ellipse (although you could just use `sp_ellipse (major_radius => 300000, minor_radius => 100000, rotate_angle => 1.5714)`)

```
my $major_radius = 300000; # longest axis
my $minor_radius = 100000; # shortest axis

# set the offset in radians, anticlockwise (1.5714 = PI/2 = north)
my $rotate_angle = 1.5714;

# now calc the bearing to rotate the coords by
my $bearing = atan2 ($d[0], $d[1]) + $rotate_angle;

#  and rotate them
my $r_x = cos ($bearing) * $D; # rotated x coord
my $r_y = sin ($bearing) * $D; # rotated y coord

#  get the scaled distances in each direction
my $a_dist = ($r_y ** 2) / ($major_radius ** 2);
my $b_dist = ($r_x ** 2) / ($minor_radius ** 2);

# this last line evaluates to 1 (true) if the candidate
#   neighbour is within or on the edge of the ellipse, 
#   and 0 (false) otherwise
return ($a_dist + $b_dist) <= 1;
```


Note the use of the word `my`. This is required to declare your own variables in the correct scope. If it is not used then the variables will not work properly. Do not declare any of the pre-calculated Biodiverse variables with this (`$D` etc) - they already exist and redeclaring will overprint them, causing unpredictable results.

If you wish to know if your function works with the spatial index then run a moving window analysis twice, once with and once without the spatial index, using the list indices generated by the [Element Counts](Indices#Element_counts.md) calculations to get the lists of neighbours. Export the results to CSV and use a difference tool to compare the results.

Functions available by default are those in the [Perl POSIX library](http://perldoc.perl.org/POSIX.html#FUNCTIONS) (from version 0.16 this is instead the [Math::Trig library](http://perldoc.perl.org/Math/Trig.html), plus [POSIX::fmod()](http://perldoc.perl.org/POSIX.html#FUNCTIONS)). If you want more then you will need to specify additional libraries in the extensions file under the BaseData section _(for which guidelines need to be implemented)_.


To access environment variables you have set, just use `$ENV{variable_name}`, eg `$ENV{my_default_radius}`.