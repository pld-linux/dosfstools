Summary:	Utilities to create and check MS-DOS FAT filesystems
Summary:	Narzêdzia do tworzenia i sprawdzanai systemów plikowych MS-DOS FAT
Name:		dosfstools
Version:	2.8
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.uni-erlangen.de/pub/Linux/LOCAL/dosfstools/%{name}-%{version}.src.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	mkdosfs-ygg

%define		_sbindir	/sbin

%description
Inside of this package there are two utilities to create and to check
MS-DOS FAT filesystems on either harddisks or floppies under Linux.
This version uses the enhanced boot sector/superblock format of DOS
3.3+ as well as provides a default dummy boot sector code.

%description -l pl
W pakiecie znajduj± siê dwa narzêdzia s³u¿±ce do tworzenia i
sprawdzania systemów plików FAT na dyskach twardych lub dyskietkach
pod Linuksem. Wersja ta u¿ywa ulepszonego formatu sektora
uruchomieniowego/superbloku u¿ywanego w DOS-ie 3.3 i nowszych oraz
obs³uguje pusty kod sektora uruchomieniowego.

%prep
%setup  -q

cp dosfsck/README README.fsck
cp mkdosfs/README README.mkdosfs

%build
%{__make} \
	OPTFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}" \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man8

rm -f $RPM_BUILD_ROOT%{_mandir}/man8/*.{msdos,vfat}.8
echo ".so dosfsck.8" > $RPM_BUILD_ROOT%{_mandir}/man8/fsck.msdos.8
echo ".so dosfsck.8" > $RPM_BUILD_ROOT%{_mandir}/man8/fsck.vfat.8
echo ".so mkdosf.8" > $RPM_BUILD_ROOT%{_mandir}/man8/mkfs.msdos.8
echo ".so mkdosf.8" > $RPM_BUILD_ROOT%{_mandir}/man8/mkfs.vfat.8

gzip -9nf CHANGES TODO README.fsck README.mkdosfs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
