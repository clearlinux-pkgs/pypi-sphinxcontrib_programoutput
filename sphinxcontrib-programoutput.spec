#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinxcontrib-programoutput
Version  : 0.16
Release  : 15
URL      : https://files.pythonhosted.org/packages/3a/70/9d31f5ecaeaddfc7857de38b3dcec099690829122c084c2cdfee8f90a967/sphinxcontrib-programoutput-0.16.tar.gz
Source0  : https://files.pythonhosted.org/packages/3a/70/9d31f5ecaeaddfc7857de38b3dcec099690829122c084c2cdfee8f90a967/sphinxcontrib-programoutput-0.16.tar.gz
Summary  : Sphinx extension to include program output
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-programoutput-license = %{version}-%{release}
Requires: sphinxcontrib-programoutput-python = %{version}-%{release}
Requires: sphinxcontrib-programoutput-python3 = %{version}-%{release}
Requires: Sphinx
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
=============================
sphinxcontrib-programoutput
=============================

%package license
Summary: license components for the sphinxcontrib-programoutput package.
Group: Default

%description license
license components for the sphinxcontrib-programoutput package.


%package python
Summary: python components for the sphinxcontrib-programoutput package.
Group: Default
Requires: sphinxcontrib-programoutput-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-programoutput package.


%package python3
Summary: python3 components for the sphinxcontrib-programoutput package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_programoutput)
Requires: pypi(sphinx)

%description python3
python3 components for the sphinxcontrib-programoutput package.


%prep
%setup -q -n sphinxcontrib-programoutput-0.16
cd %{_builddir}/sphinxcontrib-programoutput-0.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1584976392
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-programoutput
cp %{_builddir}/sphinxcontrib-programoutput-0.16/LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-programoutput/39d61007f5d1111fcf45d6fb9f274dd5e21f72b6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-programoutput/39d61007f5d1111fcf45d6fb9f274dd5e21f72b6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
