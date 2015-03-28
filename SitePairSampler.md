# Introduction #

**Site Pair Sampler** is an add-on script for _Biodiverse_, to sample compositional dissimilarity between pair of sites.  It is designed for use with Generalised Dissimilarity Modelling (GDM) or other models of compositional turnover.

It was written by Dan Rosauer to implement analyses for:
Dan F. Rosauer, Simon Ferrier, Kristen J. Williams, Glenn Manion, J. Scott Keogh and Shawn W. Laffan. _Phylogenetic generalised dissimilarity modelling: a new approach to analysing and predicting spatial turnover in the phylogenetic composition of communities_; which is currently in review with the journal _Ecography_.

# Download #
It is found in the source code version of _Biodiverse_ under the etc directory.
http://code.google.com/p/biodiverse/source/browse/#svn%2Ftrunk%2Fetc%2Fsite_pair_sampler .  Until it is released as a separate download you will need to download the full folder using a subversion checkout.

# Setup #

  * You will need to install one of the source code versions of Biodiverse.  See the [Installation](Installation.md) page.

# Running it #

  * You will need to copy and edit one of the scripts under the `site_pair_sampler/bin` folder.  Avoid names with spaces in them.  Set all the parameters as needed for your analysis.

  * If you save your version of the script to a different folder then you will need to add the site\_pair\_sampler/lib folder to your PERL5LIB environment variable, or add it as an argument every time you run the script.

  * To run it, open a command prompt and type the following, editing the path and script name to match what you are using:

```
  perl c:\site_pair_sampler\bin\GDM_Input_sample_params_basic.pl
```

> When run, it calls GD\_Modeller.pm and other components of _Biodiverse_.

  * The output files will be wherever you told the system to put them.

# Trouble shooting #

  * Please use the comments section at the bottom of this page (you will need to be logged into google), or raise an issue using the issue tracker.  http://code.google.com/p/biodiverse/issues/list