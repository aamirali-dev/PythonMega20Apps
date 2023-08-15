import sys
from datetime import datetime

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Age Calculator')
        grid = QGridLayout()
        distance_label = QLabel('Distance: ')
        self.distance_line_edit = QLineEdit()

        self.unit_combo_box = QComboBox()
        self.unit_combo_box.addItems(['Imperial (miles)', 'Metric (km)'])

        time_label = QLabel('Time (hours): ')
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton('Calculate')
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel('')

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.unit_combo_box, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = int(self.distance_line_edit.text())
        time = int(self.time_line_edit.text())
        unit = self.unit_combo_box.currentIndex()
        if unit == 1:
            unit = 'km/h'
        else:
            unit = 'miles/h'
        self.output_label.setText(f'Average speed {distance/time} {unit}')


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
