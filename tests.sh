#!/bin/sh
black --check .
pylama .
py.test -s -v -x tests/
