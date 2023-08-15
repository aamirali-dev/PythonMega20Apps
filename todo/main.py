from core.todo import Todo
from cli.cli import CLInterface
from gui.todogui import TodoGUI
from web.todoweb import TodoWeb

if __name__ == '__main__':
    # CLInterface(Todo()).run()
    # TodoGUI(Todo()).run()
    TodoWeb(Todo())

