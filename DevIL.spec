Summary:	Full featured image library
Summary(pl.UTF-8):	Biblioteka obsługi obrazów z mnóstwem funkcji
Name:		DevIL
Version:	1.7.2
%define		manual_version	1.5.5
%define		docs_version	1.6.5
Release:	3
License:	LGPL v2.1
Group:		Libraries
Source0:	http://dl.sourceforge.net/openil/%{name}-%{version}.tar.gz
# Source0-md5:	67d669df245c846ec9f54dfc086a00b6
Source1:	http://dl.sourceforge.net/openil/%{name}-Manual-%{manual_version}.zip
# Source1-md5:	6bb2ddfcbe09930c48ef84b8f99479fe
Source2:	http://dl.sourceforge.net/openil/%{name}-docs.tar.gz
# Source2-md5:	eec6ae7a028a3f058bab1a6918428ed5
Patch0:		%{name}-c++.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-gnu-inline.patch
URL:		http://openil.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	allegro-devel >= 4.1.16
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	jasper-devel
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	unzip
BuildRequires:	which
Requires:	allegro >= 4.1.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Developer's Image Library (DevIL) is a programmer's library to develop
applications with very powerful image loading capabilities, yet is
easy for a developer to learn and use. Ultimate control of images is
left to the developer, so unnecessary conversions, etc. are not
performed. DevIL utilizes a simple, yet powerful, syntax. DevIL can
load, save, convert, manipulate, filter and display a wide variety of
image formats.

Currently, DevIL can load .bmp, .cut, .dds, .doom, .gif, .ico, .icns,
.jp2, .jpg, .lbm, .mdl, .mng, .pal, .pbm, .pcd, .pcx, .pgm, .pic,
.png, .ppm, .psd, .psp, .raw, .sgi, .tga and .tif files.

Formats supported for saving include .bmp, .dds, .h, .jpg, .pal, .pbm,
.pcx, .pgm, .png, .ppm, .raw, .sgi, .tga and .tif.

%description -l pl.UTF-8
Developer's Image Library (DevIL) jest biblioteką programisty
pozwalającą tworzyć aplikacje z potężnymi możliwościami ładowania
obrazów. Pozostaje przy tym łatwa w użyciu i prosta do nauczenia się.
Ostateczna kontrola nad obrazami jest zostawiona programiście, nie
wprowadza się niepotrzebnych konwersji, itp. DevIL używa prostej, lecz
potężnej składni poleceń, wzorowanej na OpenGL-u. DevIL potrafi
ładować, zapisywać, konwertować, manipulować, filtrować szeroki
wachlarz formatów plików graficznych.

W chwili obecnej DevIL odczytuje pliki z rozszerzeniami bmp, cut, dds,
doom, gif, icns, ico, jp2, jpg, lbm, mdl, mng, pal, pbm, pcd, pcx,
pgm, pic, png, ppm, psd, psp, raw, sgi, tga i tif.

Wspierane jest zapisywanie do plików bmp, dds, h, jpg, pal, pbm, pcx,
pgm, png, ppm, raw, sgi, tga i tif.

%package devel
Summary:	DevIL devel files
Summary(pl.UTF-8):	Nagłówki DevIL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	jasper-devel
Requires:	lcms-devel
Requires:	libjpeg-devel
Requires:	libmng-devel
Requires:	libpng-devel
Requires:	libtiff-devel
# libILUT additionally: SDL-devel, allegro-devel, OpenGL-GLU-devel

%description devel
DevIL devel files.

%description devel -l pl.UTF-8
Nagłówki DevIL.

%package doc
Summary:	DevIL documentation
Summary(pl.UTF-8):	Dokumentacja DevIL
Group:		Documentation

%description doc
DevIL documentation.

%description doc -l pl.UTF-8
Dokumentacja DevIL.

%prep
%setup -q -c -a1 -a2
%patch0 -p1
%patch1 -p1
%patch2 -p1

# just SDL and messing libtool macros
rm -f acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# actual exr support missing in sources, only adds undefined symbol
CPPFLAGS="%{rpmcppflags} -DIL_NO_EXR"
%configure \
	%{?debug:--disable-release}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog README.unix
%attr(755,root,root) %{_libdir}/libIL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIL.so.1
%attr(755,root,root) %{_libdir}/libILU.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libILU.so.1
%attr(755,root,root) %{_libdir}/libILUT.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libILUT.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libIL.so
%attr(755,root,root) %{_libdir}/libILU.so
%attr(755,root,root) %{_libdir}/libILUT.so
%{_libdir}/libIL.la
%{_libdir}/libILU.la
%{_libdir}/libILUT.la
%{_includedir}/IL

%files doc
%defattr(644,root,root,755)
%doc DevIL*.pdf
