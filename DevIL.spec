Summary:	Full featured image library
Summary(pl):	Biblioteka obs�ugi obraz�w z mn�stwem funkcji
Name:		DevIL
Version:	1.6.6
%define		manual_version	1.5.5
%define		docs_version	1.4.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/openil/%{name}-%{version}.tar.gz
# Source0-md5:	57dd2156049f0335d2535724418a89ea
Source1:	http://dl.sourceforge.net/openil/%{name}-Manual-%{manual_version}.zip
# Source1-md5:	6bb2ddfcbe09930c48ef84b8f99479fe
Source2:	http://dl.sourceforge.net/openil/%{name}-Docs-%{docs_version}.zip
# Source2-md5:	eb1adc2e0ee154a97490b2178d41996a
URL:		http://openil.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	allegro-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	unzip
Requires:	OpenGL
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

Currently, DevIL can load .bmp, .cut, .dds, .doom, .gif, .ico, .jpg,
.lbm, .mdl, .mng, .pal, .pbm, .pcd, .pcx, .pgm, .pic, .png, .ppm,
.psd, .psp, .raw, .sgi, .tga and .tif files.

Formats supported for saving include .bmp, .dds, .h, .jpg, .pal, .pbm,
.pcx, .pgm, .png, .ppm, .raw, .sgi, .tga and .tif.

%description -l pl
Developer's Image Library (DevIL) jest bibliotek� programisty
pozwalaj�c� tworzy� aplikacje z pot�nymi mo�liwo�ciami �adowania
obraz�w. Pozostaje przy tym �atwa w u�yciu i prosta do nauczenia si�.
Ostateczna kontrola nad obrazami jest zostawiona programi�cie, nie
wprowadza si� niepotrzebnych konwersji, itp. DevIL u�ywa prostej, lecz
pot�nej sk�adni polece�, wzorowanej na OpenGL-u. DevIL potrafi
�adowa�, zapisywa�, konwertowa�, manipulowa�, filtrowa� szeroki
wachlarz format�w plik�w graficznych.

W chwili obecnej DevIL odczytuje pliki z rozszerzeniami bmp, cut, dds,
doom, gif, ico, jpg, lbm, mdl, mng, pal, pbm, pcd, pcx, pgm, pic, png,
ppm, psd, psp, raw, sgi, tga i tif.

Wspierane jest zapisywanie do plik�w bmp, dds, h, jpg, pal, pbm, pcx,
pgm, png, ppm, raw, sgi, tga i tif.

%package devel
Summary:	DevIL devel files
Summary(pl):	Nag��wki DevIL
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
DevIL devel files.

%description devel -l pl
Nag��wki DevIL.

%package doc
Summary:	DevIL documentation
Summary(pl):	Dokumentacja DevIL
Group:		Development/Libraries

%description doc
DevIL documentation.

%description doc -l pl
Dokumentacja DevIL.

%prep
%setup -q -n %{name} -a1 -a2

#cp %{SOURCE1} %{SOURCE2} .

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	%{?debug:--disable-release}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS CREDITS ChangeLog README.unix
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%{_includedir}/*

%files doc
%defattr(644,root,root,755)
%doc DevIL*.pdf
