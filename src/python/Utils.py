import os
import shutil


def log(log_data):
    print("\033[m" + log_data)


def logError(error_data):
    print("\033[0;32;31m" + error_data)


def makedir(dir2make):
    if not os.path.exists(dir2make):
        os.makedirs(dir2make)


def rmdir(dir2remove):
    if os.path.exists(dir2remove):
        shutil.rmtree(dir2remove, True)


def copyfile(src, des):
    shutil.copy(src, des)
