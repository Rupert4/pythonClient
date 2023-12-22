import sys
import datetime
import json
from PyQt5 import uic, QtCore, QtGui, QtWidgets
import requests
from requests.exceptions import HTTPError


class MainWindows(QtWidgets.QMainWindow):
    ServerAdress = "http://127.0.0.1:5000"
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

    def GetMessage(self,id):
        url = self.ServerAdress + "/api/Messanger/" +str(id)
        try:
            response = requests.get(url)
            response.raise_for_status()
            # requestsasync
        except HTTPError as http_err:
            return  None
        else:
            text = response.text
            return text
    def timerEvent(self):
        message = self.GetMessage(self.MessageID)
        while message is not None:
            message = json.loads(message)
            UserName = message["UserName"]
            MessageText = message["MessageText"]
            TimeStamp = message["TimeStamp"]
            msgText =f"{TimeStamp}:{UserName}:{MessageText}"
            #print(msgText)
            self.listWidget.insertItem(self.MessageID,msgText)
            self.MessageID+=1
            message = self.GetMessage(self.MessageID)
            #Threading


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindows()
    window.show()
    timer = QtCore.QTimer()
    time = QtCore.QTime(0,0,0)
    timer.timeout.connect(window.timerEvent)
    timer.start(5000)
    sys.exit(app.exec())
