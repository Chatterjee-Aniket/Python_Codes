# edit_feature:-
# Some changes:
# Program Implementation:-
todos = []
while True:
    user_action = input("Type add,show,edit or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Enter the number of the todo to edit:"))
            number = number-1
            new_todo = input("Enter a new todo:")
            todos[number] = new_todo
        case 'exit':
            break
        case _:
            print("Hey,You have entered an unknown command!")
print("Bye!")
