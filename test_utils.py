#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils
import os
import shutil
import const


def test_get_direct_subdirs():
    src_folder = const.TEST_PATH + "/folder1"
    assert type(utils.get_direct_subdirs(const.TEST_PATH)) == list
    assert len(utils.get_direct_subdirs(const.TEST_PATH)) == 5
    assert len(utils.get_direct_subdirs(src_folder, ["[320]", "[V0]", "[V2]"])) == 2


def test_get_direct_elements():
    assert type(utils.get_direct_elements(const.TEST_PATH)) == list
    assert len(utils.get_direct_elements(const.TEST_PATH)) == 6


def test_get_list_of_mergeables():
    path_to_mergeables = const.TEST_PATH + "/folder1"
    dont_merge_me = "dontmerge"
    assert type(utils.get_list_of_mergeables(path_to_mergeables, const.MP3_320, dont_merge_me)) == list
    assert len(utils.get_list_of_mergeables(path_to_mergeables, const.MP3_320, dont_merge_me)) == 2
    assert len(utils.get_list_of_mergeables(path_to_mergeables, const.MP3_V0, dont_merge_me)) == 0


def test_level_has_doublons_320():
    true_path = const.TEST_PATH + "/folder1"
    false_path = const.TEST_PATH + "/folder2"
    assert utils.level_has_doublons(true_path, const.MP3_320) is True
    assert utils.level_has_doublons(false_path, const.MP3_320) is False


def test_level_has_image_fail():
    path_to_fail = const.TEST_PATH + "/folder1"
    assert utils.level_has_image(path_to_fail) is False
    assert utils.level_has_image(const.TEST_PATH) is False


def test_level_has_image_success():
    path_to_success = const.TEST_PATH + "/folder3"
    assert utils.level_has_image(path_to_success) is True


def test_copy_from_list():
    input_folder_1 = const.TEST_PATH + "/folder1/subfolder1.2 [320]"
    input_folder_2 = const.TEST_PATH + "/folder1/subfolder1.3 [320]"
    input_list = [input_folder_1, input_folder_2]
    total_length = 0
    for x in input_list:
        total_length += len(utils.get_direct_elements(x))
    dst_folder = const.TEST_PATH + "/folder3/Mergetest "
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    utils.copy_from_list(input_list, dst_folder)
    assert len(utils.get_direct_elements(dst_folder)) == total_length
    shutil.rmtree(dst_folder)


def test_copy_images_to_list():
    src_folder = const.TEST_PATH + "/folder3"
    path_a6 = const.TEST_PATH + "/folder6 for copying"
    path_a6b1 = path_a6 + "/bla [320]"
    path_a6b2 = path_a6 + "/blo [320]"

    list_of_paths = [path_a6, path_a6b1, path_a6b2]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)

    list_of_dst = [path_a6b1, path_a6b2]
    utils.copy_images_to_list(src_folder, list_of_dst)
    copied_image1 = path_a6b1 + "/art.png"
    copied_image2 = path_a6b1 + "/cover.jpg"
    copied_image3 = path_a6b1 + "/front.jpg"
    copied_image4 = path_a6b2 + "/art.png"
    copied_image5 = path_a6b2 + "/cover.jpg"
    copied_image6 = path_a6b2 + "/front.jpg"
    assert os.path.exists(copied_image1)
    assert os.path.exists(copied_image2)
    assert os.path.exists(copied_image3)
    assert os.path.exists(copied_image4)
    assert os.path.exists(copied_image5)
    assert os.path.exists(copied_image6)
    shutil.rmtree(path_a6)


