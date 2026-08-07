todos = []
sl = 1
 
while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip()
 
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(f"{sl}. {todo}")
            sl += 1
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            num = int(input("Enter the number of the item you wish to edit: "))
            idx = num - 1
            newToDo = input("Please edit " + todos[idx] + ": ")
            todos[idx] = f"{num}. {newToDo}"
        case 'exit':
            break
 
print("Bye!")