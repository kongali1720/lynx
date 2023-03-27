# lynx
lynx-2.8.9

http://lynx.invisible-island.net/

Lynx Installation Guide

This file describes how to compile and install Lynx.  A description of Lynx
can be found in the README file.  Lynx has been ported to UN*X, VMS, Win32
and 386DOS.  The procedures for compiling these ports are quite divergent
and are detailed respectively in Sections II, III, IV and V.  General
installation, problem solving and environment variables are covered in
Sections VI and VII.  There is also a PROBLEMS file in the same directory
as INSTALLATION which contains advice for special problems people have
encountered, especially for particular machines and operating systems.

If you still have difficulties, send an e-mail message to the Lynx-Dev mailing
list (see the README file).  Try to include information about your system,
the name and version of your compiler, which curses library you are using
and the compile-time errors.  Be sure to say what version and image-number
of Lynx you are trying to build (alternately the top date of the CHANGES file).

If you don't understand what one of the defines means, try the README.defines
and *.announce files in the docs subdirectory.  The docs/CHANGES* files record
the entire development history of Lynx and are an invaluable resource for
understanding how Lynx should perform.

First, you must configure Lynx for your system regardless of the port you use.
Follow the instructions given immediately below to configure for your system,
and then go to the respective section concerning the port you wish to compile.

-------------------------------------------------------------------------------

I. General configuration instructions (all ports).

Step 1.  Compile-time Variables.

  There are a few variables that MUST be defined if Lynx is to build
  and there are others you may want to change.

  Lynx MUST be able to find lynx.cfg at start-up: using configure
  (e.g. with UNIX or Cygwin), its location is best set with --sysconfdir ;
  you can check in lynx_cfg.h after configure has run, if you wish.
  otherwise, you can use LYNX_CFG_FILE in userdefs.h ,
  environment variable LYNX_CFG or the -cfg command-line option.

  If you are using configure, you need not make any changes in userdefs.h .
  There are a few variables you can't define with configure --options
  but can define in userdefs.h , e.g. numbering fields as well as links.
  Many variables which can be defined with configure or  userdefs.h
  can also be defined in lynx.cfg or via the Options Menu.

  Lynx implements Native Language Support.  Read "ABOUT-NLS", if you want
  to build an international version of Lynx or tailor status-line prompts,
  messages and warnings to the requirements of your site.

Step 2.  Run-time Variables.

  Read  lynx.cfg  thoroughly, as many Lynx features and how to use them
  are explained there, in some cases ONLY there.  Set up local printers,
  downloaders, assumed character set, key mapping and colors in  lynx.cfg .
  Also see the sample mime.types, mailcap and jumps files
  in the samples subdirectory.

Step 3.  Alternative Character Sets.

  You may skip this, if you are not interested in special characters
  and all local files or WWW pages you will view will use the ISO-8859-1
  "ISO Latin 1" Western European character set.

  If you will be running Lynx in an environment with different incompatible
  character sets, configure CHARACTER_SET (the Display character set)
  and ASSUME_LOCAL_CHARSET to work correctly before creating bookmark files
  and other such items: read lynx.cfg for detailed instructions.
  Additional character sets and their properties may be defined with tables
  in the src/chrtrans directory: see the README.* files therein.

Step 4.  News.

  Set NNTPSERVER in lynx.cfg to your site's NNTP server
  or set the environment variable externally.  For posting to be enabled,
  NEWS_POSTING must be TRUE in userdefs.h or lynx.cfg.
  Also define LYNX_SIG_FILE in userdefs.h or lynx.cfg ,
  so that it points to users' signature files for appending to messages.

Step 5.  Anonymous Accounts *** VERY IMPORTANT!!!!! ***

  If you are building Lynx for personal use only, you can skip this.

  If you are setting up anonymous accounts to use Lynx captively,
  i.e. making Web access publicly available to users who should not
  be allowed any other type of access to your system,
  you are STRONGLY advised to use the -anonymous command-line option:
  if you do not use this option, users may be able to gain access
  to all readable files on your machine!

  Many implementations of telnetd allow passing of environment variables,
  which might be used to modify the environment in anonymous accounts,
  allowing mischief or damage by malicious users, so make sure the wrapper
  uses the -cfg and -homepage switches to specify  lynx.cfg  and start-file,
  rather than relying on variables LYNX_CFG, LYNX_CFG_FILE and WWW_HOME.

-------------------------------------------------------------------------------

II. Compile instructions -- UNIX

1a. Auto-configure.  The auto-configure script uses autoconf2.13 to generate a
    Bourne shell script, configure, which creates "makefile" and "lynx_cfg.h".

    If you are on a UNIX platform, the easiest way to build Lynx is to type:

	    ./configure
    and
	    make

    NOTE:  Configure has a number of useful options.  Please see below.

    NOTE:  The 'configure' script generates auxiliary files "config.status"
    "config.cache" and "config.log".  Normally you will not notice these;
    they are created automatically and removed by a "make distclean".

	+ If you wish to rebuild Lynx with a new host, or change ANY of the
	  parameters which are stored in config.cache, you MUST first remove
	  the config.cache file before running configure; its options do NOT
	  override the settings in that file.

	+ The config.status file is a script which creates (or regenerates)
	  the files created by the configure script.

    Please report problems in the configure/make process by including a copy
    of config.status, config.cache and config.log, as well as the pertinent
    compiler diagnostics.

    See the note in aclocal.m4 for special instructions if you must modify the
    configure script.

    NOTE:  Lynx is a curses-based application, so you must have a curses
    library available to link to.  Native curses (on the system when it was
    installed) are often broken, so you may get superior performance if you
    have either
    
	    "ncurses" ("ftp://ftp.invisible-island.net/ncurses") or
	    "slang"   ("ftp://space.mit.edu/pub/davis/slang").
    
    If you install these libraries in your home directory or a non-default
    location, you may need to set the CPPFLAGS (full path to include files) and
    LIBS (full path to library files) environment variables BEFORE running
    configure.  See "1d.  Environment".  Use the "--with-screen=ncurses" or
    "--with-screen=slang" option.

    Note that while lynx will build with a variety of versions of curses and
    ncurses, some will be less satisfactory.  Versions of ncurses before
    1.9.9g will not render color properly.  Some other versions of curses do
    not display color at all.  Likewise, lynx may not build with old versions
    of slang, e.g., before 0.99-38, because slang's interfaces change
    periodically.

    Note compiler/system specific problems below.  See also:
	https://invisible-island.net/ncurses/ncurses.faq.html

1b. Platforms.  Configure should work properly on any Unix-style system.
    It has been tested on the following platforms.

	AIX 3.2.5 (cc w/ curses)	BeOS 4.5 (gcc w/ ncurses)
	CLIX (cc w/ curses & ncurses)	DGUX
	Digital Unix 3.2C and 4.0 (gcc & cc w/ curses, ncurses & slang)
	FreeBSD 2.1.5, 3.1 (gcc 2.6.3 w/ curses & ncurses)
	HP-UX (K&R and ANSI cc, gcc w/ curses, ncurses & slang)
	IRIX 5.2 and 6.2 (cc & gcc w/ curses, ncurses & slang)
	Linux 2.0.0 (gcc 2.7.2 w/ curses, ncurses & slang)
	MkLinux 2.1.5 (gcc 2.7.2.1)	NetBSD
	NEXTSTEP 3.3 (gcc 2.7.2.3 w/ curses)
	OS/2 EMX 0.9c (ncurses) 	SCO OpenServer (cc w/ curses)
	Solaris 2.5, 2.6 & 2.7 (cc & gcc w/ curses, ncurses & slang)
	SunOS 4.1 (cc w/ curses, gcc w/ ncurses & slang)
	OS390 and BS2000.

    NOTE:  SunOS and HP-UX come with a bundled K&R compiler, which is only
    useful for compiling with the bundled curses.  Both ncurses and slang
    require a compiler that recognizes prototypes.

