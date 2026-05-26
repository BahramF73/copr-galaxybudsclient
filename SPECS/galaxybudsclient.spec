%global debug_package %{nil}
%global __strip /bin/true

Name:           galaxybudsclient
Version:        5.2.0
Release:        2%{?dist}
Summary:        Unofficial Galaxy Buds Manager for Linux

License:        GPL-3.0-only
URL:            https://github.com/timschneeb/GalaxyBudsClient
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Source1:        SOURCES/galaxybudsclient.desktop

BuildRequires:  dotnet-sdk-10.0

ExclusiveArch:  x86_64

%description
Configure and control any Samsung Galaxy Buds device and integrate them into
your desktop.

Aside from standard features known from the official Android app, this project
helps you to release the full potential of your earbuds and implements new
functionality such as:

- Detailed battery statistics
- Diagnostics and factory self-tests
- Loads of hidden debugging information
- Customizable long-press touch actions
- Firmware flashing, downgrading (Buds+, Buds Pro)
and much more...

%prep
%autosetup -n GalaxyBudsClient-%{version}

%build
dotnet restore \
       -r linux-x64 \
       --configfile GalaxyBudsClient/nuget.config \
       GalaxyBudsClient/GalaxyBudsClient.csproj

dotnet publish \
       -r linux-x64 \
       -o bin_linux64 \
       -c Release \
       -p:PublishSingleFile=true \
       --self-contained true \
       --no-restore \
       GalaxyBudsClient/GalaxyBudsClient.csproj

%install
install -D -m 755 bin_linux64/GalaxyBudsClient %{buildroot}%{_bindir}/GalaxyBudsClient
install -D -m 644 GalaxyBudsClient/Resources/icon.png %{buildroot}%{_datadir}/icons/hicolor/144x144/apps/GalaxyBudsClient.png
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/GalaxyBudsClient.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/GalaxyBudsClient
%{_datadir}/icons/hicolor/144x144/apps/GalaxyBudsClient.png
%{_datadir}/applications/GalaxyBudsClient.desktop

%changelog
* Tue May 26 2026 Bahram Farahmand <bahram.0098.bf@gmail.com> - 5.2.0-2
- Move spec and desktop files

* Tue May 26 2026 Bahram Farahmand <bahram.0098.bf@gmail.com> - 5.2.0-1
- Initial build
