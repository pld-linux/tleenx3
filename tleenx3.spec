Summary:	Tlen.pl client for GTK+2
Summary(pl):	Klient Tlen.pl dla GTK+2
Name:		tleenx3
Version:	0.1
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://tleenx.sourceforge.net/%{name}-CVS.tar.gz
# Source0-md5:	c7933931adf632b1c9fd213fb9164f54
Source1:	http://tleenx.sourceforge.net/download/sounds/default.tar.gz
# Source1-md5:	964761f483c1a0a1421ca6ebc0a5ed22
Source2:	%{name}.desktop
URL:		http://tleenx.sourceforge.net/
BuildRequires:	XFree86-libs >= 4.3.99.15
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libtlen2-devel
BuildRequires:	pkgconfig
BuildRequires:	gnet-devel >= 2.0.0
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TleenX is a Tlen.pl client written for Linux users. It is distributed
under GPL license.

%description -l pl
TleenX to klient tlen.pl napisany z my¶l± o u¿ytkownikach Linuksa.
Jest rozpowszechniany na licencji GPL.

%prep
%setup -q -n %{name} -a1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/%{name}/sounds,%{_desktopdir}}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install default/* $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
