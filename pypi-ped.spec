#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ped
Version  : 2.1.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/e1/f3/75df1fb853b8ff8f37e641ccec4b64e6f21fc3dca3580c887e0390661d97/ped-2.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e1/f3/75df1fb853b8ff8f37e641ccec4b64e6f21fc3dca3580c887e0390661d97/ped-2.1.0.tar.gz
Summary  : Quickly open Python modules in your text editor.
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: pypi-ped-bin = %{version}-%{release}
Requires: pypi-ped-license = %{version}-%{release}
Requires: pypi-ped-python = %{version}-%{release}
Requires: pypi-ped-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
ped
        ===

%package bin
Summary: bin components for the pypi-ped package.
Group: Binaries
Requires: pypi-ped-license = %{version}-%{release}

%description bin
bin components for the pypi-ped package.


%package license
Summary: license components for the pypi-ped package.
Group: Default

%description license
license components for the pypi-ped package.


%package python
Summary: python components for the pypi-ped package.
Group: Default
Requires: pypi-ped-python3 = %{version}-%{release}

%description python
python components for the pypi-ped package.


%package python3
Summary: python3 components for the pypi-ped package.
Group: Default
Requires: python3-core
Provides: pypi(ped)

%description python3
python3 components for the pypi-ped package.


%prep
%setup -q -n ped-2.1.0
cd %{_builddir}/ped-2.1.0
pushd ..
cp -a ped-2.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656393662
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ped
cp %{_builddir}/ped-2.1.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ped/909c116ce214c8ff1e296e4ad41e7e57fcfc4d74
cp %{_builddir}/ped-2.1.0/NOTICE %{buildroot}/usr/share/package-licenses/pypi-ped/af88e49e6c45ee802ab2c6ea812295c368e94a83
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ped

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ped/909c116ce214c8ff1e296e4ad41e7e57fcfc4d74
/usr/share/package-licenses/pypi-ped/af88e49e6c45ee802ab2c6ea812295c368e94a83

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
