These instructions apply to version 0.15 and later.  They are also increasingly old and have not been tested by the developers for some time.  Please report any success or failures.

They have been tested on Snow Leopard, so there might be small changes for Leopard.

You will need Administrative privileges to run the installation.

Note that this can take quite some time.  If you have not previously installed Xcode or MacPorts then it could take several hours.  It will also download a large number of files, so make sure you have network access with good bandwidth and large download limits.

You might want to consider using the Windows or Linux executable versions under a virtual machine environment such as [Virtualbox](http://www.virtualbox.org/).



# Installation #

  * These instructions assume you have [downloaded](http://code.google.com/p/biodiverse/downloads/list) and extracted the Biodiverse source code distribution into your home directory (this will be `Users/your_login_name/` and is the same as `$HOME/` and `~/`).  You then need to rename the Biodiverse folder from `biodiverse_0.17_source` to `biodiverse`.  If you prefer not to, or have extracted it elsewhere, then make sure to change the `~/biodiverse/lib` text in the following for the folder path you have used (i.e. `/opt/biodiverse` if it is there).

  * You must have the X11 software on your Mac. You will have this if you have Leopard or later. If you have an earlier version of OSX you will need to obtain it either from your original CD or from the Apple site.

  * Install the Xcode software, as it is needed to compile the MacPorts libraries.  This requires registration with Apple.  If you do not have the installation disk (it comes with the computer when you purchase it) then you need to download it.  The download is also >2GB, of which unfortunately a large part is the iPhone SDK which we don't need.  http://developer.apple.com/technologies/xcode.html.
    * If you are using OSX version 10.5 then you will need to download an older version.  This takes a bit more finding.  Go to http://connect.apple.com and then click on the _Developer Tools_ link at the right.  In the next page, search for _Xcode 3.1.4 Developer Tools_.

  * Install MacPorts unless you already have it.  If you are not sure then try to install it anyway and it will tell you.
    * Use the `pkg` installer for your operating system to download the `dmg` file, accessed from http://www.macports.org/install.php (link near the top of the page)
    * Double click on the dmg file once you have downloaded it.  The remaining instructions assume you are using the default location (`/opt`).
  * Run this command in a terminal window to get the latest versions of the MacPorts libraries.
```
sudo port -v selfupdate
```

  * Now install the perl libraries needed by Biodiverse.  The following commands will require some interaction when they download additional packages, depending on your CPAN settings.  The first two commands install the perl wrappers for Glade and Gnome2Canvas and will also install all the other necessary libraries on which they depend (this can take more than an hour so be patient).  The final three commands install the remaining perl libraries.  If you get errors then please see the [trouble shooting section](#Trouble_shooting.md) (installing the URI module can require some forcing).  (If you want to copy and paste these into the terminal then open http://biodiverse.googlecode.com/svn/trunk/etc/macports_install.sh).
```
sudo port install p5-gtk2-gladexml
sudo port install p5-gnome2-canvas
sudo port install gdal

sudo /opt/local/bin/perl -MCPAN -e 'install LWP::Simple'
#  this was added is post 0.99_004 and is not in the task file yet
sudo /opt/local/bin/perl -MCPAN -e 'HTTP::Tiny'

sudo /opt/local/bin/perl -MCPAN -e 'install Task::Biodiverse::NoGUI'
sudo /opt/local/bin/perl -MCPAN -e 'install Task::Biodiverse'
# repeat this command as one of the libs is not installed on the first go
sudo /opt/local/bin/perl -MCPAN -e 'install Task::Biodiverse::NoGUI'

```

# Running it #

  * To run Biodiverse, open a terminal window and change directory to the biodiverse/bin folder.  If it is in your home folder and called `biodiverse` then type:
```
cd ~/biodiverse/bin
```
  * Once you have done this, type the following command to open Biodiverse.
```
/opt/local/bin/perl BiodiverseGUI.pl
```
  * Alternately, you could give the full path to both Perl and Biodiverse if you want to start in a particular directory (i.e. where all your files are).
```
/opt/local/bin/perl ~/biodiverse/bin/BiodiverseGUI.pl
```
  * If you want your command prompt back after opening Biodiverse then run it as a background job.  However, the log output will then be mixed with any other commands you type so things can become confusing.
```
perl BiodiverseGUI.pl &
```



> The full path to perl is specified to ensure the MacPorts version is used.  You can dispense with the `/opt/local/bin` text if the MacPorts version is the first perl in the search path. To check if it is, type:
```
which perl
```

> If it returns `/opt/local/bin/perl` then you can just type this command to run Biodiverse.
```
perl ~/biodiverse/bin/BiodiverseGUI.pl
```

  * This needs testing on a macports system, but you can also add an alias to your profile to save a bit of typing.  Edit the file `$HOME/.profile` (e.g. `Users/your_login/.profile`) and add this line to the end of the file (remembering to edit the biodiverse path if it differs from this):
```
alias biodiverse = '/opt/local/bin/perl ~/biodiverse/bin/BiodiverseGUI.pl'
```
> The next time you open a terminal window you can just type this to start the system:
```
biodiverse
```
> If you are impatient and don't want to open a new window then type this after editing the file (note that you don't need to do it when you start a new terminal).
```
source ~/.profile
biodiverse
```


# Trouble shooting #

  * If Perl complains that it cannot locate a file when running Biodiverse then this library will need to be installed interactively using the cpan shell `sudo /opt/local/bin/cpan`. The complaint will start with text like `Can't locate Fred/Fred.pm in @INC (@INC contains:...)` In this case, install module Fred::Fred (substitute a double colon "::" for each forward slash "/", and remove the trailing ".pm" from the module it cannot locate).  E.g.: `sudo /opt/local/bin/perl -MCPAN -e 'install Fred::Fred'` .  This can happen if one or more of the modules listed in the Task::Biodiverse modules failed to install.
  * If the installation of the Task files fails then check which module causes it.  The URI is one suspect, as it failed one test at the time 0.15 was released, causing the installation to stop.  In this case start the cpan shell in interactive mode (`sudo /opt/local/bin/cpan`) and then type `force install URI`.
  * MacPorts might also complain that files are out of sync, probably if you have an existing MacPorts installation.  If this is the case then run this command to ensure all files are up to date.
```
sudo port -v selfupdate
```

  * Please report any other issues using the [project issue tracker](http://code.google.com/p/biodiverse/issues/list)