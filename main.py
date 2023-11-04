import sys
from metod_gauss import Gauss
from metod_kramer import Kramer
from PySide2.QtWidgets import QApplication, QWidget
from user_interfase import Ui_Form


__author__ = 'Borshevskiy'

class MainWindow(QWidget, Ui_Form):

    rows = 3
    colum_name = ["x1", "x2", "x3"]
    colum_name.append("b")
    accuracy = 3

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tableWidget.setRowCount(self.rows)
        self.tableWidget.setColumnCount(len(self.colum_name))
        self.tableWidget.setHorizontalHeaderLabels(self.colum_name)
        self.pushButton_3.clicked.connect(self.GaussCalculation)
        self.pushButton_2.clicked.connect(self.AccuracyСalculation)
        self.pushButton.clicked.connect(self.KramerCalculation)
        self.pushButton_4.clicked.connect(self.InitialTable)

    #   Задание точности расчетов
    def AccuracyСalculation(self):
        self.accuracy = int(self.lineEdit.text())

    #   Составление рабочей матрицы для метода Гаусса
    def GaussCalculation(self):
        self.matrix = [[] for _ in range(self.rows)]
        for row in range(self.rows):
            for colume in range(len(self.colum_name)):
                self.matrix[row].append(float(self.tableWidget.item(row, colume).text()))
        self.lineEdit_2.setText(str(Gauss(self.matrix, self.accuracy)))

    #   Составление рабочей матрицы для метода Крамера
    def KramerCalculation(self):
        self.matrix_arg = [[] for _ in range(self.rows)]
        self.matrix_free_arg = []
        for row in range(self.rows):
            self.matrix_free_arg.append(
                float(self.tableWidget.item(row, len(self.colum_name)-1).text()))
            for colume in range(len(self.colum_name)-1):
                self.matrix_arg[row].append(float(self.tableWidget.item(row, colume).text()))
        self.lineEdit_3.setText(
            str(Kramer(self.matrix_arg, self.matrix_free_arg, self.accuracy)))
            
    #   Обновление размера таблицы
    def InitialTable(self):
        self.colum_name = []
        for i in range(int(self.lineEdit_4.text())):
            self.colum_name.append(f"x{i+1}")
        self.colum_name.append("b")
        self.rows = int(self.lineEdit_4.text())
        self.tableWidget.setRowCount(self.rows)
        self.tableWidget.setColumnCount(len(self.colum_name))
        self.tableWidget.setHorizontalHeaderLabels(self.colum_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    