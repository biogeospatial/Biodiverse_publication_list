These instructions apply to version 1.99 and later.

Note that they have been tested on Ubuntu.  The package manager will differ for other Linux flavours, but the cpan command will be the same.

These also assume you have [downloaded](https://github.com/shawnlaffan/biodiverse/wiki/Downloads) the Biodiverse source code to your home directory and renamed it from whatever it was, e.g. `biodiverse_0.19_source`, to `biodiverse`.  If you have saved it somewhere else then you will need to adjust the following so any references to `$HOME/biodiverse/lib` use the appropriate directory.

**Table of contents:**
* [Installation](#installation)
* [Running it](#running-it)
* [Troubleshooting](#troubleshooting)


# Installation #

  * This will require some interaction when it downloads additional packages, depending on your CPAN settings.

  * It is also a very good idea to **not** use the system perl for this.  The operating system assumes specific versions of files are in the system perl.  Perlbrew is recommended, and is used for Biodiverse development.  http://perlbrew.pl/

  * Once you have installed the non-system perl, you need to make sure it is the one you call in subsequent steps.  You will probably need to give the full path name to the perl binary when used below, rather than just saying `perl`.


```bash
  #  if you have Ubuntu less than 14.04 -- add the GDAL repo
  sudo add-apt-repository ppa:ubuntugis/ppa 
  sudo apt-get update

  # now get the apts
  # for XML::Parser
  sudo apt-get install libexpat1-dev
  #  Gtk:
  sudo apt-get install libgnome2-canvas-perl
  sudo apt-get install libcairo2-dev libpango1.0-dev libgtk2.0-dev libgnomecanvas2-dev libglade2-dev
  # GDAL:
  sudo apt-get install libarmadillo-dev libpoppler-dev libepsilon-dev liblzma-dev
  sudo apt-get install libgdal-dev libkml-dev libfreexl-dev libgdal-perl libogdi3.2-dev

  #  skip this if you already have cpanm installed
  wget -O - https://cpanmin.us | perl - App::cpanminus

  # Now install the rest of the dependencies
  cpanm Task::Biodiverse::NoGUI
  cpanm Task::Biodiverse
  cpanm Task::Biodiverse

  # The last cpanm command is listed twice to get Gtk2::GladeXML
  # to install after its dependencies, and might be redundant 
  # now we do not use Gtk2::GladeXML

```

  *  Follow this step if there is no appropriate package for GDAL and manual compilation is needed (at one point Ubuntu did not have GDAL 1.11 packaged)
  
    These instructions are derived from https://milkator.wordpress.com/2014/05/06/set-up-gdal-on-ubuntu-14-04/

```bash
  cd ~/folder/for/builds/from/source

  sudo apt-get install build-essential python-all-dev

  gdal_version=2.1.3
  wget http://download.osgeo.org/gdal/${gdal_version}/gdal-${gdal_version}.tar.gz
  tar xvz gdal-${gdal_version}.tar.gz
  cd gdal-${gdal_version}

  #  This will install GDAL into your system level directories
  #  Set the --prefix argument to use a different location,
  #  e.g. ./configure --prefix=~HOME/gdal2.1.3
  #  and remove the sudo if appropriate 
  ./configure 
  make -j4
  sudo make install
```

  *  Now we install the perl bindings.
    This command will download and extract the GDAL
    perl bindings and open a shell in that folder.
    Make sure you are using the same version of perl as above
    (sometimes commands can change this, or you are in a new shell and perlbrew is not loaded)

```bash
  cpanm --look Geo::GDAL

  #  adjust the config path as needed 
  perl Makefile.PL --no-version-check --gdal-config=/usr/local/bin/gdal-config
  make && make test && make install

  #  if it all worked then exit
  exit
```

If you don't like the current window theme then you can change it using the Desktop Preferences.


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