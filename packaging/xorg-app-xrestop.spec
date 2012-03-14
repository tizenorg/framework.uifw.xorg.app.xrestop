Name:       xorg-app-xrestop
Summary:    X11 server resource usage monitor
Version:    0.4
Release:    7
Group:      System/X11
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/app/xrestop-%{version}.tar.gz
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
%setup -q -n xrestop-%{version}


%build

%reconfigure --disable-static \
    --libdir=%{_datadir}

make %{?jobs:-j%jobs}

%install
%make_install

%docs_package

%files
%{_bindir}/xrestop

