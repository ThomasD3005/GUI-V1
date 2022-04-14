from PyQt5 import QtWidgets as qtw
import sys


class LoginWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Window ")
        self.setFixedSize(400, 400)
        self.main_label = qtw.QLabel("Welcome!")
        layout = qtw.QHBoxLayout()
        layout.addWidget(self.main_label)
        self.setLayout(layout)



class RegisWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registration Window")
        self.setFixedSize(600, 150)

        layout = qtw.QHBoxLayout()
        layout_left = qtw.QVBoxLayout()
        layout_right = qtw.QVBoxLayout()

        self.fname_label = qtw.QLabel("Enter First Name")
        self.fname_edit = qtw.QLineEdit()
        self.lname_label = qtw.QLabel("Enter Last Name")
        self.lname_edit = qtw.QLineEdit()

        self.user_label = qtw.QLabel("Enter Desired Username")
        self.user_edit = qtw.QLineEdit()
        self.pass_label = qtw.QLabel("Enter Desired Password")
        self.pass_edit = qtw.QLineEdit()
        self.reg_button = qtw.QPushButton("Complete Registration")

        layout_left.addWidget(self.fname_label)
        layout_left.addWidget(self.fname_edit)
        layout_left.addWidget(self.lname_label)
        layout_left.addWidget(self.lname_edit)
        layout_right.addWidget(self.user_label)
        layout_right.addWidget(self.user_edit)
        layout_right.addWidget(self.pass_label)
        layout_right.addWidget(self.pass_edit)

        layout.addLayout(layout_left)
        layout.addLayout(layout_right)

        layout.addWidget(self.reg_button)

        self.setLayout(layout)



class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graphical User Interface V1")
        self.setFixedSize(600, 200)
        self.central_widget = qtw.QWidget()
        self.setCentralWidget(self.central_widget)
        layout1 = qtw.QVBoxLayout()

        self.central_widget.setLayout(layout1)

        user_label = qtw.QLabel("Enter Username")
        user_edit1 = qtw.QLineEdit()
        pass_label = qtw.QLabel("Enter Password")
        pass_edit1 = qtw.QLineEdit()
        reg_button = qtw.QPushButton("Register")
        reg_button.clicked.connect(self.RegWindowOpen)
        log_button = qtw.QPushButton("Login")
        log_button.clicked.connect(self.LoginWindowOpen)
        layout2 = qtw.QVBoxLayout()
        layout2.addWidget(user_label)
        layout2.addWidget(user_edit1)

        layout3 = qtw.QVBoxLayout()
        layout3.addWidget(pass_label)
        layout3.addWidget(pass_edit1)

        layout4 = qtw.QHBoxLayout()
        layout4.addWidget(reg_button)
        layout4.addWidget(log_button)

        layout1.addLayout(layout2)
        layout1.addLayout(layout3)
        layout1.addLayout(layout4)



    def RegWindowOpen(self,checked):

        self.demo = RegisWindow()
        self.demo.show()

    def LoginWindowOpen(self):

        self.demo = LoginWindow()
        self.demo.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)

    demo = MainWindow()
    demo.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')

