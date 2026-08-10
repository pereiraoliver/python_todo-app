import FreeSimpleGUI as sg


def feet_inches_to_meters(feet, inches):
    return feet * 0.3048 + inches * 0.0254


label1 = sg.Text("Enter feet:")
input_box1 = sg.InputText(key="feet")

label2 = sg.Text("Enter inches:")
input_box2 = sg.InputText(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output", text_color="cyan")


window = sg.Window(
    "Converter",
    layout=[[label1, input_box1], [label2, input_box2], [convert_button, output_label]],
)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Convert":
        feet = float(values["feet"])
        inches = float(values["inches"])

        meters = feet_inches_to_meters(feet, inches)
        window["output"].update(value=f"{meters:.3f} m")

        # sg.popup(f"{feet} ft and {inches} in = {meters:.3f} m")

        # Clear the input boxes after popup is closed
        window["feet"].update("")
        window["inches"].update("")


window.close()
