#
# TODO:	- package demos into examplesdir?
#	- check deps
#	- applications which use pyopengl can't locate it - try to fix it
#
%define		module	PyOpenGL
%define		_beta	c1
Summary:	OpenGL bindings for Python
Summary(pl.UTF-8):	Dowiązania do OpenGL dla Pythona
Name:		python-%{module}
Version:	3.0.0
Release:	0.%{_beta}.1
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pyopengl/%{module}-%{version}%{_beta}.tar.gz
# Source0-md5:	51a33cea33f3e8eb2eaf12f574dcb1af
Source1:	http://dl.sourceforge.net/pyopengl/%{module}-Demo-%{version}%{_beta}.tar.gz
# Source1-md5:	672c53e5dcfad16f25bf04ebe6000e0c
URL:		http://pyopengl.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	python-Numeric-devel >= 22.0
BuildRequires:	python-devel >= 1:2.5
%pyrequires_eq	python-libs
Requires:	python-Numeric >= 22.0
BuildRequires:	rpmbuild(macros) >= 1.219
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
%setup -q -n %{module}-%{version}%{_beta} -a 1

%build
%{__python} setup.py build

cd %{module}-Demo-%{version}%{_beta}
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

cd %{module}-Demo-%{version}%{_beta}
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
#cp -a OpenGL/Demo $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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
%{py_sitescriptdir}/*.egg-info

%files examples
%defattr(644,root,root,755)
%{py_sitescriptdir}/PyOpenGL-Demo
