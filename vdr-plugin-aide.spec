
%define plugin	aide
%define name	vdr-plugin-%plugin
%define version	0.0.2
%define rel	14

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
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
An OSD Help Browser for VDR. You can read VDR User Manual and other
plain text help files on the TV screen.

%prep
%setup -q -n %plugin-%version -a 1 -a 2 -a 3 -a 4

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


