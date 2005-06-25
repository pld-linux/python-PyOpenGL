%define		module	PyOpenGL
Summary:	OpenGL bindings for Python
Summary(pl):	Dowiązania do OpenGL dla Pythona
Name:		python-%{module}
Version:	2.0.2.01
Release:	1
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://dl.sourceforge.net/pyopengl/%{module}-%{version}.tar.gz
# Source0-md5:	3deac41df71fc98c814330d1eb54ce71
URL:		http://pyopengl.sourceforge.net/
BuildRequires:	glut-devel
BuildRequires:	python-numpy-devel
BuildRequires:	python-devel >= 2.2
BuildRequires:	OpenGL-devel
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	%{module}

%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1
%define		_noreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
OpenGL bindings for Python including support for GL extensions, GLU,
WGL, GLUT, GLE, and Tk.

%description -l pl
Dowiązania do OpenGL dla Pythona (GL, GLU, WGL, GLUT, GLE i Tk).

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags} -L /usr/X11R6/%{_lib}"; export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* OpenGL/doc/xhtml/*
%attr(-, root,root) %{py_sitedir}/OpenGL
