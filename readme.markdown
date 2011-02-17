# Glidein monitoring

This is the glidein monitoring used at the University of Nebraska - Lincoln.

There are three components to the monitoring:
*   glidestats - Graphs of current usage
*   sites - RRD plotting of past usage
*   gmetric - Ganglia reporting of usage.


## Dependencies
The index.py requires graphtool:
http://t2.unl.edu/store/repos/nebraska/5/nebraska/x86_64/graphtool-0.6.6-6.noarch.rpm


## Installation
There are 3 components to this monitoring.  


Additionally, condor needs the configuration value:
    JOBGLIDEIN_Site="$$([IfThenElse(IsUndefined(TARGET.GLIDEIN_Site), FileSystemDomain, TARGET.GLIDEIN_Site)])"
    SUBMIT_EXPRS = $(SUBMIT_EXPRS) JOBGLIDEIN_Site




