%define systemddir %{_usr}/lib/systemd/system
%define presetdir  %{_usr}/lib/systemd/system-preset
%define udevdir    %{_usr}/lib/udev/rules.d
%global debug_package  %{nil}

Name:		can-utils-vscom-systemd
Version:	1.0.0
Release:	1%{?ci_build_id}%{?dist}
Summary:	can udev rules

Group:		System
License:	GPL
URL:		https://github.com/bhrte/can-utils-systemd.git
Source0:	usb-can@.service
Source1:	usb-can-up@.service
Source2:	90-vscom-slcan.rules
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires:
Requires:	systemd
Requires:	can-utils

%description
can udev rules

%prep
%setup -T -c -n can-utils-systemd
cp %{SOURCE0} .
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
echo build
pwd
ls -l

%install
echo make_install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{systemddir}
mkdir -p %{buildroot}%{udevdir}
install --mode=0644 *.service %{buildroot}%{systemddir}
install --mode=0644 *.rules %{buildroot}%{udevdir}

%clean
rm -rf %{buildroot}

%post
systemctl daemon-reload

%files
%defattr(-,root,root,-)
%{systemddir}/*.service
%{udevdir}/*.rules



%changelog

