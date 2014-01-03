Summary:	Library to make sure only one instance of a program is running
Summary(pl.UTF-8):	Biblioteka zapewniająca uruchamianie tylko jednej instancji programu
Name:		libunique3
Version:	3.0.2
Release:	2
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libunique/3.0/libunique-%{version}.tar.bz2
# Source0-md5:	89c3f88c9bfc35b3f13fa2b7bda0c354
URL:		http://live.gnome.org/LibUnique
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gobject-introspection-devel >= 0.9.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.13
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
Requires:	dbus-glib >= 0.70
Requires:	glib2 >= 1:2.28.0
Obsoletes:	gtkunique
Obsoletes:	unique
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unique is a library for writing single instance application. If you
launch a single instance application twice, the second instance will
either just quit or will send a message to the running instance.

Unique makes it easy to write this kind of applications, by providing
a base class, taking care of all the IPC machinery needed to send
messages to a running instance.

%description -l pl.UTF-8
Unique jest biblioteką do pisania aplikacji o jednej instancji. Jeśli
taka aplikacja zostanie uruchomiona dwa razy, druga instancja po
prostu się zamknie lub wyśle wiadomość do już uruchomionej.

Unique ułatwia pisanie tego typu aplikacji, poprzez zapewnienie
podstawowej klasy, biorąc przy tym pod uwagę wszystkie mechanizmy IPC
potrzebne do wysyłania wiadomości do już uruchomionych instancji.

%package devel
Summary:	Header files for unique library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki unique
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.70
Requires:	gtk+3-devel >= 3.0.0
Obsoletes:	gtkunique-devel
Obsoletes:	unique-devel

%description devel
Header files for unique library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki unique.

%package static
Summary:	Static unique library
Summary(pl.UTF-8):	Statyczna biblioteka unique
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	gtkunique-static
Obsoletes:	unique-static

%description static
Static unique library.

%description static -l pl.UTF-8
Statyczna biblioteka unique.

%package apidocs
Summary:	unique library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki unique
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	unique-apidocs

%description apidocs
unique library API documentation.

%description apidocs
Dokumentacja API biblioteki unique.

%prep
%setup -q -n libunique-%{version}

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libunique-3.0.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libunique-3.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libunique-3.0.so.0
%{_libdir}/girepository-1.0/Unique-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libunique-3.0.so
%{_includedir}/unique-3.0
%{_pkgconfigdir}/unique-3.0.pc
%{_datadir}/gir-1.0/Unique-3.0.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libunique-3.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/unique-3.0
