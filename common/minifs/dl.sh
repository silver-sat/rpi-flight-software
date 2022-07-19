#!/bin/sh
curl -f -s -o "${4:-$3}" "http://${1}:${2}/download?file=$3" && echo "Success"
