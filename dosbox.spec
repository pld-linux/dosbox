#
# Conditional build:
%bcond_without	alsa	# without ALSA support for MIDI
#
Summary:	x86/DOS emulator with sound/graphics primarily for games
Summary(pl.UTF-8):	Emulator x86/DOS z dźwiękiem/grafiką głównie dla gier
Name:		dosbox
Version:	0.71
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/dosbox/%{name}-%{version}.tar.gz
# Source0-md5:	52ee21b69f7baaf88190d7935ea58359
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}.conf
URL:		http://dosbox.sourceforge.net/
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_sound-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9.0}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
%{?debug:BuildRequires:	ncurses-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fmerge-all-constants -ffast-math

%description
DOSBox emulates a 286/386 realmode/protected mode CPU, Directory
FileSystem/XMS/EMS, Tandy/Hercules/CGA/EGA/VGA/VESA graphics, a
SoundBlaster/Gravis Ultra Sound card for excellent sound compatibility
with older games...

You can "re-live" the good old days with the help of DOSBox, it can
run plenty of the old classics that don't run on your new computer!

%description -l pl.UTF-8
DOSBox emuluje tryb rzeczywisty/chroniony procesora 286/386, system
plików z katalogami, pamięć XMS/EMS, karty graficzne
Tandy/Hercules/CGA/EGA/VGA/VESA oraz karty muzyczne
SoundBlaster/Gravis Ultra Sound w celu zapewnienia znakomitej
kompatybilności ze starymi grami.

Stare wspomnienia odżyją z pomocą DOSBoksa. Dzięki niemu można
uruchomić mnóstwo klasyków, które nie odpalają się na nowych
komputerach.

%prep
%setup -q

%build
# kill AM_PATH_SDL and AM_PATH_ALSA, leave only AH_{TOP,BOTTOM}
tail -n +306 acinclude.m4 > acinclude.m4.tmp
mv -f acinclude.m4.tmp acinclude.m4
%if !%{with alsa}
echo 'AC_DEFUN([AM_PATH_ALSA], [$3])' >> acinclude.m4
%endif
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shots \
	%{?debug:--enable-debug}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS dosbox.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
