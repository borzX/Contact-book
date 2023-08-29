import sys
from random import *
import json
import math
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox,QWidget,  QTableWidget,
    QTableWidgetItem)
from PyQt5.uic import loadUi
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt


class Window_2(QMainWindow):                                # Всплывающее окно добавления контакта         
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавление контакта")
        uic.loadUi('main_w2.ui', self)
        self.setFixedSize(405, 175)
        self.lineEdit_2.setPlaceholderText("Фамилия")
        self.lineEdit_3.setPlaceholderText("Имя")
        self.lineEdit_5.setPlaceholderText("Телефон")
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.exx)


    def save(self):                                         # Зипась в фаил
        with open("phone-book.json", "r", encoding = "utf-8") as book1:
            pb = json.load(book1)
        name = (self.lineEdit_2.text())
        name2 = (self.lineEdit_3.text())
        number0 = (self.lineEdit_5.text())
        pb[name] = {"name2": name2, "phone_numbers": number0}
        with open("phone-book.json", "r+", encoding = "utf-8") as book:
            book.write(json.dumps(pb, ensure_ascii = False))
        self.textEdit.setPlaceholderText("Контакт сохранен")


    def exx(self):                                          # Закрыть всплывающее окно
        self.close()

    


class MainWindow(QMainWindow):                              # Основное окно
    def __init__(self):
            super(MainWindow, self).__init__()
            self.setFixedSize(370, 435)
            self.setWindowTitle('Контакты')
            uic.loadUi('main_form.ui', self)
            self.pushButton1.clicked.connect(self.ListContact)
            self.pushButton1_2.clicked.connect(self.window_new_contact)
            self.listWidget.itemDoubleClicked.connect(self.window_edit_contact)
            self.pushButton1_3.clicked.connect(self.exx)
            
            self.listWidget.clear()
            with open("phone-book.json", "r", encoding = "utf-8") as book1:
                pb = json.load(book1)
            self.listWidget.addItems(pb)
            if self.pushButton1.isChecked():
                pb = Qt.SortOrder.DescendingOrder               # что бы изменть параметр сортировки, нужно поменять местами
                # pb = Qt.SortOrder.AscendingOrder          
            else:
                # pb = Qt.SortOrder.DescendingOrder
                pb = Qt.SortOrder.AscendingOrder
            self.listWidget.sortItems(pb)



    def ListContact(self):
        self.listWidget.clear()
        with open("phone-book.json", "r", encoding = "utf-8") as book1:
            pb = json.load(book1)
        self.listWidget.addItems(pb)
        if self.pushButton1.isChecked():
            pb = Qt.SortOrder.DescendingOrder               # что бы изменть параметр сортировки, нужно поменять местами
            # pb = Qt.SortOrder.AscendingOrder          
        else:
            # pb = Qt.SortOrder.DescendingOrder
            pb = Qt.SortOrder.AscendingOrder
        self.listWidget.sortItems(pb)

            
    def window_new_contact(self):
        self.window = Window_2(self)
        self.window.show()

    def window_edit_contact(self):                  # Запуск окна редактирования контакта
        # label_str = self.listWidget.currentRow()  # Выведет индекс строки
        label_row = self.listWidget.currentRow()
        val = self.listWidget.item(label_row).text()
        with open("phone-book.json", "r", encoding = "utf-8") as book1:
            phone_book = json.load(book1)
        phone_book2=phone_book[val]
        phone_book3= {}
        name = val
        name2 = phone_book2["name2"]
        phone_numbers = phone_book2['phone_numbers']
        phone_book3[name] = {"name2": name2, "phone_numbers": phone_numbers}
        with open("temp_contact.json", "w", encoding = "utf-8") as book2:
            book2.write(json.dumps(phone_book3, ensure_ascii = False))
        self.window = Window_3(self)
        self.window.show()

    def exx(self):                                          # Закрыть всплывающее окно
        self.close()



class Window_3(QMainWindow):                                # Всплывающее окно редактирования контакта         
    def __init__(self, parent=MainWindow):
        super().__init__(parent)
        self.setWindowTitle("Window_3")
        uic.loadUi('main_w3.ui', self)
        self.setFixedSize(395, 230)
        self.pushButton_close.clicked.connect(self.exx)
        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_erase.clicked.connect(self.delete)
        with open("temp_contact.json", "r", encoding = "utf-8") as book1:
            phone_book = json.load(book1)
            for item in phone_book:
                name = item
        phone_book2 = phone_book[name]
        name2_t = phone_book2["name2"]
        number0_t = str(phone_book2["phone_numbers"])
        self.lineEdit_2.setText(name)
        self.lineEdit_3.setText(name2_t)
        self.lineEdit_4.setText(number0_t)
        

    def save(self):                                         # Зипась в фаил
        with open("phone-book.json", "r", encoding = "utf-8") as book1:
            pb = json.load(book1)
        name = (self.lineEdit_2.text())
        name2 = (self.lineEdit_3.text())
        number0 = (self.lineEdit_4.text())
        pb[name] = {"name2": name2, "phone_numbers": number0}
        with open("phone-book.json", "r+", encoding = "utf-8") as book:
            book.write(json.dumps(pb, ensure_ascii = False))
        self.textEdit.setPlaceholderText("Контакт сохранен")

    def delete(self):
        with open("phone-book.json", "r", encoding = "utf-8") as book1:
            phone_book = json.load(book1)
            print(phone_book)
        name = (self.lineEdit_2.text())
        pb_temp = phone_book.copy()
        del pb_temp[name]
        with open("phone-book.json", "w", encoding = "utf-8") as book:
            book.write(json.dumps(pb_temp, ensure_ascii = False))
        self.close()




    def exx(self):                                          # Закрыть всплывающее окно
        self.close()






app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())