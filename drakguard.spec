Summary:  Parental control tool
Name:     drakguard
Version:  0.7.7
Release:  %mkrel 6
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

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS
%{_sbindir}/%{name}
/usr/lib/libDrakX/icons/*


%changelog
* Sun Aug 21 2011 Александр Казанцев <kazancas@mandriva.org> 0.7.7-5mdv2011.0
+ Revision: 696025
- remove obsoletes to drakguard-policy due cycling update error. You need manually delete drakguard-police to revert initial draguard.

* Sat Aug 20 2011 Александр Казанцев <kazancas@mandriva.org> 0.7.7-4
+ Revision: 695831
- avoid conflict with drakguard-policy packets

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.7-3
+ Revision: 663853
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.7-2mdv2011.0
+ Revision: 604818
- rebuild

* Mon Jun 28 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.7.7-1mdv2010.1
+ Revision: 549331
- 0.7.7:
- localization updates

* Thu May 27 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.7.6-1mdv2010.1
+ Revision: 546346
- 0.7.6:
- translation updates

* Tue May 25 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.7.5-1mdv2010.1
+ Revision: 545913
- 0.7.5:
- properly check if ACL support is enabled (#43335).

* Tue Apr 27 2010 Eugeni Dodonov <eugeni@mandriva.com> 0.7.4-1mdv2010.1
+ Revision: 539655
- 0.7.4:
- Added patch from Tiago Marques <tiago.marques@caixamagica.pt> to support
  application blocking, msec integration, white-black lists and UI improvements
  (#43335).

* Wed Nov 18 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.7.3-2mdv2010.1
+ Revision: 467174
- rebuild

* Fri May 15 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.7.3-1mdv2010.0
+ Revision: 376195
- 0.7.3:
- properly detecting dansguardian control level (#50700).

* Wed Apr 15 2009 Thierry Vignaud <tv@mandriva.org> 0.7.2-1mdv2009.1
+ Revision: 367387
- translation updates

* Mon Mar 30 2009 Thierry Vignaud <tv@mandriva.org> 0.7.1-1mdv2009.1
+ Revision: 362305
- translation updates

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.7-2mdv2009.1
+ Revision: 350838
- rebuild

* Tue Sep 30 2008 Thierry Vignaud <tv@mandriva.org> 0.7-1mdv2009.0
+ Revision: 289961
- translation updates

* Mon Sep 22 2008 Thierry Vignaud <tv@mandriva.org> 0.6-1mdv2009.0
+ Revision: 287019
- translation updates

* Mon Aug 18 2008 Olivier Blin <blino@mandriva.org> 0.5-3mdv2009.0
+ Revision: 273296
- bump drakx-net API requirements (#42788)

* Wed Aug 13 2008 Olivier Blin <blino@mandriva.org> 0.5-2mdv2009.0
+ Revision: 271443
- 0.5
- time control settings (using "time" iptables module)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.4-2mdv2009.0
+ Revision: 220684
- rebuild

* Thu Apr 03 2008 Olivier Blin <blino@mandriva.org> 0.4-1mdv2008.1
+ Revision: 192245
- 0.4
- fix whitelisting websites, by using a site list, and not an url list
- add wait message when applying configuration
- hide inactive time control pane (the "time" netfilter module does
  not work out of the box in current kernel)

* Thu Apr 03 2008 Olivier Blin <blino@mandriva.org> 0.3-1mdv2008.1
+ Revision: 192201
- 0.3
- really quit gui when needed (like when packages instalaltion is
  cancelled, #39557)
- allow to add/remove users from users whitelist

* Thu Mar 27 2008 Olivier Blin <blino@mandriva.org> 0.2-1mdv2008.1
+ Revision: 190757
- require recent drakxtools (to be able to use stock icons in buttons)
- require recent drakx-net (#39437)
- 0.2
- adapt dansguardian language to system locale
- use scrolled window for user lists
- use stock icons for add/remove buttons
- do not allow to enter an url twice in blacklist/whitelist
- strip protocol when adding an url to blacklist/whitelist
- reload shorewall config if it has just been installed
- do not write conf if disabled
- do not write shorewall conf if shorewall disabled
- ask only one time to install packages (suggested by pterjan)
- rename icons (mostly for MCC)

* Thu Mar 27 2008 Olivier Blin <blino@mandriva.org> 0.1-1mdv2008.1
+ Revision: 190585
- initial version
- create drakguard

