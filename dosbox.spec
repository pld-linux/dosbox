Summary:	x86/DOS emulator with sound/graphics primarily for games
Summary(pl):	Emulator x86/DOS z d�wi�kiem/grafik� g��wnie dla gier
Name:		dosbox
Version:	0.58
Release:	2
License:	GPL
Group:		Applications/Emulators
Source0:	http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	91c49a597134f35f899d32a8b253205b
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}.conf
URL:		http://dosbox.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	libpng-devel
%{?debug:BuildRequires:	ncurses-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DOSBox emulates a 286/386 realmode CPU, Directory FileSystem/XMS/EMS,
a SoundBlaster card for excellent sound compatibility with older
games...

You can "re-live" the good old days with the help of DOSBox, it can
run plenty of the old classics that don't run on your new computer!

%description -l pl
DOSBox emuluje tryb rzeczywisty procesora 286/386, system plik�w z
katalogami, pami�� XMS/EMS oraz kart� SoundBlaster w celu zapewnienia
znakomitej kompatybilno�ci ze starymi grami.

Stare wspomnienia od�yj� z pomoc� DOSBoxa. Dzi�ki niemu mo�na
uruchomi� mn�stwo klasyk�w, kt�re nie odpalaj� si� na nowych
komputerach.

%prep
%setup -q

%build
%configure \
	--enable-shots \
	%{?debug:--enable-debug}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/*
%{_mandir}/man1/*
%{_desktopdir}/*
%{_pixmapsdir}/*
