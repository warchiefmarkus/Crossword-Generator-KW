import sys, subprocess
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap
import shutil

class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'CROSSWORD'
        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 880
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('OPEN WORDS', self)
        button.setToolTip('OPEN WORDS')
        button.move(0,0)
        button.resize(800,80)
        button.clicked.connect(self.on_click)
        
        button2 = QPushButton('SAVE CROSSWORD', self)
        button2.setToolTip('SAVE CROSSWORD')
        button2.move(0,80)
        button2.resize(800,80)
        button2.clicked.connect(self.on_click2)
        
        # Create widget
        self.label = QLabel(self)
        self.label.move(0,160)
        self.label.resize(640,800)
        
        
        self.show()
        
    def save(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Image Files (*.png)", options=options)
        if fileName:
            print(fileName)
            shutil.move('crossword.tmp', fileName+'.png')
            shutil.move('crossword_solved.tmp', fileName+'_solved.png')
            shutil.move('clue.txt', fileName+'_questions.txt')
        
                
        
    @pyqtSlot()
    def on_click(self):
        self.openFileNameDialog()
        
    @pyqtSlot()
    def on_click2(self):
        self.save()
 
    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"CROSSWROD FILE", "","All Files (*);;Crosswords (*.cwf)", options=options)
        if fileName:
            print(fileName)
            subprocess.call("python crossword.py  --print-clues --create-image -o crossword.tmp --solved "+fileName, shell=True)
            self.label.setPixmap(QPixmap('crossword.tmp').scaled(800, 800, QtCore.Qt.KeepAspectRatio))
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())