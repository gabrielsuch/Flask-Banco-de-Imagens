from flask import jsonify
import os

file_directory = os.getenv("FILES_DIRECTORY")
directory = os.listdir(file_directory)

def get_all_files(all_files):
    for file in directory:
        all_files.append(os.listdir(f"image/{file}"))

