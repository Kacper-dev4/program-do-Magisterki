import szereguj
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QPushButton, QWidget, QHBoxLayout, QItemDelegate, QLineEdit
)
from PyQt5.QtGui import QIntValidator
import PyQt5.QtWidgets as qtw

class IntOnlyDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        lowerBound = 0
        upperBound = 999999999
        editor = QLineEdit(parent)
        validator = QIntValidator(lowerBound, upperBound, parent)  # tylko liczby całkowite dodatnie
        editor.setValidator(validator)
        return editor


class TableEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wprowadzane danych")
        self.resize(800, 600)

        self.table = QTableWidget(2, 2)
        self.table.setHorizontalHeaderLabels(['Zadanie 1', 'Zadanie 2'])
        self.table.resizeColumnsToContents()
        self.update_row_headers()

        # Ustawiamy delegata do walidacji cyfr
        self.delegate = IntOnlyDelegate()
        self.table.setItemDelegate(self.delegate)

        self.saved_data = []

        #Combo box
        self.combo_box = qtw.QComboBox()
        self.combo_box.addItem("Ta sama kolejność", False)
        self.combo_box.addItem("Różna kolejność", True)
        self.combo_box.setFixedWidth(150)

        dlugoscPrzyciskow = 150
        # Przyciski
        self.add_row_btn = QPushButton("Dodaj maszynę")
        self.add_row_btn.setFixedWidth(dlugoscPrzyciskow)
        self.remove_row_btn = QPushButton("Usuń ostatnią maszynę")
        self.remove_row_btn.setFixedWidth(dlugoscPrzyciskow)
        self.add_col_btn = QPushButton("Dodaj zadanie")
        self.add_col_btn.setFixedWidth(dlugoscPrzyciskow)
        self.remove_col_btn = QPushButton("Usuń ostatnie zadanie")
        self.remove_col_btn.setFixedWidth(dlugoscPrzyciskow)
        self.add_to_list_btn = QPushButton("Uszereguj")
        self.add_to_list_btn.setFixedWidth(dlugoscPrzyciskow)

        self.add_row_btn.clicked.connect(self.add_row)
        self.remove_row_btn.clicked.connect(self.remove_row)
        self.add_col_btn.clicked.connect(self.add_column)
        self.remove_col_btn.clicked.connect(self.remove_column)
        #self.add_to_list_btn.clicked.connect(self.save_data_to_list)
        self.add_to_list_btn.clicked.connect(self.uszeregowanie)
        # Layouty
        button_layout = QHBoxLayout()
        for btn in [
            self.add_row_btn,
            self.remove_row_btn,
            self.add_col_btn,
            self.remove_col_btn,
            self.add_to_list_btn
        ]:
            button_layout.addWidget(btn)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.combo_box)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def update_row_headers(self):
        for row in range(self.table.rowCount()):
            self.table.setVerticalHeaderItem(row, QTableWidgetItem(f"Maszyna {row + 1}"))

    def add_row(self):
        row_index = self.table.rowCount()
        self.table.insertRow(row_index)
        self.update_row_headers()

    def remove_row(self):
        rows = self.table.rowCount()
        if rows > 0:
            self.table.removeRow(rows - 1)
            self.update_row_headers()

    def add_column(self):
        col_index = self.table.columnCount()
        self.table.insertColumn(col_index)
        self.table.setHorizontalHeaderItem(col_index, QTableWidgetItem(f"Zadanie {col_index + 1}"))
        self.table.resizeColumnsToContents()

    def remove_column(self):
        cols = self.table.columnCount()
        if cols > 0:
            self.table.removeColumn(cols - 1)

    def save_data_to_list(self):
        data = []
        for row in range(self.table.rowCount()):
            row_data = []
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                row_data.append(item.text() if item else "")
            data.append(row_data)
        self.saved_data = data
        #print("Zapisane dane:", self.saved_data)
    def uszeregowanie(self):
        self.save_data_to_list()
        szereguj.przekarz(self.saved_data,roznaKolejnosc=self.combo_box.currentData())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableEditor()
    window.show()
    sys.exit(app.exec_())
