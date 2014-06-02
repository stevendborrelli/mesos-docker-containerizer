all::	build
build::	protobuf py-egg
clean::	clean-py clean-proto clean-py-egg

DOT := \033[34m●\033[39m
TICK := \033[32m✔\033[39m

clean-py:
	find ./containerizer -name "*.py[co]" -exec rm {} \;

clean-py-egg:
	rm -rf build dist mesos_docker_containerizer.egg-info

clean-proto:
	rm -rf ./containerizer/proto/*_pb2.py

protobuf: clean-proto
	@echo "$(DOT) Building python proto modules."
	protoc ./proto/*.proto --proto_path=./proto/ --python_out=./containerizer/proto/
	@echo "$(TICK) Building python proto modules."

py-egg:
	python setup.py bdist_egg
