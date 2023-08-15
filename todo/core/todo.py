

class Todo:
    def __init__(self, todos=[]):
        self.todos = todos

    def get_all(self):
        return self.todos

    def add(self, todo):
        self.todos.append(todo)

    def __str__(self):
        result = ""
        for index, item in enumerate(self.todos):
            result += f'{index+1} - {item} \n'
        return result

    def __repr__(self):
        return f'Todo(todos={self.todos})'

    def update(self, index, new_entry):
        self.todos[index] = new_entry

    def remove(self, index):
        del self.todos[index]

    def complete(self, index):
        self.remove(index)

    def index(self, todo):
        return self.todos.index(todo)

    def save(self):
        with open('todos.db', 'w') as f:
            f.write(repr(self))

    def load(self):
        try:
            with open('todos.db', 'r') as f:
                self.todos = eval(f.read()).todos
        except FileNotFoundError:
            pass

