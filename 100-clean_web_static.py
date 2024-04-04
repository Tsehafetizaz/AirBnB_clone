#!/usr/bin/python3
from fabric.api import env, run, local

def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number == 0:
        number = 1
    
    # Clean local archives
    local("ls -t versions | tail -n +{} | xargs rm -rf".format(number + 1))
    
    # Clean remote archives
    run("ls -t /data/web_static/releases | tail -n +{} | xargs rm -rf".format(number + 1))
