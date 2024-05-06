from PIL import Image
from surya.ocr import run_ocr
from surya.model.detection import segformer
from surya.model.recognition.model import load_model
from surya.model.recognition.processor import load_processor
import os
from typing import Literal


def ocr(image_path: str):
    if os.path.exists(image_path):
        image = Image.open(image_path)
        langs = ["en", "zh"]  # Replace with your languages
        det_processor, det_model = segformer.load_processor(), segformer.load_model()
        rec_model, rec_processor = load_model(), load_processor()

        predictions = run_ocr([image], [langs], det_model, det_processor, rec_model, rec_processor)

        return predictions

    return None


def queuing_ocr_for_zip(zip_path: str):
    # todo
    return None


def queuing_ocr_for_folder(folder_path: str):
    # todo
    return None


def queuing_ocr(file_path: str, file_type: Literal['zip', 'folder', None]):
    if os.path.exists(file_path):
        if file_type == 'zip':
            return queuing_ocr_for_zip(zip_path=file_path)
        elif file_type == 'folder':
            return queuing_ocr_for_folder(folder_path=file_path)
    else:
        return None
