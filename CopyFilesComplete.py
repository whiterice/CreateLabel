 #File Copier

# Imported Modules
import sys
import os
import shutil, errno
from distutils.dir_util import copy_tree

def copyanything(src, dst):
    try:
        copy_tree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise
