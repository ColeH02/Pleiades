from PyQt5.QtWidgets import *

from main import train
from train import *

def main():
    app = QApplication([])
    button = QPushButton('Calculate ALQ')

    def on_button_clicked():
        alert = QMessageBox()
        alert.setText('ALQ:', train.ALQ)
        alert.exec()

    button.clicked.connect(on_button_clicked)
    button.show()
    app.exec()

if __name__ == "__main__":
	main()