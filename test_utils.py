#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils
import os
import shutil
import const


def test_get_direct_subdirs():
    path_a1 = const.TEST_PATH + "/folder1 for counting"
    if not os.path.exists(path_a1):
        os.makedirs(path_a1)
    path_a14 = path_a1 + "/folder1.1"
    path_a15 = path_a1 + "/folder1.2"
    path_a16 = path_a1 + "/subfolder1.1 [V2]"
    path_a17 = path_a1 + "/subfolder1.2 [320]"
    path_a171 = path_a17 + "/doc1.2.1"
    path_a172 = path_a17 + "/doc1.2.2"
    path_a18 = path_a1 + "/subfolder1.3 [320]"
    path_a181 = path_a18 + "/doc1.3.1"
    path_a182 = path_a18 + "/doc1.3.2"

    list_of_paths = [path_a14, path_a15, path_a16, path_a17, path_a18]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)
    if not os.path.exists(path_a171):
        open(path_a171, 'a').close()
    if not os.path.exists(path_a172):
        open(path_a172, 'a').close()
    if not os.path.exists(path_a181):
        open(path_a181, 'a').close()
    if not os.path.exists(path_a182):
        open(path_a182, 'a').close()

    assert type(utils.get_direct_subdirs(path_a1)) == list
    assert set(utils.get_direct_subdirs(path_a1)) == set(list_of_paths)
    assert set(utils.get_direct_subdirs(path_a1, const.MP3_FORMATS)) == set([path_a14, path_a15])
    shutil.rmtree(path_a1)


def test_get_direct_elements():
    path_a1 = const.TEST_PATH + "/folder1 for counting"
    if not os.path.exists(path_a1):
        os.makedirs(path_a1)
    path_a14 = path_a1 + "/folder1.1"
    path_a15 = path_a1 + "/folder1.2"
    path_a16 = path_a1 + "/subfolder1.1 [V2]"
    path_a17 = path_a1 + "/subfolder1.2 [320]"
    path_a171 = path_a17 + "/doc1.2.1"
    path_a172 = path_a17 + "/doc1.2.2"
    path_a18 = path_a1 + "/subfolder1.3 [320]"
    path_a181 = path_a18 + "/doc1.3.1"
    path_a182 = path_a18 + "/doc1.3.2"

    list_of_paths = [path_a14, path_a15, path_a16, path_a17, path_a18]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)
    if not os.path.exists(path_a171):
        open(path_a171, 'a').close()
    if not os.path.exists(path_a172):
        open(path_a172, 'a').close()
    if not os.path.exists(path_a181):
        open(path_a181, 'a').close()
    if not os.path.exists(path_a182):
        open(path_a182, 'a').close()

    assert type(utils.get_direct_elements(path_a1)) == list
    assert set(utils.get_direct_elements(path_a1)) == set(list_of_paths)
    shutil.rmtree(path_a1)


def test_get_list_of_mergeables():
    path_a = const.TEST_PATH + "/folder4 for merging"
    path_a4 = path_a + "/testmergeables"
    path_a41 = path_a4 + "/dontmerge [320]"
    path_a42 = path_a4 + "/dontmerge [V0]"
    path_a43 = path_a4 + "/luke [320]"
    path_a44 = path_a4 + "/leia [320]"
    path_a45 = path_a4 + "/han [V0]"

    list_of_paths = [path_a, path_a4, path_a41, path_a42, path_a43, path_a44, path_a45]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)

    list_of_320 = [path_a43, path_a44]
    list_of_v0 = [path_a45]

    dont_merge_me = "dontmerge"
    assert type(utils.get_list_of_mergeables(path_a4, const.MP3_320, dont_merge_me)) == list
    assert set(utils.get_list_of_mergeables(path_a4, const.MP3_320, dont_merge_me)) == set(list_of_320)
    assert set(utils.get_list_of_mergeables(path_a4, const.MP3_V0, dont_merge_me)) == set(list_of_v0)
    assert not set(utils.get_list_of_mergeables(path_a4, const.MP3_V2, dont_merge_me))
    shutil.rmtree(path_a)


