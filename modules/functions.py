from os.path import dirname, realpath

FILENAME = 'todos.dat'
FILEPATH = dirname(realpath(__file__)) + '/../files/' + FILENAME


def get_todos(filepath_arg=FILEPATH):
    """ Read text file and return the list of to-do items """
    with open(filepath_arg, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath_arg=FILEPATH):
    """ Write the to-do list in a text file """
    with open(filepath_arg, 'w') as file_local:
        file_local.writelines(todos_arg)


def list_index(index_arg):
    return int(index_arg) - 1


def view_index(index_arg):
    return int(index_arg) + 1


def formatting_for_write(item_arg):
    """ Format string for to-do list """
    item_arg = item_arg.lower()
    item_arg = item_arg.strip()
    item_arg = item_arg + "\n"
    return item_arg


def formatting_for_print(index_arg, item_arg):
    """ Format string for printing to-do list """
    index_arg = view_index(index_arg)
    item_arg = item_arg.capitalize()
    item_arg = item_arg.strip("\n")
    return f"{index_arg}.{item_arg}"


def except_value():
    print("Your command is not valid!")


def except_index():
    print("Invalid index!")
