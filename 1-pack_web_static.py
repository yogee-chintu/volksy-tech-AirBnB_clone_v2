#!/usr/bin/python3
"""
Fabric script to generate .tgz archive from contents of web_static folder
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    generates .tgz archive from contents of web_static folder
    """
    local("mkdir -p versions")
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(current_time)
    result = local("tar -czf {} web_static/".format(path))
    if result.failed:
        return None
    return (path)
