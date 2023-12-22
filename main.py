import sys
import datetime
import json
from PyQt5 import uic, QtCore, QtGui, QtWidgets
import requests
from requests.exceptions import HTTPError


class MainWindows(QtWidgets.QMainWindow):
    ServerAdress = "http://locallhost:5000"
    MessageID = 0

    def __init__(self, *args, **kwargs):
        super(MainWindows, self).__init__(*args, **kwargs)
        uic.loadUi('Messanger.ui', self)
        self.SendButton.clicked.connect(self.SendButton_clicked)

    def SendButton_clicked(self):
        self.SendMessage()
    def SendMessage(self):
        UserName = self.UserName.text()
        MessageText = self.Message.text()
        TimeStamp = str(datetime.datetime.today())
        message = f"{{\"UserName\": \"{UserName}\",\"MessageText\": \"{MessageText}\", \"TimeStamp\": \"{TimeStamp}\"}}"
        print("sended message:" + message)
        url = self.ServerAdress + "/api/Messanger"
        data = json.loads(message)
        request = requests.post(url,json =data)
        #print(request.status_code, request.reason)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindows()
    window.show()
    sys.exit(app.exec())
