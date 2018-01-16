#!/bin/bash
GO_NAME="sum_numbers"
PYTHON_NAME="gosum"
CFLAGS=`/usr/bin/python3.5-config --cflags`
LDFLAGS=`/usr/bin/python3.5-config --ldflags`

if [ -z $GO_NAME -o -z $PYTHON_NAME ]; then
    echo "Syntax: GO_NAME=<go program name> PYTHON_NAME=<python module name> $0"
    exit 1
fi

go build -buildmode=c-shared -o ${GO_NAME}.so ${GO_NAME}.go && \
python build.py > ${GO_NAME}.c && \
gcc ${GO_NAME}.c -dynamiclib ${GO_NAME}.so -o ${PYTHON_NAME}.so ${CFLAGS} -nostartfiles ${LDFLAGS}

