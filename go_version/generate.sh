#!/bin/bash
#export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/home/rafael/.pyenv/versions/3.7.0/lib/pkgconfig
export PYTHON_NAME="gosum"
export CFLAGS=`python3.6-config --cflags`
export LDFLAGS=`python3.6-config --ldflags`

go build -buildmode=c-shared -o ${PYTHON_NAME}.so ${PYTHON_NAME}.go && echo "ok [1]" && \
python build.py > ${PYTHON_NAME}.c && echo "ok [2]" && \
gcc -fPIC ${PYTHON_NAME}.c ${PYTHON_NAME}.so -o ${PYTHON_NAME}_module.so ${CFLAGS} -nostartfiles ${LDFLAGS} && echo "ok [3]"
