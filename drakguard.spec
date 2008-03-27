Summary:  Parental control tool
Name:     drakguard
Version:  0.2
Release:  %mkrel 1
Source0:  %name-%version.tar.bz2
License:  GPL
Group:    System/Configuration/Other
Url:      http://www.mandriva.com/
BuildRequires: perl-MDK-Common-devel gettext
Requires: drakxtools
Requires: drakx-net >= 0.32
BuildRoot: %_tmppath/%name-%version-buildroot
BuildArch: noarch

%description
This tool allows to configure parental control. It can block access to
web sites and restrict connection during a specified timeframe.

%prep
%setup -q

%build
%make

%install
rm -fr %{buildroot}
%makeinstall_std
%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS
%{_sbindir}/%{name}
%{_sbindir}/*
/usr/lib/libDrakX/icons/*
