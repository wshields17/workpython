from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog,QTableWidgetItem
import openpyxl
from optioncalc import Ui_MainWindow  # importing our generated file
import py_vollib.black_scholes_merton.implied_volatility as BSvol
import py_vollib.black_scholes_merton.greeks.analytical as BSgreeks
import sys

def multtex(tex1,tex2):
    return str((float(tex1)* float(tex2)))


       

class mywindow(QtWidgets.QMainWindow):

   def __init__(self):

      super(mywindow, self).__init__()

      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)
      self.ui.OutWeight_5.setText("0") 
      self.ui.OutWeight_2.setText("0.02")
      self.ui.OutWeight_4.setText("c")
      #self.ui.Percentage.setText(".85") 

      self.ui.Compbutton.clicked.connect(self.btnClicked)
      self.ui.actionExit.triggered.connect(self.testf)
      self.ui.actionOpen.triggered.connect(self.fd)
      #self.ui.table1.setColumnCount(4)
        
      #self.ui.table1.setRowCount(40)

      #self.ui.actionExit()=sys.exit(app.exec())

   def testf(self):
       
      sys.exit()   

   def fd(self):
      options = QFileDialog.Options()
      options |= QFileDialog.DontUseNativeDialog
      fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","Excel Files (*.xlsx)", options=options)
     
      wb = openpyxl.load_workbook(fileName)
      sheet = wb.active
      for i in range (3,20):
         for j in range(2,5 ):   
             cellinfo = str(sheet.cell(row=i, column=j).value ) 
             curcell = QTableWidgetItem(cellinfo)
             self.ui.OutWeight.setText(cellinfo) 
     
             self.ui.table1.setItem(i,j-1,curcell)
      

   def btnClicked(self):
      
      price = float(self.ui.Max.toPlainText()) 
      strike = float(self.ui.Percentage.toPlainText())
      days = float(self.ui.OutWeight.toPlainText())/365
      rate =  float(self.ui.OutWeight_2.toPlainText())
      cp = (self.ui.OutWeight_4.toPlainText()) 
      yield1 = float(self.ui.OutWeight_5.toPlainText()) 
      optprice = float(self.ui.OutWeight_6.toPlainText()) 
      vol = str(round(BSvol.implied_volatility(optprice,price , strike, days, rate,yield1, cp),3))
      self.ui.OutWeight_3.setText(vol) 

app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())
