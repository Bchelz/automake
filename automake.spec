%include	/usr/lib/rpm/macros.perl
Summary:	GNU automake - Makefile configuration tools
Summary(de):	GNU automake - Makefile-Konfigurationstools
Summary(es):	GNU automake - herramientas de configuraci�n de Makefile
Summary(fr):	automake de GNU - Outils de configuration des makefiles
Summary(pl):	GNU Automake - generator plik�w Makefile
Summary(pt_BR):	GNU automake - ferramentas de configura��o de Makefile
Summary(tr):	Makefile yap�land�rma ara�lar�
Name:		automake
Version:	1.6.2
%define	_mver	%(echo %{version} | cut -d"." -f1-2)
Release:	1
License:	GPL
Group:		Development/Building
Source0:	ftp://sourceware.cygnus.com/pub/automake/%{name}-%{version}.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		%{name}-man.patch
URL:		http://sourceware.cygnus.com/automake/
BuildRequires:	autoconf >= 2.52
BuildRequires:	rpm-perlprov
Requires(pre):	fileutils
Requires:	perl
Requires:	perl(File::Glob)
Conflicts:	autoconf < 2.52
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%define		_aclocaldir	%{_datadir}/aclocal
%define		_veramsub	automake-%{_mver}
%define		_veralsub	aclocal-%{_mver}
%define		_veramdir	%{_datadir}/%{_veramsub}
%define		_veraldir	%{_datadir}/%{_veralsub}

%description
Automake is an experimental Makefile generator. Automake was inspired
by the 4.4BSD make and include files, but aims to be portable and to
conform to the GNU standards for Makefile variables and targets.

%description -l de
Automake ist ein experimenteller Makefile-Generator, inspiriert durch
die 4.4BSD-Make und Include-Dateien, der jedoch auf Portabilit�t und
Konformit�t mit den GNU-Standards f�r Makefile-Variable und Targets
abzielt.

%description -l es
Automake es un creador experimental de Makefiles. Fue inspirado en el
4.4BSD make y incluye archivos, pero visa ser port�til y compatible
con los padrones GNU para variables y dianas de Makefile.

%description -l fr
automake est un g�n�rateur exp�rimental de makefiles. Il a �t� inspir�
par le make de BSD 4.4, mais se veut portable et conforme aux
standards GNU pour les variables et les cibles des makefiles.

%description -l pl
Automake jest eksperymentalnym generatorem plik�w Makefile'a.
Narz�dzie to jest wzorowane na make i plikach nag��wkowych z systemu
4.4BSD. Umo�liwia ono generowanie plik�w Makefile w oderwaniu od
platformy systemowej b�d�c jednocze�nie zgodnym ze standardami GNU.

%description -l pt_BR
Automake � um gerador experimental de Makefiles. Ele foi inspirado
pelo 4.4BSD make e inclui arquivos, mas visa ser port�vel e compat�vel
com os padr�es GNU para vari�veis e alvos de Makefile.

%description -l tr
Automake deneysel bir Makefile �reticisidir. 4.4BSD make ve include
dosyalar�ndan esinlenilmistir, ama ama� ta��nabilir olmak ve Makefile
de�i�kenleri ve hedefleri i�in GNU standartlar�na uyum g�stermektir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install aclocal.1 automake.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf AUTHORS ChangeLog NEWS README THANKS TODO

ln -sf %{_veralsub} $RPM_BUILD_ROOT%{_aclocaldir}
ln -sf %{_veramsub} $RPM_BUILD_ROOT%{_datadir}/automake

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%pre
# upgrade from am < 1.6 (when /usr/share/{aclocal,automake} were directories)
# step 1: save directories
if [ -d %{_aclocaldir} -a ! -L %{_aclocaldir} ]; then
	mv -f %{_aclocaldir} %{_datadir}/aclocal.rpmtmp
fi
if [ -d %{_datadir}/automake -a ! -L %{_datadir}/automake ]; then
	mv -f %{_datadir}/automake %{_datadir}/automake.rpmtmp
fi

%triggerun -- automake < 1.6
# step 2: prevent removing of new files, allow to remove old
if [ -d %{_datadir}/aclocal.rpmtmp ]; then
	rm -f %{_aclocaldir}
	ln -sf aclocal.rpmtmp %{_aclocaldir}
fi
if [ -d %{_datadir}/automake.rpmtmp ]; then
	rm -f %{_datadir}/automake
	ln -sf automake.rpmtmp %{_datadir}/automake
fi

%triggerpostun -- automake < 1.6
# step 3: restore proper symlinks and move back remaining _aclocaldir contents
if [ -d %{_datadir}/aclocal.rpmtmp ]; then
	rm -f %{_aclocaldir}
	ln -sf %{_veralsub} %{_aclocaldir}
	mv -f %{_datadir}/aclocal.rpmtmp/* %{_aclocaldir}
	rmdir %{_datadir}/aclocal.rpmtmp
fi
if [ -d %{_datadir}/automake.rpmtmp ]; then
	rm -f %{_datadir}/automake
	ln -sf %{_veramsub} %{_datadir}/automake
	rmdir %{_datadir}/automake.rpmtmp
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_infodir}/automake*

%{_aclocaldir}
%{_veraldir}
%{_mandir}/man1/*

%{_datadir}/automake
%dir %{_veramdir}
%{_veramdir}/am
%{_veramdir}/Automake
%{_veramdir}/COPYING
%{_veramdir}/INSTALL
%{_veramdir}/texinfo.tex
%{_veramdir}/ansi2knr*
%attr(755,root,root) %{_veramdir}/acinstall
%attr(755,root,root) %{_veramdir}/compile
%attr(755,root,root) %{_veramdir}/config.guess
%attr(755,root,root) %{_veramdir}/config.sub
%attr(755,root,root) %{_veramdir}/depcomp
%attr(755,root,root) %{_veramdir}/elisp-comp
%attr(755,root,root) %{_veramdir}/install-sh
%attr(755,root,root) %{_veramdir}/mdate-sh
%attr(755,root,root) %{_veramdir}/missing
%attr(755,root,root) %{_veramdir}/mkinstalldirs
%attr(755,root,root) %{_veramdir}/py-compile
%attr(755,root,root) %{_veramdir}/ylwrap
