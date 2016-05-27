from __future__ import with_statement
from fabric.api import *
from fabric.contrib.files import exists
from fabric.operations import local as lrun, run
from fabric.context_managers import env
from pprint import pprint
import os
import pdb
import sys

oscommerce_version = "2.3.4"
oscommerce_download_url = "%s%s%s" % ("https://www.oscommerce.com/files/oscommerce-",oscommerce_version,".zip")

root_dir = "/vagrant/htdocs"
download_path = "/tmp/oscommerce"

@task
def localhost():
    env.run = lrun
    env.hosts = ['localhost']
    env.use_sudo = True
    env.password = 'vagrant'

@task
def execute(*args, **kwargs):
    if env.use_sudo:
        sudo(*args, **kwargs)
    else:
        run(*args, **kwargs)

@task
def init():
    execute("mkdir -p %s" % (download_path))
    with cd(download_path):
        execute("rm oscommerce*.zip > /dev/null")
        execute("wget %s" % (oscommerce_download_url))
        execute("unzip oscommerce*.zip")
        execute("cp -rf oscommerce*/* %s" % (root_dir))
        execute("chmod -R 777 %s" % (root_dir))