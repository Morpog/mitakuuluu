# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-mitakuuluu

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Mitäkuuluu
Version:    0.1
Release:    18
Group:      Qt/Qt
License:    LICENSE
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-mitakuuluu.yaml
Requires:   sailfishsilica-qt5 libexif
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Contacts)
BuildRequires:  pkgconfig(sailfishapp)
BuildRequires:  desktop-file-utils

%description
Short description of my SailfishOS Application


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
strip -s %{buildroot}/usr/bin/harbour-mitakuuluu
strip -s %{buildroot}/usr/bin/harbour-mitakuuluu-server
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%pre
# >> pre

if /sbin/pidof harbour-mitakuuluu-server > /dev/null; then
su -l -c "dbus-send --print-reply --session --dest=org.coderus.harbour_mitakuuluu_server / org.coderus.harbour_mitakuuluu_server.exit" nemo || true
fi

if /sbin/pidof harbour-mitakuuluu > /dev/null; then
su -l -c "dbus-send --print-reply --session --dest=org.coderus.harbour_mitakuuluu / org.coderus.harbour_mitakuuluu.exit" nemo || true
fi
# << pre

%preun
# >> preun

if /sbin/pidof harbour-mitakuuluu-server > /dev/null; then
su -l -c "dbus-send --print-reply --session --dest=org.coderus.harbour_mitakuuluu_server / org.coderus.harbour_mitakuuluu_server.exit" nemo || true
fi

if /sbin/pidof harbour-mitakuuluu > /dev/null; then
su -l -c "dbus-send --print-reply --session --dest=org.coderus.harbour_mitakuuluu / org.coderus.harbour_mitakuuluu.exit" nemo || true
fi
# << preun

%files
%defattr(-,root,root,-)
/usr/share/dbus-1/services
/usr/share/lipstick/notificationcategories/
%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/themes/base/meegotouch/icons/
%{_datadir}/%{name}
%{_bindir}
# >> files
# << files
