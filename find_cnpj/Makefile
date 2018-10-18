PYTHON_NAME = "gofindcnpj"
GO_NAME = "main"
CFLAGS = `python3.6-config --cflags`
LDFLAGS = `python3.6-config --ldflags`

# Use when necessary
# PKG_CONFIG_PATH = "${PKG_CONFIG_PATH}:/home/rafael/.pyenv/versions/3.7.0/lib/pkgconfig"

build: SHELL:=/bin/bash
build: clean
	@echo "--> Recreate .so module"
	@go build -buildmode=c-shared -o ${PYTHON_NAME}.so ${GO_NAME}.go

clean:
	@echo "--> Cleaning C files"
	@rm -rf *.c *.h *.so
	@echo "--> Cleaning pyc files"
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@find . -name ".benchmarks" -type d | xargs rm -rf

benchmark:
	@LD_LIBRARY_PATH="." pytest --benchmark-only

benchmark-histogram:
	@LD_LIBRARY_PATH="." pytest --benchmark-only --benchmark-histogram

benchmark-memory:
	@LD_LIBRARY_PATH="." python -m memory_profiler test_memory_profiling.py

test:
	@LD_LIBRARY_PATH="." pytest --benchmark-skip

