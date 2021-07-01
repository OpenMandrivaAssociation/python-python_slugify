# Created by pyp2rpm-3.3.5
%global pypi_name slugify

Name:           python-%{pypi_name}
Version:        0.0.1
Release:        1
Summary:        A generic slugifier
Group:          Development/Python
License:        None
URL:            http://github.com/zacharyvoase/slugify
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%{_bindir}/slugify
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

