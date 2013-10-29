#
# Conditional build:
%bcond_with	sse	# use SSE extension
%bcond_with	sse2	# use SSE2 extension
%bcond_with	sse3	# use SSE3 extension
#
%ifarch pentium3 pentium4 %{x8664}
%define	with_sse	1
%endif
%ifarch pentium4 %{x8664}
%define	with_sse2	1
%endif
%define		manual_version	1.5.5
Summary:	Full featured image library
Summary(pl.UTF-8):	Biblioteka obsługi obrazów z mnóstwem funkcji
Name:		DevIL
Version:	1.7.8
Release:	10
License:	LGPL v2.1
Group:		Libraries
Source0:	http://downloads.sourceforge.net/openil/%{name}-%{version}.tar.gz
# Source0-md5:	7918f215524589435e5ec2e8736d5e1d
Source1:	http://downloads.sourceforge.net/openil/%{name}-Manual-%{manual_version}.zip
# Source1-md5:	6bb2ddfcbe09930c48ef84b8f99479fe
Source2:	http://downloads.sourceforge.net/openil/%{name}-docs.tar.gz
# Source2-md5:	eec6ae7a028a3f058bab1a6918428ed5
Patch0:		libpng14.patch
Patch1:		%{name}-squish.patch
Patch2:		%{name}-as-needed.patch
URL:		http://openil.sourceforge.net/
BuildRequires:	OpenEXR-devel
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
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.533
BuildRequires:	squish-devel
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	xorg-lib-libXext-devel
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

Obsługiwane jest zapisywanie do plików bmp, dds, h, jpg, pal, pbm,
pcx, pgm, png, ppm, raw, sgi, tga i tif.

%package devel
Summary:	DevIL development files
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek DevIL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenEXR-devel
Requires:	jasper-devel
Requires:	lcms-devel
Requires:	libjpeg-devel
Requires:	libmng-devel
Requires:	libpng-devel
Requires:	libtiff-devel
Requires:	squish-devel

%description devel
DevIL development files (for IL and ILU libraries).

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek DevIL (IL i ILU).

%package static
Summary:	Static DevIL libraries
Summary(pl.UTF-8):	Statyczne biblioteki DevIL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static DevIL libraries (IL and ILU).

%description static -l pl.UTF-8
Statyczne biblioteki DevIL (IL i ILU).

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

%description ILUT-devel
Development files for DevIL ILUT library.

%description ILUT-devel -l pl.UTF-8
Pliki programistyczne biblioteki DevIL ILUT.

%package ILUT-static
Summary:	Static DevIL ILUT library
Summary(pl.UTF-8):	Statyczna biblioteka DevIL ILUT
Group:		Development/Libraries
Requires:	%{name}-ILUT-devel = %{version}-%{release}

%description ILUT-static
Static DevIL ILUT library.

%description ILUT-static -l pl.UTF-8
Statyczna biblioteka DevIL ILUT.

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

%build
cd devil-%{version}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-ILU \
	--enable-ILUT \
	%{?debug:--disable-release} \
	%{!?with_sse:--disable-sse} \
	%{!?with_sse2:--disable-sse2} \
	%{!?with_sse3:--disable-sse3}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C devil-%{version} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc devil-%{version}/{AUTHORS,CREDITS,ChangeLog,README.unix}
%attr(755,root,root) %{_bindir}/ilur
%attr(755,root,root) %{_libdir}/libIL.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIL.so.1
%attr(755,root,root) %{_libdir}/libILU.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libILU.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libIL.so
%attr(755,root,root) %{_libdir}/libILU.so
%{_libdir}/libIL.la
%{_libdir}/libILU.la
%dir %{_includedir}/IL
%{_includedir}/IL/il.h
%{_includedir}/IL/ilu.h
%{_includedir}/IL/ilu_region.h
%{_pkgconfigdir}/IL.pc
%{_pkgconfigdir}/ILU.pc
%{_infodir}/DevIL_manual.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libIL.a
%{_libdir}/libILU.a

%files ILUT
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libILUT.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libILUT.so.1

%files ILUT-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libILUT.so
%{_includedir}/IL/devil_cpp_wrapper.hpp
%{_includedir}/IL/ilut.h
%{_libdir}/libILUT.la
%{_pkgconfigdir}/ILUT.pc

%files ILUT-static
%defattr(644,root,root,755)
%{_libdir}/libILUT.a

%files doc
%defattr(644,root,root,755)
%doc DevIL*.pdf
