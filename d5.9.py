# len() method:-
# Program Implementation:-
todos = []
while True:
    user_action = input("Type add,show,edit,complete or exit:")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show':
            print(len(todos))
        case 'edit':
            number = int(input("Number of the todo to edit:"))
            number = number-1
            new_todo = input("Enter a new todo:")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete:"))
            todos.pop(number-1)
        case 'exit':
            break
        case _:
            print("Hey,You have entered an unknown command!")
