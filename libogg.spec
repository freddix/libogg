Summary:	Ogg Bitstream Library
Name:		libogg
Version:	1.3.1
Release:	1
Epoch:		2
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/ogg/%{name}-%{version}.tar.gz
# Source0-md5:	ba526cd8f4403a5d351a9efaa8608fbc
Patch0:		%{name}-ac_fixes.patch
URL:		http://www.xiph.org/ogg/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libogg is a library for manipulating Ogg bitstreams. It handles both
making Ogg bitstreams and getting packets from Ogg bitstreams.

%package devel
Summary:	Ogg Bitstream Library Development
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
The libogg-devel package contains the header files and documentation
needed to develop applications with libogg.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%{__mv} $RPM_BUILD_ROOT%{_docdir}/%{name} devel-docs

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES COPYING README
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc devel-docs/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/ogg
%{_aclocaldir}/ogg.m4
%{_pkgconfigdir}/ogg.pc

