# revision 25405
# category Package
# catalog-ctan /macros/latex/required/graphics
# catalog-date 2011-05-30 14:43:49 +0200
# catalog-license lppl
# catalog-version 1.0o
Name:		texlive-graphics
Version:	1.0o
Release:	7
Summary:	Standard LaTeX graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/required/graphics
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
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
%{_texmfdistdir}/tex/latex/graphics/color.sty
%{_texmfdistdir}/tex/latex/graphics/dvipdf.def
%{_texmfdistdir}/tex/latex/graphics/dvips.def
%{_texmfdistdir}/tex/latex/graphics/dvipsnam.def
%{_texmfdistdir}/tex/latex/graphics/dvipsone.def
%{_texmfdistdir}/tex/latex/graphics/dviwin.def
%{_texmfdistdir}/tex/latex/graphics/emtex.def
%{_texmfdistdir}/tex/latex/graphics/epsfig.sty
%{_texmfdistdir}/tex/latex/graphics/graphics.sty
%{_texmfdistdir}/tex/latex/graphics/graphicx.sty
%{_texmfdistdir}/tex/latex/graphics/keyval.sty
%{_texmfdistdir}/tex/latex/graphics/lscape.sty
%{_texmfdistdir}/tex/latex/graphics/pctex32.def
%{_texmfdistdir}/tex/latex/graphics/pctexhp.def
%{_texmfdistdir}/tex/latex/graphics/pctexps.def
%{_texmfdistdir}/tex/latex/graphics/pctexwin.def
%{_texmfdistdir}/tex/latex/graphics/tcidvi.def
%{_texmfdistdir}/tex/latex/graphics/trig.sty
%{_texmfdistdir}/tex/latex/graphics/truetex.def
%doc %{_texmfdistdir}/doc/latex/graphics/00readme.txt
%doc %{_texmfdistdir}/doc/latex/graphics/changes.txt
%doc %{_texmfdistdir}/doc/latex/graphics/color.pdf
%doc %{_texmfdistdir}/doc/latex/graphics/drivers.pdf
%doc %{_texmfdistdir}/doc/latex/graphics/epsfig.pdf
%doc %{_texmfdistdir}/doc/latex/graphics/graphics.pdf
%doc %{_texmfdistdir}/doc/latex/graphics/graphicx.pdf
%doc %{_texmfdistdir}/doc/latex/graphics/grfguide.pdf
%doc %{_texmfdistdir}/doc/latex/graphics/keyval.pdf
%doc %{_texmfdistdir}/doc/latex/graphics/lscape.pdf
%doc %{_texmfdistdir}/doc/latex/graphics/trig.pdf
#- source
%doc %{_texmfdistdir}/source/latex/graphics/color.dtx
%doc %{_texmfdistdir}/source/latex/graphics/drivers.dtx
%doc %{_texmfdistdir}/source/latex/graphics/epsfig.dtx
%doc %{_texmfdistdir}/source/latex/graphics/graphics-drivers.ins
%doc %{_texmfdistdir}/source/latex/graphics/graphics.dtx
%doc %{_texmfdistdir}/source/latex/graphics/graphics.ins
%doc %{_texmfdistdir}/source/latex/graphics/graphicx.dtx
%doc %{_texmfdistdir}/source/latex/graphics/grfguide.tex
%doc %{_texmfdistdir}/source/latex/graphics/keyval.dtx
%doc %{_texmfdistdir}/source/latex/graphics/lscape.dtx
%doc %{_texmfdistdir}/source/latex/graphics/trig.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0o-3
+ Revision: 779464
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0o-2
+ Revision: 752373
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0o-1
+ Revision: 718577
- texlive-graphics
- texlive-graphics
- texlive-graphics
- texlive-graphics

