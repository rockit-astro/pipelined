Name:      rockit-pipeline
Version:   %{_version}
Release:   1
Summary:   Data pipeline
Url:       https://github.com/rockit-astro/pipelined
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/etc/bash_completion.d
mkdir -p %{buildroot}%{_sysconfdir}/pipelined/
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/pipelined %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/pipeline_workerd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/pipelined@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/pipeline_workerd@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/pipeline %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/pipeline %{buildroot}/etc/bash_completion.d/pipeline

%{__install} %{_sourcedir}/config/onemetre.json %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/config/onemetre_blue.args %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/config/onemetre_red.args %{buildroot}%{_sysconfdir}/pipelined

%{__install} %{_sourcedir}/config/clasp.json %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/config/clasp_cam1.args %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/config/clasp_cam2.args %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/data/master-bias-CAM2.fits.gz %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/data/master-dark-CAM2.fits.gz %{buildroot}%{_sysconfdir}/pipelined

%{__install} %{_sourcedir}/config/halfmetre.json %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/config/halfmetre.args %{buildroot}%{_sysconfdir}/pipelined

%{__install} %{_sourcedir}/config/superwasp.json %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/config/superwasp_cam1.args %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/config/superwasp_cam2.args %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/config/superwasp_cam3.args %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/config/superwasp_cam4.args %{buildroot}%{_sysconfdir}/pipelined

%{__install} %{_sourcedir}/config/warwick.json %{buildroot}%{_sysconfdir}/pipelined
%{__install} %{_sourcedir}/config/warwick.args %{buildroot}%{_sysconfdir}/pipelined

%package server
Summary:  Data pipeline server
Group:    Unspecified
Requires: python3-rockit-pipeline python3-astropy python3-pyds9 python3-sep python3-pillow python3-paramiko python3-scp astrometry-net

%description server

%files server
%defattr(0755,root,root,-)
%{_bindir}/pipelined
%{_bindir}/pipeline_workerd
%defattr(0644,root,root,-)
%{_unitdir}/pipelined@.service
%{_unitdir}/pipeline_workerd@.service

%package client
Summary:  Data pipeline client
Group:    Unspecified
Requires: python3-rockit-pipeline python3-pyds9 ds9 xpa

%description client

%files client
%defattr(0755,root,root,-)
%{_bindir}/pipeline
/etc/bash_completion.d/pipeline

%package data-clasp
Summary: Data pipeline configuration for CLASP telescope.
Group:   Unspecified
%description data-clasp

%files data-clasp
%defattr(0644,root,root,-)
%{_sysconfdir}/pipelined/clasp.json
%{_sysconfdir}/pipelined/clasp_cam1.args
%{_sysconfdir}/pipelined/clasp_cam2.args
%{_sysconfdir}/pipelined/master-bias-CAM2.fits.gz
%{_sysconfdir}/pipelined/master-dark-CAM2.fits.gz

%package data-halfmetre
Summary: Data pipeline configuration for the half metre telescope.
Group:   Unspecified
%description data-halfmetre

%files data-halfmetre
%defattr(0644,root,root,-)
%{_sysconfdir}/pipelined/halfmetre.json
%{_sysconfdir}/pipelined/halfmetre.args

%package data-onemetre
Summary: Data pipeline configuration for the W1m telescope.
Group:   Unspecified
%description data-onemetre

%files data-onemetre
%defattr(0644,root,root,-)
%{_sysconfdir}/pipelined/onemetre.json
%{_sysconfdir}/pipelined/onemetre_blue.args
%{_sysconfdir}/pipelined/onemetre_red.args

%package data-superwasp
Summary: Data pipeline configuration for the SuperWASP telescope.
Group:   Unspecified
%description data-superwasp

%files data-superwasp
%defattr(0644,root,root,-)
%{_sysconfdir}/pipelined/superwasp.json
%{_sysconfdir}/pipelined/superwasp_cam1.args
%{_sysconfdir}/pipelined/superwasp_cam2.args
%{_sysconfdir}/pipelined/superwasp_cam3.args
%{_sysconfdir}/pipelined/superwasp_cam4.args

%changelog

%package data-warwick
Summary: Data pipeline configuration for the Windmill Hill Observatory telescope.
Group:   Unspecified
%description data-warwick

%files data-warwick
%defattr(0644,root,root,-)
%{_sysconfdir}/pipelined/warwick.json
%{_sysconfdir}/pipelined/warwick.args

%changelog
