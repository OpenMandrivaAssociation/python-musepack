%define oname	pymusepack

Name: 	 	python-musepack
Summary: 	Python access for musepack audio files
Version: 	0.4
Release: 	%mkrel 2
License:	GPL
Group:		Development/Python
URL:		http://www.sacredchao.net/
Source:		http://www.sacredchao.net/~piman/software/%{oname}-%{version}.tar.bz2
BuildRequires:	python-devel libmpcdec-devel swig
%py_requires -d

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

