import streamlit as st
from core.todo import Todo


class TodoWeb:
    def __init__(self, todos: Todo):
        self.todos = todos
        st.title('My Todo App')
        st.subheader('This is my Todo App')
        st.write('This app is to increase your productivity')
        self.todos.load()
        self.init_todos()

        st.text_input(label='', placeholder='Add New Todo', on_change=self.add_todo, key='new_todo')
        st.session_state

    def add_todo(self):
        todo = st.session_state['new_todo']
        self.todos.add(todo)
        self.todos.save()

    def init_todos(self):
        for index, todo in enumerate(self.todos.get_all()):
            checkbox = st.checkbox(todo, key=todo)
            if checkbox:
                self.todos.complete(index)
                self.todos.save()
                del st.session_state[todo]
                st.experimental_rerun()
