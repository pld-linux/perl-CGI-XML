#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	CGI
%define		pnam	XML
%include	/usr/lib/rpm/macros.perl
Summary:	CGI::XML - Perl extension for converting CGI.pm variables to/from XML
Summary(pl.UTF-8):	CGI::XML - rozszerzenie Perla do konwersji zmiennych CGI.pm do/z formatu XML
Name:		perl-CGI-XML
Version:	0.1
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	219b1fe22dc6589a52f07b1301b88d0b
Patch0:		%{name}-test.patch
URL:		http://search.cpan.org/dist/CGI-XML/
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::XML module converts CGI.pm variables from/to XML.

%description -l pl.UTF-8
Moduł CGI::XML konwertuje zmienne CGI.pm z/do formatu XML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/XML.pm
%{_mandir}/man3/*

%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
