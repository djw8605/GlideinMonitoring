#!/usr/bin/python

from mod_python import apache

import os, subprocess
os.environ['HOME'] = "/tmp"
from graphtool.graphs.common_graphs import PieGraph

def index(req):
    allsites(req)

def handler(req):
    req.write("hello") 


def allusers(req):
    (stdout, stderr) = runCommand(". /opt/condor-7.4.3/condor.sh; condor_status -format '%s\n' 'RemoteOwner' | sort | uniq -c")
    users = {}
    for line in stdout.readlines():
         split_line = line.strip().split()
         users[split_line[1]] = split_line[0]
    pie = PieGraph()
    metadata = { 'title': 'Users Running' }
    req.content_type = "image/x-png"
    pie.run(users, req, metadata)




def allsites(req):
    (stdout, stderr) = runCommand(". /opt/condor-7.4.3/condor.sh; condor_status -format '%s\n' 'GLIDEIN_Site' -const 'IS_MONITOR_VM =!= TRUE' | sort | uniq -c")
    sites = {}
    for line in stdout.readlines():
        split_line = line.strip().split()
        sites[split_line[1]] = split_line[0]
    
    pie = PieGraph()
    metadata = { 'title': 'Sites running glideins' }
    req.content_type = "image/x-png"
    pie.run(sites, req, metadata)


    #req.write(stderr.read())

def gsitedata(req):
    (stdout, stderr) = runCommand(". /opt/condor-7.4.3/condor.sh; condor_status -format '%s\n' 'GLIDEIN_Site' -const 'IS_MONITOR_VM =!= TRUE' | sort | uniq -c")
    final_out = "<sitedata>"
    for line in stdout.readlines():
        split_line =  line.strip().split()
        final_out += "<site name=\"%s\" running=\"%s\"/>" % ( split_line[1], split_line[0] )
    final_out += "</sitedata>"
    req.write(final_out)

    
def guserdata(req):
    (stdout, stderr) = runCommand(". /opt/condor-7.4.3/condor.sh;  condor_status -submitter -format '<user name=\"%s\"' 'Name' -format ' idle=%i' 'IdleJobs' -format ' running=%i />' 'RunningJobs'")
    final_out = "<userdata>"
    final_out += stdout.read()
    final_out += "</userdata>"
    req.write(final_out)
     


def runCommand(command):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return (p.stdout, p.stderr)



