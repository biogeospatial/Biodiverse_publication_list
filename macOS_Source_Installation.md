To install Biodiverse from source for macOS three broad steps are required. First, a software management system has to be installed which can be used to install software required by Biodiverse. Second, Biodiverse requires a higher version of perl than that installed by default on macOS. This and Biodiverse's perl modules dependancies will be install. Third, Biodiverse will be installed.

# Installing Homebrew and required software.
Homebrew is a package management system which simplifies the installation of software on Apple's macOS operating system. It is used to install software required by Biodiverse. To install Homebrew (and all following software) you will be using the Terminal application. To open Terminal:
1. Double-click the Terminal application in the Applications:Utilities folder. Or do a Spotlight search for "Terminal" and open it.
2. Copy and paste the below text at the terminal prompt and then hit return.
   ```sh
   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   ```
3. Some extra packages are required which are not part of the base Homebrew installation. Install these:

   ```sh
   brew tap homebrew/boneyard osgeo/osgeo4mac
   ```
4. Install the Geospatial Data Abstraction Library (gal)
   ```sh
   brew install https://raw.githubusercontent.com/OSGeo/homebrew-osgeo4mac/master/boneyard/gdal-20.rb
   ```
5. Install other required packages:
   ```sh
   brew install gdk-pixbuf pango gtk+ gtk+3 libglade libgnomecanvas
   ```
5. Tell perl where to find the gdal configuration script:
   ```sh 
   export PERL_GDAL_CONFIG=/usr/local/Cellar/gdal-20/2.1.0/bin/gdal-config
   ```
Further information about Homebrew can be found [here](https://brew.sh).

# Installing perlbrew and required perl modules
perlbrew is an admin-free perl installation management tool. It can be used to install a version of perl that Biodiverse requires. 
1. Copy and paste this line into your terminal to install perlbrew:
   ```sh
   \curl -L https://install.perlbrew.pl | bash
   ```
2. Install the version of perl that Biodiverse requires and then use it:
   ```sh
   perlbrew install perl-5.24.0
   perlbrew switch perl-5.24.0
   ```
3. Install cpanminus for installing other perl modules:
   ```sh
   cpan App::cpanminus
   ```
4. Install all other Biodiverse required perl modules:
   ```sh
   cpanm Pango Gtk2 Gtk3 Gtk2::GladeXML Gnome2::Canvas IO::Socket::SSL.pm Glib::Object::Introspection PAR::Packer
   cpanm  --force Geo::GDAL
   ```
# Install Biodiverse
Install the Biodiverse perl modules
   ```sh
   cpanm Task::Biodiverse::NoGUI
   cpanm Task::Biodiverse
   cpanm Task::Biodiverse::NoGUI
   ```
# Building a dmg image
To build a dmg image for easy distribution of a binary version of Biodiverse follow the steps below.

1. Clone the Biodiverse git repository at the top level of you home directory:
   ```sh
   cd ~
   git clone https://github.com/shawnlaffan/biodiverse.git
   ```
2. Run the Biodiverse dmg creation script:
   ```sh
    perl ~/biodiverse/bin/mmb3.pl --verbose=1 --script ~/biodiverse/bin/BiodiverseGUI.pl -i ~/biodiverse/bin/Biodiverse_icon.ico --lib_path=/usr/local/lib
   ```
3. The dmg image can be found in ~/biodiverse/etc/mmb/builds.

Back to [OS X binary installation.](https://github.com/shawnlaffan/biodiverse/wiki/OSX_binary_installation)