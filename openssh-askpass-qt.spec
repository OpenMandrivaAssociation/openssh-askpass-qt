Summary:	QT passphrase dialog for OpenSSH
Name:		openssh-askpass-qt
Version:	0.2
Release:	18
License:	GPLv2
Group:		Graphical desktop/KDE
Url:		%{disturl}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.2-fix-exit-status.patch
BuildRequires:	pkgconfig(qt-mt)
Requires:	openssh-askpass-common
Provides:	openssh-askpass
Provides:	ssh-askpass
Provides:	ssh-extras
Requires(post,postun): update-alternatives

%description
Qt version of ssh passphrase dialog.

%files 
%{_libdir}/ssh/qt-ssh-askpass

#-----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
export QTDIR=%{_prefix}/lib/qt3
export PATH=$QTDIR/bin:$PATH
%{qt3dir}/bin/qmake qt-ssh-askpass.pro

%make

%install
mkdir -p %{buildroot}/%{_sysconfdir}/profile.d/
mkdir -p %{buildroot}/%{_libdir}/ssh
install -m 755 qt-ssh-askpass %{buildroot}/%{_libdir}/ssh/qt-ssh-askpass

%post
update-alternatives --install %{_libdir}/ssh/ssh-askpass ssh-askpass %{_libdir}/ssh/qt-ssh-askpass 30
update-alternatives --install %{_bindir}/ssh-askpass bssh-askpass %{_libdir}/ssh/qt-ssh-askpass 30

%postun
[ $1 = 0 ] || exit 0
update-alternatives --remove ssh-askpass %{_libdir}/ssh/qt-ssh-askpass
update-alternatives --remove bssh-askpass %{_libdir}/ssh/qt-ssh-askpass

