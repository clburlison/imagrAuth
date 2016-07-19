# otool -L /usr/bin/ldapsearch
#################################################
PKGTITLE="ldapsearch_NetInstall_Frameworks"
PKGVERSION=1.0
PKGID=com.clburlison.ldapsearch_NetInstall_Frameworks

pkg:

##Help - Show this help menu
help: 
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

##  copy - copy frameworks
copy:
	mkdir -p payload/System/Library/Frameworks
	mkdir -p payload/System/Library/PrivateFrameworks
	mkdir -p payload/usr/lib
	cp -rf /System/Library/Frameworks/CoreFoundation.framework payload/System/Library/Frameworks
	cp -rf /System/Library/Frameworks/Security.framework payload/System/Library/Frameworks
	cp -rf /System/Library/Frameworks/SystemConfiguration.framework payload/System/Library/Frameworks
	cp -rf /System/Library/Frameworks/IOKit.framework payload/System/Library/Frameworks
	cp -rf /System/Library/PrivateFrameworks/Heimdal.framework payload/System/Library/Frameworks
	cp -rf /System/Library/Frameworks/OpenDirectory.framework payload/System/Library/Frameworks
	cp -rf /System/Library/PrivateFrameworks/HeimODAdmin.framework payload/System/Library/PrivateFrameworks
	cp -rf /System/Library/PrivateFrameworks/CommonAuth.framework payload/System/Library/PrivateFrameworks
	cp -rf /System/Library/PrivateFrameworks/PasswordServer.framework payload/System/Library/PrivateFrameworks
	cp -rf /System/Library/PrivateFrameworks/AccountPolicy.framework payload/System/Library/PrivateFrameworks
	cp -rf /System/Library/PrivateFrameworks/CoreDaemon.framework payload/System/Library/PrivateFrameworks
	cp -rf /usr/lib/libsasl2.2.dylib payload/usr/lib
	cp -rf /usr/lib/libresolv.9.dylib payload/usr/lib
	cp -rf /usr/lib/libSystem.B.dylib payload/usr/lib

##  pkg - Create a package using pkgbuild
pkg: copy
	pkgbuild --root payload --identifier ${PKGID} --version ${PKGVERSION} --ownership recommended ./${PKGTITLE}-${PKGVERSION}.pkg
