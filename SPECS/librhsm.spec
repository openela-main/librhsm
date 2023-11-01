%global libname rhsm

Name:           lib%{libname}
Version:        0.0.3
Release:        5%{?dist}
Summary:        Red Hat Subscription Manager library

License:        LGPLv2+
URL:            https://github.com/rpm-software-management/librhsm
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         2.patch
Patch1:         4.patch
Patch2:         5.patch

BuildRequires:  meson >= 0.37.0
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44
BuildRequires:  pkgconfig(gio-2.0) >= 2.44
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2
BuildRequires:  pkgconfig(openssl)

%description
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{libname}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Jan 5 2023 Nicola Sella <nsella@redhat.com> - 0.0.3-5
- Append ctx_baseurl prefix to gpg_url

* Wed Jan 6 2021 Marek Blaha <mblaha@redhat.com> - 0.0.3-4
- Rebuild to ship also librhsm-devel subpackage

* Wed Jul 10 2019 Daniel Mach <dmach@redhat.com> - 0.0.3-3
- Generate repofile for any architecture if "ALL" is specified

* Tue Nov 13 2018 Daniel Mach <dmach@redhat.com> - 0.0.3-2
- Enable repos when generating a .repo file based on entitlement certificate.

* Mon Jul 09 2018 Igor Gnatenko <ignatenko@redhat.com> - 0.0.3-1
- Update to 0.0.3

* Thu Feb 22 2018 Igor Gnatenko <ignatenko@redhat.com> - 0.0.2-1
- Initial release
