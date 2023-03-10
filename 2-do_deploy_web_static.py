#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
       distributes an archive to your web servers
Returns False if the file at the path archive_path doesn't exist
"""
import os
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ['18.215.163.12', '54.91.24.222']


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if archive_path is None or not os.path.exists(archive_path):
        return False
    try:
        file = archive_path.split("/")[-1]
        file_no_ext = file.split(".")[0]
        path = "/data/web_static/releases/"
        # upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # create a folder with the same name as the archive
        # without the extension
        run("mkdir -p {}{}/".format(path, file_no_ext))
        # uncompress the archive to the folder
        run("tar -xzf /tmp/{} -C {}{}/".format(
            file, path, file_no_ext))
        # delete the archive from the web server
        run("rm /tmp/{}".format(file))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, file_no_ext))
        # delete the symbolic link /data/web_static/current from the web server
        run("rm -rf {}{}/web_static".format(path, file_no_ext))
        run("rm -rf /data/web_static/current")
        # create new symbolic link /data/web_static/current on web server
        # linked to the new version of your code
        run("ln -s {}{}/ /data/web_static/current".
            format(path, file_no_ext))
        return True
    except:
        return False
