#!/bin/bash

# make python

unzip urbancode.zip

unzip ibm-ucd-agent.zip
mv ibm-ucd-agent-install agent/
rm ibm-ucd-agent.zip

unzip ibm-ucd-install.zip
mv ibm-ucd-install server/
rm ibm-ucd-install.zip

unzip agent-relay.zip
mv agent-relay-install relay/
rm agent-relay.zip

# docker-compose up
