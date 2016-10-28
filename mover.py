#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils
import const
import argparse
import logging

if __name__ == '__main__':
# ================================ PART 0: LOGGING THINGS =================================
    levels = ['info', 'debug', 'error', 'warning', 'critical']
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--level', dest='level', default='info',
                        choices=['info', 'debug', 'error', 'warning', 'critical'])
    args = parser.parse_args()
    logging.basicConfig(level=getattr(logging, args.level.upper()))


# ==================================== PART 1: MERGING ====================================
    # Get all subfolders in FLAC_FOLDER (level 0).
    flac_dirs_lvl_0 = utils.get_direct_subdirs(const.FLAC_DIR)
    logging.debug("Getting list of all folders at level 0:" + str(flac_dirs_lvl_0))

    # Divide albums into clean (1 folder per format) and dirty (many folders per format, in case of VA).
    dirty_albums = []
    clean_albums = []
    for x in flac_dirs_lvl_0:
        if utils.album_is_clean(x):
            clean_albums.append(x)
        else:
            dirty_albums.append(x)

    for x in flac_dirs_lvl_0:
        logging.debug("Looking at " + x + "...")
        logging.debug("Checking if there is another level...")
        if utils.get_direct_subdirs(x, const.MP3_FORMATS):
            # There is another level, so dance once again: get all subdirs in the current subdir of FLAC_FOLDER (level 1).
            flac_dirs_lvl_1 = utils.get_direct_subdirs(x, const.MP3_FORMATS)
            logging.debug("Yes: " + str(flac_dirs_lvl_1))
            for y in flac_dirs_lvl_1:
                logging.debug("Looking at " + y + "...")
                # Check if there are at least 2 directories with 320 at lvl 2, and merge them.
                if utils.level_has_doublons(y, const.MP3_320) is True:
                    merged_dir = utils.merge_folders(y, const.MP3_320)
                    # Copy cover art into merged folder.
                    if utils.level_has_image(y):
                        utils.copy_images(y, merged_dir)

        else:
            # Level 1 is the deepest.
            # Check if there are at least 2 directories with 320 at lvl 1, and merge them.
            if utils.level_has_doublons(x, const.MP3_320) is True:
                merged_dir = utils.merge_folders(x, const.MP3_320)
                # Copy cover art into merged folder.
                if utils.level_has_image(x):
                    utils.copy_images(x, merged_dir)

    logging.debug("Checking the number of files in new folder matches number of files in FLAC folder.")

# ================================= PART 2: COPYING IMAGES ================================
    logging.debug("Copying images into transcoded folders that did not need merging...")
    # Check if there is an image at each level, and copy the image into all folders of that level.
    for x in flac_dirs_lvl_0:
        if utils.level_has_image(x):
            logging.debug("Found image(s) in: " + x + ".")
            if utils.get_direct_subdirs(x):
                mp3_dirs_lvl_1 = utils.get_direct_subdirs(x)
                for y in mp3_dirs_lvl_1:
                    logging.debug("Copying image(s) into: " + y + "...")
                    utils.copy_images(x, y)
        else:
            if utils.get_direct_subdirs(x):
                logging.debug("Found no image in: " + x)
                flac_dirs_lvl_1 = utils.get_direct_subdirs(x)
                for y in flac_dirs_lvl_1:
                    if utils.level_has_image(y):
                        logging.debug("Found image(s) in: " + y + ".")
                        if utils.get_direct_subdirs(y):
                            mp3_dirs_lvl_2 = utils.get_direct_subdirs(y)
                            for z in mp3_dirs_lvl_2:
                                logging.debug("Copying image(s) into: " + z + ".")
                                utils.copy_images(y, z)

# ==================== PART 3: MOVING MERGED FOLDERS INTO UPLOAD FOLDER ===================
    for x in flac_dirs_lvl_0:
        if utils.get_direct_subdirs(x, const.MP3_FORMATS):
            utils.move_merged_double_level(x, const.UPLOAD_DIR, const.MP3_320)
        else:
            utils.move_merged_single_level(x, const.UPLOAD_DIR, const.MP3_320)
