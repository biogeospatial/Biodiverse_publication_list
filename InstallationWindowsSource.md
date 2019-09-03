These instructions apply to version 2.99_001 and later.

These assume you have saved the Biodiverse source code to C:\biodiverse.  If you have not then change the `C:\biodiverse\lib` path in the following to the appropriate path.

_IMPORTANT_:  You need to be sure to run step 4 from the installation every time you want to run the system.  (This is until we develop a batch script to handle it).

_DO NOT USE A PATH WITH SPACES IN IT_.  This causes problems with the batch file used to run the source code version.  (This has no effect on the executable file).


# StrawberryPerl #


## Installation ##


*  Step 1.  Install Strawberry Perl 64bit, 5.24 or later, and preferably one of the variants that come with PDL installed.  The rest of these instructions assume you have used C:\strawberry as the install folder.  If you have not then edit the paths below to match what you have used.  http://strawberryperl.com/

*  Step 2.  [Download](Downloads) the source code version to obtain a stable release.  Alternately you can use a GIT client to get the latest Biodiverse code, see https://github.com/shawnlaffan/biodiverse and the clone URL there.

*  Step 3.  Open a command prompt.  The rest of these instructions assume you are at the prompt.

*  Step 4.  Run these commands, editing the folder paths as needed to match your system.

```dos
  set BDV_PATH=c:\biodiverse
  set STRAWPATH=c:\strawberry
  :: This next command should only be needed if the strawberry perl bin folders 
  :: are not in your path already, or if Rtools (or some other c-compiler toolset) 
  :: comes before the strawberry perl bin folders in the path.
  set PATH=%STRAWPATH%\bin;%STRAWPATH%\perl\site\bin;%STRAWPATH%\perl\vendor\bin;%STRAWPATH%\perl\bin;%PATH%
```

*  Step 5.  Now we need to install some files using the ppm and cpanm utilities.  In the same command prompt that you ran the commands from step 1, run the ppm install command for all ppd files.  You can copy and paste these into the command prompt.  It is best to do them one block at a time as the comments list some conditional steps.  

```
  :: Install the precompiled binaries needed for the GUI.
  set SIS_PPM=http://www.sisyphusion.tk/ppm
  :: This will also get the other Gtk2 packages
  ppm install %SIS_PPM%/Gnome2-Canvas.ppd 
  :: but themes are a separate install - be sure to say yes when it prompts to move files
  ppm install %SIS_PPM%/PPM-Sisyphusion-Gtk2_theme.ppd

  ::  This might no longer be necessary, but does not hurt.  
  ::  Math::Random::MT::Auto had test errors due to 
  ::  false positive test results caused by another module.
  cpanm Math::Random::MT::Auto
  :: If the tests report failures due 
  :: to a missing signal then force install it.
  :: (But not for other failures).
  cpanm --notest Math::Random::MT::Auto

  :: Faster utils
  cpanm List::MoreUtils::XS
  cpanm http://www.biodiverse.unsw.edu.au/downloads/Biodiverse-Utils-1.06.tar.gz

  :: Now install the rest of the dependencies
  :: You might need to re-run this line a few times as 
  :: anti-virus scanning can cause test failures due to 
  :: file locks not being released.
  :: Note also that the GDAL installation will take a _loooong_ time (~40 minutes)
  cpanm Task::Biodiverse

```


## Running it ##

The above installation process **should** install all the relevant files, so we can now run it.

*  This is the same as step 1 in the installation instructions, but needs to be run every time you open a new command prompt (unless you add the paths to your PATH variable at the windows level).  Remember to edit the folder paths if you installed Biodiverse and/or Strawberry Perl to different folders.

```dos
  set BDV_PATH=c:\biodiverse
  set STRAWPATH=c:\strawberry
  set PATH=%STRAWPATH%\bin;%STRAWPATH%\perl\site\bin;%STRAWPATH%\perl\vendor\bin;%STRAWPATH%\perl\bin;%BDV_PATH%\bin;%PATH%
```

*  Now you can run it.

```dos
  perl %BDV_PATH%\bin\BiodiverseGUI.pl
```


  * See the [trouble shooting](#trouble-shooting) section below if you encounter problems, for example modules failing to load.


# Trouble shooting #

  * If Perl complains that it cannot locate a file when running Biodiverse then this library will need to be installed interactively using cpan. The complaint will contain text like `Can't locate Fred/Fred.pm in @INC (@INC contains:...)`  In this case, install module Fred::Fred (substitute a double colon "::" for each forward slash "/", and remove the trailing ".pm" from the module it cannot locate). E.g.: `cpanm Fred::Fred` . This can happen if one or more of the modules listed in the Task distributions failed to install.

  * Please report any other issues using the [project issue tracker](https://github.com/shawnlaffan/biodiverse/issues/)