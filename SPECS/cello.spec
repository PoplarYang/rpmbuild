Name:           cello
Version:        0.1
Release:        1%{?dist}
Summary:        Hello World example implemented in clang

License:        GPLv3+
URL:            https://www.example.com/%{name}
Source0:        cello-%{version}.tar.gz
BuildArch:      mips64el

%description


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%files
/usr/local/bin/cello

%changelog
* Sun Aug 10 2020 https://github.com/PoplarYang/rpmbuild <echohelloyang@gmail.com> - %{Release}
- add cello
