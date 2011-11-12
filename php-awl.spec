# TODO:
# - R: /bin/sh ??? (what pulls that?)
%include	/usr/lib/rpm/macros.php
%define		php_min_version 5.1.0
Summary:	Andrew's Web Libraries
Summary(pl.UTF-8):	Andrew's Web Libraries - biblioteki dla aplikacji WWW
Name:		php-awl
Version:	0.49
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://debian.mcmillan.net.nz/packages/awl/awl-%{version}.tar.gz
# Source0-md5:	f8a7e6645eb5417df4a0f96af704e9d3
URL:		http://davical.org/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-date
Requires:	php-gettext
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# do not want any pear deps
%define		_noautopear	pear

# exclude optional php dependencies
%define		_noautophp	%{nil}

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
Andrew's Web Libraries.

%description -l pl.UTF-8
Andrew's Web Libraries - biblioteki dla aplikacji WWW.

%prep
%setup -q -n awl-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/awl
cp -a inc dba $RPM_BUILD_ROOT%{php_data_dir}/awl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{php_data_dir}/awl