def test_folder_is_clean_320():
    path_a1 = const.TEST_PATH + "/swdoublons"
    path_a11 = path_a1 + "/luke [320]"
    path_a12 = path_a1 + "/leia [320]"
    path_a2 = const.TEST_PATH + "/swnodoublons"
    path_a21 = path_a2 + "/luke [320]"
    path_a22 = path_a2 + "/leia [V0]"
    path_a23 = path_a2 + "/han [V2]"

    list_of_paths = [path_a1, path_a11, path_a12, path_a2, path_a21, path_a22, path_a23]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)

    assert utils.folder_is_clean(path_a1, const.MP3_320) is False
    assert utils.folder_is_clean(path_a2, const.MP3_320) is True
    shutil.rmtree(path_a1)
    shutil.rmtree(path_a2)


def test_folder_is_clean_v0():
    path_a1 = const.TEST_PATH + "/swdoublons"
    path_a11 = path_a1 + "/luke [V0]"
    path_a12 = path_a1 + "/leia [V0]"
    path_a2 = const.TEST_PATH + "/swnodoublons"
    path_a21 = path_a2 + "/luke [320]"
    path_a22 = path_a2 + "/leia [V0]"
    path_a23 = path_a2 + "/han [V2]"

    list_of_paths = [path_a1, path_a11, path_a12, path_a2, path_a21, path_a22, path_a23]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)

    assert utils.folder_is_clean(path_a1, const.MP3_V0) is False
    assert utils.folder_is_clean(path_a2, const.MP3_V0) is True
    shutil.rmtree(path_a1)
    shutil.rmtree(path_a2)


def test_folder_is_clean_v2():
    path_a1 = const.TEST_PATH + "/swdoublons"
    path_a11 = path_a1 + "/luke [V2]"
    path_a12 = path_a1 + "/leia [V2]"
    path_a2 = const.TEST_PATH + "/swnodoublons"
    path_a21 = path_a2 + "/luke [320]"
    path_a22 = path_a2 + "/leia [V0]"
    path_a23 = path_a2 + "/han [V2]"

    list_of_paths = [path_a1, path_a11, path_a12, path_a2, path_a21, path_a22, path_a23]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)

    assert utils.folder_is_clean(path_a1, const.MP3_V2) is False
    assert utils.folder_is_clean(path_a2, const.MP3_V2) is True
    shutil.rmtree(path_a1)
    shutil.rmtree(path_a2)


def test_level_has_image():
    path_a6 = const.TEST_PATH + "/folder6 for copying"
    path_a60 = path_a6 + "/images"
    path_a6b3 = path_a60 + "/art.png"
    path_a6b4 = path_a60 + "/cover.jpg"
    path_a6b5 = path_a60 + "/front.jpg"

    list_of_paths = [path_a60, path_a6]
    list_of_files = [path_a6b3, path_a6b4, path_a6b5]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)
    for x in list_of_files:
        if not os.path.exists(x):
            open(x, 'a').close()
    assert utils.level_has_image(path_a6) is False
    assert utils.level_has_image(path_a60) is True
    shutil.rmtree(path_a6)


def test_copy_from_list():
    path_a = const.TEST_PATH + "/folder6 for copying"
    path_a1 = path_a + "/luke"
    path_a11 = path_a1 + "/lightsaber.mp3"
    path_a12 = path_a1 + "/snowspeeder.mp3"
    path_a2 = path_a + "/leia"
    path_a21 = path_a2 + "/hairdo.mp3"
    path_a22 = path_a2 + "/cheek.mp3"
    output_dir_path = path_a + "/han"

    input_list = [path_a1, path_a2]
    list_of_paths = [path_a1, path_a2, output_dir_path]
    list_of_files = [path_a11, path_a12, path_a21, path_a22]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)
    for x in list_of_files:
        if not os.path.exists(x):
            open(x, 'a').close()

    total_length = 0

    for x in input_list:
        total_length += len(utils.get_direct_elements(x))
    utils.copy_from_list(input_list, output_dir_path)
    assert len(utils.get_direct_elements(output_dir_path)) == total_length
    shutil.rmtree(path_a)


