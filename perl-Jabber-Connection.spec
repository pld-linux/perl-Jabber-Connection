#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Jabber
%define		pnam	Connection
Summary:	Jabber::Connection - simple connectivity functions for Jabber
Summary(pl):	Jabber::Connection - proste funkcje ³±czenia z serwerem Jabbera
Name:		perl-Jabber-Connection
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2721fce3cebe6de646c205f34f0368d2
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Digest-SHA1 >= 1.03
BuildRequires:	perl-XML-Parser >= 2.29
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Digest-SHA1 >= 1.03
Requires:	perl-XML-Parser >= 2.29
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Jabber::Connection Perl module provides basic functions for
connecting clients and components to a Jabber server.

%description -l pl
Modu³ Perla Jabber::Connection udostêpnia podstawowe funkcje s³u¿±ce
do ³±czenia klientów i komponentów z serwerem Jabbera.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{__perl} -pi -e 's/^(use 5.006_)0(01;)(.*)$/$1$2$3/' Jabber/X.pm

%build
perl Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -f examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/Jabber/*
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
