#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/7/18
from __future__ import absolute_import

import os
import sys







def main(args):
    cwd = os.getcwd()
    sys.path.append(cwd)
    host = '127.0.0.1'
    port = 8000
    print(sys.path)
    try:
        arg = args[0]
    except IndexError:
        pass
    else:
        host, port = arg.split(":")
        port = int(port)
    print('Server on {}:{}'.format(host,port))
    from servers.server import do_server
    do_server(host=host,port=port)




if __name__ == "__main__":
    main(sys.argv[1:])