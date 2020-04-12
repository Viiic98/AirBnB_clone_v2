#!/usr/bin/python3
""" Faricb functions """
from fabric.api import run, local
from datetime import datetime


def do_pack():
    """ Create a version package of web_static folder """

    f = "versions/web_static_{:s}.tgz".format(datetime.now()
                                              .strftime("%Y%m%d%H%M%S"))
    cmnd = "tar -czvf "+f+" ./web_static/"
    local('mkdir -p versions')
    try:
        local(cmnd)
        return f
    except:
        return None
