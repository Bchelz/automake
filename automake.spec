Summary:     GNU automake - Makefile configuration tools
Summary(de): GNU automake - Makefile-Konfigurationstools
Summary(fr): automake de GNU - Outils de configuration des makefiles
Summary(pl): GNU Automake - generator plik�w Makefile
Summary(tr): Makefile yap�land�rma ara�lar�
Name:        automake
Version:     1.3b
Release:     1
Copyright:   GPL
Group:       Development/Building
Source:      ftp://ftp.cygnus.com/pub/tromey/%{name}-%{version}.tar.gz
Requires:    perl
Prereq:      /sbin/install-info
URL:         http://www.cygnus.com/~tromey/automake/
BuildArchitectures: noarch
Buildroot:   /tmp/%{name}-%{version}-root

%description
Automake is an experimental Makefile generator.  It was inspired by the
4.4BSD make and include files, but aims to be portable and to conform to the
GNU standards for Makefile variables and targets.

%description -l de
Automake ist ein experimenteller Makefile-Generator, inspiriert durch die
4.4BSD-Make und Include-Dateien, der jedoch auf Portabilit�t und Konformit�t
mit den GNU-Standards f�r Makefile-Variable und Targets abzielt.

%description -l fr
automake est un g�n�rateur exp�rimental de makefiles. Il a �t� inspir� par
le make de BSD 4.4, mais se veut portable et conforme aux standards GNU pour
les variables et les cibles des makefiles.

%description -l pl
Automake jest eksperymentalnym generatorem plik�w Makefile'a. Narz�dzie to
jest wzorowane na make i plikach nag��wk�w z systemu 4.4BSD. Umo�liwia ono
generowanie plik�w Makefile w oderwaniu od platformy systemowej b�d�c
jednoce�nie zgodnym ze standardami GNU.

%description -l tr
Automake deneysel bir Makefile �reticisidir. 4.4BSD make ve include
dosyalar�ndan esinlenilmistir, ama ama� ta��nabilir olmak ve Makefile
de�i�kenleri ve hedefleri i�in GNU standartlar�na uyum g�stermektir.

%prep
%setup -q

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr
gzip -9nf $RPM_BUILD_ROOT/usr/info/automake*

%post
/sbin/install-info /usr/info/automake.info.gz /usr/info/dir --entry \
"* automake: (automake).		                Making Makefile.in's"

%preun
/sbin/install-info --delete /usr/info/automake.info.gz /usr/info/dir --entry \
"* automake: (automake).		                Making Makefile.in's"

%files
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755, root, root) /usr/bin/*
/usr/info/automake*
%attr(-, root, root) /usr/share/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Nov 21 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3b-1]
- changed base Source url,
- cosmetic changes in %post, %preun in {un}registering autoame info page,
- added URL.

* Sat Aug  1 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3-5]
- modified pl translation,
- added -q %setup parameter,
- removed INSTALL and COPING from %doc (copyright statment is in Copyright
  field),
- Buildroot changed to /tmp/%%{name}-%%{version}-root,
- fixed %defattr macro,
- added using %%{name} and %%{version} macro in Source.

* Mon Jun 29 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.3-4]
- added pl translation,
- build from non root's account,
- added %defattr support.

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 07 1998 Erik Troan <ewt@redhat.com>
- updated to 1.3

* Tue Oct 28 1997 Cristian Gafton <gafton@redhat.com>
- added BuildRoot; added aclocal files

* Fri Oct 24 1997 Erik Troan <ewt@redhat.com>
- made it a noarch package

* Thu Oct 16 1997 Michael Fulbright <msf@redhat.com>
- Fixed some tag lines to conform to 5.0 guidelines.

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- updated to 1.2

* Wed Mar 5 1997 msf@redhat.com <Michael Fulbright>
- first version (1.0)
