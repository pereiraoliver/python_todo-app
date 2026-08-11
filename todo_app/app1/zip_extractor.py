import pathlib
import zipfile


def extract_archive(zip_filepath, dest_dir):
    zip_path = pathlib.Path(zip_filepath)
    dest_path = pathlib.Path(dest_dir)

    dest_path.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as archive:
        archive.extractall(dest_path)


if __name__ == "__main__":
    print("Dependent function")
