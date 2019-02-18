#!/bin/bash

echo "Removing documentation..."
# if we need to keep copyright files for legal reasons:
# find /usr/share/doc -depth -type f ! -name copyright | xargs rm || true
# else:
find /usr/share/doc -depth -type f | xargs rm || true
rm -rf /usr/share/man/* /usr/share/groff/* /usr/share/info/* /usr/share/lintian/* /usr/share/linda/* /var/cache/man/*
