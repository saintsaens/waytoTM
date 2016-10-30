#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import const


def get_direct_subdirs(root_dir_path, excluding_criteria=[]):
    """Return the list of the paths of directories (excluding files) directly under the directory root_dir_path, except
    folders containing name_criteria.

    :rtype: list
    :param root_dir_path: path to folder where to get the direct subdirectories.
    :param excluding_criteria: string excluding folders containing it in their name.
    :return: list of direct subdirectories.
    """
    raw_list_of_subdirs = filter(os.path.isdir, [os.path.join(root_dir_path, f) for f in os.listdir(root_dir_path)])
    list_of_subdirs = []
    # TODO: this method of excluding criteria should be improved.
    list_of_bad_subdirs = []
    if len(excluding_criteria) > 0:
        # Create a list with all the bad folders.
        for x in raw_list_of_subdirs:
            for y in excluding_criteria:
                if y in x and x not in list_of_subdirs:
                    list_of_bad_subdirs.append(x)

        # Create the opposite list.
        for z in raw_list_of_subdirs:
            if z not in list_of_bad_subdirs:
                list_of_subdirs.append(z)
    else:
        list_of_subdirs = raw_list_of_subdirs

    return list_of_subdirs


def get_direct_elements(root_dir_path):
    """
    Get the list of the paths of directories and files directly under the directory root_dir_path.
    :param root_dir_path: path to folder where to get the direct elements.
    :return: list of direct elements.
    """
    # Get list of immediate elements.
    stub_list = os.listdir(root_dir_path)

    # Remove that ugly .DS_Store.
    if ".DS_Store" in stub_list:
        stub_list.remove(".DS_Store")

    # Prepend the whole path of elements.
    list_of_elements = [os.path.join(root_dir_path, f) for f in stub_list]

    return list_of_elements


def merge_album(album_path, merging_criteria):
    # Double level.
    list_of_discpaths = get_direct_subdirs(album_path, const.MP3_FORMATS)
    if list_of_discpaths:
        for x in list_of_discpaths:
            merge_folders(x, merging_criteria)

    # Single level.
    else:
        merge_folders(album_path, merging_criteria)


def merge_folders(root_path, merging_criteria):
    """
    Create a merged folder, containing the files of all folders in root_path with merging_criteria in their name.
    :param root_path: folder containing all folders to be merged.
    :param merging_criteria: string triggering the merging.
    :return: path to the merged folder.
    """
    wildcard = const.MERGED_FOLDER_NAME + " "
    # Create destination folder for all files in the list of folders to squash.
    merged_folder = root_path + "/" + wildcard + merging_criteria
    if not os.path.exists(merged_folder):
        os.makedirs(merged_folder)

    # Get list of folders with merging criteria in their name.
    dirs_to_merge = get_list_of_mergeables(root_path, merging_criteria, wildcard)

    # Move files in new folder.
    copy_from_list(dirs_to_merge, merged_folder)

    return merged_folder


def get_list_of_mergeables(root_path, merging_criteria, not_that_one):
    """
    Get the list of folders under root_path with merging_criteria in their name,
    except for folders with not_that_one in their name.
    :param root_path: starting top folder.
    :param merging_criteria: string determining the mergeability.
    :param not_that_one: string excluding the mergeability (priority blacklist).
    :return: list of paths of directories.
    """
    # Get list of folders with naming criteria.
    list_of_subdirs = get_direct_subdirs(root_path)
    dirs_to_merge = []
    for x in list_of_subdirs:
        if merging_criteria in x:
            if not_that_one not in x:
                dirs_to_merge.append(x)

    return dirs_to_merge


def level_has_doublons(root_path, check_criteria):
    """
    Determine if root_path has at least 2 folders with check_criteria in their names.
    :param root_path: starting top folder.
    :param check_criteria: string that makes you a culprit if you have it in your name.
    :return: True if there is at least 2 folders with check_criteria in their names. False otherwise.
    """
    # print "Checking level \"" + root_path + "\" for " + check_criteria + " occurences..."
    list_of_subdirs = get_direct_subdirs(root_path)
    list_to_check = []
    for x in list_of_subdirs:
        if check_criteria in x:
            list_to_check.append(x)

    if len(list_to_check) > 1:
        return True
    else:
        return False