def test_copy_images_to_list():
    path_a6 = const.TEST_PATH + "/folder6 for copying"
    path_a60 = path_a6 + "/images"
    path_a6b1 = path_a60 + "/bla [320]"
    path_a6b2 = path_a60 + "/blo [320]"
    path_a6b3 = path_a60 + "/art.png"
    path_a6b4 = path_a60 + "/cover.jpg"
    path_a6b5 = path_a60 + "/front.jpg"

    list_of_paths = [path_a60, path_a6, path_a6b1, path_a6b2]
    list_of_files = [path_a6b3, path_a6b4, path_a6b5]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)
    for x in list_of_files:
        if not os.path.exists(x):
            open(x, 'a').close()

    list_of_dst = [path_a6b1, path_a6b2]
    utils.copy_images_to_list(path_a60, list_of_dst)
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
    path_a6 = const.TEST_PATH + "/folder6 for copying"
    src_folder = path_a6 + "/swimages"
    img1 = src_folder + "/luke.png"
    img2 = src_folder + "/leia.jpg"
    dst_folder = path_a6 + "/beholdtheimages"

    list_of_dirs = [src_folder, dst_folder]
    for x in list_of_dirs:
        if not os.path.exists(x):
            os.makedirs(x)

    list_of_files = [img1, img2]
    for x in list_of_files:
        if not os.path.exists(x):
            open(x, 'a').close()

    utils.copy_images(src_folder, dst_folder)
    new_path_img1 = dst_folder + "/luke.png"
    new_path_img2 = dst_folder + "/leia.jpg"

    assert os.path.exists(new_path_img1)
    assert os.path.exists(new_path_img2)
    shutil.rmtree(path_a6)


def test_get_flac_list():
    path_a = const.TEST_PATH + "/folder1 for counting"
    path_a1 = path_a + "/swflac"
    path_a11 = path_a1 + "/luke.flac"
    path_a12 = path_a1 + "/leia.flac"
    path_a13 = path_a1 + "/han.cue"
    path_a14 = path_a1 + "/obiwan.log"
    path_a15 = path_a1 + "/akhbar.png"
    path_a16 = path_a1 + "/chewie.m3u"
    path_a17 = path_a1 + "/alliance"

    list_of_files = [path_a11, path_a12, path_a13, path_a14, path_a15, path_a16]
    list_of_dirs = [path_a, path_a1, path_a17]

    for x in list_of_dirs:
        if not os.path.exists(x):
            os.makedirs(x)

    for x in list_of_files:
        if not os.path.exists(x):
            open(x, 'a').close()

    list_of_flacs = utils.get_flacs(path_a1)
    assert set(list_of_flacs) == set([path_a12, path_a11])
    shutil.rmtree(path_a)


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
    path_a6 = const.TEST_PATH + "/folder6 for merging"
    path_a2 = path_a6 + "/album2"
    path_a2d1b1 = path_a2 + "/bla [320]"
    path_a2d1b2 = path_a2 + "/blo [320]"
    path_a2d1b3 = path_a2 + "/bla [V0]"
    path_a2d1b4 = path_a2 + "/blo [V0]"
    path_a2d1b5 = path_a2 + "/bla [V2]"
    path_a2d1b6 = path_a2 + "/blo [V2]"

    list_of_paths = [path_a6, path_a2, path_a2d1b1, path_a2d1b2, path_a2d1b3, path_a2d1b4, path_a2d1b5, path_a2d1b6]
    for x in list_of_paths:
        if not os.path.exists(x):
            os.makedirs(x)

    merged_folder1 = path_a2 + "/" + const.MERGED_FOLDER_NAME + " " + const.MP3_320
    merged_folder2 = path_a2 + "/" + const.MERGED_FOLDER_NAME + " " + const.MP3_V0
    merged_folder3 = path_a2 + "/" + const.MERGED_FOLDER_NAME + " " + const.MP3_V2
    utils.merge_album(path_a2, const.MP3_320)
    utils.merge_album(path_a2, const.MP3_V0)
    utils.merge_album(path_a2, const.MP3_V2)
    assert os.path.exists(merged_folder1)
    assert os.path.exists(merged_folder2)
    assert os.path.exists(merged_folder3)
    shutil.rmtree(path_a6)


