Name: openssh-askpass-qt
Version: 0.2
Release: %mkrel 10
Summary: QT passphrase dialog for OpenSSH
License: GPL
Group: Graphical desktop/KDE
BuildRequires: libqt-devel
URL: http://www.mandriva.com/
Source: %name-%version.tar.bz2
Patch0: %name-0.2-fix-exit-status.patch
Buildroot: %_tmppath/%name-buildroot
Requires: openssh-askpass-common
Provides: openssh-askpass
Provides: ssh-askpass
Provides: ssh-extras

%description
Qt version of ssh passphrase dialog.

%files 
%defattr(0755,root,root,755)
%_libdir/ssh/qt-ssh-askpass

#-----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
export QTDIR=%{_prefix}/lib/qt3
export PATH=$QTDIR/bin:$PATH
%qt3dir/bin/qmake qt-ssh-askpass.pro

%make

%install
mkdir -p %buildroot/%_sysconfdir/profile.d/
mkdir -p %buildroot/%_libdir/ssh
install -m 755 qt-ssh-askpass %buildroot/%_libdir/ssh/qt-ssh-askpass

%post
update-alternatives --install %_libdir/ssh/ssh-askpass ssh-askpass %_libdir/ssh/qt-ssh-askpass 30
update-alternatives --install %_bindir/ssh-askpass bssh-askpass %_libdir/ssh/qt-ssh-askpass 30

%postun
[ $1 = 0 ] || exit 0
update-alternatives --remove ssh-askpass %_libdir/ssh/qt-ssh-askpass
update-alternatives --remove bssh-askpass %_libdir/ssh/qt-ssh-askpass

%clean
rm -rf %buildroot





%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2-9mdv2011.0
+ Revision: 666967
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-8mdv2011.0
+ Revision: 607023
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-7mdv2010.1
+ Revision: 523542
- rebuilt for 2010.1

* Sun Sep 27 2009 Olivier Blin <oblin@mandriva.com> 0.2-6mdv2010.0
+ Revision: 450187
- add missing #include cstdlib in the exit patch
  (from Arnaud Patard)
- add qt3 path in required environment variables (from Arnaud Patard)
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 03 2007 Gustavo De Nardin <gustavodn@mandriva.com> 0.2-3mdv2008.1
+ Revision: 114491
- added a patch to fix askpass exit status, which must be >0 when the user cancels
- little more clear summary and description
- fixed qmake call in build

* Fri Aug 24 2007 Helio Chissini de Castro <helio@mandriva.com> 0.2-2mdv2008.0
+ Revision: 70892
- Rebuild to 2008.0


* Thu Jul 27 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-07-27 16:23:34 (42304)
- Fixed form text
- Removed profiles
- Requires new openssh-askpass-common

* Wed Jul 26 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-07-26 20:56:18 (42214)
- import openssh-askpass-qt-0.1-1mdv2007.0

* Wed Jul 26 2006 Helio Castro <helio@mandriva.com> 0.1-1mdv2007.0
- First version os a Qt askpass for ssh-agent and keychain

