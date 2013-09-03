#
# spec file for package scons
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
Name:           scons
Summary:        Replacement for Make
License:        MIT
Group:          Development/Tools/Building
Version:        2.2.0
Release:        0
Source0:        http://freefr.dl.sourceforge.net/project/scons/scons/%{version}/%{name}-%{version}.tar.gz
Source1001: 	scons.manifest
Url:            http://www.scons.org/
BuildRequires:  fdupes
BuildRequires:  python-devel

%description
SCons is a make replacement that provides a range of enhanced features,
such as automated dependency generation and built-in compilation cache
support. SCons rule sets are Python scripts, which means that SCons
provides itself as well as the features. SCons allows you to use the
full power of Python to control compilation.

%prep
%setup -q
cp %{SOURCE1001} .

%build
export CFLAGS="$RPM_OPT_FLAGS"
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot} --install-lib=%{python_sitearch}
%fdupes %{buildroot}%{_bindir}

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license LICENSE.txt
%{_bindir}/*
%{python_sitearch}/SCons/
%{python_sitearch}/*.egg-info
%{_mandir}/man1/*.gz

%changelog
