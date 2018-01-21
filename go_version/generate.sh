#!/bin/bash
PYTHON_NAME="gosum"
CFLAGS=`/usr/bin/python3.5-config --cflags`
LDFLAGS=`/usr/bin/python3.5-config --ldflags`

go build -buildmode=c-shared -o ${PYTHON_NAME}.so ${PYTHON_NAME}.go && \
python build.py > ${PYTHON_NAME}.c && \
gcc ${PYTHON_NAME}.c ${PYTHON_NAME}.so -o ${PYTHON_NAME}_module.so ${CFLAGS} -nostartfiles ${LDFLAGS}

