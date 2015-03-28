These instructions apply to version 0.18 and later.

These assume you have saved the Biodiverse source code to C:\biodiverse.  If you have not then change the `C:\biodiverse\lib` path in the following to the appropriate path.

_IMPORTANT_:  You need to be sure to run step 4 from the installation every time you want to run the system.  (This is until we develop a batch script to handle it).

_DO NOT USE A PATH WITH SPACES IN IT_.  This causes problems with the batch file used to run the source code version.  (This has no effect on the executable file).





# StrawberryPerl #


## Installation ##


1.  Install Strawberry Perl 5.16.3, either 32 or 64 bit.  The rest of these instructions assume you have used C:\strawberry as the install folder.  If you have not then edit the paths below to match what you have used.  http://strawberryperl.com/  _IMPORTANT:  MAKE SURE YOU USE 5.16.3 and NOT 5.18, 5.16.1 or 5.16.2.  There are installation problems with these versions related to gdal, and we do not have gdal ppms for the 32 bit version of 5.18 (needed for step 6)_

2.  [Download](http://code.google.com/p/biodiverse/downloads/list) the source code version to obtain a stable release.  Alternately you can use a subversion client to get the latest Biodiverse code, see http://code.google.com/p/biodiverse/source/checkout

3.  Open a command prompt.  The rest of these instructions assume you are at the prompt.

4.  Run these commands, editing the folder paths as needed to match your system.

```
  set BDV_PATH=c:\biodiverse
  set STRAWPATH=c:\strawberry
  :: Change gtk_win64 to gtk_win32 if you are using a 32 bit installation.  Same applies gdal_win64.
  set GTK_PATH=c:\gtk_win64
  set GDAL_PATH=c:\gdal_win64
  set PATH=%STRAWPATH%\bin;%STRAWPATH%\perl\site\bin;%STRAWPATH%\perl\vendor\bin;%STRAWPATH%\perl\bin;%GTK_PATH%\c\bin;%GDAL_PATH%\bin;%PATH%
```

5.  Download the gtk\_win64 and gdal\_win64 components using an svn checkout. TortoiseSVN is the easiest way, but this command line will work if you installed the shell options with TortoiseSVN (or you have a different svn client).  _Remember to change `_win64` to `_win32` in the paths if you are using a 32 bit installation_.

```
  svn co http://biodiverse.googlecode.com/svn/branches/gtk_win_builds/etc/gtk2.10_win64 %GTK_PATH%
  svn co http://biodiverse.googlecode.com/svn/branches/gdal_win_builds/gdal_1.10.1/gdal_win64/ %GDAL_PATH%
```


6.  Now we need to install some files using the ppm and cpanm utilities.  In the same command prompt that you ran the commands from step 1, run the ppm install command for all ppd files.  You can copy and paste these into the command prompt.  If you are using a 32 bit perl then change ppm516\_x64 to be ppm516.

```
  :: Install the precompiled binaries needed for the GUI.
  :: Edit the next line to match the perl version you are using, 
  :: e.g. ppm516 for the 32 bit version, ppm516_x64 for 64 bit
  set BDV_PPM=http://biodiverse.googlecode.com/svn/branches/ppm/ppm516_x64
  ppm install %BDV_PPM%/Cairo.ppd 
  ppm install %BDV_PPM%/Glib.ppd 
  ppm install %BDV_PPM%/Gnome2-Canvas.ppd 
  ppm install %BDV_PPM%/Pango.ppd
  ppm install %BDV_PPM%/Gtk2.ppd
  ppm install %BDV_PPM%/Gtk2-GladeXML.ppd
  ppm install %BDV_PPM%/Geo-GDAL.ppd

  ::  This is not yet in the Task files on CPAN
  cpanm List::BinarySearch

  :: YAML::Syck has installation failures at v1.27 so install a patched version via PPM 
  ppm install %BDV_PPM%/YAML-Syck.ppd

  ::  this was added is post 0.99_004 and is not in the task file yet
  cpanm HTTP::Tiny

  :: Now install the rest of the dependencies
  cpanm Task::Biodiverse::NoGUI~0.19
  cpanm Task::Biodiverse~0.19
```


## Running it ##

The above installation process **should** install all the relevant files, so we can now run it.

1.  This is the same as step 1 in the installation instructions, but needs to be run every time you open a new command prompt (unless you add the paths to your PATH variable at the windows level).  Remember to edit the folder paths if you installed Biodiverse, the Gtk libs, GDAL libs and/or Strawberry Perl to different folders.  Note that Biodiverse goes looking up the directory tree for Gtk and GDAL using the installation names in the previous steps, so you only need to add them to the path if you put them somewhere else.

```
  set BDV_PATH=c:\biodiverse
  set STRAWPATH=c:\strawberry
  set PATH=%STRAWPATH%\bin;%STRAWPATH%\perl\site\bin;%STRAWPATH%\perl\vendor\bin;%STRAWPATH%\perl\bin;%BDV_PATH%\bin;%PATH%
```

2.  Now you can run it.

```
  perl %BDV_PATH%\bin\BiodiverseGUI.pl
```


  * See the [trouble shooting](#Trouble_shooting.md) section below if you encounter problems.


# Trouble shooting #

  * If you get errors about not finding gnome-canvas, glib and friends then check that the `%GTK_PATH%\c\bin` directory exists and is correctly named.
  * If Perl complains that it cannot locate a file when running Biodiverse then this library will need to be installed interactively using cpan. The complaint will contain text like `Can't locate Fred/Fred.pm in @INC (@INC contains:...)`  In this case, install module Fred::Fred (substitute a double colon "::" for each forward slash "/", and remove the trailing ".pm" from the module it cannot locate). E.g.: `cpanm Fred::Fred` . This can happen if one or more of the modules listed in the bundle failed to install.

  * Please report any other issues using the [project issue tracker](http://code.google.com/p/biodiverse/issues/list)