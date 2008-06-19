%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	NNTP
%define		_pearname	%{_class}_%{_subclass}
%define		_status		stable

Summary:	%{_pearname} - communicate with an NNTP server
Summary(pl.UTF-8):	%{_pearname} - komunikacja z serwerem NNTP
Name:		php-pear-%{_pearname}
Version:	1.4.0
Release:	1
License:	W3C / PHP 2.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	dae6d336c87668e311f6d1e5603e9207
URL:		http://pear.php.net/package/Net_NNTP/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Net_Socket >= 1.0.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Complete class for communicating with an NNTP server (this is: the
USENET), including: post, view, list, authentication, overview, header
manipulation, NNTP commands debugger, etc.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Kompletna klasa umożliwiająca komunikację z serwerem NNTP (USENET),
zawierająca: wysyłanie, przeglądanie, listowanie, uwierzytelnianie,
przegląd, manipulację nagłówkami, debugger komend NNTP, etc.

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
%{php_pear_dir}/%{_class}/%{_subclass}
