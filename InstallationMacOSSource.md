To install Biodiverse from source for macOS four broad steps are required. First, if you haven't already, you will have to install Xcode command line tools. Second, a software management system has to be installed which can be used to install software required by Biodiverse. Third, Biodiverse requires a higher version of perl than that installed by default on macOS. This and Biodiverse's perl modules dependancies will be install. Fourth, Biodiverse will be installed.

If you find issues with these instructions then please raise an [issue](https://github.com/shawnlaffan/biodiverse/issues/) or start a [discussion thread](https://github.com/shawnlaffan/biodiverse/discussions).

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

1. Homebrew is a package management system which simplifies the installation of software on Apple's macOS operating system. It is used to install software required by Biodiverse.
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install other required packages:
   ```sh
   brew install gdk-pixbuf pango gtk+ gtk+3 libglade libffi gdal openssl
   ```

3. libgnomecanvas needs to be patched to avoid a serious memory leak
   ```sh
   brew edit libgnomecanvas
   #  insert these lines into the build, immediately after the line containing "def install":
   #  system "\\curl -L https://raw.githubusercontent.com/shawnlaffan/biodiverse/master/etc/libgnomecanvas.patch > libgnomecanvas.patch"
   #  system "patch -d libgnomecanvas < libgnomecanvas.patch"
   #  then exit the editor
   brew install --build-from-source libgnomecanvas
   ```

Further information about Homebrew can be found [here](https://brew.sh).

# Installing perlbrew and required perl modules
perlbrew is an admin-free perl installation management tool. It can be used to install a version of perl that Biodiverse requires. 
1. Copy and paste this line into your terminal to install perlbrew:
   ```sh
   \curl -L https://install.perlbrew.pl | bash
   ```
2. Install the version of perl that Biodiverse requires and then use it (must be higher than 5.22):
   ```sh
   ~/perl5/perlbrew/bin/perlbrew install --noman perl-5.36.0
   #  if there are "no symbol" test failures in libperl.t then skip the tests
   #~/perl5/perlbrew/bin/perlbrew install --noman --notest perl-5.36.0
   ~/perl5/perlbrew/bin/perlbrew switch perl-5.36.0
   ```
3. Install cpanminus for installing other perl modules:
   ```sh
   perlbrew install-cpanm
   ```
4. Install Biodiverse GUI  module dependencies.  Gtk2 has known test failures, but works, so we don't test it.
   ```sh
   cpanm --notest Gtk2
   cpanm Pango Gnome2::Canvas IO::Socket::SSL Glib::Object::Introspection Scalar::Util::Numeric Browser::Start
   ```

# Install Biodiverse

1. Install Biodiverse either from source or by cloning the git repository. If using git then to install at the top level of your home directory:
    ```sh
    cd ~
    git clone --depth 1 https://github.com/shawnlaffan/biodiverse.git
    cd biodiverse
    cpanm --installdeps .
    #  only need to run these two lines for v3.1 or earlier
    cpanm Task::Biodiverse::NoGUI
    cpanm Task::Biodiverse

    #  make sure the file history can be saved
    mkdir -p ${HOME}/.local/share/
    touch $HOME/recently-used.xbel  
    ```

2. To run biodiverse switch to the correct version of perl if you haven't already (this assumes perl-5.36.0), and then run biodiverse:
    ```sh
    ~/perl5/perlbrew/bin/perlbrew switch perl-5.36.0
    perl ~/biodiverse/bin/BiodiverseGUI.pl
    ```

Back to the [main installation page.](https://github.com/shawnlaffan/biodiverse/wiki/Installation)
