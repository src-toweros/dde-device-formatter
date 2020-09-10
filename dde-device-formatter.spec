%bcond_with check

%global with_debug 1
%if 0%{?with_debug}
%global debug_package   %{nil}
%endif

Name:           dde-device-formatter
Version:        0.0.1.1
Release:        1
Summary:        A simple graphical interface for creating file system in a block device.
License:        GPLv3+
URL:            https://github.com/linuxdeepin/dde-device-formatter
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: dtkwidget-devel dtkgui-devel dtkcore-devel dde-qt-dbus-factory-devel deepin-gettext-tools
BuildRequires: udisks2-qt5 udisks2-qt5-devel qt5-linguist qt5-qtbase-devel qt5-qtx11extras-devel

%description
A simple graphical interface for creating file system in a block device.

%prep
%autosetup

%build
export PATH=$PATH:/usr/lib64/qt5/bin
mkdir build && cd build
%{_libdir}/qt5/bin/qmake ..
%{__make}

%install
pushd %{_builddir}/%{name}-%{version}/build
%make_install INSTALL_ROOT=%{buildroot}
popd

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/*

%doc README.md
%license LICENSE

%changelog
* Thu Sep 10 2020 chenbo pan <panchenbo@uniontech.com> - 0.0.1.1-1
- Initial package build
