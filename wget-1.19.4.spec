%define name        wget 
%define release     4
%define version     1.19.4
%define buildroot   %{_topdir}/%{name}-%{version}-%{release}-buildroot
%define LINKDIR     /usr/local/bin 
BuildRoot:  	%{buildroot}

Name:		%{name}
Release:        %{release}
Version:	%{version}
Summary:	rpm build of wget-1.19.4

Group:		Development/Tools
License:	GPL
Source0:	%{name}-%{version}.tar.gz
Requires:	gnutls gnutls-devel glibc-devel glibc-headers kernel-headers kernel-devel

%description
The GNU wget program downloads files from the Internet using the command-line.

%prep
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%setup -q

%build
./configure	
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
install -m 755 -d ${RPM_BUILD_ROOT}%{LINKDIR}
make install prefix=$RPM_BUILD_ROOT/opt/%{name}-%{version}.%{release}
#install -m 755 -D $RPM_BUILD_ROOT/opt/%{name}-%{version}.%{release}/bin/%{name} ${RPM_BUILD_ROOT}%{LINKDIR}/%{name}
echo "Package build is Done"
echo "coping files from Build to prefix dir"
echo "All done Dipanjan"

%post
# Create symbolic links to files
ln -fs $RPM_BUILD_ROOT/opt/%{name}-%{version}.%{release}/bin/%{name} ${RPM_BUILD_ROOT}%{LINKDIR}/%{name}

%postun
#=========================== Deletion of Symbolic links
rm -f ${RPM_BUILD_ROOT}%{LINKDIR}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/opt/*
/usr/*

%changelog
* Sat Aug 11 2018 - DM
- final cleanup
* Fri Aug 10 2018 - DM
- New rpm for WGET
- change package dir name
- link create
