Name:		perl-Convert-BinHex
Version:	1.119
Release:	10.1%{?dist}
Summary:	Macintosh BinHex extractor library for Perl
Group:		Development/Libraries
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/Convert-BinHex/
Source0:	http://search.cpan.org/CPAN/authors/id/E/ER/ERYQ/Convert-BinHex-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildRequires:	perl(ExtUtils::MakeMaker)

%description
Convert::BinHex extracts data from Macintosh BinHex files.

%prep
%setup -q -n Convert-BinHex-%{version}
%{__chmod} -x bin/*.pl docs/Convert/BinHex/*.gif
%{__cp} -a bin examples
%{__perl} -pi -e 's/^use lib .*$//' bin/*.pl
%{__perl} -pi -e 's/^(\@ISA.*)/require Exporter; $1/' t/Checker.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install PERL_INSTALL_ROOT=%{buildroot}
/usr/bin/find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
/usr/bin/find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
%{__chmod} -R u+w %{buildroot}/*

%check
%{__make} test

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README docs examples
%{perl_vendorlib}/Convert/
%{_mandir}/man3/Convert::BinHex.3*

%changelog
* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.119-10.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.119-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.119-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.119-8
- Rebuild for perl 5.10 (again)

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.119-7
- rebuild for new perl

* Sat Aug 11 2007 Paul Howarth <paul@city-fan.org> 1.119-6
- clarify license as GPL version 1 or later, or Artistic (same as perl)

* Thu Mar  8 2007 Paul Howarth <paul@city-fan.org> 1.119-5
- add perl(ExtUtils::MakeMaker) buildreq
- use tabs rather than spaces

* Sun Sep 17 2006 Paul Howarth <paul@city-fan.org> 1.119-4
- add dist tag
- fix argument order in find command with -depth

* Tue Aug 29 2006 Paul Howarth <paul@city-fan.org> 1.119-3
- use full paths for all commands used in build
- use search.cpan.org download URL
- assume rpm knows about %%check and %%{perl_vendorlib}
- cosmetic spec file changes

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Sep 15 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.119-1
- First build.
