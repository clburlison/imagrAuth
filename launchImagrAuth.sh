#!/bin/bash

/usr/bin/hdiutil mount -quiet -nobrowse "http://server/dmgs/imagrAuth.dmg"
/Volumes/imagrAuth/imagrAuth.py
/usr/bin/hdiutil unmount /Volumes/imagrAuth