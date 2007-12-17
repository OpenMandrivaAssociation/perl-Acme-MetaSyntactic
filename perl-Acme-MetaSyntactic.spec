%define module	Acme-MetaSyntactic
%define name	perl-%{module}
%define version 0.99
%define	release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Generates themed metasyntactic variables
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Acme/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(LWP::UserAgent)
BuildArch:	noarch

%description
Acme::MetaSyntactic is a perl module to generate good (as well as funny)
metasyntactic variable names. It provides several variable themes, from the
usual "foo" "bar" list, to the fight sound effects from the Batman 60s TV
serial.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test 

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Acme
%{_mandir}/*/*
%{_bindir}/*


