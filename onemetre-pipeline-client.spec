Name:      onemetre-pipeline-client
Version:   2.2.0
Release:   0
Url:       https://github.com/warwick-one-metre/pipelined
Summary:   Pipeline client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires: ds9, xpa, xpa-libs
%if 0%{?suse_version}
Requires:  python3, python34-Pyro4, python34-pyds9, python34-warwick-observatory-common
%endif
%if 0%{?centos_ver}
Requires:  python34, python34-Pyro4, python34-pyds9, python34-warwick-observatory-common
%endif

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
