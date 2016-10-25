#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils
import mover
import os
import shutil

TEST_PATH = "/Users/flavien/Workspace/waytoTM/tests/fakedatastore"


def test_get_direct_subdirs():
    assert type(utils.get_direct_subdirs(TEST_PATH)) == list
    assert len(utils.get_direct_subdirs(TEST_PATH)) == 3


def test_get_direct_elements():
    assert type(utils.get_direct_elements(TEST_PATH)) == list
    assert len(utils.get_direct_elements(TEST_PATH)) == 4


def test_get_list_of_mergeables():
    path_to_mergeables = TEST_PATH + "/folder1"
    dont_merge_me = "dontmerge"
    assert type(utils.get_list_of_mergeables(path_to_mergeables, mover.MP3_320, dont_merge_me)) == list
    assert len(utils.get_list_of_mergeables(path_to_mergeables, mover.MP3_320, dont_merge_me)) == 2
    assert len(utils.get_list_of_mergeables(path_to_mergeables, mover.MP3_V0, dont_merge_me)) == 0


def test_level_has_doublons_320():
    true_path = TEST_PATH + "/folder1"
    false_path = TEST_PATH + "/folder2"
    assert utils.level_has_doublons(true_path, mover.MP3_320) is True
    assert utils.level_has_doublons(false_path, mover.MP3_320) is False


def test_level_has_image_fail():
    path_to_fail = TEST_PATH + "/folder1"
    assert utils.level_has_image(path_to_fail) is False
    assert utils.level_has_image(TEST_PATH) is False


def test_level_has_image_success():
    path_to_success = TEST_PATH + "/folder3"
    assert utils.level_has_image(path_to_success) is True


def test_copy_from_list():
    input_folder_1 = TEST_PATH + "/folder1/subfolder1.2 [320]"
    input_folder_2 = TEST_PATH + "/folder1/subfolder1.3 [320]"
    input_list = [input_folder_1, input_folder_2]
    total_length = 0
    for x in input_list:
        total_length += len(utils.get_direct_elements(x))
    dst_folder = TEST_PATH + "/folder3/Mergetest "
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    utils.copy_from_list(input_list, dst_folder)
    assert len(utils.get_direct_elements(dst_folder)) == total_length
    shutil.rmtree(dst_folder)


def test_copy_images():
    src_folder = TEST_PATH + "/folder3"
    dst_folder = TEST_PATH + "/folder3/Mergetest "
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    utils.copy_images(src_folder, dst_folder)

    list_src_to_check = os.listdir(src_folder)
    list_of_src_images = []
    for x in list_src_to_check:
        if ".jpg" in x or ".png" in x:
            list_of_src_images.append(x)

    list_dst_to_check = os.listdir(dst_folder)
    list_of_dst_images = []
    for y in list_dst_to_check:
        if ".jpg" in y or ".png" in y:
            list_of_dst_images.append(y)

    assert len(list_of_dst_images) == len(list_of_src_images)
    shutil.rmtree(dst_folder)
