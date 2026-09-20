Name:           qt6gtk2
Version:        0.7
Release:        1
Summary:        GTK+2.0 integration plugins for Qt6
License:        GPL-2.0-or-later
Group:          System/Libraries
URL:            https://www.opencode.net/trialuser/qt6gtk2
Source0:        https://www.opencode.net/trialuser/qt6gtk2/-/archive/%{version}/qt6gtk2-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  qmake-qt6
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)

# Disable debugsource subpackage generation for this package.
%undefine _debugsource_packages

%description
Qt 6 plugin for better integration with gtk-based desktop enviroments.

%prep
%autosetup -p1

%build
qmake-qt6 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%dir %{_libdir}/qt6/plugins/platformthemes/
%{_libdir}/qt6/plugins/platformthemes/libqt6gtk2.so
%dir %{_libdir}/qt6/plugins/styles/
%{_libdir}/qt6/plugins/styles/libqt6gtk2-style.so
