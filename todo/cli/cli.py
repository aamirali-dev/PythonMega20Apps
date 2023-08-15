from core.todo import Todo


class CLInterface:
    def __init__(self, todos):
        self.todos = todos
        self.todos.load()

    def execute(self, user_action):
        if user_action.startswith('add'):
            self.todos.add(user_action.replace('add', '').strip())
        elif user_action.startswith('edit'):
            action = user_action.replace('edit', '').strip()
            index = action.split(' ')[0]
            self.todos.update(int(index) - 1, action.replace(index, '').strip())
        elif user_action.startswith('complete'):
            self.todos.complete(int(user_action.split(' ')[1]) - 1)
        elif user_action.startswith('show'):
            print(str(self.todos))
        else:
            raise ValueError('Invalid Command')

    def run(self):
        while True:
            user_action = input('Enter commands (add, edit, complete, or exit): ').strip()
            if user_action.startswith('exit'):
                self.todos.save()
                break
            else:
                try:
                    self.execute(user_action)
                except ValueError as e:
                    print(e)
                except IndexError:
                    print('There aren\'t as many todos yet')
