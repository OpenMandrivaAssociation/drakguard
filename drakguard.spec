Summary:	Parental control tool
Name:		drakguard
Version:	1.3
Release:	1
License:	GPLv2
Group:		System/Configuration/Other
Url:		http://gitweb.mageia.org/software/drakguard
Source0:	%{name}-%{version}.tar.xz
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

