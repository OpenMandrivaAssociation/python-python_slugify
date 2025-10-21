%global pypi_name python-slugify
%global altname python_slugify

Name:           python-%{altname}
Version:        8.0.4
Release:        1%{?dist}
Summary:        A Python slugify application that handles unicode.
Group:          Development/Python
License:        MIT 
URL:            https://github.com/un33k/python-slugify
Source0:        https://github.com/un33k/python-slugify/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-pip 
BuildRequires:  python-setuptools
BuildRequires:  python-text-unidecode
BuildRequires:  python-wheel

Requires:	      python-text-unidecode

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

%post
if [ -f %{_bindir}/slugify ] && [ ! -L %{_bindir}/slugify ]; then
    rm -f %{_bindir}/slugify
fi
update-alternatives --install /usr/bin/slugify slugify %{_bindir}/slugify 50

%postun
update-alternatives --remove slugify %{_bindir}/slugify || :

%pre
update-alternatives --remove slugify %{_bindir}/slugify || :

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/slugify
%{python3_sitelib}/slugify*
%{python3_sitelib}/python_slugify-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Oct 21 2025 Samuil Ivanov <samuil.ivanovbg@gmail.com> - 8.0.4-0
- Updated python-slugify to version 8.0.4
- Fixed %post,%postun and %pre scripts to handle update-alternatives safely
- Verified tests with Python 3.11
