# Glidein monitoring

This is the glidein monitoring used at the University of Nebraska - Lincoln.

There are three components to the monitoring:

*   glidestats - Graphs of current usage <http://glidein.unl.edu/glidestats/>
*   sites - RRD plotting of past usage <http://glidein.unl.edu/sites/>
*   gmetric - Ganglia reporting of usage.


## Dependencies
### Glidestats
graphtool from the repo:
<http://t2.unl.edu/store/repos/nebraska/5/nebraska/x86_64/>

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


### Sites
*   javascriptrrd library: <http://sourceforge.net/projects/javascriptrrd/>  
*   rrdtool (yum should pull it in)



## Installation

### Glidestats
Needs to be moved into a web accessable directory.  The example above uses /var/www/html/glidestats.  Image generation should then work.  


### Sites
Web accessable.  The javascriptrrd libraries should be in lib directory.





