Name:      onemetre-pipeline-server
Version:   20210430
Release:   0
Url:       https://github.com/warwick-one-metre/pipelined
Summary:   Data pipeline server for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  nfs-utils
Requires:  python3, python3-Pyro4, python3-astropy, python3-pyds9, python3-sep, python3-pillow
Requires:  python3-warwick-observatory-common, python3-warwick-observatory-pipeline
Requires:  observatory-log-client, %{?systemd_requires}

%description
Part of the observatory software for the Warwick one-meter telescope.

pipelined manages the data pipeline for frames after they have been acquired.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/pipelined

%{__install} %{_sourcedir}/pipelined %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/pipelined@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/onemetre.json %{buildroot}%{_sysconfdir}/pipelined

%files
%defattr(0755,root,root,-)
%{_bindir}/pipelined
%defattr(0644,root,root,-)
%{_unitdir}/pipelined@.service
%{_sysconfdir}/pipelined/onemetre.json

%changelog
