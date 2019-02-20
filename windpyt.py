from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog,QTableWidgetItem
import openpyxl
from testpyqt2 import Ui_MainWindow  # importing our generated file

import sys

def multtex(tex1,tex2):
    return str((float(tex1)* float(tex2)))


       

class mywindow(QtWidgets.QMainWindow):

   def __init__(self):

      super(mywindow, self).__init__()

      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)
      self.ui.Max.setText("300") 
      self.ui.Percentage.setText(".85") 

      self.ui.Compbutton.clicked.connect(self.btnClicked)
      self.ui.actionExit.triggered.connect(self.testf)
      self.ui.actionOpen.triggered.connect(self.fd)
      self.ui.table1.setColumnCount(7)
        
      self.ui.table1.setRowCount(30)

      #self.ui.actionExit()=sys.exit(app.exec())

   def testf(self):
       
      sys.exit()   

   def fd(self):
      options = QFileDialog.Options()
      options |= QFileDialog.DontUseNativeDialog
      fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Excel Files (*.xlsx)", options=options)
     
      wb = openpyxl.load_workbook(fileName)
      sheet = wb.active
      for i in range (1,25):
         for j in range(2,8,2 ):   
             cellinfo = str(sheet.cell(row=i, column=j).value ) 
             if cellinfo == 'None':
                 cellinfo = ' '
             curcell = QTableWidgetItem(cellinfo)
             self.ui.OutWeight.setText(cellinfo) 
     
             self.ui.table1.setItem(i,j-1,curcell)
      

   def btnClicked(self):
      
      tex1 = self.ui.Max.toPlainText() 
      tex2 = self.ui.Percentage.toPlainText()   
      self.ui.OutWeight.setText(multtex(tex1,tex2)) 
      

app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())