1c. Options
    To get a list of the configure script's options, type "./configure --help".
    Below is an alphabetical listing of the Lynx-specific options.  The actual
    order shown by the -help option is different.  See "docs/README.defines"
    for information on defines for which there are no option switches.

  --datadir
	Defines the location where you want the documentation files installed.
	The configure script constructs makefile actions to install lynx.cfg
	modified to reflect this in the HELPFILE setting.  (For platforms which
	do not support a configure script, such as MS-DOS, Win32 and VMS, you
	must edit lynx.cfg).

  --disable-addrlist-page		(prevent defining USE_ADDRLIST_PAGE)
	Turn off code that displays an alternative list-page, bound to 'A'
	rather than 'l', which always lists URLs rather than titles.

  --disable-alt-bindings 		(prevent defining USE_ALT_BINDINGS)
	Compiles-in an alternative set of line-edit bindings, in addition
	to the default bindings.

  --disable-bibp-urls			(define DISABLE_BIBP)
	Disable (do not compile code) support for bibp: URLs.

  --disable-color-style			(define USE_COLOR_STYLE)
	Use this option to disable optional color style.  This is implemented
	for modern curses implementations, e.g., those that support color.

	Before lynx 2.8.6dev.18, this option was disabled by default.
	You can achieve a similar color effect to match the non-color-style
	(but still allowing users to use color-style) by using the
	--without-lss-file option.

  --disable-config-info			(define NO_CONFIG_INFO)
  	Use this option to disable extended browsable configuration information
	(a screen that shows the result of the configuration script, as well
	as extended lynx.cfg viewing with a pointer to the lynx.cfg file and
	additional functionality).

  --disable-dired			(prevent defining DIRED_SUPPORT)
	Use this option to disable the optional directory-editor.

	Lynx supports directory editing (DirEd) for local directories.
	This allows users to do things like view, copy and remove files
	using a tabular display of the directory and single-keystroke
	commands instead of using the command line.  From inside Lynx, the
	keystroke sequence "g.<enter>" switches Lynx to DirEd mode on the
	current directory.  If you're building a Lynx that is to be used as
	a kind of restricted shell for users who do not have access to the
	command line and should not have access to equivalent capabilities,
	you probably want to disable DirEd with this option.  You can also
	disable some DirEd functions while allowing others.  If you have
	disabled DirEd completely, you can ignore all the more specific
	DirEd options.

	All DirEd menu functions that were enabled on compilation can be
	disabled or modified at run time via DIRED_MENU symbols in lynx.cfg.

  --disable-dired-dearchive		(define ARCHIVE_ONLY)
	Use this option to prevent DirEd from extracting files from an
	archive file.

  --disable-dired-gzip			(prevent defining OK_GZIP)
	Use this option to prevent DirEd from using gzip and gunzip.

  --disable-dired-override		(prevent defining OK_OVERRIDE)
	Normally, in DirEd directory viewing mode some key mappings are
	overridden.  Use this option to disable DirEd keymap overriding.

  --disable-dired-permit		(prevent defining OK_PERMIT)
	Use this option to prevent DirEd from changing the permissions
	on directories or files (i.e., from doing what the Unix chmod
	command or the DOS attrib command does).

  --disable-dired-tar			(prevent defining OK_TAR)
	Use this option to prevent DirEd from using the tar program.

  --disable-dired-uudecode		(prevent defining OK_UUDECODE)
	Use this option to prevent DirEd from using uudecode.

  --disable-dired-xpermit		(define NO_CHANGE_EXECUTE_PERMS)
	Use this option if you do not disable out the dired-permit
	option, but want to restrict changes of the eXecute permission
	to directories (i.e., not allow it to be changed for files).  If
	you don't do this, you can still block changes of the eXecute
	permission for files but not directories via the
	"change_exec_perms" command line restriction.

  --disable-dired-zip			(prevent defining OK_ZIP)
	Use this option to prevent DirEd from using zip and unzip.

  --disable-echo
  	Use this option to suppress the "compiling" commands during a build.
	Doing this makes it easier to find and read warning messages.

  --disable-extended-dtd		(define NO_EXTENDED_HTMLDTD)
	disable extended HTML DTD logic.  This should revert to old-style
	(2.7.1/2.7.2) behavior, but is not well-tested.

  --disable-file-upload			(define USE_FILE_UPLOAD)
	Compile-in support for form-based file-upload.

  --disable-finger			(define DISABLE_FINGER)
	Do not compile-in code used to connect to "finger" URLs.

  --disable-forms-options		(define NO_OPTION_FORMS)
	Disable the Form-based Options Menu (see --disable-menu-options).
	The default is to compile key-based & form-based Options Menu code,
	allowing users the final choice via FORMS_OPTIONS in lynx.cfg
	or the -forms_options command-line switch.

  --disable-ftp				(define DISABLE_FTP)
	Do not compile-in code used to connect to FTP servers.

  --disable-full-paths
  	Use this option to control whether full pathnames are compiled in for
	various utilities invoked by lynx as external commands.  By default,
	full pathnames are compiled in for the the locations where configure
	finds these commands at configure time.  Affected commands are chmod,
	compress, cp, gzip, install, mkdir, mv, rm, tar, touch, gunzip, unzip,
	bzip2, uudecode, zcat, zip, telnet, tn3270, rlogin.  (Not all of them
	are used on all systems or in all configurations.)

	This option makes Lynx simpler to install, but potentially less secure,
	since the commands are then set in the user's $PATH.  All of these
	commands may also be overridden individually by setting environment
	variables before configuring.  For example, you can disable the telnet
	command by doing this:

		setenv TELNET /bin/false

  --disable-gopher			(define DISABLE_GOPHER)
	Do not compile-in code used to connect to GOPHER servers.

  --disable-idna
	By default, the configure script searches for the GNU idn library,
	which lets lynx translated URLs which are in UTF-8 to ASCII.  The
	latter is needed for most network accesses.  Use this option to
	suppress the feature, e.g., to reduce size.

  --disable-included-msgs
	Do not use included messages, for i18n support.  If NLS support is
	requested, the configure script will otherwise use the messages in the
	./po subdirectory.

  --disable-justify-elts		(define USE_JUSTIFY_ELTS)
	Do not use element-justification logic.

  --disable-largefile			(prevent defining LONG_LIST)

	Use this option to disable the compiler and linker options that
	provide largefile interfaces.

  --disable-locale-charset		(define USE_LOCALE_CHARSET)
  	Use nl_langinfo(CODESET) to determine initial value for display
	charset, overrides character_set value in .lynxrc file.

  --disable-long-list			(prevent defining LONG_LIST)
	Use this option to disable long "ls -l" directory listings (when
	enabled, the actual directory style is configurable from lynx.cfg).

  --disable-menu-options		(define NO_OPTION_MENU)
	Disable the Key-based Options Menu.
	See --disable-forms-options (above) for further details.

  --disable-news			(define DISABLE_NEWS)
	Do not compile-in code used to connect to NNTP (netnews) servers.

  --disable-parent-dir-refs		(define NO_PARENT_DIR_REFERENCE)
  	Use this option to disable "Up-to" parent-links in directory listings.

  --disable-partial			(prevent defining DISP_PARTIAL)
	Turn off code that lets Lynx display parts of a long page while loading
	it.

  --disable-persistent-cookies		(prevent defining USE_PERSISTENT_COOKIES)
	Turn off support for saving cookies to a file, for subsequent reuse.
	Persistent cookie support will use (or create) the file specified by
	the 'COOKIE_FILE' option, or default to ".lynx_cookies" in the home
	directory.  (Currently there is no protection against conflict if
	several lynx sessions are active from the same account).

  --disable-prettysrc			(define USE_PRETTYSRC)
	Turn off support for colorizing the source view of HTML pages.  If
	compiled-in, new source view mode is available with -prettysrc command
	line option.

  --disable-progressbar			(define USE_PROGRESSBAR)
	Turn off support for a "progress bar" which displays at the bottom
	of the screen when doing downloads and other time-consuming (but
	interruptible) processes.  This feature can be selected in the
	options menu.

  --disable-read-eta			(define USE_READPROGRESS)
	Turn off enhanced read-progress message showing ETA (estimated time to
	completion), as well as the amount of time stalled without any data
	transferred.

  --disable-rpath-hack
	The rpath-hack makes it simpler to build programs, particularly with
	the *BSD ports which may have essential libraries in unusual places.
	But it can interfere with building an executable for the base system.
	Use this option in that case.

  --disable-scrollbar			(define USE_SCROLLBAR)
	Turn off support for scrollbar on the right-margin of the screen.
	If you configure with ncurses, this works with the mouse on xterm,
	etc.

  --disable-session-cache		(define USE_CACHE_JAR)
	Turn off support for saving/restoring session information in files.
	Configurable from lynx.cfg

  --disable-sessions			(define USE_SESSIONS)
	Turn off support for sessions, which allows the user to automatically
	save and restore history information.

  --disable-source-cache		(define USE_SOURCE_CACHE)
	Turn off support for caching HTML pages locally,
	in files or in memory.	Configurable from lynx.cfg

  --disable-trace			(define NO_LYNX_TRACE)
	Turn off code that lets you trace internal details of Lynx's operation.
	We recommend that you leave this enabled, since we need this
	information to diagnose problems with either Lynx or the sites to which
	you connect.

  --enable-ascii-ctypes			(define USE_ASCII_CTYPES)
	Compiles-in alternative case-conversion functions which ensure that
	configuration names, etc., are compared in POSIX locale.  This is
	important for operating in some locale such as Turkish.

  --enable-cgi-links			(define LYNXCGI_LINKS)
	Allows lynx to access a cgi script directly without the need for
	a http daemon.

  --enable-change-exec			(define ENABLE_OPTS_CHANGE_EXEC)
  	Allow users to change the execution status within the options screen.
	See EXEC_LINKS and EXEC_SCRIPTS.

  --enable-charset-choice		(define USE_CHARSET_CHOICE)
	Add logic for ASSUMED_DOC_CHARSET_CHOICE and DISPLAY_CHARSET_CHOICE in
	lynx.cfg, allowing user to configure a subset of the compiled-in
	charsets for normal use.

  --enable-cjk				(define CJK_EX)
	Add experimental logic for supporting CJK documents.  (This is not
	necessary for CJK support and may go away in a future release.)

  --enable-debug			(The symbol DEBUG is always defined.)
        Use this option to compile-in support for debugging.
        Note that this flag is ignored if the CFLAGS environment
        variable is set, in that case "-g" (or whatever) has to
        be included in the CFLAGS value to get debugging.
	Autoconf normally adds -g and -O options to CFLAGS if CFLAGS
	was not set, and if the compiler supports those options.

  --enable-default-colors		(define USE_DEFAULT_COLORS)
  	Enable use of default-color background (ncurses/slang).  Either
	configuration supports the use of 'default' for colors even without
	this option.  That is, 'default' is interpreted as white (foreground)
	or black (background) according to the context.  When the default
	colors configuration is built, the actual values for foreground and
	background colors are determined by the terminal.

  --enable-exec-links			(define EXEC_LINKS)
	Allows lynx to execute programs by accessing a link.

  --enable-exec-scripts 		(define EXEC_SCRIPTS)
	Allows lynx to execute programs inferred from a link.

  --enable-externs			(define USE_EXTERNALS)
	Use this option to enable external application support. (See lynx.cfg.)

  --enable-find-leaks			(define LY_FIND_LEAKS)
	Use this option to compile-in logic for testing memory leaks.

  --enable-font-switch			(define EXP_CHARTRANS_AUTOSWITCH)
	Allow Lynx to automatically change the Linux console state (switch
	fonts) according to the current Display Character Set.  (Linux console
	only.  *Use with discretion.*  See docs/README.chartrans.)

  --enable-gnutls-compat		(define USE_GNUTLS_FUNCS)
	When --with-gnutls is used, tell whether to use GNUTLS's OpenSSL
	compatibility library or use GNUTLS's low-level API directly.

  --enable-gzip-help
	Install the lynx help files in gzip'd format [*.gz] to save space.

  --enable-htmlized-cfg
	generate an HTMLized copy of lynx.cfg which will be installed with
	the other help files.

  --enable-internal-links		(define TRACK_INTERNAL_LINKS)
        With `internal links' (links within a document to a location within
        the same document) enabled, Lynx will distinguish between, for example,
        `<A HREF="foo#frag">' and `<A HREF="#frag">' within a document whose
        URL is `foo'.  It may handle such links differently, although practical
        differences would appear only if the document containing them resulted
        from a POST request or had a no-cache flag set.  This feature attempts
        to interpret URL-references as suggested by RFC 2396, and to prevent
        mistaken resubmissions of form content with the POST method.  An
        alternate opinion asserts that the feature could actually result in
        inappropriate resubmission of form content.

  --enable-ipv6         		(define ENABLE_IPV6)
	use IPV6 (with IPV4) logic.

  --enable-japanese-utf8		(define EXP_JAPANESEUTF8_SUPPORT)
	use experimental Japanese UTF-8 logic.

  --enable-kbd-layout			(define EXP_KEYBOARD_LAYOUT)
	Disabled by default, this option allows you to use translation
	tables on the input keystrokes.  Current tables include
		ROT13'd keyboard layout
		JCUKEN Cyrillic, for AT 101-key kbd
		YAWERTY Cyrillic, for DEC LK201 kbd

  --enable-local-docs
	On install, modify link from help-page to point to the local
	doc-directory, e.g., with README files.  Normally this points
	to the current release directory.

  --enable-nested-tables		(define EXP_NESTED_TABLES)
	Extends TRST to format nested tables, as well as be smarter about
	<BR> and <P> tags in table cells.

  --enable-nls				(several definitions)
	use Native Language Support (i.e., gettext).

	This relies upon external programs (msgfmt and xgettext) to format
	the message catalogs:
	
	    + Unless you set the environment variables MSGFMT and XGETTEXT to
	      the full pathnames of these utilities, the configure script will
	      search for the GNU versions of these utilities.
	      
	      It will also search for the GNU version of the corresponding
	      gettext() runtime function.  On some platforms (such as Solaris),
	      this search gives misleading results.

	    + If you set those environment variables to full pathnames, the
	      configure script will warn if they are not the GNU versions of
	      the utilities.

  --enable-nsl-fork			(define NSL_FORK)
	Disabled by default, this allows interruption of NSL requests,
	so that `z' will stop the `look-up' phase of a connection.

  --enable-syslog			(define SYSLOG_REQUESTED_URLS)
	Use this option to log NSL requests via syslog().

  --enable-underlines			(define UNDERLINE_LINKS)
	Use this option to underline links rather than using boldface.

  --enable-vertrace			(define LY_TRACELINE)
	Turn on code that prefixes trace output lines with source filename
	and line number.

  --enable-warnings
	Use this option to turn on GCC compiler warnings.

  --enable-wais
	Use this option to turn on configure check for freeWAIS library.

  --enable-widec
	Use this option to allow the configure script to look for wide-curses
	features.  If you do not specify the option, the configure script
	will look for these features if --with-screen=ncursesw is given.
	For this release of Lynx, we recommend the ncursew library built from
	ncurses 5.5.

  --sysconfdir				(affect LYNX_CFG_FILE)
	Defines the location where you want the lynx.cfg file installed.
	The configure script defines the symbol LYNX_CFG_FILE to correspond
	with the $sysconfdir environment variable.  (For platforms which do not
	support a configure script, such as MS-DOS, Win32 and VMS, you must
	edit userdefs.h if you wish to specify the location of lynx.cfg).

  --with-Xaw3d
	This option allows you to specify the X libraries used if you
	are configuring lynx to use PDCurses on a Unix platform.

  --with-XawPlus
	This option allows you to specify the X libraries used if you
	are configuring lynx to use PDCurses on a Unix platform.

  --with-build-cc=XXX
	If cross-compiling, specify a host C compiler, which is needed to
	compile a utility which generates tables for lynx.
	If you do not give this option, the configure script checks if the
	$BUILD_CC variable is set, and otherwise defaults to gcc or cc.

  --with-build-cpp=XXX
	This is unused by lynx.

  --with-build-cflags=XXX
	If cross-compiling, specify the host C compiler-flags.  You might need
	to do this if the target compiler has unusual flags which confuse the
	host compiler.

  --with-build-cppflags=XXX
	If cross-compiling, specify the host C preprocessor-flags.  You might
	need to do this if the target compiler has unusual flags which confuse
	the host compiler.

  --with-build-ldflags=XXX
	If cross-compiling, specify the host linker-flags.  You might need to
	do this if the target linker has unusual flags which confuse the host
	compiler.

  --with-build-libs=XXX
	If cross-compiling, the host libraries.  You might need to do this if
	the target environment requires unusual libraries.

  --with-bzlib[=XXX]			(define USE_BZLIB)
	Use libbz2 for decompression of some bzip2 files.

	The optional value XXX specifies the directory in which the library
	can be found, and may be either the path of the "lib" directory,
	or one level above.  In either case, the corresponding header files
	are assumed to be in the parallel "include" directory.

  --with-charsets=list			(define ALL_CHARSETS)
 	Limit the number of charsets that are compiled-in to the specified
	list of comma-separated MIME names.

  --with-cfg-file			(define LYNX_CFG_FILE)
	Specify the default configuration file's name.  Use --without-cfg-file
	to force the user to specify the configuration file on the command
	line.  The filename can be overridden by using the LYNX_CFG environment
	variable.

  --with-cfg-path			(define LYNX_CFG_PATH)
	Specify the default configuration file(s) directory search-list.  Use
	--without-cfg-path to limit this to the location of the lynx.cfg file.
	The search-list can be overridden using the LYNX_CFG_PATH environment
	variable.

  --with-curses-dir
	Specify directory under which curses/ncurses is installed.  This
	assumes a standard install, e.g., with an include and lib subdirectory.

  --with-dbmalloc
	use Conor Cahill's dbmalloc library

  --with-destdir=XXX
	set DESTDIR variable in makefiles.  This is prefixed to all directories
	in the actual install, but is not really part of the compiled-in or
	configured directory names.  It is convenient for packaging the
	installed files.  If you do not provide the option, the configure
	script uses your $DESTDIR environment variable.

  --with-dmalloc
	use Gray Watson's dmalloc library

  --with-gnutls[=XXX]			(define USE_SSL, USE_GNUTLS_INCL)
	Use this option to configure with the GNU TLS library.
	See docs/README.ssl for additional information.

	The optional value XXX specifies the directory in which the library
	can be found, and may be either the path of the "lib" directory,
	or one level above.  In either case, the corresponding header files
	are assumed to be in the parallel "include" directory.  The default
	is /usr/local/gnutls.

	See the "--enable-gnutls-compat" option.

  --with-included-gettext
	not supported in this package.  The configure script uses macros which
	are bundled together with more useful features.

	See the "--enable-nls" option.

  --with-libiconv-prefix=DIR
	search for libiconv in DIR/include and DIR/lib

  --with-lss-file{=path}		(define LYNX_LSS_FILE)
	Specify the default style-sheet file's name.  Use --without-lss-file
	to make the default behavior match the non-color-style (if no --lss
	option is given, and no COLOR_STYLE setting is in lynx.cfg).

  --with-mime-libdir=list		(define MIME_LIBDIR)
	Use this option to specify the system directory containing the
	mime.types and mailcap files.

  --with-neXtaw
	This option allows you to specify the X libraries used if you
	are configuring lynx to use PDCurses on a Unix platform.

  --with-nls-datadir=DIR
	Use this option to override the configure script's NLS data directory,
	under which the locale (i.e., language) files are installed.  The
	default value is derived at configure time, and depends on whether GNU
	or native gettext is used.

  --with-nss-compat[=XXX]		(define USE_NSS_COMPAT_INCL)
	Use this option to configure with the NSS library's OpenSSL-compatible
	interface.
	See docs/README.ssl for additional information.

	The optional value XXX specifies the directory in which the library
	can be found, and may be either the path of the "lib" directory,
	or one level above.  In either case, the corresponding header files
	are assumed to be in the parallel "include" directory.

  --with-pkg-config[=XXX]
	Use pkg-config, if available, to tell how to build with certain
	libraries, e.g., openssl and gnutls.  If pkg-config is not used,
	or if those libraries are not known to pkg-config, then the configure
	script will search for the libraries as described in the --with-ssl
	and --with-gnutls options.

	The optional value XXX specifies the pathname for pkg-config, e.g.,
	"/usr/local/bin/pkg-config".

	Note: The pkg-config program is used only if no explicit directory
	parameter is provided for the --with-ssl or --with-gnutls options.

  --with-screen=XXX
	Use this option to select the screen type.  The option value, XXX
	must be one of curses (the default), ncurses, ncursesw, pdcurses or
	slang.  Specifying a screen type causes the configure script to
	look in standard locations for the associated header and library
	files, unless you have preset the $CFLAGS and $LIBS variables.

	--with-screen=ncursesw		(define NCURSES, WIDEC_CURSES)
	--with-screen=ncurses		(define NCURSES)
	--with-screen=pdcurses		(define PDCURSES)
	--with-screen=slang		(define USE_SLANG)

	Note that some systems may have a default curses library which
	does not support color, while on others, ncurses is installed as
	the curses library.  The variant ncursesw is the wide-character
	version of ncurses.  See also the --enable-widec option.

	For the ncurses/ncursesw options, the script also accepts variants
	such as "ncursesw6", which helps it to find a specific ncurses config
	script.

	The pdcurses selection supported by the configure script is a UNIX-only
	library which uses X11.  If you are configuring with DJGPP, the likely
	choice is "curses", since that is how PDCurses is normally installed.

  --with-socks[=XXX]			(define SOCKS)
	Use this option to configure with the socks library.

	The optional value XXX specifies the directory in which the library
	can be found, and may be either the path of the "lib" directory,
	or one level above.  In either case, the corresponding header files
	are assumed to be in the parallel "include" directory.

  --with-socks5[=XXX]			(define USE_SOCKS5, SOCKS)
	Use this option to configure with the socks5 library.

	The optional value XXX specifies the directory in which the library
	can be found, and may be either the path of the "lib" directory,
	or one level above.  In either case, the corresponding header files
	are assumed to be in the parallel "include" directory.

	If you make a SOCKSified lynx, you may have trouble accessing FTP
	servers.  Also, instead of SOCKSifying lynx for use behind a firewall,
	you are better off if you make it normally, and set it up to use a
	proxy server.  You can SOCKSify the proxy server, and it will handle
	all clients, not just Lynx.  If you do SOCKSify lynx, you can turn off
	SOCKS proxy usage via a -nosocks command line switch.

  --with-ssl[=XXX]			(define USE_SSL)
	Use this option to configure with the OpenSSL library, or SSLeay.
	See docs/README.ssl for additional information.

	The optional value XXX specifies the directory in which the library
	can be found, and may be either the path of the "lib" directory,
	or one level above.  In either case, the corresponding header files
	are assumed to be in the parallel "include" directory.

  --with-system-type=XXX
	For testing, override the derived host system-type which is used to
	decide things such as special compiler options.  This is normally
	chosen automatically based on the type of system which you are
	building on.  We use it for testing the configure script.

  --with-textdomain[=XXX]		(define NLS_TEXTDOMAIN)
	Set the NLS textdomain to the given value.  This is normally "lynx".

  --with-zlib[=XXX]			(define USE_ZLIB)
	Use zlib for decompression of some gzip files.

	The optional value XXX specifies the directory in which the library
	can be found, and may be either the path of the "lib" directory,
	or one level above.  In either case, the corresponding header files
	are assumed to be in the parallel "include" directory.

