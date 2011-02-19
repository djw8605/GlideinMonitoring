


from mod_python import apache
import sys,os
def index(req):
    
    
    req.content_type = "text/html"
    curpath = os.path.abspath(__file__)
    cwd = curpath.rsplit("/", 1)[0]
    #req.write(cwd)
    f = open(os.path.join(cwd,"index.html"))

    #f = open("%s/index.html" % os.path.abspath(pathname))
    req.write(f.read())