def test_copy_merged_single_level():
    upload_folder = const.TEST_PATH + "/folder5 for uploading"
    flac_folder = const.TEST_PATH + "/folder4 for merging"
    path_a1 = flac_folder + "/album1"

    for x in const.MP3_FORMATS:
        list_of_paths = []
        new_path1 = path_a1 + "/bla " + x
        new_path2 = path_a1 + "/blo " + x
        new_path3 = path_a1 + "/" + const.MERGED_FOLDER_NAME + x
        if x is const.MP3_320:
            new_path31 = new_path3 + "/leia320.mp3"
        if x is const.MP3_V0:
            new_path31 = new_path3 + "/leiaV0.mp3"
        list_of_paths.append(new_path1)
        list_of_paths.append(new_path2)
        list_of_paths.append(new_path3)

        for y in list_of_paths:
            if not os.path.exists(y):
                os.makedirs(y)
        if x is const.MP3_320 or x is const.MP3_V0:
            if not os.path.exists(new_path31):
                open(new_path31, 'a').close()
            if not os.path.exists(new_path31):
                open(new_path31, 'a').close()

        utils.copy_merged_single_level(path_a1, x, upload_folder)
    new_merged_file1 = upload_folder + "/album1 [320]/leia320.mp3"
    new_merged_file2 = upload_folder + "/album1 [V0]/leia320.mp3"
    assert os.path.exists(new_merged_file1)
    assert os.path.exists(new_merged_file2)

    shutil.rmtree(upload_folder)
    shutil.rmtree(flac_folder)


def test_copy_merged_double_level():
    # Create all paths
    upload_folder = const.TEST_PATH + "/folder5 for uploading"
    flac_folder = const.TEST_PATH + "/folder4 for merging"
    path_a1 = flac_folder + "/album1"

    list_of_paths = []
    new_path1 = path_a1 + "/disc1"
    list_of_paths.append(new_path1)
    new_path2 = path_a1 + "/disc2"
    list_of_paths.append(new_path2)
    for x in const.MP3_FORMATS:
        new_path11 = new_path1 + "/bla " + x
        new_path12 = new_path1 + "/blo " + x
        if x is const.MP3_320:
            new_path13 = new_path1 + "/" + const.MERGED_FOLDER_NAME + " " + x
            new_path131 = new_path13 + "/leia320.mp3"
            list_of_paths.append(new_path13)
        if x is const.MP3_V0:
            new_path13 = new_path1 + "/" + const.MERGED_FOLDER_NAME + " " + x
            new_path131 = new_path13 + "/leiaV0.mp3"
            list_of_paths.append(new_path13)
        new_path21 = new_path2 + "/bla " + x
        new_path22 = new_path2 + "/blo " + x
        if x is const.MP3_320:
            new_path23 = new_path2 + "/" + const.MERGED_FOLDER_NAME + " " + x
            new_path231 = new_path23 + "/luke320.mp3"
            list_of_paths.append(new_path23)
        if x is const.MP3_V0:
            new_path23 = new_path2 + "/" + const.MERGED_FOLDER_NAME + " " + x
            new_path231 = new_path23 + "/lukeV0.mp3"
            list_of_paths.append(new_path23)
        list_of_paths.append(new_path11)
        list_of_paths.append(new_path12)
        list_of_paths.append(new_path21)
        list_of_paths.append(new_path22)

        for y in list_of_paths:
            if not os.path.exists(y):
                os.makedirs(y)
        if x is const.MP3_320 or x is const.MP3_V0:
            if not os.path.exists(new_path131):
                open(new_path131, 'a').close()
            if not os.path.exists(new_path231):
                open(new_path231, 'a').close()

        utils.copy_merged_double_level(path_a1, x, upload_folder)
    new_merged_file1 = upload_folder + "/album1 [320]/disc1/leia320.mp3"
    new_merged_file2 = upload_folder + "/album1 [320]/disc2/luke320.mp3"
    new_merged_file3 = upload_folder + "/album1 [V0]/disc1/leiaV0.mp3"
    new_merged_file4 = upload_folder + "/album1 [V0]/disc2/lukeV0.mp3"
    assert os.path.exists(new_merged_file1)
    assert os.path.exists(new_merged_file2)
    assert os.path.exists(new_merged_file3)
    assert os.path.exists(new_merged_file4)

    # shutil.rmtree(upload_folder)
    # shutil.rmtree(flac_folder)


