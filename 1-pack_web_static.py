#!/usr/bin/python3
"""
- A Fabric script that generates a .tgz archive from the
contents of the web_static folder of the AirBnB Clone repo,
using the function do_pack.
- To execute it use: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    Returns the archive path if the archive has been
    correctly generated. Otherwise, it should return None
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
