Summary:	Plasma 5 systemd control module
Name:		systemd-kcm
Version:	1.2.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://github.com/rthomsen/kcmsystemd
Source0:	http://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Patch0:		systemd-kcm-1.2.0-add-libsystemd-journal-link.patch
BuildRequires:	cmake(ECM)
BuildRequires:	boost-devel
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libsystemd-journal)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
Obsoletes:	kcmsystemd < 0.8.0
Provides:	kcmsystemd = 0.8.0

%description
Plasma 5 systemd control module.

%files -f systemd-kcm.lang
%{_kde5_services}/kcm_systemd.desktop
%{_kde5_services}/settings-system-administration.desktop
%{_kde5_libexecdir}/kauth/kcmsystemdhelper
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmsystemd.service
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmsystemd.policy
%{_qt5_plugindir}/kcm_systemd.so
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmsystemd.conf

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang systemd-kcm