1d. Environment variables
    The configure script looks for programs and libraries in known/standard
    locations.  You can override the behavior of the script by presetting
    environment variables.  If they are set, the script will try to use these
    values rather than computing new ones.  Useful variables include:

	CC - the C compiler.  If you do not override this, configure
		will try to use gcc. For instance, setting CC=cc and
		exporting this value will cause configure to use cc instead.

	CFLAGS - the C compiler options.  These also include C
		preprocessor options (such as -I), since the $CFLAGS and
		$CPPFLAGS variables are maintained separately.

	CPPFLAGS - the C preprocessor options.  For some configuration
		tests, you may need to set both $CFLAGS and $CPPFLAGS if
		you are compiling against header files in nonstandard
		locations.

	LDFLAGS - linker/loader options.

	LIBS - the libraries to be linked, with -L and -l options.  If
		you are linking against libraries in nonstandard locations
		unrelated to the install prefix (that you can specify in
		the configure script) you may have to specify these via
		the $LIBS variable.

    Lynx has compiled-in the pathnames of various programs which it executes.
    Normally the full pathnames are given, rather than the program name
    alone.  These may be preset in the environment by the capitalized version,
    e.g., INSTALL for "install".  The corresponding internal definitions
    are suffixed "_PATH", e.g., "INSTALL_PATH".


