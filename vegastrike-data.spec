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
rm -r cockpits/bomber-cockpit.cpt/#cockpit.xmesh# meshes/supernova.bmp.xmesh~ \
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
cp -a ./.%{oname}-%{version} %{buildroot}/%{_gamesdatadir}/%{oname}


mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 vegastrike.xpm \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_gamesdatadir}/%{oname}
%{_gamesdatadir}/%{oname}/*
%{_gamesdatadir}/%{oname}/.%{oname}-%{version}/*
%{_gamesdatadir}/%{oname}/.%{oname}-%{version}/.system
%{_datadir}/icons/hicolor/128x128/apps/vegastrike.xpm



