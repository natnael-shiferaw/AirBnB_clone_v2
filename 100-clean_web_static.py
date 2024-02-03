#!/usr/bin/python3
"""
- A Fabric Script that deletes out-of-date archives
- To execute it use the following command:
fab -f 100-clean_web_static.py do_clean:number=2
    -i ssh-key -u ubuntu > /dev/null 2>&1
"""

import os
from fabric.api import *

env.hosts = ['54.210.53.71', '34.224.3.246']


def do_clean(number=0):
    """A function that deletes out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    -if number is 0 or 1, keeps only the most recent archive,
    -if number is 2, keeps the most and second-most
       recent archives
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
