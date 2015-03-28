


# Introduction #

This is documentation for the load\_and\_randomise\_wrapper utility that comes with Biodiverse.  The purpose of this utility is twofold.  First, one is able to run randomisations external to the GUI, meaning an analysis can be set up to run as a background task without the GUI and its feedback windows.  Second, one can run most  randomisations within operating system memory limits (see [issue #5](https://code.google.com/p/biodiverse/issues/detail?id=#5)).

# Usage and arguments #

If using the executable version:
```
load_and_randomise_wrapper.exe <basedata file> <randomisation name> {runs [1]} {iterations [10]} {rest of args}
```

If using the perl script (source code install):
```
perl load_and_randomise_wrapper.pl <basedata file> <randomisation name> {runs [1]} {iterations [10]} {rest of args}
```

For example:
```
load_and_randomise_wrapper.exe Example.bds rand_test 10 iterations=10 function=rand_csr_by_group seed=12768545 max_iters=999 save_checkpoint=99
```

Arguments within angle brackets `<...>` are required.  Arguments within curly brackets `{...}` are optional, and will take the default values given in square brackets `[...]`.  Arguments are separated by spaces, with argument values specified after an equal sign.  There should be no spaces between the argument name, equals sign and value.  Use quotes if an argument has any special characters or whitespace (e.g. to use the name `rand structa` then put it in quotes: `"rand structa"`).

  * `basedata file`:  The basedata file (`.bds` extension) that will be randomised.
  * `randomisation name`:  The name of the randomisation that is to be used.  If the basedata file contains a randomisation of this name then that will be used.  If not then one of that name will be created.
  * `runs`:  The number of times the system will save and reload the basedata file, effectively restarting the randomisation analysis with a clean memory.
  * `iterations`:  The number of iterations per run.
  * `rest of args`:  These are all the other arguments for the randomisation, and vary depending on what is being used.  Examples include `seed` for the PRNG starting seed, `richness_multiplier` and `richness_addition` for the rand\_structured analysis, and `save_checkpoint` to periodically save copies of the basedata file if such are needed.


The simplest approach is to use as many iterations as will fit within memory while there is still sufficient memory to save the basedata file (i.e. before the system runs out of memory and crashes).  One then specifies as many runs as are needed to achieve the total number of iterations across runs, with `max_iters` as a stopping criterion.

The advantage of many iterations per run is that file saves and loads take time with large files.  Minimising the number of these will result in a shorter overall analysis time (assuming time is important).  For example, if 99 iterations are needed and up to 10 iterations can be created before the system crashes, then specify something like `load_and_randomise_wrapper.exe Example.bds rand_test 10 iterations=10 max_iters=99` (this is as per the example above).  The worst case scenario (which does happen) is 1 iteration per run.  This will work just as well as any other analysis, it will just take longer due to the file opens and saves.

# How it works #

The utility parses the arguments and then repeatedly calls another utility called `load_and_randomise` to do all the work.  The `runs` argument is the number of times `load_and_randomise` is called.  The iterations argument specifies the number of randmisation iterations each run of `load_and_randomise` completes before saving and returning control back to `load_and_randomise_wrapper` to re-call `load_and_randomise` and complete more iterations, or to exit if it has reached the `max_iters` or has completed the specified number of `runs`.


Note that randomisations are incremental across runs and iterations so that the randomisation will restart from the last iteration that was saved.  However, if basedata is loaded into a GUI project and additional iterations conducted there then these will not be saved into the basedata file when the project is saved.  The basedata must be deliberately saved from the GUI, overwriting if necessary (or to a new filename to be safe).

Note also that arguments that control the randomisation results that are changed between runs will be ignored (e.g. `richness_addition` and `seed`).  Any new PRNG seeds specified after any iterations have been run will also be ignored, and the system will start from the PRNG state at the end of the last completed iteration.  This is the same behaviour as the GUI except that the GUI disables access to the widgets to stop any changes being made.

A useful side-effect of the argument handling is that one does not need to specify all the control arguments for an existing randomisation.  Just specify the basedata, the randomisation name, runs and iterations (if non-default values are needed).  For example the following commands are equivalent if Example.bds already contains a randomisation output called rand\_test.
```
load_and_randomise_wrapper.exe Example.bds rand_test 10 iterations=10 function=rand_csr_by_group seed=12768545 max_iters=999 save_checkpoint=99
load_and_randomise_wrapper.exe Example.bds rand_test 10
```

# Limitations #

You need to be able to store all of the following within your system memory limits at the same time:  1) the BaseData file, 2) its randomised version, and 3) the largest of the output analyses and its randomised comparator.  The `rand_structured` randomisation also requires an additional copy of the BaseData for control purposes.  If you cannot store these within memory then the system will not be able to complete even a single iteration and randomisations cannot be completed.

If you cannot access a machine with bigger memory limits then the workarounds involve reducing the memory requirements using divide and conquer appraches.  These can be used in tandem, and complex analyses are best done using a scripting approach to avoid human error (after debugging of course).

  1. Reduce the number of indices being assessed in each analysis output.  The system only keeps one randomised output result in memory at a time so you might be able to squeeze below the limits this way.
  1. Subdivide the moving window analyses spatially using a set of definition queries.  _Note that this is not appropriate for most cluster analyses as definition queries exclude groups from clustering (unless that's what you want)._  For the moving window analyses, try dividing them into halves first, then quarters, etc.  An example using the western and eastern halves with two definition queries is:  `$x < 200000` and `$x >= 200000` (the `>=` in the second is needed to ensure all groups are considered).  Each subdivision should have the same calculations specified.  Any exported results can be recombined externally to Biodiverse to make a single result file (e.g. in a database or GIS program).
  1. Replicate the basedata file and store a smaller number of the outputs in each new basedata file.  Then re-run the randomisations as many times as there are new basedata, but making sure you specify the same starting seed for each.  The seed ensures the randomised basedatas will all be identical (replicated) at each iteration, and the end result is the same as doing them all within the one basedata (if it would fit within memory).  This can take much longer than the other options as each randomisation iteration must be regenerated for each replicated basedata.  This isn't ideal, but it's something we have to live with until [issue #5](https://code.google.com/p/biodiverse/issues/detail?id=#5) is fixed.  Randomisations of large data sets using the rand\_structured function will take the longest, as the system must reconverge on the richness targets for each replicated iteration (it does not record how it did it, but the seed ensures the same result each time).