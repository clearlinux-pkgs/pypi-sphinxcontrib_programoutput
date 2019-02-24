#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinxcontrib-programoutput
Version  : 0.13
Release  : 4
URL      : https://files.pythonhosted.org/packages/be/08/db26a372785a4eaebad287c9557345e606785af7af886c3fd4e368d494eb/sphinxcontrib-programoutput-0.13.tar.gz
Source0  : https://files.pythonhosted.org/packages/be/08/db26a372785a4eaebad287c9557345e606785af7af886c3fd4e368d494eb/sphinxcontrib-programoutput-0.13.tar.gz
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

%description python3
python3 components for the sphinxcontrib-programoutput package.


%prep
%setup -q -n sphinxcontrib-programoutput-0.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551038119
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-programoutput
cp LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-programoutput/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-programoutput/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
