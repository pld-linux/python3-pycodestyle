#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Python style guide checker
Summary(pl.UTF-8):	Sprawdzanie zgodności z poradnikiem stylu kodowania w Pythonie
Name:		python3-pycodestyle
Version:	2.12.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pycodestyle/
Source0:	https://files.pythonhosted.org/packages/source/p/pycodestyle/pycodestyle-%{version}.tar.gz
# Source0-md5:	a116089dc7267cfd082c779680b8cab2
URL:		https://pycodestyle.readthedocs.io/
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.8
# default binary moved
Conflicts:	python-pycodestyle < 2.5.0-4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pycodestyle is a tool to check your Python code against some of the
style conventions in PEP 8. This module was formerly called pep8.

%description -l pl.UTF-8
pycodestyle to narzędzie do sprawdzania kodu w Pythonie względem
niektórych konwencji stylistycznych opisanych w PEP 8. Ten moduł
wcześniej nazywał się pep8.

%prep
%setup -q -n pycodestyle-%{version}

%build
%py3_build

%if %{with tests}
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest -o pythonpath="$PWD/build-3" tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/pycodestyle{,-3}
ln -sf pycodestyle-3 $RPM_BUILD_ROOT%{_bindir}/pycodestyle

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/pycodestyle
%attr(755,root,root) %{_bindir}/pycodestyle-3
%{py3_sitescriptdir}/pycodestyle.py
%{py3_sitescriptdir}/__pycache__/pycodestyle.cpython-*.py[co]
%{py3_sitescriptdir}/pycodestyle-%{version}-py*.egg-info
