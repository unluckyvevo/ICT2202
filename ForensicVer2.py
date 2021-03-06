# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Anaconda3\ForensicWelcome2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWebEngineWidgets
import cardcredit as cc
import pcap as pc
import boto3
import json
import ipaddress
fDec = boto3.client('frauddetector')

filenameCSV=None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        font = QtGui.QFont()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 604)
        MainWindow.setStyleSheet("background-color:rgb(60, 110, 113)")
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
        self.lbl_IPAddress = QtWidgets.QLabel(self.tab_2)
        self.lbl_IPAddress.setGeometry(QtCore.QRect(30, 210, 81, 20))
        self.lbl_IPAddress.setObjectName("lbl_IPAddress")
        self.lbl_PhoneNumber = QtWidgets.QLabel(self.tab_2)
        self.lbl_PhoneNumber.setGeometry(QtCore.QRect(30, 260, 81, 20))
        self.lbl_PhoneNumber.setObjectName("lbl_PhoneNumber")
        self.lbl_UserAgent = QtWidgets.QLabel(self.tab_2)
        self.lbl_UserAgent.setGeometry(QtCore.QRect(30, 310, 81, 20))
        self.lbl_UserAgent.setObjectName("lbl_UserAgent")
        
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
        
        self.lbl_FraudScore = QtWidgets.QLabel(self.tab_2)
        self.lbl_FraudScore.setGeometry(QtCore.QRect(40, 440, 151, 16))
        self.lbl_FraudScore.setObjectName("lbl_FraudScore")
        
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        
        
        
 #Page 2       
 #--------------------------------------------------------------------------            
        self.browse_button = QtWidgets.QPushButton(self.tab)
        self.browse_button.setGeometry(QtCore.QRect(510, 30, 75, 23))
        self.browse_button.setObjectName("browse_button")
        self.browse_button.clicked.connect(self.pcapFilePath)
        
        self.file_path_line = QtWidgets.QLineEdit(self.tab)
        self.file_path_line.setGeometry(QtCore.QRect(280, 30, 211, 20))
        self.file_path_line.setObjectName("file_path_line")
        
        self.lbl_examine = QtWidgets.QLabel(self.tab)
        self.lbl_examine.setGeometry(QtCore.QRect(330, 0, 121, 21))
        
        font.setFamily("Garamond")
        font.setPointSize(12)
        self.lbl_examine.setFont(font)
        self.lbl_examine.setObjectName("lbl_examine")
        
        self.Submit_btn = QtWidgets.QPushButton(self.tab)
        self.Submit_btn.setGeometry(QtCore.QRect(350, 200, 75, 23))
        self.Submit_btn.setObjectName("Submit_btn")
        self.Submit_btn.clicked.connect(self.submitPCAP)
        
        
        self.lbl_Destination = QtWidgets.QLabel(self.tab)
        self.lbl_Destination.setGeometry(QtCore.QRect(430, 80, 101, 16))
        
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self.lbl_Destination.setFont(font)
        self.lbl_Destination.setObjectName("lbl_Destination")
        
        self.lbl_Source = QtWidgets.QLabel(self.tab)
        self.lbl_Source.setGeometry(QtCore.QRect(250, 80, 61, 16))
        
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        self.lbl_Source.setFont(font)
        self.lbl_Source.setObjectName("lbl_Source")
        
        self.checkBox_SinglePkt = QtWidgets.QCheckBox(self.tab)
        self.checkBox_SinglePkt.setGeometry(QtCore.QRect(260, 130, 131, 17))
        self.checkBox_SinglePkt.setObjectName("checkBox_SinglePkt")
        
        self.textBrowser_PCAP = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_PCAP.setGeometry(QtCore.QRect(0, 230, 791, 291))
        self.textBrowser_PCAP.setObjectName("textBrowser_PCAP")
        
        self.lineEdit_singlePacketNo = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_singlePacketNo.setGeometry(QtCore.QRect(380, 130, 71, 16))
        self.lineEdit_singlePacketNo.setObjectName("lineEdit_singlePacketNo")
        
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(7, 110, 1111, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_4.setGeometry(QtCore.QRect(310, 50, 201, 17))
        font.setFamily("Garamond")
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        
        self.lineEdit_SourceIP = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_SourceIP.setGeometry(QtCore.QRect(320, 80, 91, 20))
        self.lineEdit_SourceIP.setObjectName("lineEdit_SourceIP")
        
        self.lineEdit_DestIP = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_DestIP.setGeometry(QtCore.QRect(530, 80, 71, 20))
        self.lineEdit_DestIP.setObjectName("lineEdit_DestIP")
        
        self.label_IsVerbose = QtWidgets.QLabel(self.tab)
        self.label_IsVerbose.setGeometry(QtCore.QRect(170, 160, 81, 20))
        font.setFamily("Century Gothic")
        self.label_IsVerbose.setFont(font)
        self.label_IsVerbose.setObjectName("label_IsVerbose")
        
        self.radioButton_Yes = QtWidgets.QRadioButton(self.tab)
        self.radioButton_Yes.setGeometry(QtCore.QRect(300, 160, 82, 17))
        self.radioButton_Yes.setObjectName("radioButton_Yes")
        self.radioButton_Yes.setChecked(True)
        
        self.radioButton_No = QtWidgets.QRadioButton(self.tab)
        self.radioButton_No.setGeometry(QtCore.QRect(430, 160, 82, 17))
        self.radioButton_No.setObjectName("radioButton_No")
        
        self.radioButton_raw = QtWidgets.QRadioButton(self.tab)
        self.radioButton_raw.setGeometry(QtCore.QRect(510, 160, 82, 17))
        self.radioButton_raw.setObjectName("radioButton_raw")
        
        self.checkBox_SrcDest = QtWidgets.QCheckBox(self.tab)
        self.checkBox_SrcDest.setGeometry(QtCore.QRect(100, 80, 141, 20))
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.checkBox_SrcDest.setFont(font)
        self.checkBox_SrcDest.setObjectName("checkBox_SrcDest")
        
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
        
        self.lblCreditCardFraudGeneric = QtWidgets.QLabel(self.tab_3)
        self.lblCreditCardFraudGeneric.setGeometry(QtCore.QRect(110, 20, 421, 20))
        font.setFamily("Bodoni MT Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblCreditCardFraudGeneric.setFont(font)
        self.lblCreditCardFraudGeneric.setObjectName("lblCreditCardFraudGeneric")
        
        
        self.file_path_line_2 = QtWidgets.QLineEdit(self.tab_3)
        self.file_path_line_2.setGeometry(QtCore.QRect(170, 70, 211, 20))
        self.file_path_line_2.setObjectName("file_path_line_2")
        
        
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 140, 781, 401))
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
        self.lbl_Amazon.setGeometry(QtCore.QRect(30, 10, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_Amazon.setFont(font)
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
    
    def pcapFilePath(self):
        pcap_path=QtWidgets.QFileDialog.getOpenFileName(None, 'Single File', '', '*.pcap')
        self.file_path_line.setText(pcap_path[0])
  
    def is_ipv4(string):
        try:
            ipaddress.IPv4Network(string)
            return True
        except ValueError:
            return False
    
    def submitPCAP(self):
        summary=0
        pOption=0
        pOption2=0
        sIP=dIP=0
        cbx_SD=0
        
        
        if(self.checkBox_4.isChecked()):
            summary=1
       
        
        if(self.checkBox_SinglePkt.isChecked()):
            pOption=1
            if(self.radioButton_Yes.isChecked()):
                pOption2=0
            elif(self.radioButton_No.isChecked()):
                pOption2=1
            else:
                pOption2=2
       
        #10.0.2.15
        if(self.checkBox_SrcDest.isChecked()):
            cbx_SD=1
            tempSrc=self.lineEdit_SourceIP.text()
            
            print(self.lineEdit_SourceIP.text())
            if((Ui_MainWindow.is_ipv4(tempSrc)) is False):
                sIP=0
            else:
                sIP=self.lineEdit_SourceIP.text()
                
            if((Ui_MainWindow.is_ipv4(self.lineEdit_DestIP.text())) is False):
                dIP=0
            else:
                dIP=self.lineEdit_DestIP.text()
        else:
             cbx_SD=0
            
   
        test=pc.Pkts.getPCAPInfo(self.file_path_line.text(),summary,pOption,pOption2,
                                 self.lineEdit_singlePacketNo.text(),cbx_SD,sIP,dIP)
        
      
        
        for i in range(0,len(test)):
             self.textBrowser_PCAP.append(str(test[i]))
     
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
         
         for x in range(2,len(getGraph)):
             if(x==4 or x==7 or x==20 or x==23 or x==27 or x==28 or x==32 or x==33 ):
                 self.textBrowser_2.append('<img src="%s" />' %getGraph[x])
                 
             else:
                 self.textBrowser_2.append(getGraph[x])
             #self.textBrowser_2.append('<img src="%s" />' %getGraph[3])
         #self.textBrowser_2.append(getGraph[(len(getGraph)-1)])
         
         
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
         contents=f.read()
         contents = contents.replace("'", '"')
         with open('result.json', 'w') as file:
             file.write(contents)
         
         
         with open('result.json') as f:
             data = json.load(f)
        
         for modelScores in data["modelScores"]:
             diction=modelScores.get('scores')

         for key, value in diction.items():
            vl=value
         self.lbl_FraudScore.setText("Fraud Score: "+str(vl))
        
                 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_Address.setText(_translate("MainWindow", "Address:"))
        self.btn_CheckscamScore.setText(_translate("MainWindow", "Submit"))
        self.lbl_Postal.setText(_translate("MainWindow", "Postal:"))
        self.lbl_State.setText(_translate("MainWindow", "State:"))
        self.lbl_Email.setText(_translate("MainWindow", "Email:"))
        self.lbl_IPAddress.setText(_translate("MainWindow", "IP Address"))
        self.lbl_PhoneNumber.setText(_translate("MainWindow", "Phone number"))
        self.lbl_UserAgent.setText(_translate("MainWindow", "User agent"))
        self.lbl_FraudScore.setText(_translate("MainWindow", "Fraud Score:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Contact Fraud Detector"))
        self.browse_button.setText(_translate("MainWindow", "Browse...."))
        self.lbl_examine.setText(_translate("MainWindow", "Examine PCAP"))
        self.Submit_btn.setText(_translate("MainWindow", "Submit"))
        self.lbl_Destination.setText(_translate("MainWindow", "Destination:"))
        self.lbl_Source.setText(_translate("MainWindow", "Source"))
        self.checkBox_SinglePkt.setText(_translate("MainWindow", "Show a single packet"))
        self.checkBox_4.setText(_translate("MainWindow", "Show PCAP Summary"))
        self.label_IsVerbose.setText(_translate("MainWindow", "Is Verbose?"))
        self.radioButton_Yes.setText(_translate("MainWindow", "Yes"))
        self.radioButton_No.setText(_translate("MainWindow", "No"))
        self.checkBox_SrcDest.setText(_translate("MainWindow", "Enable Search ip via"))
        self.radioButton_raw.setText(_translate("MainWindow", "Raw"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Pcap Analyse"))
        self.browseCSVbtn.setText(_translate("MainWindow", "Browse..."))
        self.btn_ShowReport.setText(_translate("MainWindow", "Submit"))
        self.lblCreditCardFraudGeneric.setText(_translate("MainWindow", "Credit Card Fraud Detector"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Credit Card Fraud Detection"))
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

