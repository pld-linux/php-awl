Summary:	Andrew's Web Libraries
Summary(pl.UTF-8):   Andrew's Web Libraries - biblioteki dla aplikacji WWW
Name:		php-awl
Version:	0.9
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/rscds/awl_%{version}.tar.gz
# Source0-md5:	553836e5638469fb4ab2bee307a53589
URL:		http://rscds.sourceforge.net/
Requires:	php(pgsql)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Andrew's Web Libraries.

%description -l pl.UTF-8
Andrew's Web Libraries - biblioteki dla aplikacji WWW.

%prep
%setup -q -n awl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/php/awl

cp -a inc dba $RPM_BUILD_ROOT%{_datadir}/php/awl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{_datadir}/php/awl
