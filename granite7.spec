# TODO: use gtk4-update-icon-cache
Summary:	An extension of GTK 4
Summary(pl.UTF-8):	Rozszerzenie GTK 4
Name:		granite7
Version:	7.4.0
Release:	1
License:	GPL v3
Group:		X11/Libraries
#Source0Download: https://github.com/elementary/granite/releases
Source0:	https://github.com/elementary/granite/archive/%{version}/granite-%{version}.tar.gz
# Source0-md5:	df9f6f02220ed527f38c0a7ca173169b
URL:		http://elementaryos.org/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk4-devel >= 4.4
BuildRequires:	libgee-devel >= 0.8
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	vala >= 2:0.48
BuildRequires:	vala-libgee >= 0.8
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.50
Requires:	gtk4 >= 4.4
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Granite is an extension of GTK. Among other things, it provides the
commonly-used widgets such as modeswitchers, welcome screens,
AppMenus, search bars, and more found in elementary apps.

%description -l pl.UTF-8
Granite to rozszerzenie GTK. Dostarcza między innymi takie popularne
widżety, jak przełączniki trybów, ekrany powitalne, AppMenu, paski
wyszukiwania i inne, jakie można spotkać w aplikacjach elementary.

%package devel
Summary:	Header files for libgranite
Summary(pl.UTF-8):	Pliki nagłówkowe libgranite
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.50
Requires:	gtk4-devel >= 4.4

%description devel
This package contains the header files for libgranite.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe libgranite.

%package -n vala-granite7
Summary:	Vala API for libgranite library
Summary(pl.UTF-8):	API języka Vala do biblioteki libgranite
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.48
Requires:	vala-libgee >= 0.8
BuildArch:	noarch

%description -n vala-granite7
Vala API for libgranite library.

%description -n vala-granite7 -l pl.UTF-8
API języka Vala do biblioteki libgranite.

%prep
%setup -q -n granite-%{version}

%build
%meson \
	--default-library=shared \
	-Ddocumentation=true

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

# not supported(?)
%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48@2

# not supported by glibc (as of 2.37)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ie,rue,sma}

%find_lang granite-7

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%update_icon_cache hicolor

%files -f granite-7.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/granite-7-demo
%attr(755,root,root) %{_libdir}/libgranite-7.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgranite-7.so.7
%{_libdir}/girepository-1.0/Granite-7.0.typelib
%{_datadir}/metainfo/granite-7.metainfo.xml
%{_desktopdir}/io.elementary.granite-7.demo.desktop
%{_iconsdir}/hicolor/48x48/apps/io.elementary.granite-7.svg

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgranite-7.so
%{_includedir}/granite-7
%{_datadir}/gir-1.0/Granite-7.0.gir
%{_pkgconfigdir}/granite-7.pc

%files -n vala-granite7
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/granite-7.deps
%{_datadir}/vala/vapi/granite-7.vapi
