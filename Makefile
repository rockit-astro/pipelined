RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all:
	mkdir -p build
	${RPMBUILD} -ba observatory-pipeline-server.spec
	${RPMBUILD} -ba observatory-pipeline-client.spec
	${RPMBUILD} -ba python3-warwick-observatory-pipeline.spec
	${RPMBUILD} -ba onemetre-pipeline-data.spec
	${RPMBUILD} -ba clasp-pipeline-data.spec
	mv build/noarch/*.rpm .
	rm -rf build

