#!/usr/bin/env python3
import shutil
import os


def main():
    os.chdir("/home/student/mycode/")
    # move files into another folder within obj described in above os.chdir
    shutil.move("raynor.obj", "ceph_storage/")
    
    # collect string input for new file name
    xname = input('What is the new name for kerrigan.obj? ')

    # rename the file using the user input above
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
