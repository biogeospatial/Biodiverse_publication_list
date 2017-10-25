To install Biodiverse from source for macOS four broad steps are required. First, if you haven't already, you will have to install Xcode command line tools. Second, a software management system has to be installed which can be used to install software required by Biodiverse. Third, Biodiverse requires a higher version of perl than that installed by default on macOS. This and Biodiverse's perl modules dependancies will be install. Fourth, Biodiverse will be installed.

Note that Homebrew is only supported on recent versions of OSX, so if you have an old operating system then these instructions might not work cleanly (e.g. gdal will not install cleanly under Yosemite).  

# Install Xcode command line tools
To install Xcode command line tools (and all following software) you will be using the Terminal application. To open Terminal:
1. Double-click the Terminal application in the Applications:Utilities folder. Or do a Spotlight search for "Terminal" and open it.
2. Copy and paste the below text at the terminal prompt and then hit return.
   ```sh
    xcode-select --install
   ```
3. Once this is install you will need to agree the Apple's software licence.
   ```sh
   sudo xcodebuild -license
   ```
   Enter your password when prompted.

# Installing Homebrew and required software.
Homebrew is a package management system which simplifies the installation of software on Apple's macOS operating system. It is used to install software required by Biodiverse.
   ```sh
   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   ```
3. Some extra packages are required which are not part of the base Homebrew installation. Install these:

   ```sh
   brew tap homebrew/boneyard 
   brew tap osgeo/osgeo4mac
   ```
4. Install the Geospatial Data Abstraction Library (gdal)
   ```sh
   brew install https://raw.githubusercontent.com/OSGeo/homebrew-osgeo4mac/master/boneyard/gdal-20.rb
   ```
5. Install other required packages:
   ```sh
   brew install gdk-pixbuf pango gtk+ gtk+3 libglade libgnomecanvas
   ```
5. Tell perl where to find the gdal configuration script (might not need this. Better to set PERL_GDAL_CONFIG with the installation of Geo::GDAL below:
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
   ~/perl5/perlbrew/bin/perlbrew install perl-5.26.1
   ~/perl5/perlbrew/bin/perlbrew switch perl-5.26.1
   ```
3. Install cpanminus for installing other perl modules:
   ```sh
   perlbrew install-cpanm
   ```
4. Install all other Biodiverse required perl modules:
   ```sh
   cpanm Pango Gnome2::Canvas IO::Socket::SSL.pm Glib::Object::Introspection PAR::Packer Scalar::Util::Numeric
    cpanm --force Gtk2
   PERL_GDAL_CONFIG=/usr/local/Cellar/gdal-20/2.1.0/bin/gdal-config cpanm --force Geo::GDAL
   ```
# Install Biodiverse
1. Install the Biodiverse perl modules
   ```sh
   cpanm Task::Biodiverse::NoGUI
   cpanm Task::Biodiverse
   ```

2. Install Biodiverse either from source or by cloning the git repository. If using git then to install at the top level of your home directory:
    ```sh
    cd ~
    git clone https://github.com/shawnlaffan/biodiverse.git
    ```
3. To run biodiverse switch to the correct version of perl if you haven't already and then run biodiverse:
    ```sh
    ~/perl5/perlbrew/bin/perlbrew switch perl-5.24.0
    perl ~/biodiverse/bin/BiodiverseGUI.pl
    ```

Back to the [main installation page.](https://purl.org/biodiverse/wiki/Installation)