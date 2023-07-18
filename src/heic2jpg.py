#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: FIXME: XXX: HACK: NOTE: INTENT: USAGE:

import os
import glob
import pathlib
import argparse
import pillow_heif
from PIL import Image

parser = argparse.ArgumentParser(add_help=True)

parser.add_argument('-s', '--source', type=str, required=True)
parser.add_argument('-d', '--destination', type=str, required=True)
args = parser.parse_args()

def heic_jpg(image_path, save_path):
    heif_file = pillow_heif.read_heif(image_path)
    for img in heif_file: 
        image = Image.frombytes(
            img.mode,
            img.size,
            img.data,
            'raw',
            img.mode,
            img.stride,
        )
    image.save(save_path, "JPEG")

if __name__ == '__main__':
    os.makedirs(args.destination, exist_ok=True)
    
    image_dir = pathlib.Path(args.source)
    heic_path = list(image_dir.glob('**/*.HEIC')) + list(image_dir.glob('**/*.heic'))

    for directory in heic_path:
        image_path = str(directory)
        save_path =  f"{args.destination}/{directory.stem}.jpg"
        print(save_path)
        heic_jpg(image_path, save_path)
