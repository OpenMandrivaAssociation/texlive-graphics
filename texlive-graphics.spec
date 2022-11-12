Name:		texlive-graphics
Version:	64892
Release:	1
Summary:	Standard LaTeX graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/required/graphics
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires:	texlive-graphics-cfg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package was designed to accommodate all needs for inclusion
of graphics in LaTeX documents, replacing many earlier packages
used in LaTeX 2.09. The package aims to give a consistent
interface to including the file types that are understood in
your output, by use of 'printer drivers' (now known, simply, as
'drivers'). The distribtion of the package contains several
drivers, but others (for example, pdfTeX) are distributed
separately. The package also offers several means of
manipulating graphics in the course of inserting them into a
document (for example, rotation and scaling). For extended
documentation see epslatex. The package is part of the graphics
bundle, which is one of the collections in the LaTeX 'required'
set of packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/graphics
%doc %{_texmfdistdir}/doc/latex/graphics
#- source
%doc %{_texmfdistdir}/source/latex/graphics

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
