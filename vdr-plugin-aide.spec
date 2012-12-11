
%define plugin	aide
%define name	vdr-plugin-%plugin
%define version	0.0.2
%define rel	19

Summary:	VDR plugin: VDR Aide
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://vdr.bluox.org/download/?path=vdr-aide/
Source:		http://vdr.bluox.org/download/vdr-aide/vdr-%plugin-%version.tar.bz2
Source1:	aide-deu.tar.bz2
Source2:	aide-dutch.tar.bz2
Source3:	aide-eng.tar.bz2
Source4:	aide-rus.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
An OSD Help Browser for VDR. You can read VDR User Manual and other
plain text help files on the TV screen.

%prep
%setup -q -n %plugin-%version -a 1 -a 2 -a 3 -a 4
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY aide deu dut eng rus




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2-19mdv2010.0
+ Revision: 401089
- actually rebuild for new VDR

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2-18mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2-17mdv2009.1
+ Revision: 359273
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-16mdv2009.0
+ Revision: 197890
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-15mdv2009.0
+ Revision: 197622
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-14mdv2008.1
+ Revision: 145001
- rebuild for new vdr

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2-13mdv2008.1
+ Revision: 144965
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-12mdv2008.1
+ Revision: 103051
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-11mdv2008.0
+ Revision: 49960
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-10mdv2008.0
+ Revision: 42047
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2-9mdv2008.0
+ Revision: 22682
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-8mdv2007.0
+ Revision: 90882
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-7mdv2007.1
+ Revision: 73935
- rebuild for new vdr
- Import vdr-plugin-aide

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-5mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-3mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-2mdv2007.0
- rebuild for new vdr

* Sun Jun 11 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2-1mdv2007.0
- initial Mandriva release

