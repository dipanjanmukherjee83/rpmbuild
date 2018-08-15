%define name        wget 
%define release     5
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
Packager:       Dipanjan Mukherjee

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
#==Deletion of Symbolic links and opt dir

case "$1" in
  0)
    # This is an un-installation.
    rm -f ${RPM_BUILD_ROOT}%{LINKDIR}/%{name}
    rm -rf /opt/%{name}-%{version}.%{release}
  ;;
  1)
    # This is an upgrade.
    # Do nothing.
    :
  ;;
esac

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/opt/*
/usr/*

%changelog
* Wed Aug 15 2018 - DM
- add delete /opt in postun section and packager name and upgrade release
* Sat Aug 11 2018 - DM
- final cleanup
* Fri Aug 10 2018 - DM
- New rpm for WGET
- change package dir name
- link create
