#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		PyOpenGL
Summary:	OpenGL bindings for Python
Summary(pl.UTF-8):	Dowiązania do OpenGL dla Pythona
Name:		python-%{module}
Version:	3.0.1
Release:	5
Epoch:		1
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://downloads.sourceforge.net/pyopengl/%{module}-%{version}.tar.gz
# Source0-md5:	221d4a6a0928fcfeef26751370ec5f52
Source1:	http://downloads.sourceforge.net/pyopengl/%{module}-Demo-%{version}a1.tar.gz
# Source1-md5:	75b66abdf2d0e5003798c0fa12abee6e
URL:		http://pyopengl.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
%if %{with python2}
BuildRequires:	python-numpy-devel
BuildRequires:	python-devel
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
BuildRequires:	python3-numpy-devel
%endif
%pyrequires_eq	python-libs
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-numpy
Obsoletes:	PyOpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

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
%{__python} setup.py build --build-base build-2

cd %{module}-Demo-%{version}a1
%{__python} setup.py build --build-base build-2
cd ..
%endif

%if %{with python3}
%{__python3} setup.py build --build-base build-3

cd %{module}-Demo-%{version}a1
%{__python} setup.py build --build-base build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

cd %{module}-Demo-%{version}a1
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
cd ..

%py_postclean

#{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/OpenGL/{Demo,doc}
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

cd %{module}-Demo-%{version}a1
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

#{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/OpenGL/{Demo,doc}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc PKG-INFO
%{py_sitescriptdir}/OpenGL
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/*.egg-info
%endif

%files examples
%defattr(644,root,root,755)
%{py_sitescriptdir}/PyOpenGL-Demo
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc PKG-INFO
%{py3_sitescriptdir}/OpenGL
%{py3_sitescriptdir}/*.egg-info

%files -n python3-%{module}-examples
%defattr(644,root,root,755)
%{py3_sitescriptdir}/PyOpenGL-Demo
%endif
