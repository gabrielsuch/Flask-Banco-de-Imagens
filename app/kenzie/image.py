from flask import request, safe_join, send_file
import os


FILES_DIRECTORY = os.getenv("FILES_DIRECTORY")
EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS")
DIRECTORY = os.listdir(FILES_DIRECTORY)


def function_list_files(all_files, file):
    all_files.append(os.listdir(f"{FILES_DIRECTORY}/{file}"))

    return all_files


def function_list_files_by_extension(all_files, file):
    all_files.append(os.listdir(f"{FILES_DIRECTORY}/{file}"))

    return all_files


def function_upload():
    arquivo = request.files["file"]
    filename = arquivo.filename
    splitfile = arquivo.filename.split(".")

    if(EXTENSIONS.find(splitfile[1]) == -1):
        return {
            "message": "This extension is not supported. Only GIF, JPG and PNG are accepted!"
        }, 415

    found = False

    for dir in DIRECTORY:
        if(dir == splitfile[1]):
            path = os.listdir(f"{FILES_DIRECTORY}/{dir}")
            
            for i in path:
                if(i == filename):
                    found = True

            if(found):
                return {
                    "message": "This filename already exists, change the name before upload!"
                }, 409
            else:
                arquivo.save(f"./{FILES_DIRECTORY}/{dir}/{filename}")

    return {
        "message": "Arquivo criado com sucesso!"
    }, 201


def function_download(file_name, dir, abspath):
    filepath = safe_join(f"{abspath}/{dir}/{file_name}")
    new_file = send_file(filepath, as_attachment=True), 200
    return new_file


def function_download_dir_as_zip(data):
    file_extension = data["file_extension"]
    compression_ratio = data["compression_ratio"]

    temp_path = "/tmp"
    file = "images.zip"

    if(len(os.listdir(f"{FILES_DIRECTORY}/{file_extension}")) > 0):
        os.system(f"zip -r {temp_path}/{file} {FILES_DIRECTORY}/{file_extension} -{compression_ratio}")

        file_path = safe_join(f"/tmp/{file}")
        file_download = send_file(file_path, as_attachment=True), 200

        return file_download

    return {
        "msg": "This extension doesn't have any files!"
    }, 404