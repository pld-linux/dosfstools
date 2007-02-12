Summary:	Utilities to create and check MS-DOS FAT filesystems
Summary(es.UTF-8):	Un programa que crea sistemas de archivo de MS-DOS (FAT) en Linux
Summary(pl.UTF-8):	Narzędzia do tworzenia i sprawdzania systemów plikowych MS-DOS FAT
Summary(pt_BR.UTF-8):	Um programa que cria sistemas de arquivo do MS-DOS (FAT) no Linux
Name:		dosfstools
Version:	2.11
Release:	3
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.uni-erlangen.de/pub/Linux/LOCAL/dosfstools/%{name}-%{version}.src.tar.gz
# Source0-md5:	407d405ade410f7597d364ab5dc8c9f6
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-pl-man-pages.tar.bz2
# Source1-md5:	28913ed142dac33624b14ce1e1ce8803
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	mkdosfs-ygg

%define		_sbindir	/sbin

%description
Inside of this package there are two utilities to create and to check
MS-DOS FAT filesystems on either harddisks or floppies under Linux.
This version uses the enhanced boot sector/superblock format of DOS
3.3+ as well as provides a default dummy boot sector code.

%description -l es.UTF-8
El programa mkdosfs se usa para crear un sistema de archivos FAT
(MS-DOS) a partir de Linux.

Si su computador necesita usar sistemas de archivo MS-DOS usted debe
instalar el paquete dosfstools.

%description -l pl.UTF-8
W pakiecie znajdują się dwa narzędzia służące do tworzenia i
sprawdzania systemów plików FAT na dyskach twardych lub dyskietkach
pod Linuksem. Wersja ta używa ulepszonego formatu sektora
uruchomieniowego/superbloku używanego w DOS-ie 3.3 i nowszych oraz
obsługuje pusty kod sektora uruchomieniowego.

%description -l pt_BR.UTF-8
O programa mkdosfs é usado para criar um sistema de arquivos FAT
(MS-DOS) a partir do Linux.

O pacote dosfstools deve ser instalado se sua máquina precisa usar
sistemas de arquivo MS-DOS.

%prep
%setup -q

cp dosfsck/README README.fsck
cp mkdosfs/README README.mkdosfs

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE64_SOURCE" \
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
rm -f $RPM_BUILD_ROOT%{_mandir}/README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES TODO README.fsck README.mkdosfs
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%lang(pl) %{_mandir}/pl/man8/*
