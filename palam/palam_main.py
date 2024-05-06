import sys
from functools import partial
import random

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon,QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from Palam import Ui_MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        self.ui.btn_back.clicked.connect(partial(self.user_choice, 1))
        self.ui.btn_up.clicked.connect(partial(self.user_choice, 0))

        self.cpu1_s = self.cpu2_s = self.user_s = 0
        self.round_count = 0
        self.winner = None
        
        self.ui.lbl_s_user.setText(str(self.user_s))
        self.ui.lbl_s_cpu1.setText(str(self.cpu1_s))
        self.ui.lbl_s_cpu2.setText(str(self.cpu2_s))

    # def closeEvent(self, event):
    def result(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Scores")
        msg_box.setStyleSheet("background-color: white; font-weight: bold;")

        msg = f"Scores:\nUser: {self.user_s}    CPU1: {self.cpu1_s}    CPU2: {self.cpu2_s}\nWinner: {self.winner}"
        msg_box.setText(msg)
        
        if self.winner == "User":
            msg_box.setIconPixmap(QPixmap("Assignment20\palam\pics\you.png"))
        elif self.winner == "CPU1":
            msg_box.setIconPixmap(QPixmap("Assignment20\palam\pics\computer1.png"))
        elif self.winner == "CPU2":
            msg_box.setIconPixmap(QPixmap("Assignment20\palam\pics\computer2.png"))
        else:
            msg_box.setIconPixmap(QPixmap("draw.png"))

        msg_box.exec()

        self.user_s = self.cpu1_s = self.cpu2_s = self.round_count = 0

        self.ui.lbl_s_user.setText(str(self.user_s))
        self.ui.lbl_s_cpu1.setText(str(self.cpu1_s))
        self.ui.lbl_s_cpu2.setText(str(self.cpu2_s))

    def user_choice(self, user_choice):
        if user_choice == 1:
            self.ui.lbl_user.setPixmap(QPixmap("Assignment20/palam/pics/back.png"))
        else:
            self.ui.lbl_user.setPixmap(QPixmap("Assignment20/palam/pics/front.png"))

        cpu1_choice = random.randint(0, 1)
        cpu2_choice = random.randint(0, 1)

        if cpu1_choice == 1:
            self.ui.lbl_cpu1.setPixmap(QPixmap("Assignment20/palam/pics/back.png"))
        else:
            self.ui.lbl_cpu1.setPixmap(QPixmap("Assignment20/palam/pics/front.png"))
        
        if cpu2_choice == 1:
            self.ui.lbl_cpu2.setPixmap(QPixmap("Assignment20/palam/pics/back.png"))
        else:
            self.ui.lbl_cpu2.setPixmap(QPixmap("Assignment20/palam/pics/front.png"))

        if (user_choice == 1 and cpu1_choice == 0 and cpu2_choice == 0) or (user_choice == 0 and cpu1_choice == 1 and cpu2_choice == 1):
            self.user_s += 1

        elif (cpu1_choice == 1 and user_choice == 0 and cpu2_choice == 0) or (cpu1_choice == 0 and user_choice == 1 and cpu2_choice == 1):
            self.cpu1_s += 1

        elif (cpu2_choice == 1 and user_choice == 0 and cpu1_choice == 0) or (cpu2_choice == 0 and user_choice == 1 and cpu1_choice == 1):
            self.cpu2_s += 1

        self.round_count += 1

        if self.round_count == 5:
            if self.user_s > self.cpu1_s and self.user_s > self.cpu2_s:
                self.winner = "User"
            elif self.cpu1_s > self.user_s and self.cpu1_s > self.cpu2_s:
                self.winner = "CPU1"
            elif self.cpu2_s > self.user_s and self.cpu2_s > self.cpu1_s:
                self.winner = "CPU2"
            else:
                self.winner = "Draw"
            # self.closeEvent(None)
            self.result()

        self.ui.lbl_s_user.setText(str(self.user_s))
        self.ui.lbl_s_cpu1.setText(str(self.cpu1_s))
        self.ui.lbl_s_cpu2.setText(str(self.cpu2_s))

        # print(f"cpu1_choice: {cpu1_choice} , cpu2_choice: {cpu2_choice} , user_choice: {user_choice}")

my_app = QApplication(sys.argv)
my_window = MainWindow()

button_size = my_window.ui.btn_back.size()
icon_size = QSize(button_size.width() - 5, button_size.height() - 5)

my_window.ui.btn_back.setIconSize(icon_size)
my_window.ui.btn_back.setIcon(QIcon("Assignment20/palam/pics/back.png"))

my_window.ui.btn_up.setIconSize(icon_size)
my_window.ui.btn_up.setIcon(QIcon("Assignment20/palam/pics/front.png"))

my_window.show()
my_app.exec()