# Difference b/w String & List:-
# Program Implementation:-
user_prompt = "Enter a todo:"
todos = []
while True:
    todo = input(user_prompt)
    todos.append(todo) # todos is a list
    todo.append() # todo is a string
    print(todos)