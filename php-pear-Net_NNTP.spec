%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       NNTP
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Communicate with an NNTP server
Summary(pl):	%{_pearname} - Komunikacja z serverem NNTP
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	33ffa08d2adccaa2a8b285dd9d2d988a
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Complete class for communicating with an NNTP server (this is: the
USENET), including: post, view, list, authentication, overview, header
manipulation, NNTP commands debugger, etc.

%description -l pl
Kompletna klasa do komunikacja z serwerem NNTP (USENET), zawieraj±ca:
wysy³anie, przegl±danie, listowanie, autentyfikacja, przegl±d,
manipulacje nag³ówkami, debugger komend NNTP, etc.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/README
%{php_pear_dir}/%{_class}/*.php
