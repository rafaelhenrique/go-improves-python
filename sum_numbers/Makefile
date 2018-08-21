PYTHON_NAME = "gosum"
CFLAGS = `python3.6-config --cflags`
LDFLAGS = `python3.6-config --ldflags`

# Use when necessary
# PKG_CONFIG_PATH = "${PKG_CONFIG_PATH}:/home/rafael/.pyenv/versions/3.7.0/lib/pkgconfig"

build: SHELL:=/bin/bash
build: clean
	@echo "--> Recreate .so module"
	@go build -buildmode=c-shared -o $(PYTHON_NAME).so $(PYTHON_NAME).go && echo "Done 1/3"
	@python build.py > ${PYTHON_NAME}.c && echo "Done 2/3"
	@gcc -fPIC ${PYTHON_NAME}.c ${PYTHON_NAME}.so -o ${PYTHON_NAME}_module.so ${CFLAGS} -nostartfiles ${LDFLAGS} && echo "Done 3/3"

clean:
	@echo "--> Cleaning C files"
	@rm -rf *.c *.h *.so 

benchmark: 
	@LD_LIBRARY_PATH="." pytest .

