#
#
Summary:	Andrew's Web Libraries
Name:		php-awl
Version:	0.9
Release:	1
License:	- (enter GPL/GPL v2/LGPL/BSD/BSD-like/other license name here)
Group:		Applications
Source0:	http://dl.sourceforge.net/rscds/awl_0.9.tar.gz
# Source0-md5:	553836e5638469fb4ab2bee307a53589
URL:		http://rscds.sourceforge.net/
Requires:	php-pgsql
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Andrew's Web Libraries.

%prep
%setup -q -n awl

%build
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/php/awl
cp -a inc dba $RPM_BUILD_ROOT/%{_datadir}/php/awl/


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{_datadir}/php/awl