def test_copy_clean_single_level():
    upload_folder = const.TEST_PATH + "/folder5 for uploading"
    flac_folder = const.TEST_PATH + "/folder4 for merging"
    path_a1 = flac_folder + "/album1"

    for x in const.MP3_FORMATS:
        list_of_paths = []
        new_path = path_a1 + "/bla " + x
        list_of_paths.append(new_path)

        for y in list_of_paths:
            if not os.path.exists(y):
                os.makedirs(y)

        utils.copy_clean_single_level(path_a1, x, upload_folder)
        uploaded_dir = upload_folder + "/bla " + x
        assert os.path.exists(uploaded_dir)

    shutil.rmtree(upload_folder)
    shutil.rmtree(flac_folder)


def test_copy_clean_double_level():
    upload_folder = const.TEST_PATH + "/folder5 for uploading"
    flac_folder = const.TEST_PATH + "/folder4 for merging"
    path_a1 = flac_folder + "/album1"

    list_of_paths = []
    new_disc_path1 = path_a1 + "/disc1"
    list_of_paths.append(new_disc_path1)
    new_disc_path2 = path_a1 + "/disc2"
    list_of_paths.append(new_disc_path2)
    for x in const.MP3_FORMATS:
        new_path1 = new_disc_path1 + "/bla " + x
        list_of_paths.append(new_path1)
        new_path2 = new_disc_path2 + "/bla " + x
        list_of_paths.append(new_path2)

        for y in list_of_paths:
            if not os.path.exists(y):
                os.makedirs(y)

        utils.copy_clean_double_level(path_a1, x, upload_folder)
        uploaded_dir1 = upload_folder + "/album1 " + x + "/disc1" + "/bla " + x
        uploaded_dir2 = upload_folder + "/album1 " + x + "/disc2" + "/bla " + x

        assert os.path.exists(uploaded_dir1)
        assert os.path.exists(uploaded_dir2)
    shutil.rmtree(upload_folder)
    shutil.rmtree(flac_folder)


def test_get_merged_folder_path():
    path_a = const.TEST_PATH + "/folder4 for merging"
    path_a1 = path_a + "/album1"

    for x in const.MP3_FORMATS:
        merged_pattern = const.MERGED_FOLDER_NAME + " " + x
        list_of_paths = []
        path_a1b1 = path_a1 + "/bla " + x
        list_of_paths.append(path_a1b1)
        path_a1b2 = path_a1 + "/blo " + x
        list_of_paths.append(path_a1b2)
        path_a1m = path_a1 + "/" + merged_pattern
        list_of_paths.append(path_a1m)

        for y in list_of_paths:
            if not os.path.exists(y):
                os.makedirs(y)

        assert utils.get_merged_folder_path(path_a1, merged_pattern) == path_a1m

    shutil.rmtree(path_a)


def test_album_is_clean_single_true():
    path_a = const.TEST_PATH + "/folder4 for merging"
    path_a2 = path_a + "/album2"

    for x in const.MP3_FORMATS:
        new_path = path_a2 + "/bla " + x
        if not os.path.exists(new_path):
            os.makedirs(new_path)

    assert utils.album_is_clean(path_a2, const.MP3_FORMATS) is True
    shutil.rmtree(path_a)


def test_album_is_clean_single_false_320():
    path_a = const.TEST_PATH + "/folder4 for merging"
    path_a2 = path_a + "/album2"

    for x in const.MP3_FORMATS:
        if x is const.MP3_320:
            dir1 = path_a2 + "/bla " + x
            if not os.path.exists(dir1):
                os.makedirs(dir1)
            dir2 = path_a2 + "/blo " + x
            if not os.path.exists(dir2):
                os.makedirs(dir2)
        else:
            dir1 = path_a2 + "/bla " + x
            if not os.path.exists(x):
                os.makedirs(dir1)

    assert utils.album_is_clean(path_a2, const.MP3_FORMATS) is False
    shutil.rmtree(path_a)


