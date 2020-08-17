Name:           openresty
Version:        1.17.8.2
Release:        1%{?dist}
Summary:        OpenResty, scalable web platform by extending NGINX with Lua

License:        BSD
URL:            https://openresty.org/download/openresty-%{version}.tar.gz
Source0:        openresty-%{version}.tar.gz
Source1:        openresty.service
Requires:       pcre-devel openssl-devel gcc curl
BuildRequires:  pcre-devel openssl-devel gcc curl
#BuildArch:      mips64el
BuildArch:      x86_64

%description
This package contains the core server for OpenResty. Built for production
uses.

OpenResty is a full-fledged web platform by integrating the standard Nginx
core, LuaJIT, many carefully written Lua libraries, lots of high quality
3rd-party Nginx modules, and most of their external dependencies. It is
designed to help developers easily build scalable web applications, web
services, and dynamic web gateways.

By taking advantage of various well-designed Nginx modules (most of which
are developed by the OpenResty team themselves), OpenResty effectively
turns the nginx server into a powerful web app server, in which the web
developers can use the Lua programming language to script various existing
nginx C modules and Lua modules and construct extremely high-performance
web applications that are capable to handle 10K ~ 1000K+ connections in
a single box.

%prep
%setup -q


%build
./configure
make %{?_smp_mflags}


%install
install -d %{buildroot}/usr/local/ %{buildroot}/usr/lib/systemd/system/
make install DESTDIR=%{buildroot}
cp %{SOURCE1} %{buildroot}/usr/lib/systemd/system/

%files
/usr/local/openresty
/usr/lib/systemd/system/openresty.service

%changelog
* Sun Aug 17 2020 https://github.com/PoplarYang/rpmbuild <echohelloyang@gmail.com> - %{release}
- initial openresty
