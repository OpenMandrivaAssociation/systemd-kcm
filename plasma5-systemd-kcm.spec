%define oname systemd-kcm

Summary:	Plasma 5 systemd control module
Name:		plasma5-%{oname}
Version:	1.1.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://github.com/rthomsen/kcmsystemd
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{oname}/%{oname}-%{version}.tar.xz
Patch0:		kcmsystemd-1.1.0-kdesu-path.patch
Patch1:		kcmsystemd-1.1.0-systemd-journal.patch
Patch2:		kcmsystemd-1.1.0-desktop-localization.patch
BuildRequires:	extra-cmake-modules
BuildRequires:	boost-devel
BuildRequires:	kf5auth-devel
BuildRequires:	kf5configwidgets-devel
BuildRequires:	kf5coreaddons-devel
BuildRequires:	kf5i18n-devel
BuildRequires:	pkgconfig(libsystemd-journal)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
Conflicts:	kcmsystemd

%description
Plasma 5 systemd control module.

%files -f kcmsystemd.lang
%{_kde5_services}/kcm_systemd.desktop
%{_kde5_libexecdir}/kauth/kcmsystemdhelper
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmsystemd.service
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmsystemd.policy
%{_qt5_plugindir}/kcm_systemd.so
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmsystemd.conf

#----------------------------------------------------------------------------

%prep
%setup -qn kcmsystemd-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%cmake_kde5
%make

%install
%makeinstall_std -C build

# We ship it in plasma5-systemsettings package
rm -rf %{buildroot}%{_kde5_services}/settings-system-administration.desktop

%find_lang kcmsystemd

