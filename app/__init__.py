from flask import Flask, request, jsonify
import os


FILES_DIRECTORY = os.getenv("FILES_DIRECTORY")

os.makedirs(FILES_DIRECTORY, exist_ok=True)

EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS")
DIRECTORY = os.listdir(FILES_DIRECTORY)

new_dirs = EXTENSIONS.split(",")

for dirs in new_dirs:
    dir = dirs.strip()
    os.makedirs(f"{FILES_DIRECTORY}/{dir}", exist_ok=True)


from app.kenzie import function_list_files, function_list_files_by_extension, function_upload, function_download, function_download_dir_as_zip


app = Flask(__name__)

MAX_CONTENT_LENGTH = os.getenv("MAX_CONTENT_LENGTH")

app.config["MAX_CONTENT_LENGTH"] = 1 * 1000 * 1000


@app.get("/files")
def list_files():
    all_files = []

    for file in DIRECTORY:
        new_files = function_list_files(all_files, file)

    return jsonify(new_files), 200


@app.get("/files/<extension>")
def list_files_by_extension(extension):
    all_files = []

    for file in DIRECTORY:
        if(extension == file):
            new_files = function_list_files_by_extension(all_files, file)

            return jsonify(new_files), 200
    
    return {
        "message": "This extension does not exist."
    }, 404


@app.post("/upload")
def upload():
    return function_upload()


@app.get("/download/<file_name>")
def download(file_name):
    for dir in DIRECTORY:
        path = os.listdir(f"image/{dir}")
        abspath = os.path.abspath(FILES_DIRECTORY)

        for files in path:
            if(files == file_name):
                download_file = function_download(file_name, dir, abspath)
                return download_file

    return {
        "error": "This filename does not exists!"
    }, 404


@app.get("/download-zip")
def download_dir_as_zip():
    data = request.args

    try:
        download_file = function_download_dir_as_zip(data)

        return download_file

    except:
        return {
            "msg": "You have to use the Params! (file_extension=jpg&compression_ratio=0)"
        }, 404
