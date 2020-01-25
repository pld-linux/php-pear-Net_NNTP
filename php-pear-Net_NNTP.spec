%define		status		stable
%define		pearname	Net_NNTP
Summary:	%{pearname} - communicate with an NNTP server
Summary(pl.UTF-8):	%{pearname} - komunikacja z serwerem NNTP
Name:		php-pear-%{pearname}
Version:	1.5.2
Release:	2
License:	W3C / PHP 2.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	9ebaa7ec650588f2a7bd9c17e2121b42
URL:		http://pear.php.net/package/Net_NNTP/
BuildRequires:	php-pear-PEAR >= 1:1.4.5
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-pear-Net_Socket >= 1.0.3
Requires:	php-pear-PEAR-core >= 1:1.4.0
Suggests:	php-pear-Log
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(Log.*)

%description
Complete class for communicating with an NNTP server (this is: the
USENET), including: post, view, list, authentication, overview, header
manipulation, NNTP commands debugger, etc.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Kompletna klasa umożliwiająca komunikację z serwerem NNTP (USENET),
zawierająca: wysyłanie, przeglądanie, listowanie, uwierzytelnianie,
przegląd, manipulację nagłówkami, debugger komend NNTP, etc.

Ta klasa ma w PEAR status %{status}.

%prep
%pear_package_setup

mv docs/%{pearname}/docs/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
%pear_package_install

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/NNTP
%{_examplesdir}/%{name}-%{version}
