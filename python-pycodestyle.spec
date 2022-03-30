#
# Conditional build:
%bcond_without	doc	# API documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python style guide checker
Summary(pl.UTF-8):	Sprawdzanie zgodności z poradnikiem stylu kodowania w Pythonie
Name:		python-pycodestyle
# NOTE: before upgrading to >=2.8.0 check for python2-compatible flake8 release supporting new pycodestyle
Version:	2.7.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pycodestyle/
Source0:	https://files.pythonhosted.org/packages/source/p/pycodestyle/pycodestyle-%{version}.tar.gz
# Source0-md5:	b6d333b5ef185b73b54ec0e9292d7d9e
URL:		https://pycodestyle.readthedocs.io/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
%{?with_doc:BuildRequires:	sphinx-pdg}
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pycodestyle is a tool to check your Python code against some of the
style conventions in PEP 8. This module was formerly called pep8.

%description -l pl.UTF-8
pycodestyle to narzędzie do sprawdzania kodu w Pythonie względem
niektórych konwencji stylistycznych opisanych w PEP 8. Ten moduł
wcześniej nazywał się pep8.

%package -n python3-pycodestyle
Summary:	Python style guide checker
Summary(pl.UTF-8):	Sprawdzanie zgodności z poradnikiem stylu kodowania w Pythonie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4
# default binary moved
Conflicts:	python-pycodestyle < 2.5.0-4

%description -n python3-pycodestyle
pycodestyle is a tool to check your Python code against some of the
style conventions in PEP 8. This module was formerly called pep8.

%description -n python3-pycodestyle -l pl.UTF-8
pycodestyle to narzędzie do sprawdzania kodu w Pythonie względem
niektórych konwencji stylistycznych opisanych w PEP 8. Ten moduł
wcześniej nazywał się pep8.

%package apidocs
Summary:	API documentation for pycodestyle module
Summary(pl.UTF-8):	Dokumentacja API modułu pycodestyle
Group:		Documentation

%description apidocs
API documentation for pycodestyle module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu pycodestyle.

%prep
%setup -q -n pycodestyle-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m testsuite.test_all
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python} -m testsuite.test_all
%endif
%endif

%if %{with doc}
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/pycodestyle{,-2}

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/pycodestyle{,-3}
ln -sf pycodestyle-3 $RPM_BUILD_ROOT%{_bindir}/pycodestyle
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE README.rst
%attr(755,root,root) %{_bindir}/pycodestyle-2
%{py_sitescriptdir}/pycodestyle.py[co]
%{py_sitescriptdir}/pycodestyle-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pycodestyle
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE README.rst
%attr(755,root,root) %{_bindir}/pycodestyle
%attr(755,root,root) %{_bindir}/pycodestyle-3
%{py3_sitescriptdir}/pycodestyle.py
%{py3_sitescriptdir}/__pycache__/pycodestyle.cpython-*.py[co]
%{py3_sitescriptdir}/pycodestyle-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
