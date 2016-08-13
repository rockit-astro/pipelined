Name:      onemetre-pipeline-server
Version:   1.16
Release:   0
Url:       https://github.com/warwick-one-metre/pipelined
Summary:   Data pipeline server for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-pyds9, python3-Pyro4, python3-sep, python3-warwickobservatory, onemetre-obslog-client, %{?systemd_requires}
BuildRequires: systemd-rpm-macros

%description
Part of the observatory software for the Warwick one-meter telescope.

pipelined manages the data pipeline for frames after they have been acquired.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/pipelined %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/pipelined.service %{buildroot}%{_unitdir}

%pre
%service_add_pre pipelined.service

%post
%service_add_post pipelined.service

%preun
%stop_on_removal pipelined.service
%service_del_preun pipelined.service

%postun
%restart_on_update pipelined.service
%service_del_postun pipelined.service

%files
%defattr(0755,root,root,-)
%{_bindir}/pipelined
%defattr(-,root,root,-)
%{_unitdir}/pipelined.service

%changelog
