from PyQt5 import QtCore, QtGui, QtWidgets

from testpyqt import Ui_MainWindow

class MyMainWindow(QtGui.QWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

    def keyPressEvent(self, event):
        # implement the method here
        self.Max.setText(self.label.text() + 'a')





if __name__ == '__main__':
    app = QtGui.QGuiApplication([])
    win = MyMainWindow()
    win.show()
    app.exec_()        