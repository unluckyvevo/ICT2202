# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Anaconda3\ForensicWelcome2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWebEngineWidgets
import cardcredit as cc
import boto3
import json
fDec = boto3.client('frauddetector')

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
        self.lbl_Address = QtWidgets.QLabel(self.tab_2)
        self.lbl_Address.setGeometry(QtCore.QRect(30, 30, 81, 20))
        self.lbl_Address.setObjectName("lbl_Address")
        self.btn_CheckscamScore = QtWidgets.QPushButton(self.tab_2)
        self.btn_CheckscamScore.setGeometry(QtCore.QRect(270, 370, 75, 23))
        self.btn_CheckscamScore.setObjectName("btn_CheckscamScore")
        self.btn_CheckscamScore.clicked.connect(self.sentScamCheck)
        self.lineEdit_Address = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_Address.setGeometry(QtCore.QRect(140, 30, 131, 20))
        self.lineEdit_Address.setObjectName("lineEdit_Address")
        self.lbl_Postal = QtWidgets.QLabel(self.tab_2)
        self.lbl_Postal.setGeometry(QtCore.QRect(30, 80, 81, 20))
        self.lbl_Postal.setObjectName("lbl_Postal")
        self.lbl_State = QtWidgets.QLabel(self.tab_2)
        self.lbl_State.setGeometry(QtCore.QRect(30, 120, 81, 20))
        self.lbl_State.setObjectName("lbl_State")
        self.lbl_Email = QtWidgets.QLabel(self.tab_2)
        self.lbl_Email.setGeometry(QtCore.QRect(30, 160, 81, 20))
        self.lbl_Email.setObjectName("lbl_Email")
        self.lbl_Email_2 = QtWidgets.QLabel(self.tab_2)
        self.lbl_Email_2.setGeometry(QtCore.QRect(30, 210, 81, 20))
        self.lbl_Email_2.setObjectName("lbl_Email_2")
        self.lbl_Email_3 = QtWidgets.QLabel(self.tab_2)
        self.lbl_Email_3.setGeometry(QtCore.QRect(30, 260, 81, 20))
        self.lbl_Email_3.setObjectName("lbl_Email_3")
        self.lbl_Email_4 = QtWidgets.QLabel(self.tab_2)
        self.lbl_Email_4.setGeometry(QtCore.QRect(30, 310, 81, 20))
        self.lbl_Email_4.setObjectName("lbl_Email_4")
        self.lineEdit_Postal = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_Postal.setGeometry(QtCore.QRect(140, 80, 131, 20))
        self.lineEdit_Postal.setObjectName("lineEdit_Postal")
        self.lineEdit_State = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_State.setGeometry(QtCore.QRect(140, 120, 131, 20))
        self.lineEdit_State.setObjectName("lineEdit_State")
        self.lineEdit_Email = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_Email.setGeometry(QtCore.QRect(140, 160, 131, 20))
        self.lineEdit_Email.setObjectName("lineEdit_Email")
        self.lineEdit_IP_Address = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_IP_Address.setGeometry(QtCore.QRect(140, 210, 131, 20))
        self.lineEdit_IP_Address.setObjectName("lineEdit_IP_Address")
        self.lineEdit_PhoneNumber = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_PhoneNumber.setGeometry(QtCore.QRect(140, 260, 131, 20))
        self.lineEdit_PhoneNumber.setObjectName("lineEdit_PhoneNumber")
        self.lineEdit_UserAgent = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_UserAgent.setGeometry(QtCore.QRect(140, 310, 131, 20))
        self.lineEdit_UserAgent.setObjectName("lineEdit_UserAgent")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        
        
        
 #Page 2       
 #--------------------------------------------------------------------------            
        self.browse_button = QtWidgets.QPushButton(self.tab)
        self.browse_button.setGeometry(QtCore.QRect(510, 40, 75, 23))
        self.browse_button.setObjectName("browse_button")
        self.file_path_line = QtWidgets.QLineEdit(self.tab)
        self.file_path_line.setGeometry(QtCore.QRect(280, 40, 211, 20))
        self.file_path_line.setObjectName("file_path_line")
        self.lbl_examine = QtWidgets.QLabel(self.tab)
        self.lbl_examine.setGeometry(QtCore.QRect(330, 10, 101, 16))
        self.lbl_examine.setObjectName("lbl_examine")
        self.Submit_btn = QtWidgets.QPushButton(self.tab)
        self.Submit_btn.setGeometry(QtCore.QRect(350, 200, 75, 23))
        self.Submit_btn.setObjectName("Submit_btn")
        self.Save_to_csv = QtWidgets.QPushButton(self.tab)
        self.Save_to_csv.setGeometry(QtCore.QRect(580, 520, 75, 23))
        self.Save_to_csv.setObjectName("Save_to_csv")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(460, 90, 81, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(260, 90, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_3.setGeometry(QtCore.QRect(260, 120, 131, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(0, 230, 791, 291))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(390, 120, 41, 16))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(7, 110, 1111, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_4.setGeometry(QtCore.QRect(310, 60, 201, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 90, 51, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(540, 90, 51, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(190, 140, 61, 16))
        self.label_4.setObjectName("label_4")
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setGeometry(QtCore.QRect(300, 140, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_2.setGeometry(QtCore.QRect(430, 140, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.tabWidget.addTab(self.tab, "")
        
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
#Page3     
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
        self.textBrowser_2.document().setDefaultFont(QtGui.QFont('Fonospace'))
        
#Page4       
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
         self.textBrowser_2.append(getGraph[2])
         for x in range(3,len(getGraph)):
             self.textBrowser_2.append('<img src="%s" />' %getGraph[x])
             #self.textBrowser_2.append('<img src="%s" />' %getGraph[3])
         
         
    def sentScamCheck(self):
         result = fDec.get_event_prediction(
            detectorId='sample_detector',
            detectorVersionId='1',
            eventId='string',
            eventTypeName='sample_registration',
            entities=[
                {
                    'entityType': 'sample_customer',
                    'entityId': 'unknown'
                },
            ],
            eventTimestamp='2020-10-01T00:00:00Z',
            eventVariables={
                'billing_address': str(self.lineEdit_Address.text()),
                'billing_postal': str(self.lineEdit_Postal.text()),
                'billing_state': str(self.lineEdit_State.text()),
                'email_address': str(self.lineEdit_Email.text()),
                'ip_address': str(self.lineEdit_IP_Address.text()),
                'phone_number': str(self.lineEdit_PhoneNumber.text()),
                'user_agent': str(self.lineEdit_UserAgent.text()),
            },
            externalModelEndpointDataBlobs={
                'string': {
                    'byteBuffer':'bytes',
                    'contentType': 'string'
                }
            }
        )
         print(result)
         
         with open('result.json', 'w') as f:
            print(result, file=f)
         f = open("result.json", "r")
         
         f = f.replace("'", '"')
         jsonList = json.load(f)
         faggot=jsonList['scores']
         print(faggot)
        
        
         
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_Address.setText(_translate("MainWindow", "Address:"))
        self.btn_CheckscamScore.setText(_translate("MainWindow", "Submit"))
        self.lbl_Postal.setText(_translate("MainWindow", "Postal:"))
        self.lbl_State.setText(_translate("MainWindow", "State:"))
        self.lbl_Email.setText(_translate("MainWindow", "Email:"))
        self.lbl_Email_2.setText(_translate("MainWindow", "IP Address"))
        self.lbl_Email_3.setText(_translate("MainWindow", "Phone number"))
        self.lbl_Email_4.setText(_translate("MainWindow", "User agent"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.browse_button.setText(_translate("MainWindow", "Browse...."))
        self.lbl_examine.setText(_translate("MainWindow", "Examine PCAP"))
        self.Submit_btn.setText(_translate("MainWindow", "Submit"))
        self.Save_to_csv.setText(_translate("MainWindow", "Save to CSV"))
        self.checkBox.setText(_translate("MainWindow", "Destination"))
        self.checkBox_2.setText(_translate("MainWindow", "Source"))
        self.checkBox_3.setText(_translate("MainWindow", "Show a single packet"))
        self.checkBox_4.setText(_translate("MainWindow", "Show PCP Summary"))
        self.label_4.setText(_translate("MainWindow", "Is Verbose?"))
        self.radioButton.setText(_translate("MainWindow", "Yes"))
        self.radioButton_2.setText(_translate("MainWindow", "No"))
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