def test_album_is_clean_single_false_v0():
    path_a = const.TEST_PATH + "/folder4 for merging"
    path_a2 = path_a + "/album2"

    for x in const.MP3_FORMATS:
        if x is const.MP3_V0:
            dir1 = path_a2 + "/bla " + x
            if not os.path.exists(dir1):
                os.makedirs(dir1)
            dir2 = path_a2 + "/blo " + x
            if not os.path.exists(dir2):
                os.makedirs(dir2)
        else:
            dir1 = path_a2 + "/bla " + x
            if not os.path.exists(x):
                os.makedirs(dir1)

    assert utils.album_is_clean(path_a2, const.MP3_FORMATS) is False
    shutil.rmtree(path_a)


def test_album_is_clean_single_false_v2():
    path_a = const.TEST_PATH + "/folder4 for merging"
    path_a2 = path_a + "/album2"

    for x in const.MP3_FORMATS:
        if x is const.MP3_V2:
            dir1 = path_a2 + "/bla " + x
            if not os.path.exists(dir1):
                os.makedirs(dir1)
            dir2 = path_a2 + "/blo " + x
            if not os.path.exists(dir2):
                os.makedirs(dir2)
        else:
            dir1 = path_a2 + "/bla " + x
            if not os.path.exists(x):
                os.makedirs(dir1)

    assert utils.album_is_clean(path_a2, const.MP3_FORMATS) is False
    shutil.rmtree(path_a)


def test_album_is_clean_double_false_d1_320():
    path_a = const.TEST_PATH + "/folder4"
    path_a2 = path_a + "/album2"
    path_a2d1 = path_a2 + "/disc1"
    path_a2d2 = path_a2 + "/disc2"

    list_of_dirs = []
    for x in const.MP3_FORMATS:
        if x is const.MP3_320:
            dir1 = path_a2d1 + "/bla " + x
            list_of_dirs.append(dir1)
            dir2 = path_a2d1 + "/blo " + x
            list_of_dirs.append(dir2)
            dir3 = path_a2d2 + "/bla " + x
            list_of_dirs.append(dir3)
        else:
            dir1 = path_a2d1 + "/bla " + x
            list_of_dirs.append(dir1)
            dir2 = path_a2d2 + "/bla " + x
            list_of_dirs.append(dir2)

    for y in list_of_dirs:
        if not os.path.exists(y):
            os.makedirs(y)

    assert utils.album_is_clean(path_a2, const.MP3_FORMATS) is False
    shutil.rmtree(path_a)


def test_album_is_clean_double_false_d1_v0():
    path_a = const.TEST_PATH + "/folder4"
    path_a2 = path_a + "/album2"
    path_a2d1 = path_a2 + "/disc1"
    path_a2d2 = path_a2 + "/disc2"

    list_of_dirs = []
    for x in const.MP3_FORMATS:
        if x is const.MP3_V0:
            dir1 = path_a2d1 + "/bla " + x
            list_of_dirs.append(dir1)
            dir2 = path_a2d1 + "/blo " + x
            list_of_dirs.append(dir2)
            dir3 = path_a2d2 + "/bla " + x
            list_of_dirs.append(dir3)
        else:
            dir1 = path_a2d1 + "/bla " + x
            list_of_dirs.append(dir1)
            dir2 = path_a2d2 + "/bla " + x
            list_of_dirs.append(dir2)

    for y in list_of_dirs:
        if not os.path.exists(y):
            os.makedirs(y)

    assert utils.album_is_clean(path_a2, const.MP3_FORMATS) is False
    shutil.rmtree(path_a)


def test_album_is_clean_double_false_d1_v2():
    path_a = const.TEST_PATH + "/folder4"
    path_a2 = path_a + "/album2"
    path_a2d1 = path_a2 + "/disc1"
    path_a2d2 = path_a2 + "/disc2"

    list_of_dirs = []
    for x in const.MP3_FORMATS:
        if x is const.MP3_V2:
            dir1 = path_a2d1 + "/bla " + x
            list_of_dirs.append(dir1)
            dir2 = path_a2d1 + "/blo " + x
            list_of_dirs.append(dir2)
            dir3 = path_a2d2 + "/bla " + x
            list_of_dirs.append(dir3)
        else:
            dir1 = path_a2d1 + "/bla " + x
            list_of_dirs.append(dir1)
            dir2 = path_a2d2 + "/bla " + x
            list_of_dirs.append(dir2)

    for y in list_of_dirs:
        if not os.path.exists(y):
            os.makedirs(y)

    assert utils.album_is_clean(path_a2, const.MP3_FORMATS) is False
    shutil.rmtree(path_a)


