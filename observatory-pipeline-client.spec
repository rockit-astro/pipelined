Name:      observatory-pipeline-client
Version:   20220522
Release:   0
Url:       https://github.com/warwick-one-metre/pipelined
Summary:   Pipeline client for the Warwick La Palma telescopes.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  ds9, xpa
Requires:  python3, python3-Pyro4, python3-pyds9, python3-warwick-observatory-common, python3-warwick-observatory-pipeline

%description

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
