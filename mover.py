#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils
import const
import argparse
import logging


# ================================ PART 0: LOGGING THINGS =================================
if __name__ == '__main__':
    levels = ['info', 'debug', 'error', 'warning', 'critical']
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--level', dest='level', default='info',
                        choices=['info', 'debug', 'error', 'warning', 'critical'])
    args = parser.parse_args()
    logging.basicConfig(level=getattr(logging, args.level.upper()))


# ==================================== PART 1: MERGING ====================================
    # Get all subfolders in FLAC_FOLDER (level 0).
    all_flac_albums = utils.get_direct_subdirs(const.FLAC_DIR)
    logging.debug("List of dirs at level 0:" + str(all_flac_albums))
    logging.info("Getting list of all albums...")

    # Divide albums into clean (1 folder per format) and dirty (many folders per format, in case of VA).
    logging.info("Dividing into clean and dirty albums...")
    dirty_albums = []
    clean_albums = []
    for x in all_flac_albums:
        if utils.album_is_clean(x, const.MP3_FORMATS):
            clean_albums.append(x)
        else:
            dirty_albums.append(x)
    logging.debug("Clean albums: " + str(clean_albums))
    logging.debug("Dirty albums: " + str(dirty_albums))

    # Merge all those dirty Various Artists into a single merged folder.
    logging.info("Merging dirty albums...")
    for album in dirty_albums:
        list_of_transcoded_formats = utils.album_has_formats(album)
        for x in list_of_transcoded_formats:
            utils.merge_album(album, x)

    logging.info("Copying images everywhere, trying to bring back some color to this world...")
    for album in all_flac_albums:
        utils.copy_images_in_album(album)

# ==================== PART 2: MOVING FOLDERS INTO UPLOAD FOLDER ===================
    logging.info("Copying transcoded folders into the upload folder...")
    for album in dirty_albums:
        list_of_transcoded_formats = utils.album_has_formats(album)
        if utils.get_direct_subdirs(album, const.MP3_FORMATS):
            for x in list_of_transcoded_formats:
                utils.copy_merged_double_level(album, x)
        else:
            for x in list_of_transcoded_formats:
                utils.copy_merged_single_level(album, x)

    for album in clean_albums:
        list_of_transcoded_formats = utils.album_has_formats(album)
        if utils.get_direct_subdirs(album, const.MP3_FORMATS):
            for x in list_of_transcoded_formats:
                utils.copy_clean_double_level(album, x)
        else:
            for x in list_of_transcoded_formats:
                utils.copy_clean_single_level(album, x)
