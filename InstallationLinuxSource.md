These instructions apply to version 0.19 and later.

Note that they have been tested on Ubuntu.  The package manager will differ for other Linux flavours, but the cpan command will be the same.

These also assume you have [downloaded](http://code.google.com/p/biodiverse/downloads/list) the Biodiverse source code to your home directory and renamed it from whatever it was, e.g. `biodiverse_0.17_source`, to `biodiverse`.  If you have saved it somewhere else then you will need to adjust the following so any references to `$HOME/biodiverse/lib` use the appropriate directory.

**Table of contents:**
* [Installation](#installation)
* [Running it](#running-it)
* [Troubleshooting](#troubleshooting)


# Installation #

  * This will require some interaction when it downloads additional packages, depending on your CPAN settings.

  * It is also a very good idea to **not** use the system perl for this.  The operating system assumes specific versions of files are in the system perl.  Perlbrew is recommended, and is used for Biodiverse development.  http://perlbrew.pl/

  * Once you have installed the non-system perl, you need to make sure it is the one you call in subsequent steps.  You will probably need to give the full path name to the perl binary when used below, rather than just saying `perl`.


```bash
  #  add the GDAL repo
  sudo add-apt-repository ppa:ubuntugis/ppa 
  sudo apt-get update

  # now get the apts
  #  Gtk:
  sudo apt-get install libgnome2-canvas-perl
  sudo apt-get install libcairo2-dev libpango1.0-dev libgtk+2.0-dev libgnomecanvas2-dev libglade2-dev
  # GDAL:
  sudo apt-get install libarmadillo-dev libpoppler-dev libepsilon-dev liblzma-dev
  sudo apt-get install libgdal-dev libkml-dev libfreexl-dev gdal-perl libogdi3.2-dev

  #  skip this if you already have cpanm installed
  cpan App::cpanminus

  # Now install the rest of the dependencies
  cpanm Task::Biodiverse::NoGUI
  cpanm Task::Biodiverse
  cpanm Task::Biodiverse

  #  The last cpan command is listed twice to get Gnome::Canvas
  #  and Gtk2::GladeXML to install after their dependencies.

  #  Now we need to get GDAL
  #  Manual compilation is needed.
  #  Download and uncompress the Geo::GDAL tarball (maybe using cpanm, or from https://metacpan.org/pod/Geo::GDAL).  
  #  Then in the uncompressed Geo::GDAL folder (editing the config path to point to your bin/gdal-config file):

  #  The most recent perl GDAL bindings need gdal 1.11, and for some reason this is not yet packaged for Ubuntu.
  #  This means we need to manually install it.
  #  These instructins are derived from https://milkator.wordpress.com/2014/05/06/set-up-gdal-on-ubuntu-14-04/
  
  cd ~/folder/for/builds/from/source

  sudo apt-get install build-essential python-all-dev

  wget http://download.osgeo.org/gdal/1.11.1/gdal-1.11.1.tar.gz
  tar xvz gdal-1.11.1.tar.gz
  cd gdal-1.11.1

  ./configure --with-python --with-perl
  make
  sudo make install
  
  #  Now we install the perl bindings.
  #  This command will download and extract the GDAL perl bindings and open a shell in that folder.
  #  Make sure you are using the same version of perl as above
  #  (sometimes commands can change this, or you are in a new shell and perlbrew is not loaded)

  cpanm --look Geo::GDAL

  perl Makefile.PL --no-version-check --gdal-config=/usr/local/bin/gdal-config
  make
  make test
  make install

```

If you don't like the current window theme then you can change it using the Desktop Preferences (also via the `gnome-appearance-properties` tool).


# Running it #

  * To run Biodiverse, open a terminal window and change directory to the biodiverse/bin folder.  If it is in your home folder and called `biodiverse` then type:
```bash
cd ~/biodiverse/bin
```
  * Once you have done this, type the following command to open Biodiverse.
```bash
perl BiodiverseGUI.pl
```
  * Alternately, you could give the full path to Biodiverse if you want to start in a particular directory (i.e. where all your files are).
```bash
perl ~/biodiverse/bin/BiodiverseGUI.pl
```
  * If you want your command prompt back after opening Biodiverse then run it as a background job.  However, the log output will then be mixed with any other commands you type.
```bash
perl BiodiverseGUI.pl &
```


  * You can also add the `biodiverse/bin` folder to your PATH variable to save some typing. You might also need to edit the shebang line in BiodiverseGUI.pl to point to the correct perl executable.

# Troubleshooting #
  * Ubuntu 11 appears to need this before running the other installer commands:  `sudo apt-get install libgnome2-canvas-perl`
  * Please report any issues using the [project issue tracker](https://github.com/shawnlaffan/biodiverse/issues/)