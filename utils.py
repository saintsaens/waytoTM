#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil


# Return the list of directories (excluding files) directly under the directory root_dir_path.
def get_direct_subdirs(root_dir_path):
    # Get list of immediate subdirectories.
    list_of_subdirs = filter(os.path.isdir, [os.path.join(root_dir_path, f) for f in os.listdir(root_dir_path)])

    return list_of_subdirs


# Return the list of directories and files directly under the directory root_dir_path.
def get_direct_elements(root_dir_path):
    # Get list of immediate elements.
    stub_list = os.listdir(root_dir_path)

    # Remove that ugly .DS_Store.
    if stub_list.count(".DS_Store") > 0:
        stub_list.remove(".DS_Store")

    # Prepend the whole path of elements.
    list_of_elements = [os.path.join(root_dir_path, f) for f in stub_list]

    return list_of_elements


def merge_folders(root_path, merging_criteria):
    # Create destination folder for all files in the list of folders to squash.
    merged_folder = root_path + "/Merged " + merging_criteria
    if not os.path.exists(merged_folder):
        os.makedirs(merged_folder)

    # Get list of folders with merging criteria in their name.
    wildcard = "Merged"
    dirs_to_merge = get_list_of_mergeables(root_path, merging_criteria, wildcard)

    # Move files in new folder.
    copy_from_list(dirs_to_merge, merged_folder)

    # Delete old folders.

    return merged_folder


def get_list_of_mergeables(root_path, merging_criteria, not_that_one):
    # Get list of folders with naming criteria.
    list_of_subdirs = get_direct_subdirs(root_path)
    dirs_to_merge = []
    for x in list_of_subdirs:
        if merging_criteria in x:
            # Don't scan the wildcard
            if not_that_one not in x:
                dirs_to_merge.append(x)

    return dirs_to_merge


# Return NOK if level has no doublons, otherwise return OK.
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


# Given a folder, check if there is a file with ".jpg" or ".png" in it.
# Return 1 if there is, and 0 otherwise.
def check_image(root_path):
    list_to_check = get_direct_elements(root_path)
    for x in list_to_check:
        if ".jpg" in x or ".png" in x:
            return True
    return False


def copy_from_list(src_dirs_list, dst_dir):
    for x in src_dirs_list:
        files_to_move = os.listdir(x)
        for y in files_to_move:
            src_file_path = x + "/" + y
            dst_file_path = dst_dir + "/" + y
            # Check if file already exist before copying/moving it to the dst.
            if not os.path.exists(dst_file_path):
                shutil.copyfile(src_file_path, dst_file_path)


def copy_images(src_dir, dst_dir):
    list_to_check = os.listdir(src_dir)

    # Get list of all images in src directory.
    list_src_of_images = []
    for x in list_to_check:
        if ".jpg" in x or ".png" in x:
            list_src_of_images.append(x)

    # Copy each image onto the dst directory.
    for x in list_src_of_images:
        src_file_path = src_dir + "/" + x
        dst_file_path = dst_dir + "/" + x
        if not os.path.exists(dst_file_path):
            shutil.copyfile(src_file_path, dst_file_path)
