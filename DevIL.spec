Summary:	Full featured image library
Summary(pl):	Biblioteka obs³ugi obrazów z mnóstwem funkcji
Name:		DevIL
Version:	1.6.5
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/openil/%{name}-%{version}.tar.gz
# Source0-md5:	e55f14ad26660887d9c671f71c65fae3
Source1:	http://openil.sourceforge.net/docs/%{name}%20Manual.pdf
# Source1-md5:	329597aebae8c4387866771888485eb5
Source2:	http://openil.sourceforge.net/docs/%{name}%20Reference%20Guide.pdf
# Source2-md5:	c5fec53a179df61d2401311c63fbfef0
URL:		http://openil.sourceforge.net/
BuildRequires:	allegro-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
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
Developer's Image Library (DevIL) jest bibliotek± programisty
pozwalaj±c± tworzyæ aplikacje z potê¿nymi mo¿liwo¶ciami ³adowania
obrazów. Pozostaje przy tym ³atwa w u¿yciu i prosta do nauczenia siê.
Ostateczna kontrola nad obrazami jest zostawiona programi¶cie, nie
wprowadza siê niepotrzebnych konwersji, itp. DevIL u¿ywa prostej, lecz
potê¿nej sk³adni poleceñ, wzorowanej na OpenGL-u. DevIL potrafi
³adowaæ, zapisywaæ, konwertowaæ, manipulowaæ, filtrowaæ szeroki
wachlarz formatów plików graficznych.

W chwili obecnej DevIL odczytuje pliki z rozszerzeniami bmp, cut, dds,
doom, gif, ico, jpg, lbm, mdl, mng, pal, pbm, pcd, pcx, pgm, pic, png,
ppm, psd, psp, raw, sgi, tga i tif.

Wspierane jest zapisywanie do plików bmp, dds, h, jpg, pal, pbm, pcx,
pgm, png, ppm, raw, sgi, tga i tif.

%package devel
Summary:	DevIL devel files
Summary(pl):	Nag³ówki DevIL
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
DevIL devel files.

%description devel -l pl
Nag³ówki DevIL.

%package doc
Summary:	DevIL documentation
Summary(pl):	Dokumentacja DevIL
Group:		Development/Libraries

%description doc
DevIL documentation.

%description doc -l pl
Dokumentacja DevIL.

%prep
%setup -q -n %{name}

cp %{SOURCE1} %{SOURCE2} .

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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
%doc DevIL%20Manual.pdf DevIL%20Reference%20Guide.pdf
