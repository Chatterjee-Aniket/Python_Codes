user_prompt = "Enter a title:"
todos = []
while True:
    todo = input(user_prompt)
    todos.append(todo.title())
    print(todos)
