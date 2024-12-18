#!/bin/bash
lftp -c "set ftp:list-options -a;
set ssl:verify-certificate false;
open ftp://sg.linuxtreff.ch:"$password"@sg.linuxtreff.ch; 
lcd /home/jarop/git/sg-linuxtreff-ch/output;
cd .;
mirror --reverse --delete --use-cache --verbose --allow-chown --no-umask --parallel=2"
