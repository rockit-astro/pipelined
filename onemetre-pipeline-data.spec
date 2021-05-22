Name:      onemetre-pipeline-data
Version:   20210430
Release:   0
Url:       https://github.com/warwick-one-metre/pipelined
Summary:   Data pipeline configuration for W1m telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  nfs-utils
Requires:  python3, python3-Pyro4, python3-astropy, python3-pyds9, python3-sep, python3-pillow
Requires:  python3-warwick-observatory-common, python3-warwick-observatory-pipeline
Requires:  observatory-log-client, %{?systemd_requires}

%description

%build
mkdir -p %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/onemetre.json %{buildroot}%{_sysconfdir}/pipelined

%files
%defattr(0644,root,root,-)
%{_sysconfdir}/pipelined/onemetre.json

%changelog
