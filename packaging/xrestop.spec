Summary: X Resource Monitor
Name: xrestop
Version: 0.4
Release: 10
License: GPL-2.0+
Group: Development/Tools
URL: http://www.freedesktop.org/Software/xrestop
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

BuildRequires: ncurses-devel libXres-devel libXext-devel libX11-devel
BuildRequires: libXau-devel

%description
A utility to monitor application usage of X resources in the X Server, and
display them in a manner similar to 'top'.  This is a very useful utility
for tracking down application X resource usage leaks.

%prep
%setup -q

%build
%reconfigure
make %{?jobs:-j%jobs}
# SUBDIRS=

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
make DESTDIR="$RPM_BUILD_ROOT" install
#SUBDIRS=

%remove_docs

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root,-)
/usr/share/license/%{name}
#%doc AUTHORS COPYING NEWS README
%{_bindir}/xrestop
#%{_mandir}/man1/xrestop.1*
