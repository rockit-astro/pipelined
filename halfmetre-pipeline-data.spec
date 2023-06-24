Name:      halfmetre-pipeline-data
Version:   20230624
Release:   0
Url:       https://github.com/warwick-one-metre/pipelined
Summary:   Data pipeline configuration for the Half metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/halfmetre.json %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/halfmetre.args %{buildroot}%{_sysconfdir}/pipelined

%files
%defattr(0644,root,root,-)
%{_sysconfdir}/pipelined/halfmetre.json
%{_sysconfdir}/pipelined/halfmetre.args

%changelog
