%global  kf_version 6.6.0

Name: kf6-kunitconversion
Version: 6.6.0
Release: 0%{?dist}
Summary: Provides functions to convert values in different physical units
License: LGPLv2+
URL:     https://invent.kde.org/frameworks/kcalendarcore
Source0: %{name}-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  kf6-extra-cmake-modules >= %{majmin_ver_kf6}
BuildRequires:  kf6-rpm-macros
BuildRequires:  make


BuildRequires: kf6-kconfig-devel >= %{majmin_ver_kf6}
BuildRequires: kf6-ki18n-devel

BuildRequires: pkgconfig(libical)

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qttools-devel
BuildRequires: qt6-qtdeclarative-devel

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
%{summary}.
It supports converting different prefixes (e.g. kilo, mega, giga) as well as
converting between different unit systems (e.g. liters, gallons).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang kunitconversion6

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kunitconversion6.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6UnitConversion.so.*

%files devel
%{_kf6_includedir}/KUnitConversion/
%{_kf6_libdir}/cmake/KF6UnitConversion/
%{_kf6_libdir}/libKF6UnitConversion.so
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch
