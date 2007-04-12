Name: openssh-askpass-qt
Version:	0.2
Release:	%mkrel 1
Summary:	Qt version of ssh auth agent for keychain
License:	GPL
Group: System/
BuildRequires: libqt-devel
URL: http://www.mandriva.com
Source: %name-%version.tar.bz2
Buildroot: %_tmppath/%name-buildroot
Requires: openssh-askpass-common
Provides: openssh-askpass
Provides: ssh-askpass
Provides: ssh-extras

%description
Qt version of ssh auth agent for keychain

%files 
%defattr(0755,root,root,755)
%_libdir/ssh/qt-ssh-askpass

#-----------------------------------------------------------------------------

%prep
%setup -q

%build
qmake qt-ssh-askpass.pro

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



