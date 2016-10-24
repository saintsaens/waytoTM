#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils
import mover
import os

TEST_PATH = "/Users/flavien/Workspace/waytoTM/tests/fakedatastore"


def test_get_direct_subdirs():
    assert type(utils.get_direct_subdirs(TEST_PATH)) == list
    assert len(utils.get_direct_subdirs(TEST_PATH)) == 3


def test_get_direct_elements_type():
    assert type(utils.get_direct_elements(TEST_PATH)) == list
    assert len(utils.get_direct_elements(TEST_PATH)) == 4


def test_get_list_of_mergeables():
    path_to_mergeables = TEST_PATH + "/folder1"
    dont_merge_me = "dontmerge"
    assert type(utils.get_list_of_mergeables(path_to_mergeables, mover.MP3_320, dont_merge_me)) == list
    assert len(utils.get_list_of_mergeables(path_to_mergeables, mover.MP3_320, dont_merge_me)) == 2
    assert len(utils.get_list_of_mergeables(path_to_mergeables, mover.MP3_V0, dont_merge_me)) == 0


def test_check_level_320_nok():
    nok_path = TEST_PATH + "/folder1"
    assert utils.check_level(nok_path, mover.MP3_320) == "NOK"


def test_check_level_320_ok():
    ok_path = TEST_PATH + "/folder2"
    assert utils.check_level(ok_path, mover.MP3_320) == "OK"


def test_check_image_fail():
    path_to_fail = TEST_PATH + "/folder1"
    assert utils.check_image(path_to_fail) == False
    assert utils.check_image(TEST_PATH) == False


def test_check_image_success():
    path_to_success = TEST_PATH + "/folder3"
    assert utils.check_image(path_to_success) == True


def test_copy_from_list():
    input_folder_1 = TEST_PATH + "/folder1/subfolder1.2 [320]"
    input_folder_2 = TEST_PATH + "/folder1/subfolder1.3 [320]"
    input_list = [input_folder_1, input_folder_2]
    total_length = 0
    for x in input_list:
        total_length += len(utils.get_direct_elements(x))
    dst_folder = TEST_PATH + "/folder3/Mergetest "
    # TODO: if directory exists, purge it.
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    utils.copy_from_list(input_list, dst_folder)
    assert len(utils.get_direct_elements(dst_folder)) == total_length


def test_copy_images():
    src_folder = TEST_PATH + "/folder3"
    dst_folder = TEST_PATH + "/folder3/Mergetest "
    # TODO: if directory exists, purge it.
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    utils.copy_images(src_folder, dst_folder)

    list_src_to_check = os.listdir(src_folder)
    list_of_src_images = []
    for x in list_src_to_check:
        if ".jpg" in x:
            list_of_src_images.append(x)
        elif ".png in x":
            list_of_src_images.append(x)

    list_dst_to_check = os.listdir(dst_folder)
    list_of_dst_images = []
    for y in list_dst_to_check:
        if ".jpg" in y:
            list_of_dst_images.append(y)
        elif ".png in y":
            list_of_dst_images.append(y)

    assert len(list_of_dst_images) == len(list_of_src_images)
