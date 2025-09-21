Summary:	Full featured image library
Summary(pl.UTF-8):	Biblioteka obsługi obrazów z mnóstwem funkcji
Name:		DevIL
Version:	1.8.0
Release:	3
License:	LGPL v2.1
Group:		Libraries
Source0:	http://downloads.sourceforge.net/openil/%{name}-%{version}.tar.gz
# Source0-md5:	4d8c21aa4822ac86d77e44f8d7c9becd
Patch0:		%{name}-cmake.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-ILUT.patch
Patch3:		%{name}-jasper3.patch
URL:		http://openil.sourceforge.net/
BuildRequires:	OpenEXR-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	allegro-devel >= 4.1.16
BuildRequires:	cmake >= 2.6
BuildRequires:	jasper-devel >= 3
BuildRequires:	lcms2-devel >= 2
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	squish-devel
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	xorg-lib-libXext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

Obsługiwane jest zapisywanie do plików bmp, dds, h, jpg, pal, pbm,
pcx, pgm, png, ppm, raw, sgi, tga i tif.

%package devel
Summary:	DevIL development files
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek DevIL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenEXR-devel
Requires:	jasper-devel >= 3
Requires:	lcms-devel
Requires:	libjpeg-devel
Requires:	libmng-devel
Requires:	libpng-devel
Requires:	libtiff-devel
Requires:	squish-devel
Obsoletes:	DevIL-static < 1.8

%description devel
DevIL development files (for IL and ILU libraries).

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek DevIL (IL i ILU).

%package ILUT
Summary:	DevIL ILUT library
Summary(pl.UTF-8):	Biblioteka DevIL ILUT
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL >= 1.2.5
Requires:	allegro >= 4.1.16

%description ILUT
DevIL ILUT library - connection to higher level libraries.

%description ILUT -l pl.UTF-8
Biblioteka DevIL ILUT - łącznik z bibliotekami wyższego poziomu.

%package ILUT-devel
Summary:	Development files for DevIL ILUT library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki DevIL ILUT
Group:		Development/Libraries
Requires:	%{name}-ILUT = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	SDL-devel >= 1.2.5
Requires:	allegro-devel >= 4.1.16
Requires:	xorg-lib-libXext-devel
Obsoletes:	DevIL-ILUT-static < 1.8

%description ILUT-devel
Development files for DevIL ILUT library.

%description ILUT-devel -l pl.UTF-8
Pliki programistyczne biblioteki DevIL ILUT.

%package doc
Summary:	DevIL documentation
Summary(pl.UTF-8):	Dokumentacja DevIL
Group:		Documentation
BuildArch:	noarch

%description doc
DevIL documentation.

%description doc -l pl.UTF-8
Dokumentacja DevIL.

%prep
%setup -q -n DevIL
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
# although there is configure.ac, but it misses some auxiliary files (m4/*)
# and Makefile.am files are outdated (refer to no longer existing *.c files)
install -d DevIL/build
cd DevIL/build
%cmake ..

# info is not covered by CMakeLists
cd ../docs
# missing file
cat >version.texi <<EOF
@set UPDATED 8 March 2009
@set UPDATED-MONTH March 2009
@set EDITION %{version}
@set VERSION %{version}
EOF
makeinfo DevIL_manual.texi

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C DevIL/build install \
	DESTDIR=$RPM_BUILD_ROOT

install -Dp DevIL/docs/DevIL_manual.info $RPM_BUILD_ROOT%{_infodir}/DevIL_manual.info

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc DevIL/{AUTHORS,CREDITS,ChangeLog,NEWS,README.md,TODO}
%attr(755,root,root) %{_bindir}/ilur
%attr(755,root,root) %{_libdir}/libIL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIL.so.1
%attr(755,root,root) %{_libdir}/libILU.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libILU.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libIL.so
%attr(755,root,root) %{_libdir}/libILU.so
%dir %{_includedir}/IL
%{_includedir}/IL/il.h
%{_includedir}/IL/ilu.h
%{_includedir}/IL/ilu_region.h
%{_pkgconfigdir}/IL.pc
%{_pkgconfigdir}/ILU.pc
%{_infodir}/DevIL_manual.info*

%files ILUT
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libILUT.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libILUT.so.1

%files ILUT-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libILUT.so
%{_includedir}/IL/devil_cpp_wrapper.hpp
%{_includedir}/IL/ilut.h
%{_pkgconfigdir}/ILUT.pc

%files doc
%defattr(644,root,root,755)
%doc DevIL-docs/DevIL*.pdf
