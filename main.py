from os.path import exists
from modules import functions
from time import strftime

datetime = strftime("%b %d, %Y %H:%M:%S")
print(f"It's {datetime}")

if not exists(functions.FILEPATH):
    with open(functions.FILEPATH, 'x') as file:
        file.close()

while True:
    user_action = input("Type add & todo, show, edit & index, complete & index or exit: ")
    user_action = user_action.lower()
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        if not todo:
            todo = input("Enter a todo: ")

        todos = functions.get_todos()
        todos.append(functions.formatting_for_write(todo))

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        if todos:
            print()
            for index, item in enumerate(todos):
                print(functions.formatting_for_print(index, item))
            print()
        else:
            print("Todo list in empty!")

    elif user_action.startswith('edit'):
        try:
            index = user_action[5:]
            if not index:
                index = input('Number of todo to edit: ')
            index = functions.list_index(index)

            todo = input('Enter new todo: ')

            todos = functions.get_todos()
            todos[index] = functions.formatting_for_write(todo)
            functions.write_todos(todos)

        except ValueError:
            functions.except_value()
            continue

        except IndexError:
            functions.except_index()
            continue

    elif user_action.startswith('complete'):
        try:
            index = user_action[9:]
            if not index:
                index = input('Number of todo to complete: ')
            index = functions.list_index(index)

            todos = functions.get_todos()
            todo_complete = todos.pop(index)
            functions.write_todos(todos)

            print()
            print(f"{functions.formatting_for_print(index, todo_complete)}: completed!")
            print()

        except ValueError:
            functions.except_value()
            continue

        except IndexError:
            functions.except_index()
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Unknown command!")

print('Bye!')
