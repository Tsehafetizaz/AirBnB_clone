#!/usr/bin/python3
from fabric.api import put, run, env

env.hosts = ['web-01.ip', 'web-02.ip']

def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not archive_path:
        return False
    
    try:
        # Upload the archive
        put(archive_path, '/tmp/')
        archive_name = archive_path.split("/")[-1]
        base_dir = "/data/web_static/releases/" + archive_name.split(".")[0] + "/"
        run("mkdir -p " + base_dir)
        
        # Uncompress the archive
        run("tar -xzf /tmp/{} -C {}".format(archive_name, base_dir))
        run("rm /tmp/{}".format(archive_name))
        
        # Move content
        run("mv {}web_static/* {}".format(base_dir, base_dir))
        run("rm -rf {}web_static".format(base_dir))
        
        # Update the symbolic link
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(base_dir))
        return True
    except:
        return False