-- 1997/7/27 - T. Dickey <dickey@clark.net>

1e. Examples
    If you are compiling Lynx for your personal use and are restricted to your
    home directory, a simple method for building would be to choose some
    directory, say ".lynx", and then type:

	./configure --prefix=~/.lynx --exec-prefix=~/.lynx
    and
	make install

    Now you only need to add "~/.lynx/bin" to your PATH and edit "~/.lynx/lib/
    lynx.cfg" as described above.

    I personally use the following csh shell script to set environment
    variables and configure options rather than type them each time.
	#!/bin/csh -f
	setenv CPPFLAGS "-I$HOME/slang -I$HOME/.usr/include"
	setenv LIBS "-L$HOME/.slang/lib -L$HOME/.usr/lib"
	./configure --exec-prefix=$HOME --bindir=$HOME/.lynx \
		--mandir=$HOME/.usr/man --sysconfdir=$HOME/.usr/lib \
		--with-screen=slang --with-zlib

    CPPFLAGS in this example defines the full path to the slang and zlib
    header files, which are not kept in standard directories.  Likewise, LIBS
    defines the nonstandard locations of libslang.a and libz.a.  Setting the
    option --bindir tells the configure script where I want to install the
    lynx binary; setting --mandir tells it where to put the lynx.1 man page,
    and setting --sysconfdir tells it (while at the same time defining
    LYNX_CFG_FILE) where to put the configuration file "lynx.cfg", when I type
    "make install".  The --with-screen=slang and --with-zlib options are
    explained above.

