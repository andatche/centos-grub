Name: grub
Version: 0.97
Release: bb1
Summary: GRUB - the Grand Unified Boot Loader.
Group: System Environment/Base
License: GPL
URL: http://www.gnu.org/software/%{name}/
Source0: ftp://alpha.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
# let's have some sort of organization for the patches
# patches 0-19 are for config file related changes (menu.lst->grub.conf)
Patch0: grub-0.93-configfile.patch
Patch1: grub-0.90-symlinkmenulst.patch

# patches 20-39 are for grub-install bits
Patch20: grub-0.97-install.in.patch
Patch21: grub-0.94-installcopyonly.patch
Patch22: grub-0.94-addsyncs.patch

# patches 40-59 are for miscellaneous build related patches
# link against curses statically
Patch40: grub-0.95-staticcurses.patch

# patches submitted upstream and pending approval
# change the message so that how to accept changes is clearer (#53846)
Patch81: grub-0.93-endedit.patch

# patches 100-199 are for features proposed but not accepted upstream
# add support for appending kernel arguments
Patch100: grub-0.90-append.patch
# add support for lilo -R-esque select a new os to boot into
Patch101: grub-0.97-once.patch

# patches 200-299 are for graphics mode related patches
Patch200: grub-0.95-graphics.patch
Patch201: grub-0.91-splashimagehelp.patch
Patch202: grub-0.93-graphics-bootterm.patch
Patch203: grub-0.95-hiddenmenu-tweak.patch

# patches 500+ are for miscellaneous little things
# support for non-std devs (eg cciss, etc)
Patch500: grub-0.93-special-device-names.patch
# i2o device support
Patch501: grub-0.94-i2o.patch
# detect cciss/ida/i2o
Patch502: grub-0.95-moreraid.patch

# for some reason, using the initrd max part of the setup.S structure
# causes problems on x86_64 and with 4G/4G
Patch505: grub-0.94-initrdmax.patch

# we need to use O_DIRECT to avoid hitting oddities with caching
Patch800: grub-0.95-odirect.patch

# the 2.6 kernel no longer does geometry fixups.  so now I get to do it
# instead in userspace everywhere.  
Patch1000: grub-0.95-geometry-26kernel.patch

# Support for booting from a RAID1 device
Patch1100: grub-0.95-md.patch
Patch1101: grub-0.95-md-rework.patch

# Ignore everything before the XPM header in the bootsplash
Patch1102: grub-0.95-xpmjunk.patch

# Don't go to "graphics" mode unless we find the bootsplash and it's an xpm,
# and don't print any errors about the missing file while current_term is
# "graphics".
Patch1103: grub-0.95-splash-error-term.patch

# Mark the simulation stack executable
Patch1104: grub-0.97-nxstack.patch
Patch1105: grub-0.97-nx-multiinstall.patch

# always use a full path for mdadm.
Patch1110: grub-0.97-mdadm-path.patch
# always install into the mbr if we're on a raid1 /boot.
Patch1111: grub-0.95-md-mbr.patch

# gcc4 fixes.
Patch1115: grub-0.97-gcc4.patch

# Make non-MBR installs work again on non-raid1.
Patch1120: grub-0.95-nonmbr.patch

# Make "grub-install --recheck" look like the menace it is.
Patch1130: grub-0.95-recheck-bad.patch

# Fix missing prototypes, since grub nicely sets -Wmissing-prototypes and
# then tries to build conftests without them.
Patch1135: grub-0.97-prototypes.patch

# put /usr/lib/grub back in /usr/share/grub like it was before, so other
# scripts don't screw up.
Patch1140: grub-0.97-datadir.patch

# install correctly on dmraid devices
Patch1145: grub-0.97-dmraid.patch
Patch1146: grub-0.97-dmraid-recheck-bad.patch
Patch1147: grub-0.97-dmraid-partition-names.patch

# fix mactel keyboard bugs
Patch1148: grub-0.97-mactel-kbd.patch

