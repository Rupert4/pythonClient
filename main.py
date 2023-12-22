import sys
import datetime
from PyQt6 import uic, QtCore, QtGui, QtWidgets


class MainWindows(QtWidgets.QMainWindow):
    ServerAdress = "http://locallhost:5000"
    MessageID = 0

    def __init__(self, *args, **kwargs):
        super(MainWindows, self).__init__(*args, **kwargs)
        uic.loadUi('Messanger.ui', self)
        # self.SendButton.clicked.connect(self.SendButton_clicked)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindows()
    window.show()
    sys.exit(app.exec())
