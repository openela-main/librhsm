Name:           librhsm
Version:        0.0.3
Release:        7%{?dist}.1
Summary:        Red Hat Subscription Manager library

License:        LGPLv2+
URL:            https://github.com/rpm-software-management/librhsm
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Patches backported from upstream
Patch0001:      0001-Replace-bool-option-with-int-to-generate-repo-files.patch
Patch0002:      0002-Generate-repofile-for-any-architecture-if-ALL-is-spe.patch
Patch0003:      0003-Enable-repos-when-generating-a-.repo-file-based-on-e.patch
Patch0004:      0004-Append-ctx_baseurl-prefix-to-gpg_url-RhBug-1708628.patch
Patch0005:      0005-Fix-relocating-certificate-paths-to-etc-rhsm-host.patch

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
%{_includedir}/rhsm/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Nov 21 2023 Petr Pisar <ppisar@redhat.com> - 0.0.3-7.1
- Correct a License tag to LGPLv2+ (RHEL-21336)
- Fix relocating certificate paths to /etc/rhsm-host (RHEL-21335)

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.0.3-7
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jun 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.0.3-6
- Rebuilt for RHEL 9 BETA for openssl 3.0
  Related: rhbz#1971065

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.0.3-5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Thu Mar 24 2021 Daniel Mach - 0.0.3-4
- Fix License in spec to LGPLv2.1+ (was LGPLv2+)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Stephen Gallagher <sgallagh@redhat.com> - 0.0.3-1
- Initial release
