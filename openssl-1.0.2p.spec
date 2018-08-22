%define name        openssl
%define version     1.0.2p
%define release     1
%define buildroot   %{_topdir}/%{name}-%{version}-buildroot
%define LINKDIR     /usr/local/bin


Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        open ssl rpm package build

Group:          Development/Tools
License:        GPL
Source0:        %{name}-%{version}.tar.gz 

Requires:       gnutls gnutls-devel glibc-devel glibc-headers kernel-headers kernel-devel
Packager:       Dipanjan Mukherjee

BuildRoot:      %{buildroot}


%description
The GNU opensll package build. 

%prep
[ ${RPM_BUILD_ROOT} != "/" ] && rm -rf ${RPM_BUILD_ROOT}
%setup -q

%pre
install -m 755 -d ${RPM_BUILD_ROOT}/opt/%{name}-%{version}
install -m 755 -d ${RPM_BUILD_ROOT}%{LINKDIR}


%build
./config --prefix=${RPM_BUILD_ROOT}/opt/%{name}-%{version} --openssldir=${RPM_BUILD_ROOT}/opt/%{name}-%{version} 
make 
make test


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make install 
echo "Package build is Done"


%post
# Create symbolic links to files
ln -fs $RPM_BUILD_ROOT/opt/%{name}-%{version}/bin/%{name} ${RPM_BUILD_ROOT}%{LINKDIR}/%{name}


%postun
#==Deletion of Symbolic links and /opt/%{Name} dir

case "$1" in
  0)
    # This is an un-installation.
    rm -f %{LINKDIR}/%{name}
    rm -rf /opt/%{name}-%{version}
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
%defattr(-,root,root,-)
/opt/*
/usr/*


%changelog
* Wed Aug 22 2018 - DM
- New rpm for openssl
