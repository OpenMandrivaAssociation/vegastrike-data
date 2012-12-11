%define	oname	vegastrike
%define	name	%{oname}-data
%define	version	0.5.1.r1
%define	release	%mkrel 1
%define	Summary	Data files for %{oname}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{Summary}
License:	GPLv2+
Group:		Games/Arcade
Source0:	%{name}-%{version}.tar.bz2
URL:		http://vegastrike.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	%{oname} >= %{version}

%description
%{Summary}

%prep
%setup -q 
# get rid of a few files we have no interest in packaging..
rm -rf aclocal.m4 configure.ac Makefile.in vegastrike-data.spec stamp-h.in bin
rm -rf `find -name CVS -type d` `find -name Makefile.am -type f`

# some cleanup
rm -r cockpits/bomber-cockpit.cpt/#cockpit.xmesh# \
 modules/builtin `find -name "*.xmesh"`
find . -type f -print0 | xargs -0 chmod -x
chmod +x units/findunits.py modules/webpageize.py
sed -i 's/\r//g' documentation/mission_howto.txt
# remove the stale included manpages and the .xls abonimation
rm documentation/*.1 documentation/*.xls


%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_gamesdatadir}/%{oname}
cp -a * %{buildroot}%{_gamesdatadir}/%{oname}
# include 'system files' strangely hidden in .vegastrike-0.5.0 directory
# for whatever reason...otherwise music & other stuff is gone...
# cp -a ./.%{name}-%{version} %{buildroot}/%{_gamesdatadir}/%{oname}


mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 vegastrike.xpm \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_gamesdatadir}/%{oname}
%{_gamesdatadir}/%{oname}/*
# %{_gamesdatadir}/%{oname}/.%{oname}-%{version}/*
# %{_gamesdatadir}/%{oname}/.%{oname}-%{version}/.system
%{_datadir}/icons/hicolor/128x128/apps/vegastrike.xpm





%changelog
* Wed Jun 13 2012 Zombie Ryushu <ryushu@mandriva.org> 0.5.1.r1-1mdv2012.0
+ Revision: 805467
- hidden dir issue?
- hidden dir issue?
- on copy issue
- no xmwesh
- no cvsignore
- fix setup name
- Upgrade to 0.5.1

* Wed Sep 22 2010 Tomas Kindl <supp@mandriva.org> 0.5.0-3mdv2011.0
+ Revision: 580620
- fix missing music #59963

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.5.0-2mdv2010.0
+ Revision: 434662
- rebuild

  + Emmanuel Andry <eandry@mandriva.org>
    - New version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.4.3-5mdv2009.0
+ Revision: 242920
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 0.4.3-3mdv2008.0
+ Revision: 70417
- use %%mkrel


* Thu Mar 03 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.4.3-2mdk
- split out music to own package to make it easier to maintain and making updates smaller
- clean out some more files we have no interest in packagaing

* Wed Feb 16 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.4.3-1mdk
- data version 0.4.3
- some file cleaning..

* Tue Oct 28 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.4.1-1mdk
- data version 0.4.1
- music version 0.3.1
- rearranged files a little

* Tue Apr 29 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.3.0-2mdk
- be sure to own correct dirs (*hugs oliviers bot*)

* Tue Apr 22 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.3.0-1mdk
- initial mdk release

