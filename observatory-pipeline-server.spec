Name:      observatory-pipeline-server
Version:   20220924
Release:   0
Url:       https://github.com/warwick-one-metre/pipelined
Summary:   Data pipeline server.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  nfs-utils
Requires:  python3, python3-Pyro4, python3-astropy, python3-pyds9, python3-sep, python3-pillow
Requires:  python3-warwick-observatory-common, python3-warwick-observatory-pipeline, %{?systemd_requires}

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/pipelined %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/pipelined@.service %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/pipeline_workerd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/pipeline_workerd@.service %{buildroot}%{_unitdir}

%files
%defattr(0755,root,root,-)
%{_bindir}/pipelined
%{_bindir}/pipeline_workerd

%defattr(0644,root,root,-)
%{_unitdir}/pipelined@.service
%{_unitdir}/pipeline_workerd@.service

%changelog
