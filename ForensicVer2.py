# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Anaconda3\ForensicWelcome2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWebEngineWidgets
import cardcredit as cc


filenameCSV=None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 604)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(260, 170, 141, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(300, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(260, 90, 131, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(260, 60, 231, 20))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(280, 30, 101, 20))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(260, 220, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 130, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.browse_button = QtWidgets.QPushButton(self.tab)
        self.browse_button.setGeometry(QtCore.QRect(470, 40, 75, 23))
        self.browse_button.setObjectName("browse_button")
        self.file_path_line = QtWidgets.QLineEdit(self.tab)
        self.file_path_line.setGeometry(QtCore.QRect(230, 40, 211, 20))
        self.file_path_line.setObjectName("file_path_line")
        self.lbl_examine = QtWidgets.QLabel(self.tab)
        self.lbl_examine.setGeometry(QtCore.QRect(290, 10, 101, 16))
        self.lbl_examine.setObjectName("lbl_examine")
        self.Submit_btn = QtWidgets.QPushButton(self.tab)
        self.Submit_btn.setGeometry(QtCore.QRect(300, 200, 75, 23))
        self.Submit_btn.setObjectName("Submit_btn")
        self.Save_to_csv = QtWidgets.QPushButton(self.tab)
        self.Save_to_csv.setGeometry(QtCore.QRect(580, 490, 75, 23))
        self.Save_to_csv.setObjectName("Save_to_csv")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(390, 80, 81, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(230, 80, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_3.setGeometry(QtCore.QRect(230, 110, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_4.setGeometry(QtCore.QRect(250, 170, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(350, 170, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(80, 230, 531, 261))
        self.textBrowser.setObjectName("textBrowser")
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_5.setGeometry(QtCore.QRect(390, 110, 70, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_6.setGeometry(QtCore.QRect(390, 140, 70, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_7.setGeometry(QtCore.QRect(230, 140, 111, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        
#--------------------------------------------------------------------------      
        self.browseCSVbtn= QtWidgets.QPushButton(self.tab_3)
        self.browseCSVbtn.setGeometry(QtCore.QRect(400, 70, 75, 23))
        self.browseCSVbtn.setObjectName("browseCSVbtn")
        self.browseCSVbtn.clicked.connect(self.on_browseCSV)
        
        self.btn_ShowReport = QtWidgets.QPushButton(self.tab_3)
        self.btn_ShowReport.setGeometry(QtCore.QRect(260, 110, 75, 23))
        self.btn_ShowReport.setObjectName("btn_ShowReport")
        self.btn_ShowReport.clicked.connect(self.displayChart)
        
        self.file_path_line_2 = QtWidgets.QLineEdit(self.tab_3)
        self.file_path_line_2.setGeometry(QtCore.QRect(170, 70, 211, 20))
        self.file_path_line_2.setObjectName("file_path_line_2")
        
        
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 140, 671, 401))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tab_3, "")
        
       
#-----------------------------------------------------------------------        
        
        
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.tab_4)
        self.webEngineView.setGeometry(QtCore.QRect(30, 190, 601, 341))
        local_url = QtCore.QUrl.fromLocalFile(r'C:\Users\User\Anaconda3\ForensicProject\index.html')
        self.webEngineView.load(local_url)
        self.webEngineView.setObjectName("webEngineView")
        
        

        self.lbl_Amazon = QtWidgets.QLabel(self.tab_4)
        self.lbl_Amazon.setGeometry(QtCore.QRect(200, 40, 251, 21))
        self.lbl_Amazon.setObjectName("lbl_Amazon")
       
        
        
#-----------------------------------------------------------------------                
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def on_browse(self):
       filename=QtWidgets.QFileDialog.getOpenFileName(None, 'Single File', '', '*.txt')
       print(filename)
       self.file_path_line.setText(filename[0])
       
       df = pd.DataFrame({'name': ['Raphael', 'Donatello'],

                   'mask': ['red', 'purple'],

                   'weapon': ['sai', 'bo staff']})
       df.to_csv('Test.txt',index=False) # saves the DataFrame to a text file
       self.dataframe_label.setText(df.to_string())
       
       
       
       
    def on_browseCSV(self):
         filenameCSV=QtWidgets.QFileDialog.getOpenFileName(None, 'Single File', '', '*.csv')
         self.file_path_line_2.setText(filenameCSV[0])
         
         #self.textBrowser_2.setText("test")
         #print("__________")
         #print(cc.fraudDetector.getfile()[0])
         
        
         
    def displayChart(self):
         filePath=self.file_path_line_2.text()
         getGraph=cc.fraudDetector.getfile(filePath)
         
         self.textBrowser_2.setText(getGraph[0])
         self.textBrowser_2.append(getGraph[1])
         self.textBrowser_2.append('<img src="%s" />' %getGraph[2])
         self.textBrowser_2.append('<img src="%s" />' %getGraph[3])
         
         
    def enterWeb(self):
        websiteURL=self.WebsiteLine.text()
        #self.webEngineView.setUrl(QtCore.QUrl(websiteURL))
        
       
        local_url = QtCore.QUrl.fromLocalFile(r'C:\Users\User\Anaconda3\ForensicProject\index.html')
        self.webEngineView.load(local_url)
        
         
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Select from Existing Cases"))
        self.pushButton.setText(_translate("MainWindow", "Ok"))
        self.label_3.setText(_translate("MainWindow", "Enter the name of the case"))
        self.label.setText(_translate("MainWindow", "Create New Case"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Tom"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Dick"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Harry"))
        self.pushButton_2.setText(_translate("MainWindow", "Create Case"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.browse_button.setText(_translate("MainWindow", "Browse...."))
        self.lbl_examine.setText(_translate("MainWindow", "Examine PCAP"))
        self.Submit_btn.setText(_translate("MainWindow", "Submit"))
        self.Save_to_csv.setText(_translate("MainWindow", "Save to CSV"))
        self.checkBox.setText(_translate("MainWindow", "Destination"))
        self.checkBox_2.setText(_translate("MainWindow", "Source"))
        self.checkBox_3.setText(_translate("MainWindow", "Src Port"))
        self.checkBox_4.setText(_translate("MainWindow", "Set Limit..."))
        self.checkBox_5.setText(_translate("MainWindow", "Dst Port"))
        self.checkBox_6.setText(_translate("MainWindow", "Flow"))
        self.checkBox_7.setText(_translate("MainWindow", "Unique DNS Lookup"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Pcap Analyse"))
        self.browseCSVbtn.setText(_translate("MainWindow", "Browse..."))
        self.btn_ShowReport.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Fraud Detection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Website "))
        self.lbl_Amazon.setText(_translate("MainWindow", "Amazon Credit Card Face Recognition"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

