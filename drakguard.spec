Summary:  Parental control tool
Name:     drakguard
Version:  0.7.3
Release:  %mkrel 2
Source0:  %name-%version.tar.lzma
License:  GPL
Group:    System/Configuration/Other
Url:      http://www.mandriva.com/
BuildRequires: perl-MDK-Common-devel gettext
Requires: drakxtools >= 10.22
Requires: drakx-net >= 0.41
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
