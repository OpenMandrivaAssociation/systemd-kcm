%define oname systemd-kcm

Summary:	Plasma 5 systemd control module
Name:		plasma5-%{oname}
Version:	1.1.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://github.com/rthomsen/kcmsystemd
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{oname}/%{oname}-%{version}.tar.xz
Patch0:		kcmsystemd-1.1.0-systemd-journal.patch
BuildRequires:	cmake(ECM)
BuildRequires:	boost-devel
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	pkgconfig(libsystemd-journal)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
Obsoletes:	kcmsystemd < 0.8.0
Provides:	kcmsystemd = 0.8.0

%description
Plasma 5 systemd control module.

%files -f kcmsystemd.lang
%{_kde5_services}/kcm_systemd.desktop
%{_kde5_services}/settings-system-administration.desktop
%{_kde5_libexecdir}/kauth/kcmsystemdhelper
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmsystemd.service
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmsystemd.policy
%{_qt5_plugindir}/kcm_systemd.so
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmsystemd.conf

#----------------------------------------------------------------------------

%prep
%setup -qn kcmsystemd-%{version}
%patch0 -p1
%cmake_kde5

%build
%ninja

%install
%ninja_install -C build

%find_lang kcmsystemd
