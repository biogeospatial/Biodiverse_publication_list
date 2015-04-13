These instructions apply to version 0.17.

# Installation #

  * Decompress and untar the Biodiverse package file to your hard drive.  The following assumes you have unzipped it so `$HOME/biodiverse` is the top level.  If you use a different path then modify the commands as appropriate.
  * You might need to also install some of the dependencies, depending on your Linux installation.  See the [InstallationLinuxSource](InstallationLinuxSource) page for details (the lines containing apt-get).

# Running it #

  * Biodiverse can be run by double clicking on `BiodiverseGUI_linux`.
  * If you want to keep the command log visible after you close Biodiverse then run it from a terminal.
    * In the terminal, type `$HOME/biodiverse/BiodiverseGUI_linux`.
  * If you want to avoid all the typing then edit your profile to add the biodiverse directory to your $PATH environment variable.

# Troubleshooting and changes #

  * Ensure that you have installed the latest `GTK+`, `Glade` and `GnomeCanvas` packages.

  * If you don't like the current window theme then you can change them using the Desktop Preferences (also via the `gnome-appearance-properties` tool).  You can download and install more themes from http://art.gnome.org/themes/gtk2

  * Please report any other issues using the [project issue tracker](https://github.com/shawnlaffan/biodiverse/issues/)