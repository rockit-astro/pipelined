Name:      clasp-pipeline-data
Version:   20230628
Release:   0
Url:       https://github.com/warwick-one-metre/pipelined
Summary:   Data pipeline configuration for the CLASP telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/clasp.json %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/clasp_cam1.args %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/clasp_cam2.args %{buildroot}%{_sysconfdir}/pipelined

%files
%defattr(0644,root,root,-)
%{_sysconfdir}/pipelined/clasp.json
%{_sysconfdir}/pipelined/clasp_cam1.args
%{_sysconfdir}/pipelined/clasp_cam2.args

%changelog