def level_has_image(root_path):
    """
    Determine if there is at least a file with ".jpg" or ".png" in root_path.
    :param root_path: starting top folder.
    :return: True if there is at least a file with ".jpg" or ".png" in root_path. False otherwise.
    """
    list_to_check = get_direct_elements(root_path)
    for x in list_to_check:
        if ".jpg" in x or ".png" in x:
            return True
    return False


def copy_from_list(src_dirs_list, dst_dir):
    """
    Copy the contents of each item in src_dirs_list into dst_dir.
    If file already exists, do not copy it.
    :param src_dirs_list: list of all source directories paths from where to copy all contents.
    :param dst_dir: unique destination folder path to where the contents must be copied.
    :return: nothing.
    """
    for x in src_dirs_list:
        files_to_move = os.listdir(x)
        for y in files_to_move:
            src_file_path = x + "/" + y
            dst_file_path = dst_dir + "/" + y
            # Check if file already exist before copying/moving it to the dst.
            if not os.path.exists(dst_file_path):
                shutil.copyfile(src_file_path, dst_file_path)


def copy_images_in_album(album_path):
    # Double level.
    list_of_discpaths = get_direct_subdirs(album_path, [const.MP3_320])
    if list_of_discpaths:
        for x in list_of_discpaths:
            if level_has_image(x):
                list_of_dirs = get_direct_subdirs(x)
                copy_images_to_list(x, list_of_dirs)

    # Single level.
    if level_has_image(album_path):
        list_of_dirs = get_direct_subdirs(album_path)
        copy_images_to_list(album_path, list_of_dirs)


def copy_images_to_list(src_dir, list_of_dst_dir):
    for x in list_of_dst_dir:
        copy_images(src_dir, x)


def copy_images(src_dir, dst_dir):
    """
    Copy all files with \".jpg\" or \".png\" in src_dir into dst_dir.
    If file already exists, do not copy it.
    :param src_dir: source directory path.
    :param dst_dir: destination directory path.
    :return: nothing.
    """
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


def get_flacs(src_dir):
    """
    Get the list of all flac files in src_dir.
    :param src_dir: path to the directory containing all the flac files to get.
    :return: list of flac files
    """
    list_of_flacs = []
    elements = get_direct_elements(src_dir)
    for x in elements:
        if ".flac" in x:
            list_of_flacs.append(x)
    return list_of_flacs


def copy_merged_single_level(album_path, upload_folder_path=const.UPLOAD_DIR, mp3_format=const.MP3_320):
    """
    Copy and rename the merged folder into the upload folder.
    :param album_path: path of the album where the merged folder is.
    :param upload_folder_path: path of the destination folder.
    :param mp3_format: format type to append to the merged folder name.
    :return: nothing.
    """
    album_path_stub = os.path.basename(os.path.normpath(album_path))
    clean_merged_folder_path = upload_folder_path + "/" + album_path_stub + " " + mp3_format

    merged_folder_path = get_merged_folder_path(album_path)
    if merged_folder_path and not os.path.exists(clean_merged_folder_path):
        shutil.copytree(merged_folder_path, clean_merged_folder_path)


def copy_merged_double_level(album_path, upload_folder_path=const.UPLOAD_DIR, mp3_format=const.MP3_320):
    """
    Copy and rename the merged folders into the upload folder, when album is divided into discs (additional folder
    level).
    :param album_path: path of the album where the merged folders are.
    :param upload_folder_path: destination folder path.
    :param mp3_format: format type to append to the appropriate folders.
    :return: nothing.
    """
    album_path_stub = os.path.basename(os.path.normpath(album_path))

    # Create renamed destination album folder.
    clean_album_folder_path = upload_folder_path + "/" + album_path_stub + " " + mp3_format
    if not os.path.exists(clean_album_folder_path):
        os.makedirs(clean_album_folder_path)

    list_of_discpaths = get_direct_subdirs(album_path)
    for disc_path in list_of_discpaths:
        disc_path_stub = os.path.basename(os.path.normpath(disc_path))
        clean_merged_folder_path = clean_album_folder_path + "/" + disc_path_stub
        dirname_path = get_merged_folder_path(disc_path)
        if dirname_path and not os.path.exists(clean_merged_folder_path):
            shutil.copytree(dirname_path, clean_merged_folder_path)


