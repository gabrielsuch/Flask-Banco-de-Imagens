from flask import Flask, jsonify, request, send_file, safe_join
import os
import zipfile
from app.kenzie.image import get_all_files


app = Flask(__name__)

MAX_CONTENT_LENGTH = os.getenv("MAX_CONTENT_LENGTH")

app.config["MAX_CONTENT_LENGTH"] = 1 * 1000 * 1000

file_directory = os.getenv("FILES_DIRECTORY")
extensions = os.getenv("ALLOWED_EXTENSIONS")
directory = os.listdir(file_directory)


@app.get("/files")
def list_files():
    all_files = []

    get_all_files(all_files)
    
    return jsonify(all_files), 200


@app.get("/files/<extension>")
def list_files_by_extension(extension):
    all_files = []

    for file in directory:
        if(extension == file):
            all_files.append(os.listdir(f"image/{file}"))

            return jsonify(all_files), 200
    
    return {
        "message": "This extension does not exist."
    }, 404


@app.post("/upload")
def upload():
    arquivo = request.files["file"]
    filename = arquivo.filename
    splitfile = arquivo.filename.split(".")

    if(extensions.find(splitfile[1]) == -1):
        return {
            "message": "This extension is not supported. Only GIF, JPG and PNG are accepted!"
        }, 415

    found = False

    for dir in directory:
        if(dir == splitfile[1]):
            path = os.listdir(f"image/{dir}")
            
            for i in path:
                if(i == filename):
                    found = True

            if(found):
                return {
                    "message": "This filename already exists, change the name before upload!"
                }, 409
            else:
                arquivo.save(f"./image/{dir}/{filename}")

    return {
        "message": "Arquivo criado com sucesso!"
    }, 201


@app.get("/download/<file_name>")
def download(file_name):
    for dir in directory:
        path = os.listdir(f"image/{dir}")
        abspath = os.path.abspath(file_directory)

        for files in path:
            if(files == file_name):
                filepath = safe_join(f"{abspath}/{dir}/{file_name}")
                return send_file(filepath, as_attachment=True), 200

    return {
        "error": "This filename does not exists!"
    }, 404


@app.get("/download-zip")
def download_dir_as_zip():
    data = request.args

    try:
        file_extension = data["file_extension"]
        filepath = os.listdir(f"image/{file_extension}")
        zip = zipfile.ZipFile("images.zip", "w", zipfile.ZIP_DEFLATED)

        os.system("mv images.zip /tmp")

        for i in filepath:
            zip.write(f"image/{file_extension}/{i}")

        return {
            "msg": "ZIP file downloaded!"
        }, 200

    except:
        return {
            "msg": "You have to use the Params! (file_extension=jpg)"
        }, 404