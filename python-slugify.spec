%global pypi_name python-slugify
%global altname python_slugify

Name:           python-%{altname}
Version:        8.0.4
Release:        2
Summary:        A Python slugify application that handles unicode.
Group:          Development/Python
License:        MIT
URL:            https://github.com/un33k/python-slugify
Source0:        https://github.com/un33k/python-slugify/archive/v%{version}/%{altname}-v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(text-unidecode)
BuildRequires:  python%{pyver}dist(wheel)

Requires:       python%{pyver}dist(text-unidecode)

%description
Best attempt to create slugs from unicode strings while keeping it DRY.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
python3 ./test.py

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/slugify
%{python3_sitelib}/slugify*
%{python3_sitelib}/python_slugify-%{version}-py%{python3_version}.egg-info

