#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils

FLAC_FOLDER = "/Users/flavien/Music/What/FLAC"
MP3_FORMATS = ["[320]", "[V0]", "[V2]"]
MP3_320 = "[320]"
MP3_V0 = "[V0]"
MP3_V2 = "[V2]"

# Get all subfolders in FLAC_FOLDER (level 0).
flac_dirs_lvl_0 = utils.get_direct_subdirs(FLAC_FOLDER)
for x in flac_dirs_lvl_0:
    # print "Getting contents of " + x + "..."
    # print "Checking if there is another level..."
    if utils.get_direct_subdirs(x):
        # print "Yes"
        # There is another level, so dance once again.
        flac_dirs_lvl_1 = utils.get_direct_subdirs(x)
        for y in flac_dirs_lvl_1:
            # print "Getting contents of " + y + "..."
            # Check if there are at least 2 directories with 320, and merge them.
            if utils.check_level(y, MP3_320) == "NOK":
                merged_dir = utils.merge_folders(y, MP3_320)
                # Copy cover art.
                if utils.check_image(y) == 1:
                    utils.copy_images(y, merged_dir)
    else:
        # Check if there are at least 2 directories with 320, and merge them.
        if utils.check_level(x, MP3_320) == "NOK":
            utils.merge_folders(x, MP3_320)

# print "Is there a cover art in the FLAC folder?"


# print "Copying image from FLAC to new folder."

# print "Checking the number of files in new folder matches number of files in FLAC folder."

# print "Deleting old folders."

