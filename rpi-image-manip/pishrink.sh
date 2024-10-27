#!/bin/sh

# docker build -t pishrink pishrink
docker run -it --rm --privileged=true -v `pwd`:/workdir pishrink "$@"
