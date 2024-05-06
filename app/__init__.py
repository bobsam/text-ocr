import os
from typing import Literal
from app.ocr import queuing_ocr, ocr

image_folder = ''

image_zip = ''


def start_ocr():
    """
    开始OCR操作
    :return: OCR结果
    """
    file_type: Literal['zip', 'folder', None] = None
    file_path = ''

    if bool(image_folder) and len(image_folder) > 0:
        file_type = 'folder'
        file_path = image_folder
    elif bool(image_zip) and len(image_zip) > 0:
        file_type = 'zip'
        file_path = image_zip

    return queuing_ocr(file_path=file_path, file_type=file_type)


def test_ocr_single_file(file_path: str):
    """
    测试单个图片文件的OCR
    :param file_path: 文件地址
    :return: OCR结果
    """
    if bool(file_path) and len(file_path) > 0 and os.path.exists(file_path):
        result = ocr(image_path=file_path)
        return result

    return None
