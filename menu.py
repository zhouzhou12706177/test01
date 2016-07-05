#!coding = utf-8
import sys
from PyQt4 import QtGui,QtCore



class windowTest(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(windowTest,self).__init__(parent)
        self.setWindowTitle("menubar and toolbar")

        file = self.menuBar().addMenu('file')


        self.setFixedHeight(600)
        self.setFixedWidth(600)





app=QtGui.QApplication(sys.argv)
win=windowTest()
win.show()
app.exec_()