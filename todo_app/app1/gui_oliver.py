import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="-todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(
    values=functions.get_todos(), key="-todos", enable_events=True, size=[45, 10]
)

buttons = sg.Column([[sg.Button("Edit")], [sg.Button("Delete")]])
# edit_button = sg.Button("Edit")
# delete_button = sg.Button("Delete")

window = sg.Window(
    "My To-Do App",
    layout=[[label], [input_box, add_button], [list_box, buttons]],
    font=("Helvetica", 16),
)

while True:
    event, values = window.read()

    print(f"event: {event}")
    print(f"values: {values}")
    match event:
        case "-todos":
            selected_todo = values["-todos"][0]
            window["-todo"].update(selected_todo)
        case "Add":
            todos = functions.get_todos()
            new_todo = values["-todo"] + "\n"
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
        case "Delete":
            todos = functions.get_todos()
            idx = todos.index(",".join(values["-todos"]))
            todos.pop(idx)
            functions.write_todos(todos)
            window["-todos"].update(values=todos)
            window["-todo"].update("")
        case sg.WIN_CLOSED:
            break

window.close()
