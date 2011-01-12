#!/bin/sh

running=`condor_status -schedd -format '%s\n' 'TotalRunningJobs' -const 'Name == "glidein.unl.edu"'`

gmetric --name="Running Jobs" --value="$running" --type=uint32 --units="Jobs" --tmax=600

