Summary:	GNU automake - Makefile configuration tools
Summary(de):	GNU automake - Makefile-Konfigurationstools
Summary(fr):	automake de GNU - Outils de configuration des makefiles
Summary(pl):	GNU Automake - generator plik�w Makefile
Summary(tr):	Makefile yap�land�rma ara�lar�
Name:		automake
Version:	1.4
Release:	9
License:	GPL
Group:		Development/Building
Group(pl):	Programowanie/Budowanie
Source0:	ftp://sourceware.cygnus.com/pub/automake/%{name}-%{version}.tar.gz
Patch0:		automake-info.patch
Patch1:		automake-armnetwinder.patch
Patch2:		automake-1.4-19980208.patch
Patch3:		automake-man.patch
Patch4:		automake-Makefile.patch
URL:		http://sourceware.cygnus.com/automake/
BuildRequires:	autoconf
BuildRequires:	perl
Requires:	perl
Prereq:		/usr/sbin/fix-info-dir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Automake is an experimental Makefile generator. Automake was inspired by
the 4.4BSD make and include files, but aims to be portable and to conform
to the GNU standards for Makefile variables and targets.

%description -l de
Automake ist ein experimenteller Makefile-Generator, inspiriert durch die
4.4BSD-Make und Include-Dateien, der jedoch auf Portabilit�t und
Konformit�t mit den GNU-Standards f�r Makefile-Variable und Targets
abzielt.

%description -l fr
automake est un g�n�rateur exp�rimental de makefiles. Il a �t� inspir� par
le make de BSD 4.4, mais se veut portable et conforme aux standards GNU
pour les variables et les cibles des makefiles.

%description -l pl
Automake jest eksperymentalnym generatorem plik�w Makefile'a. Narz�dzie to
jest wzorowane na make i plikach nag��wkowych z systemu 4.4BSD. Umo�liwia
ono generowanie plik�w Makefile w oderwaniu od platformy systemowej b�d�c
jednocze�nie zgodnym ze standardami GNU.

%description -l tr
Automake deneysel bir Makefile �reticisidir. 4.4BSD make ve include
dosyalar�ndan esinlenilmistir, ama ama� ta��nabilir olmak ve Makefile
de�i�kenleri ve hedefleri i�in GNU standartlar�na uyum g�stermektir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1

%build
autoconf
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/*info*,%{_mandir}/man1/*} \
	AUTHORS ChangeLog NEWS README THANKS TODO

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,THANKS,TODO}.gz
%attr(755,root,root) %{_bindir}/*
%{_infodir}/automake*

%{_aclocaldir}
%{_mandir}/man1/*

%dir %{_datadir}/automake
%{_datadir}/automake/*.am
%{_datadir}/automake/texinfo.tex
%attr(755,root,root) %{_datadir}/automake/config.guess
%attr(755,root,root) %{_datadir}/automake/config.sub
%attr(755,root,root) %{_datadir}/automake/install-sh
%attr(755,root,root) %{_datadir}/automake/mdate-sh
%attr(755,root,root) %{_datadir}/automake/elisp-comp
%attr(755,root,root) %{_datadir}/automake/acinstall
%attr(755,root,root) %{_datadir}/automake/ylwrap
%attr(755,root,root) %{_datadir}/automake/mkinstalldirs
%attr(755,root,root) %{_datadir}/automake/missing
