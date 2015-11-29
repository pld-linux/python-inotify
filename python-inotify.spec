#
%define		module		inotify
#
Summary:	Inotify module for Python
Summary(pl.UTF-8):	Moduł inotify dla języka Python
Name:		python-%{module}
Version:	0.1.0
Release:	2
License:	GPL, other
Group:		Libraries/Python
Source0:	http://rudd-o.com/wp-content/uploads/projects/files/python-inotify/python-%{module}-%{version}.tar.gz
# Source0-md5:	361bcab2f0cd57cdaf6fe6fe433778b0
URL:		http://rudd-o.com/projects/python-inotify/
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A module designed to make the Linux inotify interface programmatically
available for Python.

%description -l pl.UTF-8
TODO

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%{__install} -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_install

%py_postclean
mv $RPM_BUILD_ROOT%{_bindir}/inotify $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE ChangeLog TODO
%{py_sitedir}/*
%{_examplesdir}/%{name}-%{version}
