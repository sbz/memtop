%define _release master
%define _version 0.0.1

Name:           memtop
Version:        %{_version}
Release:        0%{?dist}
License:        BSD
Summary:        memory top(1) like in Python
Url:            https://github.com/sbz/memtop
Group:          Development/Languages/Python
Source:         https://github.com/sbz/memtop/archive/%{name}-%{_release}.zip
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-setuptools
Requires:       python-psutil

%description
memory top(1) like in Python.

%prep
%setup -q -n %{name}-%{_release}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md
%{python_sitelib}/*
%attr(0744, root, root) /usr/bin/memtop

%changelog
* Tue Feb 07 2017 Sofian Brabez <sbz@6dev.net> - %{version}
- Initial package.
