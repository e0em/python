import sys
from pyqt4 import QtGui
app = QtGui.QApplication(sys.argv)
w = QtGui.QWidget()
w.resize(250,150)
w.move(300,300)
w.setWindowTitle('My 1st GUI App!')
w.show()
status = app.exec_()
sys.exit(status)
