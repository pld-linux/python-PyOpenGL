
%define		module	PyOpenGL

%include	/usr/lib/rpm/macros.python
Summary:	OpenGL bindings for Python
Summary(pl):	Dowi±zania do OpenGL dla Pythona
Name:		python-%{module}
Version:	2.0.0.34b3
Release:	1
License:	LGPL
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Source0:	http://prdownloads.sourceforge.net/%{module}/%{module}-%{version}.tar.gz
URL:		http://pyopengl.sourceforge.net/
%requires_eq	python
BuildRequires:	python-devel >= 1.5
BuildRequires:	OpenGL-devel
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	%{module}

%define         _noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1
%define         _noreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
OpenGL bindings for Python including support for GL extensions, GLU,
WGL, GLUT, GLE, and Tk.

%description -l pl
Dowi±zania do OpenGL dla Pythona.

%package devel
Summary:	C header files for pygame modules
Summary(pl):	Pliki nag³ówkowe jêzyka C modu³ów pygame
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
%requires_eq	python
Requires:	%{name} = %{version}

%description devel
C header files for pygame modules.

%description devel -l pl
Pliki nag³ówkowe jêzyka C modu³ów pygame.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags} -I%{_prefix}/X11R6/include"; export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

gzip -9nf README* WHATSNEW 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz docs/* examples
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.ttf
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%{py_sitedir}/%{module}/*.py[co]

%files devel
%defattr(644,root,root,755)
%{py_incdir}/%{module}
