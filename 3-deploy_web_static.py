#!/usr/bin/python3
"""Module that contains do_pack, do_deploy and deploy functions."""
from fabric.api import local, env, put, run
from time import strftime
import os.path
env.hosts = ['54.160.217.25', '3.87.244.249']


def do_pack():
    """Generate .tgz archive of web_static/ folder."""
    timenow = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        f_name = "versions/web_static_{}.tgz".format(timenow)
        local("tar -cvzf {} web_static/".format(f_name))
        return f_name
    except:
        return None


def do_deploy(archive_path):
    """Distributes archive to my web servers."""
    if os.path.isfile(archive_path) is False:
        return False
    try:
        f_name = archive_path.split("/")[-1]
        no_ext = f_name.split(".")[0]
        path_no_ext = "/data/web_static/releases/{}/".format(no_ext)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}".format(f_name, path_no_ext))
        run("rm /tmp/{}".format(f_name))
        run("mv {}web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}web_static".format(path_no_ext))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(path_no_ext, symlink))
        return True
    except:
        return False


def deploy():
    """Creates and distributes an archive."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    success = do_deploy(archive_path)
    return success
