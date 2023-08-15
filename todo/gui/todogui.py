import PySimpleGUI as sg
from core.todo import Todo


class TodoGUI:
    def __init__(self, todos: Todo):
        self.todos = todos
        self.todos.load()

    def run(self):
        self._initialize_components()
        self._main_loop()

    def _initialize_components(self):
        self.label = sg.Text('Type in a to-do')
        self.input_box = sg.Input(tooltip='Enter todo', key='todo')
        self.add_button = sg.Button('Add')
        self.listbox = sg.Listbox(values=self.todos.get_all(), key='todos', enable_events=True, size=[45, 10])
        self.edit_button = sg.Button('Edit')
        self.complete_button = sg.Button('Complete')
        self.exit_button = sg.Button('Exit')
        self.window = sg.Window('My Todo App',
                                layout=[[self.label],
                                        [self.input_box, self.add_button],
                                        [self.listbox, self.edit_button, self.complete_button],
                                        [self.exit_button]])

    def _main_loop(self):
        while True:
            event, values = self.window.read()
            if event == 'Add':
                self.todos.add(values['todo'])
                self.window['todos'].update(values=self.todos.get_all())
            elif event == 'Edit':
                try:
                    self.todos.update(self.todos.index(values['todos'][0]), values['todo'])
                except IndexError:
                    sg.popup('Please select an element first')
                self.window['todos'].update(values=self.todos.get_all())
            elif event == 'Complete':
                try:
                    self.todos.complete(self.todos.index(values['todos'][0]))
                except IndexError:
                    sg.popup('Please select an element first')
                self.window['todos'].update(values=self.todos.get_all())
                self.window['todo'].update(value='')
            elif event == 'todos':
                self.window['todo'].update(value=values['todos'][0])
            elif event == 'Exit':
                self.todos.save()
                break
            elif event == sg.WIN_CLOSED:
                self.todos.save()
                break
        self.window.close()


