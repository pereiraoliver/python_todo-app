import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="-todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(
    values=functions.get_todos(), key="-todos", enable_events=True, size=[45, 10]
)
buttons = sg.Column([[sg.Button("Edit")], [sg.Button("Complete")]])
exit_button = sg.Button("Exit")

layout = [[label], [input_box, add_button], [list_box, buttons], [exit_button]]

window = sg.Window(
    "My To-Do App",
    layout=layout,
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
        case "Complete":
            todo_to_complete = values["-todos"][0]
            todos = functions.get_todos()
            # idx = todos.index(",".join(values["-todos"]))
            # idx = todos.index(values["-todos"][0])
            # todos.pop(idx)
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["-todos"].update(values=todos)
            window["-todo"].update("")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
