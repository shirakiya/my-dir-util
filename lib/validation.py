# -*- coding: utf-8 -*-
import os
import imghdr

VALID_IMAGE_FORMAT = ['jpeg', 'png']


def validate_dir(dir):
    if os.path.isdir(dir):
        return True
    return False


def validate_image(path):
    if os.path.getsize(path) == 0:
        return False
    if imghdr.what(path) not in VALID_IMAGE_FORMAT:
        return False
    return True
