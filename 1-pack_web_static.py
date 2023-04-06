#!/usr/bin/python3
import os
import tarfile
import datetime

def do_pack():
    now = datetime.datetime.utcnow()
    file_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    archive_path = os.path.join("versions", file_name)
    if not os.path.exists("versions"):
        os.makedirs("versions")

    try:
        with tarfile.open(archive_path, "w:gz") as archive:
            archive.add("web_static", arcname=os.path.basename("web_static"))
        return archive_path
    except:
        return None
