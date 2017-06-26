# -*- coding: utf-8 -*-
import os
import stat
import zipfile
import datetime as dt

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def read(path, loader=None):
    with open(path) as fh:
        if not loader:
            return fh.read()
        return loader(fh.read())


def archive(src, dest, filename):
    output = os.path.join(dest, filename)
    zfh = zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED)

    for root, _, files in os.walk(src):
        for file in files:
            filePath = os.path.join(root, file)
            zfh.write(filePath)
            # set global read+write+execute permissions (needed to execute binaries)
            # TODO: set permission from file
            info = zfh.getinfo(filePath.strip("./"))
            info.external_attr = 0777 << 16L
    zfh.close()
    return os.path.join(dest, filename)


def timestamp(fmt='%Y-%m-%d-%H%M%S'):
    now = dt.datetime.utcnow()
    return now.strftime(fmt)
