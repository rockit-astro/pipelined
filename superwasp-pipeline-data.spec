Name:      superwasp-pipeline-data
Version:   20221029
Release:   0
Url:       https://github.com/warwick-one-metre/pipelined
Summary:   Data pipeline configuration for the SuperWASP telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/superwasp.json %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/superwasp_cam1.args %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/superwasp_cam2.args %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/superwasp_cam3.args %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/superwasp_cam4.args %{buildroot}%{_sysconfdir}/pipelined

%files
%defattr(0644,root,root,-)
%{_sysconfdir}/pipelined/superwasp.json
%{_sysconfdir}/pipelined/superwasp_cam1.args
%{_sysconfdir}/pipelined/superwasp_cam2.args
%{_sysconfdir}/pipelined/superwasp_cam3.args
%{_sysconfdir}/pipelined/superwasp_cam4.args

%changelog