2. Wais support (optional)
    To add direct WAIS support, get the freeWAIS distribution from
    "ftp://ftp.cnidr.org/pub/NIDR.tools/freewais", and compile it.  The
    compile process will create the libraries you will need, wais.a and
    client.a.  Edit the Makefile in the top level directory and add the
    library locations under the DIRECT WAIS ACCESS heading.  Edit the Makefile
    for the WWW Library in "WWW/Library/Implementation/makefile" to point to
    the include directory for the freewais distribution.  Precompiled
    libraries are available for many platforms if you don't wish to compile
    one yourself.

-------------------------------------------------------------------------------

III. Compile instructions -- VMS

Step 1.  Downloading binary files.
    Lynx must handle all IO as streams, and on VMS, output files are always
    created with Stream_LF format via the C RTL's fopen().  The file headers
    indicate Implied Carriage Control, even when the transfer was in binary
    mode, which can confuse downloading software and cause corruption of
    the file contents.  To deal with this, you should define the symbol
    USE_FIXED_RECORDS as TRUE in userdefs.h and/or lynx.cfg.  This will
    instruct Lynx to correct the header information to indicate FIXED 512
    records, with No Implied Carriage Control.  If Lynx fails to do the
    conversion (because the file wasn't mapped to a binary MIME type) you can
    execute FIXED512.COM externally to correct the header information.  The
    command file uses Joe Meadow's FILE utility, or the SET FILE/ATTRIBUTES
    command on current versions of VMS, to modify the headers.  See the
    comments in FIXED512.COM, userdefs.h and lynx.cfg for more information.

Step 2.  Passive FTP
    If your system requires the PASV FTP code instead of the standard PORT FTP
    code (e.g., to deal with a firewall) then set the FTP_PASSIVE option in
    lynx.cfg

Step 3a.
    Lynx uses the VMS port of gzip for uncompressing streams which have
    Content-Encoding headers indicated compression with gzip or the
    Unix compress.  If you do not have gzip installed on your system
    you can get it from "ftp://ftp.wku.edu/" in the fileserv directory.
    The command Lynx uses to uncompress on VMS is "gzip -d".

    If you are using the SOCKETSHR library, read SOCKETSHR.announce and
    make sure you have defined SOCKETSHR and SOCKETSHR_LIBRARY as explained
    therein.

    A "build.com" and "build-slang.com" script for building Lynx with curses
    or slang is in the top level directory.  All you have to do is type
    "@build" or "@build-slang" and answer its prompt for your system's TCP-IP
    software.  Current choices are:
	   MULTINET (default)
	   UCX
	   WIN_TCP
	   CMU_TCP
	   SOCKETSHR_TCP
	   TCPWARE
    It will autosense whether you have VAXC, DECC or GNUC on VAX or AXP and
    build appropriately.  If a WWWLib already exists for that TCP-IP software,
    it will prompt you for whether you want to rebuild it.  If you want to
    build a WWWLib separately, you can type "@libmake.com" with your default
    directory set to [.WWW.Library.vms] instead doing it via "build.com" in
    the top directory.  You may need to modify "build-slang.com", as described
    in its header, so that it can find slang.olb on your system.  If you have
    both DECC and VAXC, it will use DECC to benefit from the newer and more
    efficient memory management functions.

Step 3b.  (optional compilation method)
    If you have and want to use MMS, read the header of descrip.mms in the
    top directory and be sure you include the appropriate macro definitions
    when you invoke it:

	$ MMS /Macro = (MULTINET=1)		for VAXC - MultiNet
	$ MMS /Macro = (WIN_TCP=1)		for VAXC - Wollongong TCP/IP
	$ MMS /Macro = (UCX=1)			for VAXC - UCX
	$ MMS /Macro = (CMU_TCP=1)		for VAXC - OpenCMU TCP/IP
	$ MMS /Macro = (SOCKETSHR_TCP=1)	for VAXC - SOCKETSHR/NETLIB
	$ MMS /Macro = (TCPWARE=1)		for VAXC - TCPWare TCP/IP

	$ MMS /Macro = (MULTINET=1, DEC_C=1)	for DECC - MultiNet
	$ MMS /Macro = (WIN_TCP=1, DEC_C=1)	for DECC - Wollongong TCP/IP
	$ MMS /Macro = (UCX=1, DEC_C=1)		for DECC - UCX
	$ MMS /Macro = (CMU_TCP=1, DEC_C=1)	for DECC - OpenCMU TCP/IP
	$ MMS /Macro = (SOCKETSHR_TCP=1,DEC_C=1) for DECC - SOCKETSHR/NETLIB
	$ MMS /Macro = (TCPWARE=1, DEC_C=1)	for DECC - TCPWare TCP/IP

	$ MMS /Macro = (MULTINET=1, GNU_C=1)	for GNUC - MultiNet
	$ MMS /Macro = (WIN_TCP=1, GNU_C=1)	for GNUC - Wollongong TCP/IP
	$ MMS /Macro = (UCX=1, GNU_C=1)		for GNUC - UCX
	$ MMS /Macro = (CMU_TCP=1, GNU_C=1)	for GNUC - OpenCMU TCP/IP
	$ MMS /Macro = (SOCKETSHR_TCP=1,GNU_C=1) for GNUC - SOCKETSHR/NETLIB
	$ MMS /Macro = (TCPWARE=1, GNU_C=1)	for GNUC - TCPWare TCP/IP

    If you just type "MMS" it will default to the MULTINET and VAXC
    configuration.  MMS will build the WWW library and Lynx sources, and
    link the executable.  However, not all of the header dependencies are
    specified.  If you are not a developer, and need a clean build, you
    should use build.com instead of the MMS utility.

    If you want SOCKS support on VMS, you must add SOCKS as a compilation
    definition, and the SOCKS library to the link command.  However, instead
    of SOCKSifying Lynx for use behind a firewall, you are better off if you
    build Lynx normally, and set up Lynx to use a proxy server (see below).
    You instead can SOCKSify the proxy server, and it will handle all clients,
    not just Lynx.

-------------------------------------------------------------------------------

IV. Compile instructions -- Win32 (Windows95/98/NT)

Borland C:
---------

Simplified:
----------

Sources:
    Download the current sources (choose a zip-file) from
	https://lynx.invisible-island.net/
    and unzip them into a directory where you will build Lynx.

Compiler:
    Download the Borland C/C++ 5.51 compiler from
	http://forms.embarcadero.com/forms/BCC32CompilerDownload

    This is a file named "freecompilertools.exe".

    Run that to install the compiler, e.g., in
	c:\app\bcc55

    Do not install into a directory with spaces in its name, such as
	c:\program files

Libraries:
    Download these "setup" files from http://gnuwin32.sourceforge.net
	libiconv-1.9.2-1.exe (libiconv)
	libintl-0.14.4.exe (libintl)
	openssl-0.9.8h-1-setup.exe (openssl)
	pdcurses-2.6.exe (pdcurses)
	zlib-1.2.3.exe (zlib)

    Install all of the packages in the same directory, "c:\app\GnuWin32".

    A fix is needed in GnuWin32 include/zconf.h: change line reading
    	#if 1	/* HAVE_UNISTD_H -- this line is updated by ./configure */
    to
    	#ifdef HAVE_UNISTD_H

    Prepare import-libraries using Borland's implib program.  The ".lib"
    files that it uses are a different format than the import libraries
    distributed with GnuWin2.  From Lynx's source directory run
        bcblibs

Environment:
    At this point, the bin-directory for the compiler and for the GnuWin32
    libraries should be in your path.

Building:
    From Lynx's source directory
	cd src\chrtrans
	makew32 clean
	makew32
	cd ..\..
	makew32 clean
	makew32

-------------------------------------------------------------------------------

Detailed:
--------
    The original Win32 port was built with Borland C++ 4.52, but later
    versions reportedly can be used.  Before compiling the Lynx sources, you
    need a curses library, and it is recommended that you have the zlib
    library.  Get pdcurses2.3 from "http://pdcurses.sourceforge.net/".  I
    have modified it so that mouse support is no longer broken for Lynx (see
    "http://www.fdisk.com/doslynx/").  You will want to get zlib from
    "http://www.zlib.net/ ".  Compile these libraries, and
    put them in a convenient place (pdcurses inside the Lynx directory).

    Unpack the latest Lynx source distribution, and make an obj directory
    under the source root to contain the compile output.  Copy in your
    IDE file.  A sample IDE file and helper libraries are available at
    "http://www.fdisk.com/doslynx/wlynx/source/".

    First build the .h files in src\chrtrans using "makew32.bat".  Double
    check for new .tbl files; hand edit in any new ones, and then do "makew32".
    Jump into Borland C++, load the project (IDE file) and compile Lynx.
    Alternately, after compiling the chartrans tables, you can come back to
    the top directory and compile manually, i.e., do "make -f makefile.bcb".

    I also have a binary available at "http://www.fdisk.com/doslynx/".  This
    binary was compiled with pdcurses 2.3, hacked so win32 mouse support works,
    and with zlib, so Lynx can do gzip routines internally.  More hints and
    information can be found in "http://www.fdisk.com/doslynx/lynxport.htm".

-- 1997/10/12 - W. Buttles <lynx-port@fdisk.com>
-- 2010/11/27 - URL's updated by Doug Kaufman <dkaufman@rahul.net>

-------------------------------------------------------------------------------

Cygwin:
    It is possible to compile under the cygwin system, which will allow you to
    use the configure script described above for Unix.  Type, for example,
    "./configure --with-screen=ncurses --with-libz" in a Dos window running the
    cygwin bash$ shell.  You also have the choice of using either pdcurses or
    slang.  You will need a launch program such as sh.exe to call helper
    applications.  Paths may need to be in cygwin style, rather than Windows
    style (e.g., TMPDIR=/cygdrive/d/cygwin/tmp, rather than
    TMPDIR=d:\cygwin\tmp).

Visual C++:
    You must have compiled zlib and PDCurses with the -MT (threaded code)
    option.  This is not the default with zlib (see Makefile.msc).

    Copy into lib the following
	zconf.h
	zlib.h
	zlib.lib

    from the zlib build-tree, and
	curses.h
	pdcurses.lib

    from the PDCurses build-tree.

    Then
	make-msc

    to build lynx.

-------------------------------------------------------------------------------

V. Compile instructions -- 386 DOS

    Compiling for DOS with DJGPP has traditionally been a multistep
    procedure. Now, if you have a full installation of DJGPP you can
    also install using the configure script, just as in the UNIX
    section. This needs to be done under a BASH shell. Use a shell
    script to run configure as in the example at the end of this
    section. Otherwise you can follow the below instructions. The
    multistep procedure for DOS may not be supported in the future
    and use of the configure script is recommended. The information
    about required libraries and unpacking applies to both methods of
    compiling.

    First install the C compiler and its libraries (see readme.1st from
    DJGPP distribution).

    Originally, lynx makefiles come with the initial -O2 optimization
    level. If you experience compilation process too slow due to paging
    to the disk (DPMI server provide virtual memory, when in lack of
    RAM), you may change optimization to -O1 or turn the optimization
    off entirely.

    If using optimization level -O2 or -O3 with older versions of DJGPP
    and GCC, you may need to "stubedit" your "cc1.exe" file to enlarge
    compiler stack size. For instance, if using DJGPP 2.02 and GCC 2.8.1,
    to compile with -O3 optimization, the stub needs to be edited to give
    a larger stack. To do this go into djgpp\lib\gcc-lib\djgpp\2.81 and
    either type the command:
   	 "stubedit cc1.exe bufsize=63k minstack=2M",
    or edit interactively with: "stubedit cc1.exe". Current versions of
    DJGPP and GCC generally work with the standard stack.

    Unpack the source code using a DOS program like UNZIP386.  If you are
    using PKUNZIP to unpack the .zip archive, you must use the -d command
    line switch to restore the directory structure contained in the archive,
    i.e., do "pkunzip -d lynx-cur.zip".  No switch is required if you use
    unzip386 or unzip.  If you are trying to compile the 386DOS port under a
    WinNT DOS shell, be sure to unpack the source with a DOS program so
    that all directories will be adjusted to the DOS 8.3 file format necessary
    for compiling with DJGPP.  Do NOT use Winzip, because that will create
    long filenames that will not be recognized by DJGPP tools.

    If you wish to compile with "USE_ZLIB" (recommended), you must have the
    zlib library.  Get the source from
	    http://www.zlib.net
    and compile it.  Put libz.a in the lib subdirectory of DJGPP, and put
    zlib.h and zconf.h in the include subdirectory.

    In addition to the files in the Lynx distribution, you will need a curses
    package and a TCP package.  You can use PDCurses (available at
    "http://pdcurses.sourceforge.net/") and the DJGPP port of WATTCP.  The
    updated version of WATTCP is known as WATT-32, and is available at
    "http://home.broadpark.no/~gvanem/".  You can also use slang (available at
    "http://www.jedsoft.org/slang/") as your screen library.  You must
    compile these before you go any further.  If you wish to use PDCurses 2.6,
    you need to first apply the following patch:

--- dos/gccdos.mak.ori	2002-01-11 20:11:18.000000000 -0800
+++ dos/gccdos.mak	2003-12-13 21:29:28.000000000 -0800
@@ -40,11 +40,11 @@
 	CFLAGS  = -c -g -Wall -DPDCDEBUG
 	LDFLAGS = -g
 else
-	CFLAGS  = -c -O -Wall
+	CFLAGS  = -c -O2 -Wall
 	LDFLAGS =
 endif

-CPPFLAGS	= -I$(PDCURSES_HOME) -I$(CCINCDIR) -D_NAIVE_DOS_REGS
+CPPFLAGS	= -I$(PDCURSES_HOME) -I$(CCINCDIR) -D_NAIVE_DOS_REGS -DHAVE_STRING_H

 CCFLAGS		= $(CFLAGS) $(CPPFLAGS)

@@ -64,10 +64,10 @@
 all:	$(PDCLIBS) $(DEMOS)

 clean:
 	-del *.o
-	-del curses.lib
-	-del panel.lib
+	-del pdcurses.a
+	-del panel.a

 demos:	$(DEMOS)

@@ -287,33 +287,27 @@
 #------------------------------------------------------------------------

 firework.exe:	firework.o $(LIBCURSES)
-	$(LINK) $(LDFLAGS) -o firework firework.o $(LIBCURSES)
-	$(COFF2EXE) firework
+	$(LINK) $(LDFLAGS) -o firework.exe firework.o $(LIBCURSES)
 	strip $@

 newdemo.exe:	newdemo.o $(LIBCURSES)
-	$(LINK) $(LDFLAGS) -o newdemo newdemo.o $(LIBCURSES)
-	$(COFF2EXE) newdemo
+	$(LINK) $(LDFLAGS) -o newdemo.exe newdemo.o $(LIBCURSES)
 	strip $@

 ptest.exe:	ptest.o $(LIBCURSES) $(LIBPANEL)
-	$(LINK) $(LDFLAGS) -o ptest ptest.o $(LIBCURSES) $(LIBPANEL)
-	$(COFF2EXE) ptest
+	$(LINK) $(LDFLAGS) -o ptest.exe ptest.o $(LIBCURSES) $(LIBPANEL)
 	strip $@

 testcurs.exe:	testcurs.o $(LIBCURSES)
-	$(LINK) $(LDFLAGS) -o testcurs testcurs.o $(LIBCURSES)
-	$(COFF2EXE) testcurs
+	$(LINK) $(LDFLAGS) -o testcurs.exe testcurs.o $(LIBCURSES)
 	strip $@

 tuidemo.exe:	tuidemo.o tui.o $(LIBCURSES)
-	$(LINK) $(LDFLAGS) -o tuidemo tuidemo.o tui.o $(LIBCURSES)
-	$(COFF2EXE) tuidemo
+	$(LINK) $(LDFLAGS) -o tuidemo.exe tuidemo.o tui.o $(LIBCURSES)
 	strip $@

 xmas.exe:	xmas.o $(LIBCURSES)
-	$(LINK) $(LDFLAGS) -o xmas xmas.o $(LIBCURSES)
-	$(COFF2EXE) xmas
+	$(LINK) $(LDFLAGS) -o xmas.exe xmas.o $(LIBCURSES)
 	strip $@


--- dos/pdckbd.c.ori	2002-09-01 00:13:30.000000000 -0800
+++ dos/pdckbd.c	2004-01-19 20:30:02.000000000 -0800
@@ -362,7 +362,7 @@
 		return ((int) (0xb8 << 8));
 	if (ascii == 0xe0 && scan == 0x53 && pdc_key_modifiers & PDC_KEY_MODIFIER_SHIFT) /* Shift Del */
 		return ((int) (0xb9 << 8));
-	if (ascii == 0x00 || ascii == 0xe0)
+	if (ascii == 0x00 || (ascii == 0xe0 && scan != 0x00))
 		return ((int) (scan << 8));
 	return ((int) (ascii));
 }
