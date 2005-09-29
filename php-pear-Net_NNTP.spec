%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	NNTP
%define		_pearname	%{_class}_%{_subclass}
%define		_status		stable

Summary:	%{_pearname} - communicate with an NNTP server
Summary(pl):	%{_pearname} - komunikacja z serwerem NNTP
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1.1
License:	W3C / PHP 2.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c51bfa31c55d2f784171373d9532980c
URL:		http://pear.php.net/package/Net_NNTP/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Complete class for communicating with an NNTP server (this is: the
USENET), including: post, view, list, authentication, overview, header
manipulation, NNTP commands debugger, etc.

In PEAR status of this package is: %{_status}.

%description -l pl
Kompletna klasa umo¿liwiaj±ca komunikacjê z serwerem NNTP (USENET),
zawieraj±ca: wysy³anie, przegl±danie, listowanie, uwierzytelnianie,
przegl±d, manipulacjê nag³ówkami, debugger komend NNTP, etc.

Ta klasa ma w PEAR status %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
