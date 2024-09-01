import sys
import subprocess
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QRadioButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Silent Shores")
        self.setGeometry(600, 400, 800, 700)
        
        self.labelImage = QLabel(self)
        self.labelImage.setPixmap(QPixmap("island.png"))
        self.labelImage.resize(800, 300)
        self.labelImage.move(0, 0)
        
        self.labelSelect = QLabel("Select an Application to isolate:", self)
        self.labelSelect.resize(360, 50)
        self.labelSelect.move(300, 340)
        
        self.labelStatus = QLabel("STATUS: INACTIVE", self)
        self.labelStatus.resize(360, 50)
        self.labelStatus.move(340, 530)
        self.labelStatus.setStyleSheet("color: red;")
        
        self.radioBrowser = QRadioButton("Web Browser", self)
        self.radioBrowser.move(360, 380)
        self.radioOffice = QRadioButton("Office Suite", self)
        self.radioOffice.move(360, 410)
        self.radioEmail = QRadioButton("E-mail", self)
        self.radioEmail.move(360, 440)
        
        self.buttonLaunch = QPushButton("Launch", self)
        self.buttonLaunch.clicked.connect(self.isolate)
        self.buttonLaunch.setFixedSize(100, 40)
        self.buttonLaunch.move(350, 610)
        
        self.apply_theme()
        
    def apply_theme(self):
        stylesheet = """
        QMainWindow {
            background-color: #2e2e2e;
        }
        QLabel, QRadioButton {
            font-size: 14px;
            color: #e0e0e0;
        }
        QPushButton {
            color: #e0e0e0;
            background-color: #3e3e3e;
            border: 1px solid #444;
        }
        QPushButton:hover {
            background-color: #555;
        }
        """
        self.setStyleSheet(stylesheet)
        
    def isolate(self):
        if self.radioBrowser.isChecked():
            try:
                process = subprocess.Popen(('firejail', 'firefox'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                if process.returncode != 0:
                    raise Exception(stderr.decode().strip())
                else:
                    self.labelStatus.setText("STATUS: ACTIVE")
                    self.labelStatus.setStyleSheet("color: green;")
            except Exception:
                self.labelStatus.setText("STATUS: ERROR")
                self.labelStatus.setStyleSheet("color: red;")	
        elif self.radioOffice.isChecked():
            try:
                process = subprocess.Popen(('firejail', 'libreoffice'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                if process.returncode != 0:
                    raise Exception(stderr.decode().strip())
                else:
                    self.labelStatus.setText("STATUS: ACTIVE")
                    self.labelStatus.setStyleSheet("color: green;")
            except Exception:
                self.labelStatus.setText("STATUS: ERROR")
                self.labelStatus.setStyleSheet("color: red;")
        elif self.radioEmail.isChecked():
            try:
                process = subprocess.Popen(('firejail', 'thunderbird'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                if process.returncode != 0:
                    raise Exception(stderr.decode().strip())
                else:
                    self.labelStatus.setText("STATUS: ACTIVE")
                    self.labelStatus.setStyleSheet("color: green;")
            except Exception:
                self.labelStatus.setText("STATUS: ERROR")
                self.labelStatus.setStyleSheet("color: red;")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())