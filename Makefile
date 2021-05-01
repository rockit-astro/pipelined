RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all:
	mkdir -p build
	${RPMBUILD} -ba onemetre-pipeline-server.spec
	${RPMBUILD} -ba observatory-pipeline-client.spec
	${RPMBUILD} -ba python3-warwick-observatory-pipeline.spec
	mv build/noarch/*.rpm .
	rm -rf build