def test_album_is_clean_double_false_d2_320():
    path_a = const.TEST_PATH + "/folder4"
    path_a2 = path_a + "/album2"
    path_a2d1 = path_a2 + "/disc1"
    path_a2d2 = path_a2 + "/disc2"

    list_of_dirs = []
    for x in const.MP3_FORMATS:
        if x is const.MP3_320:
            dir1 = path_a2d1 + "/bla " + x
            list_of_dirs.append(dir1)
            dir2 = path_a2d2 + "/bla " + x
            list_of_dirs.append(dir2)
            dir3 = path_a2d2 + "/blo " + x
            list_of_dirs.append(dir3)
        else:
            dir1 = path_a2d1 + "/bla " + x
            list_of_dirs.append(dir1)
            dir2 = path_a2d2 + "/bla " + x
            list_of_dirs.append(dir2)

    for y in list_of_dirs:
        if not os.path.exists(y):
            os.makedirs(y)

    assert utils.album_is_clean(path_a2, const.MP3_FORMATS) is False
    shutil.rmtree(path_a)


def test_album_is_clean_double_false_d2_v0():
    path_a = const.TEST_PATH + "/folder4"
    path_a2 = path_a + "/album2"
    path_a2d1 = path_a2 + "/disc1"
    path_a2d2 = path_a2 + "/disc2"

    list_of_dirs = []
    for x in const.MP3_FORMATS:
        if x is const.MP3_V0:
            dir1 = path_a2d1 + "/bla " + x
            list_of_dirs.append(dir1)
            dir2 = path_a2d2 + "/bla " + x
            list_of_dirs.append(dir2)
            dir3 = path_a2d2 + "/blo " + x
            list_of_dirs.append(dir3)
        else:
            dir1 = path_a2d1 + "/bla " + x
            list_of_dirs.append(dir1)
            dir2 = path_a2d2 + "/bla " + x
            list_of_dirs.append(dir2)

    for y in list_of_dirs:
        if not os.path.exists(y):
            os.makedirs(y)

    assert utils.album_is_clean(path_a2, const.MP3_FORMATS) is False
    shutil.rmtree(path_a)


def test_album_is_clean_double_false_d2_v2():
    path_a = const.TEST_PATH + "/folder4"
    path_a2 = path_a + "/album2"
    path_a2d1 = path_a2 + "/disc1"
    path_a2d2 = path_a2 + "/disc2"

    list_of_dirs = []
    for x in const.MP3_FORMATS:
        if x is const.MP3_V2:
            dir1 = path_a2d1 + "/bla " + x
            list_of_dirs.append(dir1)
            dir2 = path_a2d2 + "/bla " + x
            list_of_dirs.append(dir2)
            dir3 = path_a2d2 + "/blo " + x
            list_of_dirs.append(dir3)
        else:
            dir1 = path_a2d1 + "/bla " + x
            list_of_dirs.append(dir1)
            dir2 = path_a2d2 + "/bla " + x
            list_of_dirs.append(dir2)

    for y in list_of_dirs:
        if not os.path.exists(y):
            os.makedirs(y)

    assert utils.album_is_clean(path_a2, const.MP3_FORMATS) is False
    shutil.rmtree(path_a)


def test_album_is_clean_double_true():
    path_a = const.TEST_PATH + "/folder4"
    path_a2 = path_a + "/album2"
    path_a2d1 = path_a2 + "/disc1"
    path_a2d2 = path_a2 + "/disc2"

    list_of_dirs = []
    for x in const.MP3_FORMATS:
        dir1 = path_a2d1 + "/bla " + x
        list_of_dirs.append(dir1)
        dir2 = path_a2d2 + "/bla " + x
        list_of_dirs.append(dir2)

    for y in list_of_dirs:
        if not os.path.exists(y):
            os.makedirs(y)

    assert utils.album_is_clean(path_a2, const.MP3_FORMATS) is True
    shutil.rmtree(path_a)


