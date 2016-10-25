#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil


def get_direct_subdirs(root_dir_path):
    """Return the list of directories (excluding files) directly under the directory root_dir_path.
    :rtype: list
    """
    # Get list of immediate subdirectories.
    list_of_subdirs = filter(os.path.isdir, [os.path.join(root_dir_path, f) for f in os.listdir(root_dir_path)])

    return list_of_subdirs


def get_direct_elements(root_dir_path):
    """Return the list of directories and files directly under the directory root_dir_path.
    :rtype: list
    """
    # Get list of immediate elements.
    stub_list = os.listdir(root_dir_path)

    # Remove that ugly .DS_Store.
    if stub_list.count(".DS_Store") > 0:
        stub_list.remove(".DS_Store")

    # Prepend the whole path of elements.
    list_of_elements = [os.path.join(root_dir_path, f) for f in stub_list]

    return list_of_elements


def merge_folders(root_path, merging_criteria):
    """Return a folder containing the files of all folders in root_path with merging_criteria in their name.
    :rtype: path
    """
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
    """Return the list of folders in root_path with merging_criteria in their name,
    except for folders with not_that_one in their name.
    :rtype: list
    """
    # Get list of folders with naming criteria.
    list_of_subdirs = get_direct_subdirs(root_path)
    dirs_to_merge = []
    for x in list_of_subdirs:
        if merging_criteria in x:
            # Don't scan the wildcard
            if not_that_one not in x:
                dirs_to_merge.append(x)

    return dirs_to_merge


def level_has_doublons(root_path, check_criteria):
    """Return True if root_path has at least 2 folders with check_criteria in their names, and False otherwise.
    :rtype: bool
    """
    # print "Checking level \"" + root_path + "\" for " + check_criteria + " occurences..."
    list_of_subdirs = get_direct_subdirs(root_path)
    list_to_check = []
    for x in list_of_subdirs:
        if check_criteria in x:
            list_to_check.append(x)
    # print "Found " + str(len(list_to_check)) + "."

    if len(list_to_check) > 1:
        return True
    else:
        return False


def level_has_image(root_path):
    """Return True if there is at least a file with ".jpg" or ".png" in root_path.
    :rtype: bool
    """
    list_to_check = get_direct_elements(root_path)
    for x in list_to_check:
        if ".jpg" in x or ".png" in x:
            return True
    return False


def copy_from_list(src_dirs_list, dst_dir):
    """Copy the contents of each item in src_dirs_list into dst_dir."""
    for x in src_dirs_list:
        files_to_move = os.listdir(x)
        for y in files_to_move:
            src_file_path = x + "/" + y
            dst_file_path = dst_dir + "/" + y
            # Check if file already exist before copying/moving it to the dst.
            if not os.path.exists(dst_file_path):
                shutil.copyfile(src_file_path, dst_file_path)


def copy_images(src_dir, dst_dir):
    """Copy all files with \".jpg\" or \".png\" in src_dir into dst_dir."""
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
