#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
from time import strftime

def do_pack():
    now = datetime.now()
    time_stamp = now.strftime("%Y%m%d%H%M%S")
    Filename = "web_static_{}.tgz".format(time_stamp)
    local("mkdir -p versions")
    result = local("tar -czvf versions/{} web_static".format(Filename))
    if result.failed:
        return None
    return "versions/{}".format(Filename)
