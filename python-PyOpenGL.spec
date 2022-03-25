#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
%bcond_with	tests	# tests (display required)

%define		module		PyOpenGL
Summary:	OpenGL bindings for Python
Summary(pl.UTF-8):	Dowiązania do OpenGL dla Pythona
Name:		python-%{module}
Version:	3.1.0
Release:	5
Epoch:		1
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/pyopengl/
Source0:	https://files.pythonhosted.org/packages/source/p/pyopengl/%{module}-%{version}.tar.gz
# Source0-md5:	0de021941018d46d91e5a8c11c071693
Source1:	http://downloads.sourceforge.net/pyopengl/%{module}-Demo-3.0.1a1.tar.gz
# Source1-md5:	75b66abdf2d0e5003798c0fa12abee6e
URL:		http://pyopengl.sourceforge.net/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-numpy
BuildRequires:	python-pygame
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-numpy
BuildRequires:	python3-pygame
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
Requires:	python-numpy
Obsoletes:	PyOpenGL
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenGL bindings for Python including support for GL extensions, GLU,
WGL, GLUT, GLE, and Tk.

%description -l pl.UTF-8
Dowiązania do OpenGL dla Pythona wraz z rozszerzeniami GL, GLU, WGL,
GLUT, GLE i Tk.

%package examples
Summary:	Demos for PyOpenGL
Summary(pl.UTF-8):	Programy demonstracyjne dla pakietu PyOpenGL
Group:		Development/Languages/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description examples
Demos for PyOpenGL.

%description examples -l pl.UTF-8
Programy demonstracyjne dla pakietu PyOpenGL.

%package -n python3-%{module}
Summary:	OpenGL bindings for Python
Summary(pl.UTF-8):	Dowiązania do OpenGL dla Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2
Requires:	python3-numpy

%description -n python3-%{module}
OpenGL bindings for Python including support for GL extensions, GLU,
WGL, GLUT, GLE, and Tk.

%description -n python3-%{module} -l pl.UTF-8
Dowiązania do OpenGL dla Pythona wraz z rozszerzeniami GL, GLU, WGL,
GLUT, GLE i Tk.

%package -n python3-%{module}-examples
Summary:	Demos for PyOpenGL
Summary(pl.UTF-8):	Programy demonstracyjne dla pakietu PyOpenGL
Group:		Development/Languages/Python
Requires:	python3-%{module} = %{epoch}:%{version}-%{release}

%description -n python3-%{module}-examples
Demos for PyOpenGL.

%description -n python3-%{module}-examples -l pl.UTF-8
Programy demonstracyjne dla pakietu PyOpenGL.

%prep
%setup -q -n %{module}-%{version} -a 1

%build
%if %{with python2}
%py_build

cd %{module}-Demo-3.0.1a1
%py_build
cd ..

%if %{with tests}
cd tests
%{__python} test_core.py
cd ..
%endif
%endif

%if %{with python3}
%py3_build

cd %{module}-Demo-3.0.1a1
%py3_build
cd ..

%if %{with tests}
cd tests
%{__python3} test_core.py
cd ..
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

cd %{module}-Demo-3.0.1a1
%py_install
cd ..

%py_postclean
%endif

%if %{with python3}
%py3_install

cd %{module}-Demo-3.0.1a1
%py3_install
cd ..
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc license.txt
%{py_sitescriptdir}/OpenGL
%{py_sitescriptdir}/PyOpenGL-%{version}-py*.egg-info

%files examples
%defattr(644,root,root,755)
%{py_sitescriptdir}/PyOpenGL-Demo
%{py_sitescriptdir}/PyOpenGL_Demo-3.0.1a1-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc license.txt
%{py3_sitescriptdir}/OpenGL
%{py3_sitescriptdir}/PyOpenGL-%{version}-py*.egg-info

%files -n python3-%{module}-examples
%defattr(644,root,root,755)
%{py3_sitescriptdir}/PyOpenGL-Demo
%{py3_sitescriptdir}/PyOpenGL_Demo-3.0.1a1-py*.egg-info
%endif
