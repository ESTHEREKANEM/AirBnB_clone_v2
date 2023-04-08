#!/usr/bin/python3
"""In the following example, the SSH key and the username used for accessing to the server are passed in the command line
"""
from fabric.api import env, put, run, sudo
from os.path import exists
import os

env.hosts = ['54.146.79.137', '54.152.191.29']

def do_deploy(archive_path):
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        file_name = os.path.basename(archive_path)
        folder_name = "/data/web_static/releases/{}".format(file_name.split(".")[0])
        run("sudo mkdir -p {}/".format(folder_name))
        run("sudo tar -xzf /tmp/{} -C {}/".format(file_name, folder_name))
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(folder_name))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Exception occurred during deployment: ", e)
        return False
