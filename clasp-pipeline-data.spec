Name:      clasp-pipeline-data
Version:   20220524
Release:   0
Url:       https://github.com/warwick-one-metre/pipelined
Summary:   Data pipeline configuration for the CLASP telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/clasp1.json %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/clasp2.json %{buildroot}%{_sysconfdir}/pipelined

%files
%defattr(0644,root,root,-)
%{_sysconfdir}/pipelined/clasp1.json
%{_sysconfdir}/pipelined/clasp2.json

%changelog
