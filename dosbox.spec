Summary:	x86/DOS emulator with sound/graphics primarily for games
Summary(pl):	Emulator x86/DOS z d¼wiêkiem/grafik± g³ównie dla gier
Name:		dosbox
Version:	0.58
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	91c49a597134f35f899d32a8b253205b
BuildRequires:	libpng-devel
%{?debug:BuildRequires:	ncurses-devel}
BuildRequires:	SDL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DOSBox emulates a 286/386 realmode CPU, Directory FileSystem/XMS/EMS,
a SoundBlaster card for excellent sound compatibility with older
games...

You can "re-live" the good old days with the help of DOSBox, it can
run plenty of the old classics that don't run on your new computer!

%description -l pl
DOSBox emuluje tryb rzeczywisty procesora 286/386, system plików z
katalogami, pamiêæ XMS/EMS oraz kartê SoundBlaster w celu zapewnienia
znakomitej kompatybilno¶ci ze starymi grami.

Stare wspomnienia od¿yj± z pomoc± DOSBoxa. Dziêki niemu mo¿na
uruchomiæ mnóstwo klasyków, które nie odpalaj± siê na nowych
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
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
