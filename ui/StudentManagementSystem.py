import sqlite3
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QComboBox, QToolBar, QStatusBar, \
    QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')
        self.setMinimumSize(500, 400)

        file_menu_item = self.menuBar().addMenu('&File')
        help_menu_item = self.menuBar().addMenu('&Help')
        edit_menu_item = self.menuBar().addMenu('&Edit')

        add_student_action = QAction(QIcon('icons/add.png'), 'Add Student', self)
        file_menu_item.addAction(add_student_action)
        add_student_action.triggered.connect(self.insert)

        about_action = QAction('About', self)
        help_menu_item.addAction(about_action)
        about_action.triggered.connect(self.about)

        search_action = QAction(QIcon('icons/search.png'), 'Search', self)
        edit_menu_item.addAction(search_action)
        search_action.triggered.connect(self.search)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('Id', 'Name', 'Course', 'Mobile'))
        self.setCentralWidget(self.table)
        self.load_table()

        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton('Edit Record')
        edit_button.clicked.connect(self.edit)
        delete_button = QPushButton('Delete Record')
        delete_button.clicked.connect(self.delete)

        children = self.findChildren(QPushButton)
        for child in children:
            self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)

    def delete(self):
        index = student_management_system.table.currentRow()
        student_id = student_management_system.table.item(index, 0).text()
        dialog = DeleteDialog(student_id)
        dialog.exec()
    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def about(self):
        dialog = AboutDialog()
        dialog.exec()
    def load_data(self, data):
        self.table.setRowCount(0)
        for index, row in enumerate(data):
            self.table.insertRow(index)
            for col_num, data in enumerate(row):
                self.table.setItem(index, col_num, QTableWidgetItem(str(data)))

    def get_data(self, query='SELECT * FROM students'):
        connnection = sqlite3.connect('database.db')
        result = list(connnection.execute(query))
        connnection.close()
        return result
    def load_table(self):
        self.load_data(self.get_data())

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()

    def load_search_results(self, filter):
        items = self.table.findItems(filter, Qt.MatchFlag.MatchFixedString)
        for item in items:
            self.table.item(item.row(), 1).setSelected(True)

class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('About')
        content = '''
        This APP was created during the course "The Python Mega Course".
        Feel free to modify and reuse this app.
        '''
        self.setText(content)

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Insert Student Data')
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText('Name')
        layout.addWidget(self.student_name)

        self.course_name = QComboBox()
        courses = ['bio', 'math', 'astro', 'phy']
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText('Mobile')
        layout.addWidget(self.mobile)

        self.submit = QPushButton('Register')
        self.submit.clicked.connect(self.add_student)
        layout.addWidget(self.submit)

        self.setLayout(layout)

    def get_details(self):
        name = self.student_name.text()
        mobile = self.mobile.text()
        course = self.course_name.currentText()
        return (name, mobile, course)

    def commit(self, execute):
        connecton = sqlite3.connect('database.db')
        cursor = connecton.cursor()
        execute(cursor)
        connecton.commit()
        cursor.close()
        connecton.close()

    def add_student(self):
        self.commit(
            execute=lambda cursor: cursor.execute(
                'INSERT INTO students (name, course, mobile) VALUES (?,?,?)',
                self.get_details()
            ))
        self.close()
        student_management_system.load_table()

class EditDialog(InsertDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Update Student Data')

        index = student_management_system.table.currentRow()
        self.id = student_management_system.table.item(index, 0).text()
        name = student_management_system.table.item(index, 1).text()
        course = student_management_system.table.item(index, 2).text()
        mobile = student_management_system.table.item(index, 3).text()
        self.student_name.setText(name)
        self.course_name.setCurrentText(course)
        self.mobile.setText(mobile)
        self.submit.setText('Update')

    def add_student(self):

        name, course, mobile = self.get_details()
        self.commit(
            execute=lambda cursor: cursor.execute(
                        'UPDATE students SET name = ?, course = ?, mobile = ? WHERE id = ?',
                        (name, course, mobile, self.id)
                    ))
        self.close()
        student_management_system.load_table()


class DeleteDialog(QDialog):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.setWindowTitle('Delete Student Data')

        layout = QGridLayout()
        confirmation = QLabel('Are you sure you want to delete?')
        yes = QPushButton('Yes')
        no = QPushButton('No')

        layout.addWidget(confirmation, 0, 0,  1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)
        self.setLayout(layout)

        no.clicked.connect(self.close)
        yes.clicked.connect(self.delete)

    def delete(self):
        connecton = sqlite3.connect('database.db')
        cursor = connecton.cursor()
        cursor.execute('DELETE FROM students WHERE id = ?', (self.id, ))
        connecton.commit()
        cursor.close()
        connecton.close()
        self.close()
        student_management_system.load_table()

class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()
        self.search = QLineEdit()
        self.search.setPlaceholderText('Name')
        layout.addWidget(self.search)

        search = QPushButton('Search')
        search.clicked.connect(self.handle_search)
        layout.addWidget(search)

        self.setLayout(layout)

    def handle_search(self):
        search = self.search.text()
        self.close()
        student_management_system.load_search_results(filter=search)



app = QApplication(sys.argv)
student_management_system = MainWindow()
student_management_system.show()
sys.exit(app.exec())