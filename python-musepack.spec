%define oname	pymusepack

Name: 	 	python-musepack
Summary: 	Python access for musepack audio files
Version: 	0.4
Release: 	%mkrel 7
License:	GPL
Group:		Development/Python
URL:		http://www.sacredchao.net/
Source:		http://www.sacredchao.net/~piman/software/%{oname}-%{version}.tar.bz2
BuildRequires:	python-devel libmpcdec-devel swig
%py_requires -d
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This Python module lets you load and decode Musepack (MPC/MP+ files). It also
includes a module to read and write APEv2 metadata tags.

%prep
%setup -qn %{oname}-%{version}

%build
env CFLAGS="%{optflags}" python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

mkdir -p %{buildroot}/%{_bindir}
cp plaympc.py %{buildroot}/%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/plaympc.py
%attr(755,root,root) %{_libdir}/python*/site-packages/musepack/mpc.so
%{_libdir}/python*/site-packages/musepack/*.py*
%{_libdir}/python*/site-packages/%{oname}*.egg-info




%changelog
* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 0.4-7mdv2011.0
+ Revision: 594076
- rebuild

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.4-6mdv2010.0
+ Revision: 442317
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.4-5mdv2009.0
+ Revision: 259708
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.4-4mdv2009.0
+ Revision: 247516
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.4-2mdv2008.1
+ Revision: 136451
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4-2mdv2007.0
+ Revision: 124947
- make it work
- Import python-musepack

* Mon Aug 15 2005 Austin Acton <austin@mandriva.org> 0.4-1mdk
- initial package