def test_folder_has_formats_320():
    path_a = const.TEST_PATH + "/folder4"
    path_a2 = path_a + "/album2"
    path_a2d1 = path_a2 + "/bla [320]"

    if not os.path.exists(path_a2d1):
        os.makedirs(path_a2d1)

    assert utils.folder_has_formats(path_a2) == [const.MP3_320]
    shutil.rmtree(path_a)


def test_folder_has_formats_320_v0():
    path_a = const.TEST_PATH + "/folder4"
    path_a2 = path_a + "/album2"
    path_a2d1 = path_a2 + "/bla [320]"
    path_a2d2 = path_a2 + "/bla [V0]"

    if not os.path.exists(path_a2d1):
        os.makedirs(path_a2d1)
    if not os.path.exists(path_a2d2):
        os.makedirs(path_a2d2)

    assert utils.folder_has_formats(path_a2) == [const.MP3_320, const.MP3_V0]
    shutil.rmtree(path_a)


def test_folder_has_formats_320_v0_v2():
    path_a = const.TEST_PATH + "/folder4"
    path_a2 = path_a + "/album2"
    path_a2d1 = path_a2 + "/bla [320]"
    path_a2d2 = path_a2 + "/bla [V0]"
    path_a2d3 = path_a2 + "/bla [V2]"

    if not os.path.exists(path_a2d1):
        os.makedirs(path_a2d1)
    if not os.path.exists(path_a2d2):
        os.makedirs(path_a2d2)
    if not os.path.exists(path_a2d3):
        os.makedirs(path_a2d3)

    assert utils.folder_has_formats(path_a2) == const.MP3_FORMATS
    shutil.rmtree(path_a)


def test_album_has_formats_double_320():
    path_a = const.TEST_PATH + "/folder4"
    path_a2 = path_a + "/album1"
    path_a2d1 = path_a2 + "/disc1"
    path_a2d2 = path_a2 + "/disc2"

    list_of_dirs = []
    dir1 = path_a2d1 + "/bla " + const.MP3_320
    list_of_dirs.append(dir1)
    dir2 = path_a2d2 + "/bla " + const.MP3_320
    list_of_dirs.append(dir2)

    for y in list_of_dirs:
        if not os.path.exists(y):
            os.makedirs(y)

    assert utils.album_has_formats(path_a2) == [const.MP3_320]
    shutil.rmtree(path_a)


def test_album_has_formats_double_320_v2():
    path_a = const.TEST_PATH + "/folder4"
    path_a2 = path_a + "/album1"
    path_a2d1 = path_a2 + "/disc1"
    path_a2d2 = path_a2 + "/disc2"

    list_of_dirs = []
    dir1 = path_a2d1 + "/bla " + const.MP3_320
    list_of_dirs.append(dir1)
    dir2 = path_a2d1 + "/bla " + const.MP3_V2
    list_of_dirs.append(dir2)
    dir3 = path_a2d2 + "/bla " + const.MP3_320
    list_of_dirs.append(dir3)
    dir4 = path_a2d2 + "/bla " + const.MP3_V2
    list_of_dirs.append(dir4)

    for y in list_of_dirs:
        if not os.path.exists(y):
            os.makedirs(y)

    assert utils.album_has_formats(path_a2) == [const.MP3_320, const.MP3_V2]
    shutil.rmtree(path_a)


def test_album_has_formats_double_320_v0_v2():
    path_a = const.TEST_PATH + "/folder4"
    path_a2 = path_a + "/album2"
    path_a2d1 = path_a2 + "/disc1"
    path_a2d2 = path_a2 + "/disc2"

    list_of_dirs = []
    for x in const.MP3_FORMATS:
        dir1 = path_a2d1 + "/bla " + x
        list_of_dirs.append(dir1)
        dir2 = path_a2d2 + "/bla " + x
        list_of_dirs.append(dir2)

    for y in list_of_dirs:
        if not os.path.exists(y):
            os.makedirs(y)

    assert utils.album_has_formats(path_a2) == const.MP3_FORMATS
    shutil.rmtree(path_a)