# fix error reporting
Patch1149: grub-0.97-stderr.patch

# fix grub-install to notice mpath partitions
Patch1150: grub-0.97-mpath.patch

# Handle larger kernel command lines
Patch1151: grub-0.97-cmdline-size.patch

# fix cciss handling in "convert" function
Patch1152: grub-0.97-bz429187-cciss.patch

# handle virtio block devices.
Patch1153: grub-install_virtio_blk_support.patch

# don't assume writable strings
Patch1154: grub-0.97-xfs-writable-strings.patch

# Support booting from GPT
Patch1155: grub-0.96-gpt_partition_support.patch

ExclusiveArch: i386 x86_64
BuildRequires: binutils >= 2.9.1.0.23, ncurses-devel, texinfo
BuildRequires: automake /usr/lib/crt1.o
PreReq: /sbin/install-info
Requires: mktemp
Requires: /usr/bin/cmp
Requires: system-logos
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
GRUB (Grand Unified Boot Loader) is an experimental boot loader
capable of booting into most free operating systems - Linux, FreeBSD,
NetBSD, GNU Mach, and others as well as most commercial operating
systems.

%prep
%setup -q
%patch0 -p1 -b .config
%patch1 -p1 -b .menulst

%patch20 -p1 -b .install
%patch21 -p1 -b .copyonly
%patch22 -p1 -b .addsync

%patch40 -p1 -b .static

%patch81 -p0 -b .endedit

%patch100 -p1 -b .append
%patch101 -p1 -b .bootonce

%patch200 -p1 -b .graphics
%patch201 -p1 -b .splashhelp
%patch202 -p1 -b .bootterm
%patch203 -p1 -b .hidden

%patch500 -p1 -b .raid
%patch501 -p1 -b .i2o
%patch502 -p1 -b .moreraid

# This patch fixes #116311 .
%patch505 -p1 -b .initrdmax

%patch800 -p1 -b .odirect

%patch1000 -p1 -b .26geom

%patch1100 -p1 -b .md
%patch1101 -p1 -b .md-rework

%patch1102 -p1 -b .xpmjunk

%patch1103 -p1 -b .splash-error-term

%patch1104 -p1 -b .nxstack
%patch1105 -p1 -b .nx-multiinstall

%patch1110 -p1 -b .mdadm-path
%patch1111 -p1 -b .md-mbr

%patch1115 -p1 -b .gcc4

%patch1120 -p1 -b .nonmbr

%patch1130 -p1 -b .recheck-bad

%patch1135 -p1 -b .prototypes

%patch1140 -p1 -b .datadir

%patch1145 -p1 -b .dmraid
%patch1146 -p1 -b .dmraid-recheck-bad
%patch1147 -p1 -b .dmraid-partition-names

%patch1148 -p1 -b .mactel-kbd

%patch1149 -p1 -b .stderr

%patch1150 -p1 -b .mpath

%patch1151 -p1 -b .cmdline-size

%patch1152 -p1 -b .cciss

%patch1153 -p1 -b .virtio
%patch1154 -p1 -b .xfs-writable-strings

%patch1155 -p1 -b .gpt_partition_support

%build
autoreconf --install --force
GCCVERS=$(gcc --version | head -1 | cut -d\  -f3 | cut -d. -f1)

# Must ignore warnings for gpt_partition_support patch to compile - NOT GREAT!
CFLAGS="-Os -g -fno-strict-aliasing -Wall -Wno-shadow -Wno-unused"
#CFLAGS="-Os -g -fno-strict-aliasing -Wall -Werror -Wno-shadow -Wno-unused"

if [ "$GCCVERS" == "4" ]; then
	CFLAGS="$CFLAGS -Wno-pointer-sign"
fi
%ifarch x86_64
CFLAGS="$CFLAGS -static" 
%endif
export CFLAGS
%configure --sbindir=/sbin --disable-auto-linux-mem-opt
make

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall sbindir=${RPM_BUILD_ROOT}/sbin
mkdir -p ${RPM_BUILD_ROOT}/boot/grub

