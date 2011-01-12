#!/bin/sh

running=`/usr/bin/condor_status -schedd -format '%s\n' 'TotalRunningJobs' -const 'Name == "glidein.unl.edu"'`
/usr/bin/gmetric --name="Running Jobs" --value="$running" --type=uint32 --units="Jobs" --tmax=600


idle=`/usr/bin/condor_status -schedd -const 'Name == "glidein.unl.edu"' -format '%s\n' 'TotalIdleJobs'`
/usr/bin/gmetric --name="Idle Jobs" --value="$idle" --type=uint32 --units="Jobs" --tmax=600


