Summary:	Utilities to create and check MS-DOS FAT filesystems
Summary(es):	Un programa que crea sistemas de archivo de MS-DOS (FAT) en Linux.
Summary(pl):	Narzêdzia do tworzenia i sprawdzanai systemów plikowych MS-DOS FAT
Summary(pt_BR):	Um programa que cria sistemas de arquivo do MS-DOS (FAT) no Linux
Name:		dosfstools
Version:	2.8
Release:	2
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.uni-erlangen.de/pub/Linux/LOCAL/dosfstools/%{name}-%{version}.src.tar.gz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-pl-man-pages.tar.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	mkdosfs-ygg

%define		_sbindir	/sbin

%description
Inside of this package there are two utilities to create and to check
MS-DOS FAT filesystems on either harddisks or floppies under Linux.
This version uses the enhanced boot sector/superblock format of DOS
3.3+ as well as provides a default dummy boot sector code.

%description -l es
El programa mkdosfs se usa para crear un sistema de archivos FAT
(MS-DOS) a partir de Linux.

Si su computador necesita usar sistemas de archivo MS-DOS usted debe
instalar el paquete dosfstools.

%description -l pl
W pakiecie znajduj± siê dwa narzêdzia s³u¿±ce do tworzenia i
sprawdzania systemów plików FAT na dyskach twardych lub dyskietkach
pod Linuksem. Wersja ta u¿ywa ulepszonego formatu sektora
uruchomieniowego/superbloku u¿ywanego w DOS-ie 3.3 i nowszych oraz
obs³uguje pusty kod sektora uruchomieniowego.

%description -l pt_BR
O programa mkdosfs é usado para criar um sistema de arquivos FAT
(MS-DOS) a partir do Linux.

O pacote dosfstools deve ser instalado se sua máquina precisa usar
sistemas de arquivo MS-DOS.

%prep
%setup  -q

cp dosfsck/README README.fsck
cp mkdosfs/README README.mkdosfs

%build
%{__make} \
	OPTFLAGS="%{rpmcflags}" \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man8

rm -f $RPM_BUILD_ROOT%{_mandir}/man8/*.{msdos,vfat}.8
echo ".so dosfsck.8" > $RPM_BUILD_ROOT%{_mandir}/man8/fsck.msdos.8
echo ".so dosfsck.8" > $RPM_BUILD_ROOT%{_mandir}/man8/fsck.vfat.8
echo ".so mkdosfs.8" > $RPM_BUILD_ROOT%{_mandir}/man8/mkfs.msdos.8
echo ".so mkdosfs.8" > $RPM_BUILD_ROOT%{_mandir}/man8/mkfs.vfat.8
bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES TODO README.fsck README.mkdosfs
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%lang(pl) %{_mandir}/pl/man8/*
