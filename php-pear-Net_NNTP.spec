%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	NNTP
%define		_pearname	%{_class}_%{_subclass}
%define		_status		alpha
%define		subver	a1
%define		rel		1
Summary:	%{_pearname} - communicate with an NNTP server
Summary(pl.UTF-8):	%{_pearname} - komunikacja z serwerem NNTP
Name:		php-pear-%{_pearname}
Version:	1.5.0
Release:	0.%{subver}.%{rel}
License:	W3C / PHP 2.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	491f1926dd8d9189b771d895642bf8c3
URL:		http://pear.php.net/package/Net_NNTP/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Net_Socket >= 1.0.3
Requires:	php-pear-PEAR-core >= 1:1.4.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(Log.*)

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

mv docs/%{_pearname}/docs/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}
