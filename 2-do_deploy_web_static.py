#!/usr/bin/python3
""" Faricb functions """
from fabric.api import *
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['35.190.146.135', '35.185.29.47']


def do_deploy(archive_path):
    """ Send the current version of static web to the servers """

    f_name = archive_path.split('/')[1]

    put(archive_path, '/tmp/')
    run('mkdir -p /data/web_static/releases/{:s}/'.format(f_name))
    run('tar -xzf /tmp/{:s} -C /data/web_static/releases/{:s}'
        .format(f_name, f_name))
    run('rm /tmp/{:s}'.format(f_name))
    run('mv /data/web_static/releases/{:s}/web_static/* \
         /data/web_static/releases/{:s}'
        .format(f_name,
                f_name))
    run('rm -rf /data/web_static/releases/{:s}/web_static'.format(f_name))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{:s} /data/web_static/current'
        .format(f_name))
    print("New version deployed!")
