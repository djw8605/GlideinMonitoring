# Glidein monitoring

This is the glidein monitoring used at the University of Nebraska - Lincoln.

There are three components to the monitoring:

*   glidestats - Graphs of current usage
*   sites - RRD plotting of past usage
*   gmetric - Ganglia reporting of usage.


## Dependencies
The glidestats requires graphtool from the repo:
http://t2.unl.edu/store/repos/nebraska/5/nebraska/x86_64/

mod_python for the image generating.  Configuration for the mod_python should be something like:
    <Directory "/var/www/html/glidestats">
        <Files *.html>
            SetHandler default-handler
        </Files>
        # AddHandler mod_python .py
        
        SetHandler mod_python
        PythonHandler mod_python.publisher
        PythonDebug On
        DirectoryIndex index.py
    </Directory>




## Installation

### Glidestats
For glidestats:
Needs to be moved into a web accessable directory.  The example above uses /var/www/html/glidestats.  


Condor needs the configuration value:
    JOBGLIDEIN_Site="$$([IfThenElse(IsUndefined(TARGET.GLIDEIN_Site), FileSystemDomain, TARGET.GLIDEIN_Site)])"
    SUBMIT_EXPRS = $(SUBMIT_EXPRS) JOBGLIDEIN_Site




