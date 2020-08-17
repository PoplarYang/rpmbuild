Name:           s3test
Version:        0.1
Release:        1%{?dist}
Summary:        simple storage service test implemented in golang

License:        GPLv3+
URL:            https://github.com/PoplarYang/rpmbuild
#Source0:        s3-test_linux_mips64el
Source0:        http://pkzxwcntr.bkt.clouddn.com/s3-test_linux_mips64el
BuildArch:      mips64el

%description

%install
install -d %{buildroot}/usr/local/bin/
install -m 0755 %{SOURCE0} %{buildroot}/usr/local/bin/s3test

%files
/usr/local/bin/s3test

%changelog
* Sun Aug 10 2020 https://github.com/PoplarYang/rpmbuild <echohelloyang@gmail.com> - %{Release}
- add simple storage service test
