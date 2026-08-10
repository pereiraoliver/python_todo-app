import pathlib
import zipfile


def make_archive(filetpaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filetpaths:
            path = pathlib.Path(filepath)
            archive.write(filepath, arcname=path.name)


if __name__ == "__main__":
    print("Dependent function")