def test_copy_images_in_album_double():
    src_folder = const.TEST_PATH + "/folder7 for images"
    path_a2d1 = src_folder + "/disc1"
    path_a2d1b1 = path_a2d1 + "/bla [320]"
    path_a2d1b1d1 = path_a2d1 + "/art.png"
    path_a2d1b1d2 = path_a2d1 + "/cover.jpg"
    path_a2d1b1d3 = path_a2d1 + "/front.jpg"
    path_a2d2 = src_folder + "/disc2"
    path_a2d2b1 = path_a2d2 + "/bla [320]"

    # Create all files and folders with those paths.
    list_of_paths_dirs = [src_folder, path_a2d1, path_a2d2, path_a2d1b1, path_a2d2b1]
    for x in list_of_paths_dirs:
        if not os.path.exists(x):
            os.makedirs(x)
    list_of_paths_images = [path_a2d1b1d1, path_a2d1b1d2, path_a2d1b1d3]
    for y in list_of_paths_images:
        if not os.path.exists(y):
            open(y, 'a').close()

    utils.copy_images_in_album(src_folder)
    copied_image1 = path_a2d1b1 + "/art.png"
    copied_image2 = path_a2d1b1 + "/cover.jpg"
    copied_image3 = path_a2d1b1 + "/front.jpg"
    copied_image4 = path_a2d2b1 + "/art.png"
    copied_image5 = path_a2d2b1 + "/cover.jpg"
    copied_image6 = path_a2d2b1 + "/front.jpg"
    assert os.path.exists(copied_image1)
    assert os.path.exists(copied_image2)
    assert os.path.exists(copied_image3)
    assert not os.path.exists(copied_image4)
    assert not os.path.exists(copied_image5)
    assert not os.path.exists(copied_image6)
    shutil.rmtree(src_folder)


def test_copy_images():
    src_folder = const.TEST_PATH + "/folder3"
    dst_folder = src_folder + "/Mergetest "
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


def test_get_flac_list():
    src_folder = const.TEST_PATH + "/folder2"
    list_of_flacs = utils.get_flacs(src_folder)
    assert len(list_of_flacs) == 3


def test_merge_album_double():
    path_a6 = const.TEST_PATH + "/folder6 for merging"
    path_a2 = path_a6 + "/album2"
    path_a2d1 = path_a2 + "/disc1"
    path_a2d1b1 = path_a2d1 + "/bla [320]"
    path_a2d1b2 = path_a2d1 + "/blo [320]"
    path_a2d2 = path_a2 + "/disc2"
    path_a2d2b1 = path_a2d2 + "/bla [320]"
    path_a2d2b2 = path_a2d2 + "/blo [320]"

    list_of_paths = [path_a6, path_a2, path_a2d1, path_a2d1b1, path_a2d1b2, path_a2d2, path_a2d2b1, path_a2d2b2]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)

    merged_folder1 = path_a2d1 + "/" + const.MERGED_FOLDER_NAME + " " + const.MP3_320
    merged_folder2 = path_a2d2 + "/" + const.MERGED_FOLDER_NAME + " " + const.MP3_320
    utils.merge_album(path_a2, const.MP3_320)
    assert os.path.exists(merged_folder1)
    assert os.path.exists(merged_folder2)
    shutil.rmtree(path_a6)


def test_merge_folders():
    test_path_a1 = const.TEST_PATH + "/folder4 for merging/album1"
    test_path_a1b1 = test_path_a1 + "/bla [320]"
    test_path_a1b2 = test_path_a1 + "/blo [320]"

    if not os.path.exists(test_path_a1):
        os.makedirs(test_path_a1)
    if not os.path.exists(test_path_a1b1):
        os.makedirs(test_path_a1b1)
    if not os.path.exists(test_path_a1b2):
        os.makedirs(test_path_a1b2)

    merged_folder = utils.merge_folders(test_path_a1, const.MP3_320)
    assert os.path.exists(merged_folder)
    shutil.rmtree(test_path_a1)