@@ -522,7 +522,7 @@
 		_watch_breaks();
 #else
 # ifdef GO32
-	(void*)signal(SIGINT,(setting ? SIG_DFL : SIG_IGN));
+/*	(void*)signal(SIGINT,(setting ? SIG_DFL : SIG_IGN)); */
 /*	__djgpp_set_ctrl_c(setting);*/
 	setcbrk(setting);
 # else
--- pdcurses/kernel.c.ori	2002-11-27 03:24:32.000000000 -0800
+++ pdcurses/kernel.c	2003-12-13 21:22:38.000000000 -0800
@@ -27,6 +27,10 @@
 #include <memory.h>
 #endif

+#ifdef HAVE_STRING_H
+#include <string.h>
+#endif
+
 #ifdef UNIX
 #include <defs.h>
 #include <term.h>
--- pdcurses/pdcutil.c.ori	2001-01-10 00:27:22.000000000 -0800
+++ pdcurses/pdcutil.c	2003-12-13 21:24:58.000000000 -0800
@@ -49,7 +49,7 @@
 #  include <limits.h>
 #endif

-#ifdef STDC_HEADERS
+#if defined(STDC_HEADERS) || defined(HAVE_STRING_H)
 #  include <string.h>
 #endif

--- pdcurses/pdcwin.c.ori	2002-05-25 17:13:32.000000000 -0800
+++ pdcurses/pdcwin.c	2003-12-13 21:26:02.000000000 -0800
@@ -27,6 +27,10 @@
 # include <memory.h>
 #endif

