%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	NNTP
%define		_pearname	%{_class}_%{_subclass}
%define		_status		alpha

Summary:	%{_pearname} - communicate with an NNTP server
Summary(pl):	%{_pearname} - komunikacja z serwerem NNTP
Name:		php-pear-%{_pearname}
Version:	0.10.3
Release:	2
License:	W3C / PHP 2.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b46a324e8e6a46d7d449b5bb45a38bb2
URL:		http://pear.php.net/package/Net_NNTP/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Complete class for communicating with an NNTP server (this is: the
USENET), including: post, view, list, authentication, overview, header
manipulation, NNTP commands debugger, etc.

In PEAR status of this package is: %{_status}.

%description -l pl
Kompletna klasa do komunikacja z serwerem NNTP (USENET), zawierająca:
wysyłanie, przeglądanie, listowanie, autentyfikacja, przegląd,
manipulacje nagłówkami, debugger komend NNTP, etc.

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
%doc %{_pearname}-%{version}/docs/examples
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
