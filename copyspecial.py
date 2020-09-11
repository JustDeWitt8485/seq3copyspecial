#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = """Tracy DeWitt,
Manuel Velasco,
README,
https://stackoverflow.com/questions/24705679/
misunderstanding-of-python-os-path-abspath,
https://youtu.be/K8L6KVGG-7o,
"""

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    spfile_list = []
    sp_pattern = re.compile(r'__(\w+)__')
    for item in os.listdir(dirname):
        if sp_pattern.search(item):
            spfile_list.append(os.path.abspath(os.path.join(dirname, item)))
    return spfile_list


def copy_to(path_list, dest_dir):
    """ This function copies the path_list to the dest_dir """
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)

    for item in path_list:
        shutil.copy(item, dest_dir)


def zip_to(path_list, dest_zip):
    """ This will create a zipfile containing the files """
    list_zip = ['zip', '-j', dest_zip]
    list_zip.extend(path_list)
    subprocess.run(list_zip)


def main(args):
    """Main driver code for copyspecial. """
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='dest zipfile for special files')

    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    ns_list = get_special_paths(ns.fromdir)

    # Check to see if ns.todir exists if it does
    # invoke the function copy_to on ns.todir
    if ns.todir:
        copy_to(ns_list, ns.todir)

    # Check to see if ns.tozip exists if it does
    # invoke the function zip_to on ns.tozip
    if ns.tozip:
        zip_to(ns_list, ns.tozip)

    # If neither of these run else print('\n'.join(ns_list))
    if not ns.tozip and not ns.todir:
        print('\n'.join(ns_list))


if __name__ == "__main__":
    main(sys.argv[1:])
