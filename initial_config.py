#!/usr/bin/python

import shutil
import zipfile
import os

def move_server():
    shutil.move('ibm-ucd-install', 'server')

def extract_agent():
    shutil.copy('ibm-ucd-install/overlay/opt/tomcat/webapps/ROOT/tools/ibm-ucd-agent.zip', 'agent')
    agent_zip = zipfile.ZipFile('agent/ibm-ucd-agent.zip', 'r')
    agent_zip.extractall('agent')
    agent_zip.close()
    os.remove('agent/ibm-ucd-agent.zip')

if __name__ == "__main__":
    extract_agent()
    move_server()
    print "Files copied..."
    print "Now run ... $ docker-compose up"