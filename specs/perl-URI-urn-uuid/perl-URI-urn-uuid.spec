# $Id$
# Authority: dag
# Upstream: Tatsuhiko Miyagawa <miyagawa@bulknews.net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI-urn-uuid

Summary: UUID URN Namespace
Name: perl-URI-urn-uuid
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI-urn-uuid/

Source: http://www.cpan.org/modules/by-module/URI/URI-urn-uuid-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Data::UUID)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
Requires: perl(Data::UUID)
Requires: perl(URI)

%filter_from_requires /^perl*/d
%filter_setup


%description
UUID URN Namespace.

This package contains the following Perl module:

    URI::urn::uuid

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/URI::urn::uuid.3pm*
%dir %{perl_vendorlib}/URI/
%dir %{perl_vendorlib}/URI/urn/
#%{perl_vendorlib}/URI/urn/uuid/
%{perl_vendorlib}/URI/urn/uuid.pm

%changelog
* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 0.03-1
- Updated to version 0.03.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
