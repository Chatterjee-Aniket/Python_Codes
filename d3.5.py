todos = []
while True:
    user_action = input("Type add,show or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break
        case _:
            print("Sorry, You have entered an unknown command!")
print("Bye!")