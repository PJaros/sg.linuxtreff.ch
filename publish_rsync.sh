#!/bin/bash
rsync -vr --progress --delete /home/jarop/git/sg-linuxtreff-ch/output/ "sg.linuxtreff.ch:sg.linuxtreff.ch"
