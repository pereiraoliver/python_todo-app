import os
import time

import FreeSimpleGUI as sg
import functions

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")

clock = sg.Text("", key="-clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="-todo")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(
    values=functions.get_todos(), key="-todos", enable_events=True, size=[45, 10]
)
buttons = sg.Column([[sg.Button("Edit", size=10)], [sg.Button("Complete", size=10)]])
exit_button = sg.Button("Exit", size=10)

layout = [[clock], [label], [input_box, add_button], [list_box, buttons], [exit_button]]

window = sg.Window(
    "My To-Do App",
    layout=layout,
    font=("Helvetica", 16),
)

while True:
    event, values = window.read(timeout=1000)

    if event == sg.WIN_CLOSED:
        break

    window["-clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    try:
        match event:
            case "-todos":
                selected_todo = values["-todos"][0]
                window["-todo"].update(selected_todo)
            case "Add":
                todos = functions.get_todos()
                new_todo = values["-todo"] + "\n"
                if values["-todo"] == "":
                    raise ValueError("Invalid value")
                todos.append(new_todo)
                functions.write_todos(todos)
                window["-todos"].update(values=todos)
                window["-todo"].update("")
            case "Edit":
                todos = functions.get_todos()
                idx = todos.index(",".join(values["-todos"]))
                todos[idx] = values["-todo"]
                functions.write_todos(todos)
                window["-todos"].update(values=todos)
                window["-todo"].update("")
            case "Complete":
                todo_to_complete = values["-todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["-todos"].update(values=todos)
                window["-todo"].update("")
            case "Exit":
                break
    except (ValueError, IndexError):
        sg.popup("Item is empty. Please Try again", font=("Helvetica", 16))

window.close()