def test_copy_merged_single_level():
    upload_folder = const.TEST_PATH + "/folder5 for uploading"
    flac_folder = const.TEST_PATH + "/folder4 for merging"
    path_a1 = flac_folder + "/album1"
    path_a1b1 = flac_folder + "/album1/bla [320]"
    path_a1b2 = flac_folder + "/album1/blo [320]"
    path_a1m = flac_folder + "/album1/Merged [320]"
    path_a1md = flac_folder + "/album1/Merged [320]/caca.flac"

    list_of_paths = [path_a1, path_a1b1, path_a1b2, path_a1m]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)
    if not os.path.exists(path_a1md):
        open(path_a1md, 'a').close()

    utils.copy_merged_single_level(path_a1, upload_folder, const.MP3_320)
    new_merged_folder = upload_folder + "/album1 [320]"
    assert os.path.exists(new_merged_folder)
    shutil.rmtree(path_a1)
    shutil.rmtree(new_merged_folder)


def test_copy_merged_double_level():
    # Create all paths
    upload_folder = const.TEST_PATH + "/folder5 for uploading"
    flac_folder = const.TEST_PATH + "/folder4 for merging"
    path_a2 = flac_folder + "/album2"
    path_a2d1 = path_a2 + "/disc1"
    path_a2d1b1 = path_a2d1 + "/bla [320]"
    path_a2d1b2 = path_a2d1 + "/blo [320]"
    path_a2d1m = path_a2d1 + "/Merged [320]"
    path_a2d1md = path_a2d1 + "/Merged [320]/caca1.flac"
    path_a2d2 = path_a2 + "/disc2"
    path_a2d2b1 = path_a2d2 + "/bla [320]"
    path_a2d2b2 = path_a2d2 + "/blo [320]"
    path_a2d2m = path_a2d2 + "/Merged [320]"
    path_a2d2md = path_a2d2 + "/Merged [320]/caca2.flac"

    # Create all files and folders with those paths.
    list_of_paths = [path_a2, path_a2d1, path_a2d2, path_a2d1b1, path_a2d1b2, path_a2d2b1, path_a2d2b2, path_a2d1m,
                     path_a2d2m]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)
    if not os.path.exists(path_a2d1md):
        open(path_a2d1md, 'a').close()
    if not os.path.exists(path_a2d2md):
        open(path_a2d2md, 'a').close()

    # Do the dragons, and assert for tests.
    utils.copy_merged_double_level(path_a2, upload_folder, const.MP3_320)
    new_merged_folder1 = upload_folder + "/album2 [320]"
    new_merged_folder11 = upload_folder + "/album2 [320]/disc1"
    new_merged_folder12 = upload_folder + "/album2 [320]/disc2"
    assert os.path.exists(new_merged_folder1)
    assert os.path.exists(new_merged_folder11)
    assert os.path.exists(new_merged_folder12)
    shutil.rmtree(path_a2)
    shutil.rmtree(new_merged_folder1)


def test_copy_clean_single_level():
    upload_folder = const.TEST_PATH + "/folder5 for uploading"
    flac_folder = const.TEST_PATH + "/folder4 for merging"
    path_a2 = flac_folder + "/album2"
    path_a2d1 = path_a2 + "/blo [320]"
    path_a2d2 = path_a2 + "/bla [V0]"
    path_a2d3 = path_a2 + "/bli [V2]"

    # Create all files and folders with those paths.
    list_of_paths = [path_a2, path_a2d1, path_a2d2, path_a2d3]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)

    utils.copy_clean_single_level(path_a2, upload_folder)
    uploaded_dir1 = upload_folder + "/blo [320]"
    assert os.path.exists(uploaded_dir1)
    shutil.rmtree(path_a2)
    shutil.rmtree(uploaded_dir1)


