#
# TODO:	- download and include PyOpenGL-Demo (it's now in separate package)
#	- check deps
#
%define		module	PyOpenGL
%define		_beta	b8
Summary:	OpenGL bindings for Python
Summary(pl.UTF-8):	Dowiązania do OpenGL dla Pythona
Name:		python-%{module}
Version:	3.0.0
Release:	0.%{_beta}.1
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pyopengl/%{module}-%{version}%{_beta}.tar.gz
# Source0-md5:	1d9afbf0a403d916997937ef0dde2520
URL:		http://pyopengl.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	python-Numeric-devel >= 22.0
BuildRequires:	python-devel >= 1:2.5
%pyrequires_eq	python-libs
Requires:	python-Numeric >= 22.0
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
Requires:	%{name} = %{version}-%{release}

%description examples
Demos for PyOpenGL.

%description examples -l pl.UTF-8
Programy demonstracyjne dla pakietu PyOpenGL.

%prep
%setup -q -n %{module}-%{version}%{_beta}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
#cp -a OpenGL/Demo $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/OpenGL/{Demo,doc}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%%doc README* OpenGL/doc/xhtml/*
%{py_sitescriptdir}/OpenGL
%{py_sitescriptdir}/*.egg-info

%files examples
%defattr(644,root,root,755)
#%%{_examplesdir}/%{name}-%{version}
