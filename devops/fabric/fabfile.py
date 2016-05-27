from __future__ import with_statement
from fabric.api import *
from fabric.contrib.files import exists
from pprint import pprint
import os
import pdb
import sys

oscommerce_version = "2.3.4"
oscommerce_download_url = "%s%s%s" % ("https://www.oscommerce.com/files/oscommerce-",oscommerce_version,".zip")

root_dir = "/vagrant/htdocs"
env.hosts = ["192.168.49.49"]
env.use_sudo = True
env.user = "vagrant"
env.group = "vagrant"
download_path = "/tmp/oscommerce"

@task
def execute(*args, **kwargs):
    if env.use_sudo:
        sudo(*args, **kwargs)
    else:
        run(*args, **kwargs)

@task
def init():
    run("mkdir -p %s" % (download_path))
    with cd(download_path):
        execute("rm oscommerce*.zip")
        execute("wget %s" % (oscommerce_download_url))
        execute("unzip oscommerce*.zip")
        execute("cp -rf oscommerce*/* %s" % (root_dir))
        execute("chmod -R 777 %s" % (root_dir))