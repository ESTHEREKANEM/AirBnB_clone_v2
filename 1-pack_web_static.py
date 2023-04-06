#!/usr/bin/python3
from fabric.api import local
from datetime import date
from time import strftime

def do_pack():
    """ This Script generates archive the contents of web_static """
    file_Name = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(file_Name))
        return "versions/web_static_{}.tgz".format(file_Name)

    except Exception as e:
        print("Exception occurred while creating archive: ", e)
        return None
