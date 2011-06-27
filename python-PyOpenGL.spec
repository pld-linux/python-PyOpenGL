%define		module		PyOpenGL
Summary:	OpenGL bindings for Python
Summary(pl.UTF-8):	Dowiązania do OpenGL dla Pythona
Name:		python-%{module}
Version:	3.0.1
Release:	4
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
BuildRequires:	python-numpy-devel
BuildRequires:	python-devel
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

%prep
%setup -q -n %{module}-%{version} -a 1

%build
%{__python} setup.py build

cd %{module}-Demo-%{version}a1
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

cd %{module}-Demo-%{version}a1
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/OpenGL/{Demo,doc}

%clean
rm -rf $RPM_BUILD_ROOT

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
