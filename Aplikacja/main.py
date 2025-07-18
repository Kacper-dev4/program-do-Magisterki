import szereguj
import sys
import csv
import random
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QPushButton, QWidget, QHBoxLayout, QItemDelegate, QLineEdit,
    QAction, QMessageBox, QFileDialog, QDialog, QLabel  
)
from PyQt5.QtGui import QIntValidator
import PyQt5.QtWidgets as qtw



class RangeDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ustawienia losowania")

        self.min_edit = QLineEdit()
        self.max_edit = QLineEdit()
        self.rows_edit = QLineEdit()
        self.cols_edit = QLineEdit()

        # Tylko liczby całkowite dodatnie
        validator = QIntValidator(1, 999999)
        for edit in [self.min_edit, self.max_edit, self.rows_edit, self.cols_edit]:
            edit.setValidator(validator)

        self.min_edit.setPlaceholderText("Minimalna wartość")
        self.max_edit.setPlaceholderText("Maksymalna wartość")
        self.rows_edit.setPlaceholderText("Liczba maszyn (wiersze)")
        self.cols_edit.setPlaceholderText("Liczba zadań (kolumny)")

        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.accept)
        btn_cancel = QPushButton("Anuluj")
        btn_cancel.clicked.connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Minimalna wartość:"))
        layout.addWidget(self.min_edit)
        layout.addWidget(QLabel("Maksymalna wartość:"))
        layout.addWidget(self.max_edit)
        layout.addWidget(QLabel("Liczba maszyn (wiersze):"))
        layout.addWidget(self.rows_edit)
        layout.addWidget(QLabel("Liczba zadań (kolumny):"))
        layout.addWidget(self.cols_edit)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn_ok)
        btn_layout.addWidget(btn_cancel)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def get_values(self):
        try:
            min_val = int(self.min_edit.text())
            max_val = int(self.max_edit.text())
            rows = int(self.rows_edit.text())
            cols = int(self.cols_edit.text())
            return min_val, max_val, rows, cols
        except ValueError:
            return None, None, None, None



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

        self.setWindowTitle("Aplikacja Flow Shop")
        self.resize(800, 600)

        self.table = QTableWidget(2, 2)
        self.table.setHorizontalHeaderLabels(['Zadanie 1', 'Zadanie 2'])
        self.table.resizeColumnsToContents()
        self.update_row_headers()

        # Ustawiamy delegata do walidacji cyfr
        self.delegate = IntOnlyDelegate()
        self.table.setItemDelegate(self.delegate)
        self.saved_data = []

        # Menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('Plik')
        help_menu = menubar.addMenu('Pomoc')
        
        exit_action = QAction('Zamknij program', self)
        exit_action.triggered.connect(self.close)

        save_action = QAction('Zapisz',self)
        save_action.triggered.connect(self.save_table)

        load_action = QAction('Wczytaj',self)
        load_action.triggered.connect(self.load_table)

        random_action = QAction('Wygeneruj losowe',self)
        random_action.triggered.connect(self.random_fill_table)

        file_menu.addAction(save_action)
        file_menu.addAction(load_action)
        file_menu.addAction(random_action)
        file_menu.addAction(exit_action)

        #Combo box
        self.combo_box = qtw.QComboBox()
        self.combo_box.addItem("Ta sama kolejność", False)
        self.combo_box.addItem("Różna kolejność", True)
        self.combo_box.setFixedWidth(150)

        self.combo_box.currentIndexChanged.connect(self.check_conditions)

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

    def update_column_headers(self):
         for column in range(self.table.columnCount()):
            self.table.setHorizontalHeaderItem(column, QTableWidgetItem(f"Zadanie {column + 1}"))
            self.table.resizeColumnsToContents()


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


    def save_table(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Zapisz plik", "", "CSV Files (*.csv)")
        if filename:
            try:
                with open(filename, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    for row in range(self.table.rowCount()):
                        row_data = []
                        for column in range(self.table.columnCount()):
                            item = self.table.item(row, column)
                            row_data.append(item.text() if item else "")
                        writer.writerow(row_data)
                QMessageBox.information(self, "Zapisano", "Dane zostały zapisane pomyślnie.")
            except Exception as e:
                QMessageBox.warning(self, "Błąd zapisu", str(e))

    def load_table(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Wczytaj plik", "", "CSV Files (*.csv)")
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    data = list(reader)

                    self.table.setRowCount(len(data))
                    self.table.setColumnCount(max(len(row) for row in data))
                    
                    for row_idx, row in enumerate(data):
                        for col_idx, value in enumerate(row):
                            self.table.setItem(row_idx, col_idx, QTableWidgetItem(value))
                            
                self.update_row_headers()
                self.update_column_headers()
                QMessageBox.information(self, "Wczytano", "Dane zostały wczytane pomyślnie.")
            except Exception as e:
                QMessageBox.warning(self, "Błąd wczytywania", str(e))

    def random_fill_table(self):
        dialog = RangeDialog()
        if dialog.exec_() == QDialog.Accepted:
            min_val, max_val, rows, cols = dialog.get_values()

            if None in [min_val, max_val, rows, cols]:
                QMessageBox.warning(self, "Błąd", "Podaj poprawne liczby całkowite dodatnie!")
                return

            if min_val > max_val:
                QMessageBox.warning(self, "Błąd", "Minimalna wartość nie może być większa od maksymalnej!")
                return

            # Ustaw dokładnie nowy rozmiar tabeli
            self.table.clearContents()
            self.table.setRowCount(0)
            self.table.setColumnCount(0)

            self.table.setRowCount(rows)
            self.table.setColumnCount(cols)

         # Ustaw nagłówki
            for col in range(cols):
                self.table.setHorizontalHeaderItem(col, QTableWidgetItem(f"Zadanie {col + 1}"))
            self.update_row_headers()

        # Wypełnij losowymi wartościami
            for row in range(rows):
                for col in range(cols):
                    value = str(random.randint(min_val, max_val))
                    self.table.setItem(row, col, QTableWidgetItem(value))

            self.table.resizeColumnsToContents()
  

    def check_conditions(self):
        combo_data = self.combo_box.currentData()
        row_count = self.table.rowCount()

        if combo_data == True and row_count < 4:
            QMessageBox.critical(
                self,
                "Błąd",
                "Wybrano opcję wymagającą co najmniej 4 maszyn!"
            )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableEditor()
    window.show()
    sys.exit(app.exec_())
