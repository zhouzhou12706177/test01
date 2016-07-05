import sys
from PyQt4 import QtGui,QtCore

class windowTest(QtGui.QDialog):
    def __init__(self):
        super(windowTest,self).__init__(parent=None)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("haha")
        self.setLayout(QtGui.QVBoxLayout())

        textLa=QtGui.QLabel()
        textLa.setText('%s'%self.layout())
        
        
        self.layout().addWidget(textLa)
        
        self.te=QtGui.QTextEdit()
        
        self.layout().addWidget(self.te)
        
        self.button=QtGui.QPushButton("set label")
        self.button.setStyleSheet("background-color:red;text-align:left;")
        self.button.setFixedWidth(180)
        self.button.clicked.connect(self.on_button)
        
        self.layout().addWidget(self.button)
        
        self.frame=QtGui.QWidget()
        self.frame.setLayout(QtGui.QVBoxLayout())
        first_line=QtGui.QFrame()
        first_line.setFrameStyle(QtGui.QFrame.HLine|QtGui.QFrame.Plain)
        #frame.setLineWidth(20)
        #frame.setFixedHeight(100)
        first_line.setStyleSheet("background-color:red;border-bottom:1px solid rgba(0,255,0,255);")
        self.frame.layout().addWidget(first_line)
        self.frame.layout().setContentsMargins(0,0,0,0)
        
        self.layout().addWidget(self.frame)
        
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        
    def on_button(self):
        print "hello"
        self.setWindowTitle(self.te.toPlainText())

app=QtGui.QApplication(sys.argv) 

win=windowTest()
win.show()
app.exec_()