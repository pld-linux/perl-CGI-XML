%include	/usr/lib/rpm/macros.perl
Summary:	CGI-XML perl module
Summary(pl):	Modu³ perla CGI-XML
Name:		perl-CGI-XML
Version:	0.1
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-XML-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-XML-Parser
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-XML module converts CGI.pm variables from/to XML.

%description -l pl
Modu³ CGI-XML konwertuje zmienne CGI.pm z/do formatu XML.

%prep
%setup -q -n CGI-XML-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/CGI/XML
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/CGI/XML.pm
%{perl_sitearch}/auto/CGI/XML

%{_mandir}/man3/*

%dir %{_prefix}/src/examples/%{name}-%{version}
%attr(755,root,root) %{_prefix}/src/examples/%{name}-%{version}/*
