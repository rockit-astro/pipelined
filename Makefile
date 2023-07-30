RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

all:
	mkdir -p build
	date --utc +%Y%m%d%H%M%S > VERSION
	${RPMBUILD} --define "_version %(cat VERSION)" -ba rockit-pipeline.spec
	${RPMBUILD} --define "_version %(cat VERSION)" -ba python3-rockit-pipeline.spec

	mv build/noarch/*.rpm .
	rm -rf build VERSION

install:
	@date --utc +%Y%m%d%H%M%S > VERSION
	@python3 -m build --outdir .
	@sudo pip3 install rockit.pipeline-$$(cat VERSION)-py3-none-any.whl
	@rm VERSION
	@sudo cp pipelined pipeline_workerd pipeline /bin/
	@sudo cp pipelined@.service pipeline_workerd@.service /usr/lib/systemd/system/
	@sudo cp completion/pipeline /etc/bash_completion.d/
	@sudo install -d /etc/pipelined
	@echo ""
	@echo "Installed server, client, and service files."
	@echo "Now copy the relevant json config files to /etc/pipelined/"