def get_merged_folder_path(dir_path, merged_pattern=const.MERGED_FOLDER_NAME):
    """
    Get the full path of the merged folder in the specified directory.
    :param dir_path: path to the directory where the merged folder is.
    :param merged_pattern: string to look for when listing all directories.
    :return: path to the merged folder.
    """
    list_of_dirpaths = get_direct_subdirs(dir_path)
    for dirname_path in list_of_dirpaths:
        if merged_pattern in dirname_path:
            return dirname_path
    return ""


def copy_clean_single_level(album_path, pattern, upload_folder_path=const.UPLOAD_DIR):
    """
    In a given album without discs, copy all folders with pattern in their name into an upload folder.
    :param album_path: path of the album where the transcoded folders are.
    :param upload_folder_path: path to the destination upload folder.
    :param pattern: criteria to copy folders (only folders with the given criteria are copied).
    :return:
    """
    dirs_to_upload = get_direct_subdirs(album_path)
    for dirname_path in dirs_to_upload:
        if pattern in dirname_path:
            dirname_path_stub = os.path.basename(os.path.normpath(dirname_path))
            dirname_new_path = upload_folder_path + "/" + dirname_path_stub
            if dirname_path and not os.path.exists(dirname_new_path):
                shutil.copytree(dirname_path, dirname_new_path)


def copy_clean_double_level(album_path, pattern, upload_folder_path=const.UPLOAD_DIR):
    """
    In a given album with discs, copy all folders with pattern in their name into an upload folder.
    :param album_path: path of the album where the transcoded folders are.
    :param upload_folder_path: path to the destination upload folder.
    :param pattern: criteria to copy folders (only folders with the given criteria are copied).
    :return:
    """
    album_path_stub = os.path.basename(os.path.normpath(album_path))

    # Create renamed destination album folder.
    clean_album_folder_path = upload_folder_path + "/" + album_path_stub + " " + pattern
    if not os.path.exists(clean_album_folder_path):
        os.makedirs(clean_album_folder_path)

    #
    list_of_discpaths = get_direct_subdirs(album_path)
    for disc_path in list_of_discpaths:
        disc_path_stub = os.path.basename(os.path.normpath(disc_path))
        dirs_to_upload = get_direct_subdirs(disc_path)
        for dirname_path in dirs_to_upload:
            if pattern in dirname_path:
                dirname_path_stub = os.path.basename(os.path.normpath(dirname_path))
                dirname_new_path = clean_album_folder_path + "/" + disc_path_stub + "/" + dirname_path_stub
                if dirname_path and not os.path.exists(dirname_new_path):
                    shutil.copytree(dirname_path, dirname_new_path)


def album_is_clean(album_path, check_criteria=[]):
    """
    Determine if album is clean, by checking the number of occurrences of check_criteria in its subfolders.
    Example: if check_criteria is ["320"], an album is clean if it has at most 1 folder with "320" in it.
    :param album_path:
    :param check_criteria:
    :return:
    """

    # Double level.
    list_of_discpaths = get_direct_subdirs(album_path, const.MP3_FORMATS)
    if list_of_discpaths:
        for x in list_of_discpaths:
            for y in check_criteria:
                if not folder_is_clean(x, y):
                    return False
        return True

    # Single level.
    for y in check_criteria:
        if not folder_is_clean(album_path, y):
            return False
    return True


def folder_is_clean(dir_path, check_criteria):
    list_of_doublons = []
    list_of_dirpaths = get_direct_subdirs(dir_path)
    for x in list_of_dirpaths:
        if check_criteria in x:
            list_of_doublons.append(x)
    if len(list_of_doublons) > 1:
        return False
    return True
