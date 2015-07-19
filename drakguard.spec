Summary:	Parental control tool
Name:		drakguard
Version:	0.7.7
Release:	17
License:	GPLv2
Group:		System/Configuration/Other
Url:		http://www.mandriva.com/
Source0:	%{name}-%{version}.tar.lzma
Patch0:		drakguard-0.7.7-fix_acl_enabled_test.patch
Patch1:		drakguard-0.7.7-use-kerneltz-option.patch
Patch2:		drakguard-0.7.7-squid3.2.patch
Patch3:		drakguard-0.7.7-urpmi.patch
BuildArch:	noarch
BuildRequires:	gettext
BuildRequires:	perl-MDK-Common-devel
Requires:	drakxtools >= 10.22
Requires:	drakx-net >= 0.41

%description
This tool allows to configure parental control. It can block access to
web sites and restrict connection during a specified timeframe.

%prep
%setup -q
%apply_patches

%build
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc NEWS
%{_sbindir}/%{name}
/usr/lib/libDrakX/icons/*

