Name:		texlive-chhaya
Version:	61719
Release:	2
Summary:	Linguistic glossing in Marathi language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chhaya
License:	gpl3+ other-free fdl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chhaya.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chhaya.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chhaya.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
muNbii vidyaapiitthaacyaa chaayaalekhn niymaavliis anusruun
bhaassaavaijnyaanik chaayaaNgaaNce sNkssep purvnnaaraa
aajnyaasNc. This package provides macros for linguistic
glossing as per the rules given by Mumbai University.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/chhaya
%{_texmfdistdir}/tex/latex/chhaya
%doc %{_texmfdistdir}/doc/latex/chhaya

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
