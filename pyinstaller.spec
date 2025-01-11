%undefine _debugsource_packages
%global pypi_name pyinstaller
%global optflags %{optflags} -Wno-strict-aliasing

Name:           %{pypi_name}
Version:        6.11.1
Release:        1
Summary:        PyInstaller bundles a Python application and all its dependencies into a single package
Group:          Development/Python
License:        GPLv2-or-later with a special exception which allows to use PyInstaller to build and distribute non-free programs (including commercial ones)
URL:            https://www.pyinstaller.org/
Source0:        https://files.pythonhosted.org/packages/source/p/pyinstaller/pyinstaller-%{version}.tar.gz

BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(zlib)

%description
PyInstaller bundles a Python application and all its
dependencies into a single package.

%prep
%autosetup -n %{pypi_name}-%{version}
# Force build of bootloader
rm -r PyInstaller/bootloader

%build
%py_build

%install
%py_install

%files
%license COPYING.txt
%doc PyInstaller/lib/README.rst
%{_bindir}/pyi-archive_viewer
%{_bindir}/pyi-bindepend
%{_bindir}/pyi-grab_version
%{_bindir}/pyi-makespec
%{_bindir}/pyi-set_version
%{_bindir}/pyinstaller
