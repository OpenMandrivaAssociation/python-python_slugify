# Created by pyp2rpm-3.3.5
%global pypi_name python-slugify
%global altname python_slugify

Name:           python-%{altname}
Version:        5.0.2
Release:        2
Summary:        A generic slugifier
Group:          Development/Python
License:        None
URL:            http://github.com/zacharyvoase/slugify
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

Provides:	python3dist(python_slugify)
Provides:	python3dist(python-slugify)

%description


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python-%{altname}
%{_bindir}/slugify
%{python3_sitelib}/slugify
%{python3_sitelib}/%{altname}-%{version}-py%{python3_version}.egg-info

