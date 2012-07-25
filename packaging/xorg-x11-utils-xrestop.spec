
Name:       xorg-x11-utils-xrestop
Summary:    X11 server resource usage monitor
Version:    0.4
Release:    7
Group:      System/X11
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.gz
Source1001: packaging/xorg-x11-utils-xrestop.manifest 
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(ice)


%description
xrestop uses the X-Resource extension to provide top(1)-like statistics
for each connected X11 client's server-side resource usage. It is intended
as a developer tool to aid more efficient server resource usage and debug
server-side resource leakage.
.
xrestop requires the X-Resource extension, supported by XFree86 4.3 and
above, and by the freedesktop.org X server.


%prep
%setup -q -n %{name}-%{version}


%build
cp %{SOURCE1001} .

%reconfigure --disable-static \
    --libdir=%{_datadir}

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install





%files
%manifest xorg-x11-utils-xrestop.manifest
%defattr(-,root,root,-)
%{_bindir}/xrestop
%{_mandir}/man1/xrestop.1.gz

