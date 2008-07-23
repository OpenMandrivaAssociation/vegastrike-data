%define	oname	vegastrike
%define	name	%{oname}-data
%define	version	0.4.3
%define	release	%mkrel 5
%define	Summary	Data files for %{oname}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{Summary}
License:	GPL
Group:		Games/Arcade
Source0:	%{oname}-data-%{version}.tar.bz2
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

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_gamesdatadir}/%{oname}
cp -a * $RPM_BUILD_ROOT%{_gamesdatadir}/%{oname}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mv $RPM_BUILD_ROOT%{_gamesdatadir}/%{oname}/documentation/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
#%{__tar} -jxf %{SOURCE0} -C $RPM_BUILD_ROOT%{_gamesdatadir}/%{oname}
#%{__tar} -jxf %{SOURCE1} -C $RPM_BUILD_ROOT%{_gamesdatadir}/%{oname}
#%{__rm} -f $RPM_BUILD_ROOT%{_gamesdatadir}/%{oname}/data/*.spec

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_gamesdatadir}/%{oname}
%{_gamesdatadir}/%{oname}/*
%{_mandir}/man1/*.1*

