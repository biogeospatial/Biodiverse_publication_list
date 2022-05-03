# Available downloads #

**Table of contents:**
* [Available downloads](#available-downloads)
  * [Biodiverse GUI](#biodiverse-gui)
    * [Quick Start Guide](#quick-start-guide)
    * [Stable Release](#stable-release)
      * [Known issues](#known-issues)
    * [Development Release](#development-release)
  * [Site Pair Sampler](#site-pair-sampler)
  * [Utility scripts](#utility-scripts)
  * [Older versions](#older-versions)


## Biodiverse GUI ##


There is also a series of blog posts at http://biodiverse-analysis-software.blogspot.com.au/

### Quick Start Guide ###

A [quick start guide](http://biodiverse.unsw.edu.au/downloads/Biodiverse_Quick_Start_Guide_2018-09-05.pdf) is available.


### Stable Release ###

_The current stable release is version 3.1, released 13-Mar-2020._

The [release notes](http://purl.org/biodiverse/wiki/ReleaseNotes#version-31) summarise the changes in this version.

All versions are for 64 bit architectures.


* [Windows (~68MB)](https://github.com/shawnlaffan/biodiverse/releases/download/r3.1_mac_updates/biodiverse_3.1_win.zip)

* [Linux (~14MB)](https://github.com/shawnlaffan/biodiverse/releases/download/r3.1_mac_updates/biodiverse_3.1_linux.zip)

* [MacOS (~68MB)](https://github.com/shawnlaffan/biodiverse/releases/download/r3.1_mac_updates/biodiverse_3.1_mac.zip)

* [Source code](https://github.com/shawnlaffan/biodiverse/releases/tag/r3.1)

* [Installation instructions](https://github.com/shawnlaffan/biodiverse/wiki/Installation)


#### Known issues ####

  * On MacOS Catalina there are issues accessing the Desktop, Documents and similar directories.  The workaround is to either use a separate Biodiverse directory or to run the GUI from the command line.  [More details are in issue 778](https://github.com/shawnlaffan/biodiverse/issues/778#issuecomment-759140901), which is being used to track this.
  * On Windows, an existing installation of the GDAL stack can interfere with those packaged with Biodiverse.  This in being tracked in [Issue 795, which also provides an interim workaround](https://github.com/shawnlaffan/biodiverse/issues/795). 
  * There appear to be problems with the cp936 locale, and probably other CJK character set locales.  The workaround for now is to set your locale and region to US (see details in [Issue 506](/shawnlaffan/biodiverse/issues/506)).

### Development Release ###

Development releases are in the 3.99 series, leading to version 4.

The [release notes](https://github.com/shawnlaffan/biodiverse/wiki/ReleaseNotes#version-399-dev-series) summarise the changes in this version.

* Windows executable and source code releases [are available through GitHub](https://github.com/shawnlaffan/biodiverse/releases/tag/r3.99_003)

There are no Linux or Mac dev releases at this stage but they can be provided if there is a need.

## Site Pair Sampler ##

[Site pair sampler for GDM analyses](http://biodiverse.unsw.edu.au/downloads/site_pair_sample_64bit.7z).

For further details, see:

Rosauer, D.F., Ferrier, S., Williams, K.J., Manion, G, Keogh, S & Laffan, S.W. (2014), Phylogenetic Generalised Dissimilarity Modelling: a new approach to analysing and predicting spatial turnover in the phylogenetic composition of communities. Ecography.  http://dx.doi.org/10.1111/j.1600-0587.2013.00466.x


## Utility scripts ##

* [Multidirectional Turnover Analyser Perl Script](http://biodiverse.unsw.edu.au/downloads/multidirectional_turnover_analyser.pl).

Requires a [source code installation](Installation).

For further details, see:

Di Virgilio, G., Laffan, S.W. & Ebach, M.C. (2012) Fine scale quantification of floral and faunal breaks and their geographic correlates, with an example from south-eastern Australia. Journal of Biogeography, 39, 1862-1876.  http://dx.doi.org/10.1111/j.1365-2699.2012.02739.x

## Older versions ##

* Older versions can be accessed via (http://biodiverse.unsw.edu.au/downloads/) or the [deprecated downloads URL](http://biodiverse.unsw.edu.au/downloads/deprecated/).

