#File Rename

# Imported Modules
import sys
import os
import shutil, errno

def RenameMe(work_dir, name_init, name_final):
    try:

        os.chdir(work_dir) 
        os.rename(name_init, name_final)        

        
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise
