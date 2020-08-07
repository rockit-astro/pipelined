Name:      onemetre-pipeline-server
Version:   2.3.2
Release:   0
Url:       https://github.com/warwick-one-metre/pipelined
Summary:   Data pipeline server for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  onemetre-pixelshift, nfs-utils
Requires:  python3, python3-Pyro4, python3-pyds9, python3-sep, python3-pillow, python3-warwick-observatory-common
Requires:  observatory-log-client, %{?systemd_requires}

%description
Part of the observatory software for the Warwick one-meter telescope.

pipelined manages the data pipeline for frames after they have been acquired.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/pipelined %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/pipelined.service %{buildroot}%{_unitdir}

%post
%systemd_post pipelined.service

%preun
%systemd_preun pipelined.service

%postun
%systemd_postun_with_restart pipelined.service

%files
%defattr(0755,root,root,-)
%{_bindir}/pipelined
%defattr(0644,root,root,-)
%{_unitdir}/pipelined.service

%changelog
