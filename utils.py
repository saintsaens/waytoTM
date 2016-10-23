#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def get_direct_subdirs(root_dir_path):
    # Get list of immediate subdirectories.
    list_of_subdirs = filter(os.path.isdir, [os.path.join(root_dir_path, f) for f in os.listdir(root_dir_path)])

    # Remove that ugly .DS_Store.
    if list_of_subdirs.count(".DS_Store") > 0:
        list_of_subdirs.remove(".DS_Store")

    return list_of_subdirs


def get_direct_elements(root_dir_path):
    # Get list of immediate elements.
    list_of_elements = [os.path.join(root_dir_path, f) for f in os.listdir(root_dir_path)]

    # Remove that ugly .DS_Store.
    if list_of_elements.count(".DS_Store") > 0:
        list_of_elements.remove(".DS_Store")

    return list_of_elements


def merge_folders(root_path, merging_criteria):
    # Get list of folders with naming criteria.
    list_of_subdirs = get_direct_subdirs(root_path)
    list_to_merge =[]
    # print "Merging 320 files in " + root_path
    for x in list_of_subdirs:
        if merging_criteria in x:
            list_to_merge.append(x)
            # print x

    # Create new folder.
    # TODO: create function for the correct name.
    new_path = root_path + "/Merged " + merging_criteria
    if not os.path.exists(new_path):
        os.makedirs(new_path)

    # Move files in new folder.
    # Check sum of all files in old folders matches number of files in new folder.
    # Delete old folders.


def check_level(root_path, check_criteria):
    # print "Checking level \"" + root_path + "\" for " + check_criteria + " occurences..."
    list_of_subdirs = get_direct_subdirs(root_path)
    list_to_check = []
    for x in list_of_subdirs:
        if check_criteria in x:
            list_to_check.append(x)
    # print "Found " + str(len(list_to_check)) + "."

    if len(list_to_check) > 1:
        return "NOK"
    else:
        return "OK"
