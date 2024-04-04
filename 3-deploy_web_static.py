#!/usr/bin/python3
from fabric.api import env

def deploy():
    """Creates and distributes an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
