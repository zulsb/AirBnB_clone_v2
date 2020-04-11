#!/usr/bin/python3
"""Module that contains do_pack function."""
from fabric.api import local
from time import strftime


def do_pack():
    """Generate .tgz archive of web_static/ folder."""
    time_now = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        f_name = "versions/web_static_{}.tgz".format(time_now)
        local("tar -cvzf {} web_static/".format(f_name))
        return f_name
    except:
        return None
