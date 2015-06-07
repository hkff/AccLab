#!/bin/sh
tar -zcf pyAAL.tar --exclude='*.idea' --exclude='*.pyc' --exclude='coverage/html/*' --exclude='simul/*' --exclude='*.toc' --exclude='*.blg' --exclude='*.bbl' --exclude='*.aux' --exclude='*.out' --exclude='*.log'  --exclude='examples/test1.aal' --exclude='examples/simul.aal' pyAAL/  
