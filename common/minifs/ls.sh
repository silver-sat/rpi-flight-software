#!/bin/sh
${GROUND_IP:=192.168.100.101}
${MINIFS_PORT:=5001}
curl -s 'http://${GROUND_IP}:${MINIFS_PORT}/list'