def test_copy_clean_double_level():
    upload_folder = const.TEST_PATH + "/folder5 for uploading"
    flac_folder = const.TEST_PATH + "/folder4 for merging"
    path_a2 = flac_folder + "/album2"
    path_a2d1 = path_a2 + "/disc1"
    path_a2d1b1 = path_a2d1 + "/disc1 [320]"
    path_a2d1b2 = path_a2d1 + "/disc1 [V0]"
    path_a2d2 = path_a2 + "/disc2"
    path_a2d2b1 = path_a2d2 + "/disc2 [320]"
    path_a2d2b2 = path_a2d2 + "/disc2 [V0]"

    # Create all files and folders with those paths.
    list_of_paths = [path_a2, path_a2d1, path_a2d2, path_a2d1b1, path_a2d1b2, path_a2d2b1, path_a2d2b2]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)

    utils.copy_clean_double_level(path_a2, upload_folder)
    uploaded_dir1 = upload_folder + "/album2 [320]"
    uploaded_dir11 = upload_folder + "/album2 [320]/disc1 [320]"
    uploaded_dir12 = upload_folder + "/album2 [320]/disc2 [320]"
    assert os.path.exists(uploaded_dir1)
    assert os.path.exists(uploaded_dir11)
    assert os.path.exists(uploaded_dir12)
    shutil.rmtree(path_a2)
    shutil.rmtree(uploaded_dir1)


def test_get_merged_folder_path():
    path_a1 = const.TEST_PATH + "/folder4 for merging/album1"
    path_a1b1 = path_a1 + "/bla [320]"
    path_a1b2 = path_a1 + "/blo [320]"
    path_a1m = path_a1 + "/Merged [320]"
    path_a1md = path_a1 + "/Merged [320]/caca.flac"

    list_of_paths = [path_a1, path_a1b1, path_a1b2, path_a1m]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)
    if not os.path.exists(path_a1md):
        open(path_a1md, 'a').close()

    assert utils.get_merged_folder_path(path_a1) == path_a1m
    shutil.rmtree(path_a1)


def test_album_is_clean_single_true():
    path_a2 = const.TEST_PATH + "/folder4 for merging/album2"
    path_a2b1 = path_a2 + "/bla [320]"

    list_of_paths = [path_a2, path_a2b1]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)

    assert utils.album_is_clean(path_a2, const.MP3_320) is True
    shutil.rmtree(path_a2)


def test_album_is_clean_single_false():
    path_a2 = const.TEST_PATH + "/folder4 for merging/album2"
    path_a2b1 = path_a2 + "/bla [320]"
    path_a2b2 = path_a2 + "/blo [320]"

    list_of_paths = [path_a2, path_a2b1, path_a2b2]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)

    assert utils.album_is_clean(path_a2, const.MP3_320) is False
    shutil.rmtree(path_a2)


def test_album_is_clean_double_false():
    path_a2 = const.TEST_PATH + "/folder4 for merging/album2"
    path_a2d1 = path_a2 + "/disc1"
    path_a2d1b1 = path_a2d1 + "/bla [320]"
    path_a2d1b2 = path_a2d1 + "/blo [320]"
    path_a2d2 = path_a2 + "/disc2"
    path_a2d2b1 = path_a2d2 + "/bla [320]"
    path_a2d2b2 = path_a2d2 + "/blo [320]"

    # Create all files and folders with those paths.
    list_of_paths = [path_a2, path_a2d1, path_a2d2, path_a2d1b1, path_a2d1b2, path_a2d2b1, path_a2d2b2]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)

    assert utils.album_is_clean(path_a2, const.MP3_320) is False
    shutil.rmtree(path_a2)


def test_album_is_clean_double_true():
    path_a2 = const.TEST_PATH + "/folder4 for merging/album2"
    path_a2d1 = path_a2 + "/disc1"
    path_a2d1b1 = path_a2d1 + "/bla [320]"
    path_a2d2 = path_a2 + "/disc2"
    path_a2d2b1 = path_a2d2 + "/bla [320]"

    # Create all files and folders with those paths.
    list_of_paths = [path_a2, path_a2d1, path_a2d2, path_a2d1b1, path_a2d2b1]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)

    assert utils.album_is_clean(path_a2, const.MP3_320) is True
    shutil.rmtree(path_a2)
