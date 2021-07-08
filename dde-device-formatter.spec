Name:           dde-device-formatter
Version:        0.0.1.6
Release:        1
Summary:        A simple graphical interface for creating file system in a block device
License:        GPLv3+
URL:            https://github.com/linuxdeepin/dde-device-formatter
Source0:        %{name}-%{version}.tar.gz

BuildRequires: dtkwidget-devel dtkgui-devel dtkcore-devel qt5-devel
BuildRequires: dtkwidget-devel
BuildRequires: dtkgui-devel
BuildRequires: udisks2-qt5-devel
BuildRequires: deepin-gettext-tools

%description
%{summary}.

%prep
%autosetup

%build
export PATH=%{_qt5_bindir}:$PATH
mkdir build && pushd build
%qmake_qt5 ../ VERSION=%{version} LIB_INSTALL_DIR=%{_libdir} DEFINES+="VERSION=%{version}"
%make_build
popd

%install
%make_install -C build INSTALL_ROOT="%buildroot"


%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/*

%changelog
* Thu Jul 08 2021 weidong <weidong@uniontech.com> - 0.0.1.6-1
- Update 0.0.1.6

* Thu Sep 10 2020 chenbo pan <panchenbo@uniontech.com> - 0.0.1.1-1
- Initial package build
