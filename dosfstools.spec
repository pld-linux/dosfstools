Summary:	Utilities to create and check MS-DOS FAT filesystems.
Name:		dosfstools
Version:	2.2
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source:		ftp://ftp.uni-erlangen.de/pub/Linux/LOCAL/dosfstools/%{name}-%{version}.src.tar.gz
Obsoletes:	mkdosfs-ygg
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Inside of this package there are two utilities to create and to
check MS-DOS FAT filesystems on either harddisks or floppies under
Linux.  This version uses the enhanced boot sector/superblock
format of DOS 3.3+ as well as provides a default dummy boot sector
code.

%prep
%setup -q

%build
make OPTFLAGS="$RPM_OPT_FLAGS" PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
cp dosfsck/README README.fsck
cp mkdosfs/README README.mkdosfs

make install \
	PREFIX=$RPM_BUILD_ROOT \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man8

rm -f $RPM_BUILD_ROOT%{_mandir}/man8/*.{msdos,vfat}.8
echo ".so dosfsck.8" > $RPM_BUILD_ROOT%{_mandir}/man8/fsck.msdos.8
echo ".so dosfsck.8" > $RPM_BUILD_ROOT%{_mandir}/man8/fsck.vfat.8
echo ".so mkdosf.8" > $RPM_BUILD_ROOT%{_mandir}/man8/mkfs.msdos.8
echo ".so mkdosf.8" > $RPM_BUILD_ROOT%{_mandir}/man8/mkfs.vfat.8

strip $RPM_BUILD_ROOT/sbin/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* \
	CHANGES TODO README.fsck README.mkdosfs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,TODO,README.fsck,README.mkdosfs}.gz
%attr(755,root,root) /sbin/*
%{_mandir}/man8/*
