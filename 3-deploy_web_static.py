#!/usr/bin/python3
"""
Fabric script to create and distribute archived web_static to web servers
"""
from fabric.api import local
do_pack = __import__('1-pack_web_static').do_pack


def do_deploy():
    """
    creates and distributes archived web_static to web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return True
