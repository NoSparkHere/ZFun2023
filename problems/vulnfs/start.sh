#!/bin/sh

# use chroot to change root directory to /app, and then launch /usr/local/bin/vuln-file-server
cd /home/user
/usr/local/bin/vuln-file-server