rm -f ${RPM_BUILD_ROOT}/%{_infodir}/dir

%clean
rm -fr $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/grub.info.gz
  /sbin/install-info --info-dir=%{_infodir} %{_infodir}/multiboot.info.gz
fi

%preun
if [ "$1" = 0 ] ;then
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/grub.info.gz
  /sbin/install-info --delete --info-dir=%{_infodir} %{_infodir}/multiboot.info.gz
fi

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README COPYING TODO docs/menu.lst
/boot/grub
/sbin/grub
/sbin/grub-install
/sbin/grub-terminfo
/sbin/grub-md5-crypt
%{_bindir}/mbchk
%{_infodir}/grub*
%{_infodir}/multiboot*
%{_mandir}/man*/*
%{_datadir}/grub

%changelog
* Mon Feb 08 2010 Ben Arblaster <ben@brightbox.co.uk> - 0.97-bb1
- Allow booting from GTP

* Tue Jun 30 2009 Peter Jones <pjones@redhat.com> - 0.97-13.5
- Don't assume that gcc provides us with writable strings in the xfs driver
  Resolves: rhbz#496949

* Wed May 20 2009 Peter Jones <pjones@redhat.com> - 0.97-13.4
- Allow grub-install to work on virtio_blk devices (patch from markmc)
  Resolves: rhbz#498388

* Thu Feb 07 2008 Peter Jones <pjones@redhat.com> - 0.97-13.2
- Update patch for CCISS to not break some device mapper rules.
  Resolves: rhbz#429187

* Mon Feb 04 2008 Peter Jones <pjones@redhat.com> - 0.97-13.1
- Fix handling of CCISS devices when installing to the MBR.
  Resolves: rhbz#429187
- Allow longer kernel command lines
  Resolves: rhbz#336341

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 0.97-13
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Sep 21 2006 Peter Jones <pjones@redhat.com> - 0.97-12
- Reenable patch 505, which fixes #116311

* Tue Aug 15 2006 Peter Jones <pjones@redhat.com> - 0.97-11
- Disable patch 505 (#164497)

* Wed Aug  2 2006 Peter Jones <pjones@redhat.com> - 0.97-10
- Fix grub-install for multipath

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.97-9.1
- rebuild

* Fri Jul  7 2006 Peter Jones <pjones@redhat.com> - 0.97-9
- fix broken error reporting from helper functions

* Mon Jun 12 2006 Peter Jones <pjones@redhat.com> - 0.97-8
- Fix BIOS keyboard handler to use extended keyboard interrupts, so the
  Mac Mini works.

* Mon Jun  5 2006 Jesse Keating <jkeating@redhat.com> - 0.97-7
- Added BuildRequires on a 32bit library

* Sat May 27 2006 Peter Jones <pjones@redhat.com> - 0.97-6
- Fix mactel keyboard problems, patch from Juergen Keil, forwarded by Linus.

* Mon Mar 13 2006 Peter Jones <pjones@redhat.com> - 0.97-5
- Fix merge error for "bootonce" patch (broken in 0.95->0.97 update)
- Get rid of the 0.97 "default" stuff, since it conflicts with our working
  method.

* Mon Mar  9 2006 Peter Jones <pjones@redhat.com> - 0.97-4
- Fix running "install" multiple times on the same fs in the same invocation
  of grub.  (bz #158426 , patch from lxo@redhat.com)

* Mon Feb 13 2006 Peter Jones <pjones@redhat.com> - 0.97-3
- fix partition names on dmraid

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.97-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Jan 13 2006 Peter Jones <pjones@redhat.com> - 0.97-2
- add dmraid support

* Wed Dec 14 2005 Peter Jones <pjones@redhat.com> - 0.97-1
- update to grub 0.97

* Mon Dec  5 2005 Peter Jones <pjones@redhat.com> - 0.95-17
- fix configure conftest.c bugs
- add -Wno-unused to defeat gcc41 "unused" checking when there are aliases.

* Mon Aug  1 2005 Peter Jones <pjones@redhat.com> - 0.95-16
- minor fix to the --recheck fix.

* Mon Jul 25 2005 Peter Jones <pjones@redhat.com> 0.95-15
- Make "grub-install --recheck" warn the user about how bad it is,
  and keep a backup file, which it reverts to upon detecting some errors.

* Wed Jul  6 2005 Peter Jones <pjones@redhat.com> 0.95-14
- Fix changelog to be UTF-8

* Thu May 19 2005 Peter Jones <pjones@redhat.com> 0.95-13
- Make the spec work with gcc3 and gcc4, so people can test on existing
  installations.
- don't treat i2o like a cciss device, since its partition names aren't done
  that way. (#158158)

* Wed Mar 16 2005 Peter Jones <pjones@redhat.com> 0.95-12
- Make installing on a partition work again when not using raid

* Thu Mar  3 2005 Peter Jones <pjones@redhat.com> 0.95-11
- Make it build with gcc4

* Sun Feb 20 2005 Peter Jones <pjones@redhat.com> 0.95-10
- Always install in MBR for raid1 /boot/

* Sun Feb 20 2005 Peter Jones <pjones@redhat.com> 0.95-9
- Always use full path for mdadm in grub-install

* Tue Feb  8 2005 Peter Jones <pjones@redhat.com> 0.95-8
- Mark the simulation stack executable
- Eliminate the use of inline functions in stage2/builtins.c

* Wed Jan 11 2005 Peter Jones <pjones@redhat.com> 0.95-7
- Make grub ignore everything before the XPM header in the splash image,
  fixing #143879
- If the boot splash image is missing, use console mode instead 
  of graphics mode.
- Don't print out errors using the graphics terminal code if we're not
  actually in graphics mode.

* Mon Jan  3 2005 Peter Jones <pjones@redhat.com> 0.95-6
- reworked much of how the RAID1 support in grub-install works.  This version
  does not require all the devices in the raid to be listed in device.map,
  as long as you specify a physical device or partition rather than an md
  device.  It should also work with a windows dual-boot on the first partition.

* Fri Dec 17 2004 Peter Jones <pjones@redhat.com> 0.95-5
- added support for RAID1 devices to grub-install, partly based on a
  patch from David Knierim. (#114690)

* Tue Nov 30 2004 Jeremy Katz <katzj@redhat.com> 0.95-4
- add patch from upstream CVS to handle sparse files on ext[23]
- make geometry detection a little bit more robust/correct
- use O_DIRECT when reading/writing from devices.  use aligned buffers as 
  needed for read/write (#125808)
- actually apply the i2o patch
- detect cciss/cpqarray devices better (#123249)

* Thu Sep 30 2004 Jeremy Katz <katzj@redhat.com> - 0.95-3
- don't act on the keypress for the menu (#134029)

* Mon Jun 28 2004 Jeremy Katz <katzj@redhat.com> - 0.95-2
- add patch from Nicholas Miell to make hiddenmenu work more 
  nicely with splashimage mode (#126764)

* Fri Jun 18 2004 Jeremy Katz <katzj@redhat.com> - 0.95-1
- update to 0.95
- drop emd patch, E-MD isn't making forward progress upstream
- fix static build for x86_64 (#121095)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun  9 2004 Jeremy Katz <katzj@redhat.com>
- require system-logos (#120837)

* Fri Jun  4 2004 Jeremy Katz <katzj@redhat.com>
- buildrequire automake (#125326)

* Thu May 06 2004 Warren Togami <wtogami@redhat.com> - 0.94-5
- i2o patch from Markus Lidel

* Wed Apr 14 2004 Jeremy Katz <katzj@redhat.com> - 0.94-4
- read geometry off of the disk since HDIO_GETGEO doesn't actually 
  return correct data with a 2.6 kernel

* Fri Mar 12 2004 Jeremy Katz <katzj@redhat.com>
- add texinfo buildrequires (#118146)

* Wed Feb 25 2004 Jeremy Katz <katzj@redhat.com> 0.94-3
- don't use initrd_max_address

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com> 0.94-2
- rebuilt

* Thu Feb 12 2004 Jeremy Katz <katzj@redhat.com> 0.94-1
- update to 0.94, patch merging and updating as necessary

* Sat Jan  3 2004 Jeremy Katz <katzj@redhat.com> 0.93-8
- new bootonce patch from Padraig Brady so that you don't lose 
  the old default (#112775)

* Mon Nov 24 2003 Jeremy Katz <katzj@redhat.com>
- add ncurses-devel as a buildrequires (#110732)

* Tue Oct 14 2003 Jeremy Katz <katzj@redhat.com> 0.93-7
- rebuild

* Wed Jul  2 2003 Jeremy Katz <katzj@redhat.com> 
- Requires: /usr/bin/cmp (#98325)

* Thu May 22 2003 Jeremy Katz <katzj@redhat.com> 0.93-6
- add patch from upstream to fix build with gcc 3.3

* Wed Apr  2 2003 Jeremy Katz <katzj@redhat.com> 0.93-5
- add patch to fix support for serial terminfo (#85595)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jan 17 2003 Jeremy Katz <katzj@redhat.com> 0.93-3
- add patch from HJ Lu to support large disks (#80980, #63848)
- add patch to make message when ending edit clearer (#53846)

* Sun Dec 29 2002 Jeremy Katz <katzj@redhat.com> 0.93-2
- add a patch to reset the terminal type to console before doing 'boot' from
  the command line (#61069)

* Sat Dec 28 2002 Jeremy Katz <katzj@redhat.com> 0.93-1
- update to 0.93
- update configfile patch
- graphics patch rework to fit in as a terminal type as present in 0.93
- use CFLAGS="-Os -g"
- patch configure.in to allow building if host_cpu=x86_64, include -m32 in
  CFLAGS if building on x86_64
- link glibc static on x86_64 to not require glibc32
- include multiboot info pages
- drop obsolete patches, reorder remaining patches into some semblance of order

* Thu Sep  5 2002 Jeremy Katz <katzj@redhat.com> 0.92-7
- splashscreen is in redhat-logos now

* Tue Sep  3 2002 Jeremy Katz <katzj@redhat.com> 0.92-6
- update splashscreen again

* Mon Sep  2 2002 Jeremy Katz <katzj@redhat.com> 0.92-5
- update splashscreen

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 0.92-4
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com> 0.92-3
- automated rebuild

* Fri May  3 2002 Jeremy Katz <katzj@redhat.com> 0.92-2
- add patch from Grant Edwards to make vga16 + serial happier (#63491)

* Wed May  1 2002 Jeremy Katz <katzj@redhat.com> 0.92-1
- update to 0.92
- back to autoreconf
- make it work with automake 1.6/autoconf 2.53
- use "-falign-jumps=1 -falign-loops=1 -falign-functions=1" instead of
  "-malign-jumps=1 -malign-loops=1 -malign-functions=1"	to not use 
  deprecated gcc options

* Tue Apr  9 2002 Jeremy Katz <katzj@redhat.com> 0.91-4
- new splash screen

* Fri Mar  8 2002 Jeremy Katz <katzj@redhat.com> 0.91-3
- include patch from Denis Kitzmen to fix typo causing several options to 
  never be defined (in upstream CVS)
- include patch from upstream CVS to make displaymem always use hex for 
  consistency
- add patch from GRUB mailing list from Keir Fraser to add a --once flag to
  savedefault function so that you can have the equivalent of lilo -R 
  functionality (use 'savedefault --default=N --once' from the grub shell)
- back to autoconf

* Sun Jan 27 2002 Jeremy Katz <katzj@redhat.com> 
- change to use $grubdir instead of /boot/grub in the symlink patch (#58771)

* Fri Jan 25 2002 Jeremy Katz <katzj@redhat.com> 0.91-2
- don't ifdef out the auto memory passing, use the configure flag instead
- add a patch so that grub respects mem= from the kernel command line when 
  deciding where to place the initrd (#52558)

* Mon Jan 21 2002 Jeremy Katz <katzj@redhat.com> 0.91-1
- update to 0.91 final
- add documentation on splashimage param (#51609)

* Wed Jan  2 2002 Jeremy Katz <katzj@redhat.com> 0.91-0.20020102cvs
- update to current CVS snapshot to fix some of the hangs on boot related
  to LBA probing (#57503, #55868, and others)

* Fri Dec 21 2001 Erik Troan <ewt@redhat.com> 0.90-14
- fixed append patch to not require arguments to begin with
- changed to autoreconf from autoconf

* Wed Oct 31 2001 Jeremy Katz <katzj@redhat.com> 0.90-13
- include additional patch from Erich to add sync calls in grub-install to 
  work around updated images not being synced to disk
- fix segfault in grub shell if 'password --md5' is used without specifying
  a password (#55008)

* Fri Oct 26 2001 Jeremy Katz <katzj@redhat.com> 0.90-12
- Include Erich Boleyn <erich@uruk.org>'s patch to disconnect from the 
  BIOS after APM operations.  Should fix #54375

* Wed Sep 12 2001 Erik Troan <ewt@redhat.com>
- added patch for 'a' option in grub boot menu

* Wed Sep  5 2001 Jeremy Katz <katzj@redhat.com> 0.90-11
- grub-install: if /boot/grub/grub.conf doesn't exist but /boot/grub/menu.lst 
  does, create a symlink

* Fri Aug 24 2001 Jeremy Katz <katzj@redhat.com>
- pull in patch from upstream CVS to fix md5crypt in grub shell (#52220)
- use mktemp in grub-install to avoid tmp races

* Fri Aug  3 2001 Jeremy Katz <katzj@redhat.com>
- link curses statically (#49519)

* Thu Aug  2 2001 Jeremy Katz <katzj@redhat.com>
- fix segfault with using the serial device before initialization (#50219)

* Thu Jul 19 2001 Jeremy Katz <katzj@redhat.com>
- add --copy-only flag to grub-install

* Thu Jul 19 2001 Jeremy Katz <katzj@redhat.com>
- copy files in grub-install prior to device probe

* Thu Jul 19 2001 Jeremy Katz <katzj@redhat.com>
- original images don't go in /boot and then grub-install does the right
  thing

* Thu Jul 19 2001 Jeremy Katz <katzj@redhat.com>
- fix the previous patch
- put the password prompt in the proper location

* Thu Jul 19 2001 Jeremy Katz <katzj@redhat.com>
- reset the screen when the countdown is cancelled so text will disappear 
  in vga16 mode

* Mon Jul 16 2001 Jeremy Katz <katzj@redhat.com>
- change configfile defaults to grub.conf

* Sun Jul 15 2001 Jeremy Katz <katzj@redhat.com>
- updated to grub 0.90 final

* Fri Jul  6 2001 Matt Wilson <msw@redhat.com>
- modifed splash screen to a nice shade of blue

* Tue Jul  3 2001 Matt Wilson <msw@redhat.com>
- added a first cut at a splash screen

* Sun Jul  1 2001 Nalin Dahyabhai <nalin@redhat.com>
- fix datadir mismatch between build and install phases

* Mon Jun 25 2001 Jeremy Katz <katzj@redhat.com>
- update to current CVS 
- forward port VGA16 patch from Paulo César Pereira de 
  Andrade <pcpa@conectiva.com.br>
- add patch for cciss, ida, and rd raid controllers
- don't pass mem= to the kernel

* Wed May 23 2001 Erik Troan <ewt@redhat.com>
- initial build for Red Hat
