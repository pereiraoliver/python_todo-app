import FreeSimpleGUI as sg
from zip_extractor import extract_archive

label1 = sg.Text("Select ZIP file:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse(
    "Choose", key="zip_file", file_types=(("ZIP Files", "*.zip"),)
)

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="cyan")


window = sg.Window(
    "ZIP Extractor",
    layout=[
        [label1, input1, choose_button1],
        [label2, input2, choose_button2],
        [extract_button, output_label],
    ],
)

while True:
    event, values = window.read()

    match event:
        case sg.WIN_CLOSED:
            break

        case "Extract":
            zip_file = values["zip_file"]
            folder = values["folder"]

            if not zip_file:
                window["output"].update(value="Please select a ZIP file.")
                continue

            if not folder:
                window["output"].update(value="Please select a destination folder.")
                continue

            extract_archive(zip_file, folder)

            window["output"].update(value="Extraction completed!")


window.close()
