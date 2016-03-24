Name:      onemetre-pipeline-client
Version:   1.1
Release:   0
Url:       https://github.com/warwick-one-metre/pipelined
Summary:   Pipeline client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4

%description
Part of the observatory software for the Warwick one-meter telescope.

pipeline is a commandline utility for configuring the pipeline.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/pipeline %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/pipeline %{buildroot}/etc/bash_completion.d/pipeline

%files
%defattr(0755,root,root,-)
%{_bindir}/pipeline
/etc/bash_completion.d/pipeline

%changelog
