%define		module	PyOpenGL
%include	/usr/lib/rpm/macros.python
Summary:	OpenGL bindings for Python
Summary(pl):	Dowi±zania do OpenGL dla Pythona
Name:		python-%{module}
Version:	2.0.0.44
Release:	2
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://prdownloads.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
Patch0:		%{name}-x11.patch
URL:		http://pyopengl.sourceforge.net/
BuildRequires:	glut-devel
BuildRequires:	python-numpy-devel
BuildRequires:	python-devel >= 2.2
BuildRequires:	OpenGL-devel
BuildRequires:	rpm-pythonprov
%requires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	%{module}

%define         _noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1
%define         _noreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
OpenGL bindings for Python including support for GL extensions, GLU,
WGL, GLUT, GLE, and Tk.

%description -l pl
Dowi±zania do OpenGL dla Pythona (GL, GLU, WGL, GLUT, GLE i Tk).

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

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

gzip -9nf README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz OpenGL/doc/html/*
%attr(-, root,root) %{py_sitedir}/OpenGL
