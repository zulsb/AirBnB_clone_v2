#!/usr/bin/python3
"""Module that contains do_pack function."""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generate .tgz archive of web_static/ folder."""
    timenow = datetime.now()
    try:
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(timenow)
        local("tar -cvzf {} web_static/".format(filename))
        return filename
    except:
        return None
