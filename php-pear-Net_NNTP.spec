%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       NNTP
%define		_pearname	%{_class}_%{_subclass}
%define		_status		alpha
Summary:	%{_pearname} - Communicate with an NNTP server
Summary(pl):	%{_pearname} - Komunikacja z serverem NNTP
Name:		php-pear-%{_pearname}
Version:	0.9.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	1748a8d1a9cf5194f4f8bd91cb117b6f
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Complete class for communicating with an NNTP server (this is: the
USENET), including: post, view, list, authentication, overview, header
manipulation, NNTP commands debugger, etc.

This class has in PEAR status: %{_status}.

%description -l pl
Kompletna klasa do komunikacja z serwerem NNTP (USENET), zawieraj±ca:
wysy³anie, przegl±danie, listowanie, autentyfikacja, przegl±d,
manipulacje nag³ówkami, debugger komend NNTP, etc.

Ta klasa ma w PEAR status %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/README
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
