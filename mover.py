#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils
import personal_constants
import argparse
import logging

MP3_320 = "[320]"
MP3_V0 = "[V0]"
MP3_V2 = "[V2]"
MP3_FORMATS = [MP3_320, MP3_V0, MP3_V2]

if __name__ == '__main__':
    levels = ['info', 'debug', 'error', 'warning', 'critical']
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--level', dest='level', default='info',
                        choices=['info', 'debug', 'error', 'warning', 'critical'])
    args = parser.parse_args()
    logging.basicConfig(level=getattr(logging, args.level.upper()))

# Get all subfolders in FLAC_FOLDER (level 0).
flac_dirs_lvl_0 = utils.get_direct_subdirs(personal_constants.FLAC_FOLDER)

for x in flac_dirs_lvl_0:
    logging.debug("Getting contents of " + x + "...")
    logging.debug("Checking if there is another level...")
    if utils.get_direct_subdirs(x):
        logging.debug("Yes")
        # There is another level, so dance once again: get all subdirs in the current subdir of FLAC_FOLDER (level 1).
        flac_dirs_lvl_1 = utils.get_direct_subdirs(x)
        for y in flac_dirs_lvl_1:
            logging.debug("Getting contents of " + y + "...")
            # Check if there are at least 2 directories with 320 at lvl 2, and merge them.
            if utils.check_level(y, MP3_320) == "NOK":
                merged_dir = utils.merge_folders(y, MP3_320)
                # Copy cover art.
                if utils.check_image(y) == 1:
                    utils.copy_images(y, merged_dir)
    else:
        # Check if there are at least 2 directories with 320 at lvl 1, and merge them.
        if utils.check_level(x, MP3_320) == "NOK":
            utils.merge_folders(x, MP3_320)

logging.debug("Checking the number of files in new folder matches number of files in FLAC folder.")
logging.debug("Deleting old folders.")