+#ifdef HAVE_STRING_H
+#include <string.h>
+#endif
+
 #ifndef HAVE_MEMMOVE
 # define memmove PDC_memmove
 #endif

    If you wish to compile with SSL enabled, you need to get and compile
    OpenSSL. The DJGPP port has been successfully compiled with the
    development version of OpenSSL. DJGPP can compile OpenSSL from the
    standard source distribution (http://www.openssl.org/). See the file
    "INSTALL.DJGPP" in the OpenSSL distribution.

    If you have trouble applying the patches, try using the "patch" program,
    ("http://www.delorie.com/pub/djgpp/current/v2gnu/pat261b.zip").
    To read the Unix man style documentation, use, for example, "less"
    ("http://www.delorie.com/pub/djgpp/current/v2gnu/lss374b.zip").
    Compile or place your compiled PDCurses library in /djgpp/pdcur26, and
    compile or place your compiled WATT-32 library in /djgpp/watt32.  If
    using the SLANG library, put libslang.a in your DJGPP/lib directory and put
    slang.h in your DJGPP/include directory, or in the appropriate directories
    specified by LIBRARY_PATH and INCLUDE_PATH in your DJGPP.ENV file.

    Move to the "lynx2-*/WWW/Library/djgpp" directory.  If compiling with
    PDCurses, do "make".  If using SLANG, do "make -f makefile.sla".  This
    should compile libwww.a.  Next move to the "lynx2-*/src/chrtrans" directory
    and do "make -f makefile.dos" to compile the character tables.  Then move
    to the "lynx2-*/src" directory.  There are three choices for compiling at
    this point.  You can do "make -f makefile.dos" to compile with PDCurses,
    "make -f makefile.wsl" to compile with SLANG, or "make -f makefile.dsl" to
    compile with SLANG and the DJGPP keyhandler.  At the time of this writing,
    it is not clear what the advantages and disadvantages of each version are.
    The PDCurses version has the most experience and allows remapping of ALT
    and Function keys.  The SLANG version seems to have better screen handling.
    It allows mapping of function keys, but not ALT keys.  The SLANG with DJGPP
    keyhandler allows mapping of ALT and Function keys, but has the risk of
    incompatibilities from mixing different programs.

    If you wish to compile with support for internationalization of messages,
    you first need to install the DOS ports of the GNU gettext and libiconv
    packages, available from any DJGPP mirror site.  Then uncomment the lines
    for INTLFLAGS in src/makefile.dsl and in WWW/Library/djgpp/makefile.sla,
    and remove the "#" from the LIBS line in src/makefile.dsl.  Make similar
    changes if using one of the other DOS makefiles.  See the gettext
    documentation for information on creating and using message files for
    different languages.

    If all goes well, you will have a lynx.exe file.  If you have trouble,
    check to be sure djgpp.env is the way it came in the original package.

    To test Lynx_386 you must have a packet driver installed. The simplest
    method is to use a null packet driver that just allows Lynx to start
    up, but doesn't do anything else. One such executable driver has been
    posted, uuencoded, to the lynx-dev mailing list in January 1998,
    but is corrupted in the mailing list archive. You can get this at
    "http://www.ncf.ca/ncf/pda/computer/dos/net/nullpkt.zip". Start the
    dummy packet driver with "nullpkt 0x60", and take it out of memory with
    "nullpkt -u". You can also use slip8250.com. See the CRYNWR package
    "ftp://ftp.simtel.net/pub/simtelnet/msdos/pktdrvr/pktd11.zip". Usage
    is "slip8250 0x60", but you may have to invoke it as, for example,
    "slip8250 0x60 6 3 0x2F8" so that it uses COM2 and IRQ 3, in order to
    avoid an IRQ conflict with a mouse or some other device. Another packet
    driver is slipper.exe, which is available from many sites, including
    "http://www.cavazza.it/file/bbs/intsoft/slippr15.zip". To remove it from
    memory use termin.com (usage "termin 0x60"), available in the CRYNWR
    package. To connect over a dialup PPP connection you need dosppp or klos'
    pppshare. (Find at:
    "http://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/net/dosppp/dosppp06.zip"
    "http://www.ncf.carleton.ca/ncf/pda/computer/dos/net/dosppp06.zip"
    "http://www.cavazza.it/file/bbs/intsoft/dosppp06.zip"
    "http://www.cavazza.it/file/bbs/intsoft/pppshare.exe")

    File access looks like this:

    file:///c:/
    file:///c:/dos
    file:///c:/dos/command.com
    file://localhost/c:/
    file://localhost/c:/dos
    file://localhost/c:/dos/command.com

    See "http://www.fdisk.com/doslynx/lynxport.htm" for more hints and
    some precompiled libraries. One problem you can encounter is editing
    userdefs.h and lynx.cfg, which have unix-style end of lines. You would
    be well advised to use an editor that can handle end of lines terminated
    with a single LF character. You can also unpack the source code using
    unzip386 or unzip with the -a or -aa switch to convert unix LF to dos CRLF.
    That will make texts more readable under DOS. If you compile lynx
    regularly, you may automate the procedure by creating a batch file such
    as the following.

	cd djgpp\watt32\src
	configur djgpp
	make -f djgpp.mak
	cd ..\..\..\www\library\djgpp
	make
	cd ..\..\..\src\chrtrans
	make -f makefile.dos
	cd ..\..\src
	make -f makefile.dos
	strip lynx.exe
	cd ..

    This batch file expects the DJGPP port of WATT-32 to be installed in the
    lynx2-* directory.  Place a copy of this batch file, named "djgpp.bat",
    in the lynx2-* directory, move to that directory and type "djgpp".  A more
    complete batch file with error checking and annotation can be found at:
    "http://lists.nongnu.org/archive/html/lynx-dev/1997-11/msg00250.html".

    If you use the configure method, remember that if you configure with
    the option "--enable-nls", you also need to set LIBS="-liconv". A
    sample shell script to run configure using PDCurses follows. If you
    compile to use SLANG, note that the DJGPP keyhandler will be used
    instead of the SLANG keyhandler unless you define "NO_DJ_KEYHANDLER".

    #!/bin/sh
    CFLAGS="-O2 -I/djgpp/pdcur26 -I/djgpp/watt32/inc" \
    LIBS="-L/djgpp/pdcur26/lib -L/djgpp/watt32/lib -liconv" \
    ./configure --prefix=d:/djgpp/lynx-rel/lynx-cnf \
    --with-screen=curses \
    --disable-full-paths \
    --enable-addrlist-page \
    --enable-change-exec \
    --enable-cgi-links \
    --enable-charset-choice \
    --enable-color-style \
    --enable-exec-links \
    --enable-externs \
    --enable-file-upload \
    --enable-nested-tables \
    --enable-nls \
    --sysconfdir=d:/djgpp/lynx-rel/lynx-cnf \
    --with-bzlib \
    --with-zlib \
    --with-ssl

-- 1997/9/29 - D. Kaufman <dkaufman@rahul.net>
-- 1997/10/3 - B. Schiavo <Wschiavo@concentric.net>
-- Last update - 2010/11/27

-------------------------------------------------------------------------------

VI. General installation instructions

    Once you have compiled Lynx, test it out first on a local file.  Be sure
    Lynx can find lynx.cfg.  A _sample_ test command line would be:
    'lynx -cfg=/usr/local/lib/lynx.cfg .'.  Once you are satisfied that
    Lynx works, go ahead and install it.  For Unix, type "make install".

    For VMS, you need to have the executable in a public place, make it
    accessible, define it as a foreign command, and copy lynx.cfg to
    "Lynx_Dir".  Look at lynx.com in the samples directory as a model for
    installing Lynx.  To include lynx.hlp in the system HELP library, use
    the command: "$ library/replace sys$help:helplib.hlb lynx.hlp".

    Local copies of the Lynx online help should be made accessible in response
    to the Lynx 'h'elp command by defining HELPFILE in userdefs.h and/or
    lynx.cfg to an appropriate file://localhost/path URL.  On Unix, all you
    need to do is type "make install-help."  If you are installing manually,
    copy the files "COPYHEADER" and "COPYING" into the lynx_help directory
    BEFORE moving the lynx_help tree to its final location.  These files are
    referenced hypertextually from help documents.

    If you have old, pre-existing bookmark files from earlier versions of
    Lynx, those files may have to be updated.  Conversion may just consist
    of adding one META line near the top, or may require creating new book-
    mark files and editing in bookmarks from outdated files.

    IMPORTANT!  Be sure you have read the warnings about setting up an
    anonymous account with Lynx if you plan to give public access to Lynx.

    After applying patches or editing files to correct for an unsuccessful
    build, be certain to do a "make clean" (or "make distclean" for those
    using auto-configure) before attempting to compile again.

-------------------------------------------------------------------------------

VII. Setting environment variables before running Lynx (optional)

1. All ports

   The Lynx Users Guide describes all of the environment variables used by
   Lynx.  This should be checked later along with reading lynx.cfg after you
   have installed Lynx.

2. Win32 (95/98/NT) and 386 DOS

    These ports cannot start before setting certain environment variables.
    Here are some environment variables that should be set, usually in a
    batch file that runs the lynx executable.  Make sure that you have enough
    room left in your environment.  You may need to change your "SHELL="
    setting in config.sys.  In addition, lynx looks for a "SHELL" environment
    variable when shelling to DOS.  If  you wish to preserve the environment
    space when shelling, put a line like this in your AUTOEXEC.BAT file also
    "SET SHELL=C:\COMMAND.COM /E:4096".  It should match CONFIG.SYS.

    HOME         Where to keep the bookmark file and personal config files.
    TEMP or TMP  Bookmarks are kept here with no HOME.  Temp files here.
    USER         Set to your login name (optional)
    LYNX_CFG     Set to the full path and filename for lynx.cfg
    LYNX_LSS     Set to the full path and filename for lynx.lss
    LYNX_SAVE_SPACE  The (modifiable) location for downloaded file storage.
    SSL_CERT_FILE Set to the full path and filename for your file of trusted
                  certificates

    386 version only:
    WATTCP.CFG   Set to the full path for the WATTCP.CFG directory
    RL_CLCOPY_CMD Command to copy a URL to a "clipboard" file
    RL_PASTE_CMD  Command to go to a URL in your "clipboard" file

    Define these in your batch file for running Lynx.  For example, if your
    application line is "D:\win32\lynx.bat", lynx.bat for Win32 may look like:
	@ECHO OFF
	set home=d:\win32
	set temp=d:\tmp
	set lynx_cfg=d:\win32\lynx.cfg
	set lynx_save_space=d:\download
	d:\win32\lynx.exe %1 %2 %3 %4 %5

    For lynx_386, a typical batch file might look like:

	@echo off
	set HOME=f:/lynx2-8
	set USER=your_login_name
	set LYNX_CFG=%HOME%/lynx.cfg
	set WATTCP.CFG=%HOME%
	f:\lynx2-8\lynx %1 %2 %3 %4 %5 %6 %7 %8 %9

    You need to make sure that the WATTCP.CFG file has the correct information
    for IP number, Gateway, Netmask, and Domain Name Server.  This can also be
    automated in the batch file.

    Adapted from "readme.txt" by Wayne Buttles and "readme.dos" by Doug
    Kaufman.

VIII. Acknowledgment

   Thanks to the many volunteers who offered suggestions for making this
   installation manual as accurate and complete as possible.

-- 1999/04/24 - H. Nelson <lynx-admin@irm.nara.kindai.ac.jp>
-- vile:txtmode
-- $LynxId: INSTALLATION,v 1.130 2018/07/08 15:22:44 tom Exp $
