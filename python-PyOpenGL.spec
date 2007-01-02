%define		module	PyOpenGL
Summary:	OpenGL bindings for Python
Summary(pl):	Dowi±zania do OpenGL dla Pythona
Name:		python-%{module}
Version:	2.0.2.01
Release:	2
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pyopengl/%{module}-%{version}.tar.gz
# Source0-md5:	3deac41df71fc98c814330d1eb54ce71
Patch0:		%{name}-link.patch
URL:		http://pyopengl.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	python-Numeric-devel >= 22.0
BuildRequires:	python-devel >= 2.2
%pyrequires_eq	python-libs
Requires:	python-Numeric >= 22.0
Obsoletes:	PyOpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
OpenGL bindings for Python including support for GL extensions, GLU,
WGL, GLUT, GLE, and Tk.

%description -l pl
Dowi±zania do OpenGL dla Pythona wraz z rozszerzeniami GL, GLU, WGL,
GLUT, GLE i Tk.

%package examples
Summary:	Demos for PyOpenGL
Summary(pl):	Programy demonstracyjne dla pakietu PyOpenGL
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Demos for PyOpenGL.

%description examples -l pl
Programy demonstracyjne dla pakietu PyOpenGL.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a OpenGL/Demo $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/OpenGL/{Demo,doc}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* OpenGL/doc/xhtml/*
%dir %{py_sitedir}/OpenGL
%{py_sitedir}/OpenGL/__init__.py[co]
%{py_sitedir}/OpenGL/quaternion.py[co]
%{py_sitedir}/OpenGL/trackball.py[co]
%{py_sitedir}/OpenGL/scripts
%{py_sitedir}/OpenGL/version
# GL
%dir %{py_sitedir}/OpenGL/GL
%dir %{py_sitedir}/OpenGL/GL/[!G_]*
%dir %{py_sitedir}/OpenGL/GL/_3DFX
%{py_sitedir}/OpenGL/GL/*/*.py[co]
%attr(755,root,root) %{py_sitedir}/OpenGL/GL/*/*.so
%{py_sitedir}/OpenGL/GL/GL__init__.py[co]
%{py_sitedir}/OpenGL/GL/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/OpenGL/GL/_GL__init__.so
# GLU
%dir %{py_sitedir}/OpenGL/GLU
%dir %{py_sitedir}/OpenGL/GLU/[!G]*
%{py_sitedir}/OpenGL/GLU/*/*.py[co]
%attr(755,root,root) %{py_sitedir}/OpenGL/GLU/*/*.so
%{py_sitedir}/OpenGL/GLU/GLU__init__.py[co]
%{py_sitedir}/OpenGL/GLU/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/OpenGL/GLU/_GLU__init__.so
# GLE
%{py_sitedir}/OpenGL/GLE.py[co]
%attr(755,root,root) %{py_sitedir}/OpenGL/_GLE.so
# GLUT
%{py_sitedir}/OpenGL/GLUT.py[co]
%attr(755,root,root) %{py_sitedir}/OpenGL/_GLUT.so
# GLX
%{py_sitedir}/OpenGL/GLX
# Tk
%{py_sitedir}/OpenGL/Tk
# WGL
%{py_sitedir}/OpenGL/WGL

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
