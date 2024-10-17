%define upstream_name	 Acme-MetaSyntactic
%define upstream_version 1.012

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Generates themed metasyntactic variables
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Acme/Acme-MetaSyntactic-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(LWP::UserAgent)
BuildArch:	noarch

%description
Acme::MetaSyntactic is a perl module to generate good (as well as funny)
metasyntactic variable names. It provides several variable themes, from the
usual "foo" "bar" list, to the fight sound effects from the Batman 60s TV
serial.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Acme
%{_mandir}/*/*
%{_bindir}/*
/usr/lib/perl5/vendor_perl/5.16.3/Test/MetaSyntactic.pm
/usr/lib/perl5/vendor_perl/5.16.3/eta.pm


%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.990.0-1mdv2010.0
+ Revision: 406833
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.99-4mdv2009.0
+ Revision: 255258
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.99-2mdv2008.1
+ Revision: 136656
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.99-2mdv2008.0
+ Revision: 90051
- rebuild


* Sat Nov 18 2006 Olivier Thauvin <nanardon@mandriva.org> 0.99-1mdv2007.0
+ Revision: 85426
- 0.99

* Mon Sep 04 2006 Olivier Thauvin <nanardon@mandriva.org> 0.89-1mdv2007.0
+ Revision: 59683
- 0.89

* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org> 0.85-1mdv2007.0
+ Revision: 53695
- 0.85
- Import perl-Acme-MetaSyntactic

* Thu Aug 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.84-1mdv2007.0
- New version 0.84

* Sat Jul 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.80-1mdv2007.0
- New version 0.80

* Thu Jun 22 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.79-1mdv2007.0
- New version 0.79
- better source URL

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.78-1mdv2007.0
- New version 0.78

* Thu Jun 08 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.77-1mdv2007.0
- New release 0.77

* Wed May 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.76-1mdv2007.0
- New release 0.76

* Sun May 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.75-1mdk
- New release 0.75

* Tue May 09 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.72-1mdk
- New release 0.72

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.71-1mdk
- New release 0.71

* Fri Apr 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.69-1mdk
- New release 0.69
- better source URL
- better buildrequires syntax

* Tue Apr 04 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.68-1mdk
- New release 0.68
- fix directory ownership

* Mon Mar 13 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.65-1mdk
- 0.65

* Mon Feb 13 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.61-1mdk
- 0.61

* Mon Jan 30 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.59-1mdk
- 0.59

* Tue Jan 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.55-1mdk
- New release 0.55

* Fri Dec 16 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.52-1mdk
- 0.52
- Add BuildRequire

* Mon Dec 05 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.51-1mdk
- 0.51

* Mon Oct 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.46-1mdk
- 0.46

* Tue Oct 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.42-1mdk
- 0.42

* Sat Sep 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.40-1mdk
- 0.40

* Fri Aug 19 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.35-1mdk
- 0.35

* Tue Aug 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.33-1mdk
- 0.33

* Tue Jul 19 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.31-1mdk
- 0.31

* Tue Jun 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.28-1mdk
- 0.28

* Fri Jun 17 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.26-1mdk
- New release 0.26

* Tue Jun 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.24-1mdk
- New release 0.24

* Sat May 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.23-1mdk
- 0.23

* Tue May 17 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.22-1mdk
- 0.22

* Tue May 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.20-1mdk
- 0.20

* Tue Apr 26 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.19-1mdk
- 0.19

* Mon Mar 14 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.13-1mdk
- 0.13

* Thu Feb 17 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.09-1mdk
- 0.09

* Mon Jan 31 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.07-1mdk
- 0.07

* Mon Jan 17 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.05-1mdk
- Initial MDK release.


