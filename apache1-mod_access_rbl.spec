%define		mod_name	access_rbl
%define 	apxs		/usr/sbin/apxs1
Summary:	Apache module: access based on RBL
Summary(pl.UTF-8):	Moduł Apache'a: dostęp oparty o RBL
Name:		apache1-mod_%{mod_name}
Version:	0.1
Release:	0.2
License:	Apache Group
Group:		Networking/Daemons
Source0:	http://www.blars.org/mod_access_rbl.tar.gz
# Source0-md5:	9a3a513435e57fe589d6b0cb8c7d7eb4
URL:		http://www.blars.org/mod_access_rbl.html
BuildRequires:	apache1-devel >= 1.3.39
Requires:	apache1(EAPI)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		_sysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)

%description
mod_access_rbl is a superset replacement for mod_access. Both modules
cannot be used at the same time.

%description -l pl.UTF-8
mod_access_rbl to rozbudowany zamiennik mod_access. Oba moduły nie
mogą być używane jednocześnie.

%prep
%setup -q -c

%build
%{apxs} -c mod_%{mod_name}.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkglibdir},%{_sysconfdir}/conf.d}
install mod_%{mod_name}.so $RPM_BUILD_ROOT%{_pkglibdir}

echo 'LoadModule %{mod_name}_module	modules/mod_%{mod_name}.so' > \
	$RPM_BUILD_ROOT%{_sysconfdir}/conf.d/10_mod_%{mod_name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rbl
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_%{mod_name}.conf
%attr(755,root,root) %{_pkglibdir}/*
