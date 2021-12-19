# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import face_recognition
from simple_facerec import SimpleFacerec
import cv2
import os
import time
import pandas as pd
from threading import Thread
import numpy as np
import gc
import pika
import serial

gc.enable()

# Load face detector
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

class Ui_Attendance(QWidget):
    def setupUi(self, Attendance):

        # controll the tab
        self.Attendance = Attendance

        # capture
        self.capture = None

        # staff name
        self.displayName = None
        self.staffName = None

        # check tab 1 enable
        self.isTab1Enable = False

        # admin password
        self.adminPass = "12345"

        # check open or lock btn status
        self.isOpenCl = False
        self.isLockCl = False

        Attendance.setObjectName("Attendance")
        Attendance.resize(921, 543)
        Attendance.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Attendance.setAcceptDrops(False)
        Attendance.setIconSize(QtCore.QSize(16, 16))
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.imgLabel = QtWidgets.QLabel(self.tab_1)
        self.imgLabel.setGeometry(QtCore.QRect(20, 30, 581, 451))
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(630, 200, 261, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.nameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout.addWidget(self.nameLabel)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.previewImgLabel1 = QtWidgets.QLabel(self.tab_1)
        self.previewImgLabel1.setGeometry(QtCore.QRect(640, 260, 241, 231))
        self.previewImgLabel1.setText("")
        self.previewImgLabel1.setObjectName("previewImgLabel1")
        self.btnOpen = QtWidgets.QPushButton(self.tab_1)
        self.btnOpen.setGeometry(QtCore.QRect(630, 30, 261, 51))
        self.btnOpen.setObjectName("btnOpen")
        self.btnLock = QtWidgets.QPushButton(self.tab_1)
        self.btnLock.setGeometry(QtCore.QRect(630, 90, 261, 51))
        self.btnLock.setObjectName("btnLock")
        Attendance.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.imgLabel2 = QtWidgets.QLabel(self.tab_2)
        self.imgLabel2.setGeometry(QtCore.QRect(20, 30, 611, 451))
        self.imgLabel2.setText("")
        self.imgLabel2.setObjectName("imgLabel2")
        self.btnAddName = QtWidgets.QPushButton(self.tab_2)
        self.btnAddName.setGeometry(QtCore.QRect(660, 30, 241, 51))
        self.btnAddName.setObjectName("btnAddName")
        self.btnCapture = QtWidgets.QPushButton(self.tab_2)
        self.btnCapture.setGeometry(QtCore.QRect(660, 90, 241, 51))
        self.btnCapture.setObjectName("btnCapture")
        self.previewImgLabel2 = QtWidgets.QLabel(self.tab_2)
        self.previewImgLabel2.setGeometry(QtCore.QRect(670, 280, 221, 201))
        self.previewImgLabel2.setText("")
        self.previewImgLabel2.setObjectName("previewImgLabel2")
        self.name = QtWidgets.QLineEdit(self.tab_2)
        self.name.setGeometry(QtCore.QRect(660, 150, 241, 41))
        self.name.setText("")
        self.name.setObjectName("name")
        self.dplName = QtWidgets.QLineEdit(self.tab_2)
        self.dplName.setGeometry(QtCore.QRect(660, 200, 241, 41))
        self.dplName.setText("")
        self.dplName.setObjectName("dplName")
        Attendance.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.btnDel = QtWidgets.QPushButton(self.tab_3)
        self.btnDel.setGeometry(QtCore.QRect(650, 20, 241, 51))
        self.btnDel.setObjectName("btnDel")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(20, 80, 601, 410))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.btnChangePass = QtWidgets.QPushButton(self.tab_3)
        self.btnChangePass.setGeometry(QtCore.QRect(650, 90, 241, 51))
        self.btnChangePass.setObjectName("btnChangePass")
        self.nameSearch = QtWidgets.QLineEdit(self.tab_3)
        self.nameSearch.setGeometry(QtCore.QRect(20, 20, 291, 41))
        self.nameSearch.setObjectName("nameSearch")
        self.btnSearch = QtWidgets.QPushButton(self.tab_3)
        self.btnSearch.setGeometry(QtCore.QRect(480, 20, 141, 41))
        self.btnSearch.setObjectName("btnSearch")
        Attendance.addTab(self.tab_3, "")

        self.retranslateUi(Attendance)
        Attendance.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Attendance)

    def retranslateUi(self, Attendance):
        _translate = QtCore.QCoreApplication.translate
        Attendance.setWindowTitle(_translate("Attendance", "Attendance"))
        self.label_3.setText(_translate("Attendance", "Tên"))
        self.nameLabel.setText(_translate("Attendance", "Unknown"))
        self.btnOpen.setText(_translate("Attendance", "Mở cửa"))
        self.btnLock.setText(_translate("Attendance", "Đóng cửa"))
        Attendance.setTabText(Attendance.indexOf(self.tab_1), _translate("Attendance", "Trang chính"))
        self.btnAddName.setText(_translate("Attendance", "Thêm thành viên"))
        self.btnCapture.setText(_translate("Attendance", "Chụp ảnh"))
        self.name.setPlaceholderText(_translate("Attendance", "Tên thành viên"))
        self.dplName.setPlaceholderText(_translate("Attendance", "Tên hiển thị, viết liền không dấu"))
        Attendance.setTabText(Attendance.indexOf(self.tab_2), _translate("Attendance", "Thêm thành viên"))
        self.btnDel.setText(_translate("Attendance", "Xóa người sử dụng"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Attendance", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Attendance", "DISPLAY NAME"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Attendance", "NAME"))
        self.btnChangePass.setText(_translate("Attendance", "Đổi mật khẩu Admin"))
        self.nameSearch.setPlaceholderText(_translate("Attendance", "Tên thành viên"))
        self.btnSearch.setText(_translate("Attendance", "Tìm"))
        Attendance.setTabText(Attendance.indexOf(self.tab_3), _translate("Attendance", "Danh sách thành viên"))

        header = self.tableWidget.horizontalHeader()
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1,250)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        # Change tab
        Attendance.currentChanged.connect(self.tabChange)
        
        # worker xử lý việc chấm công
        self.Worker1 = Worker1(self)
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.imageUpdateSlot)

        #lock door
        self.btnLock.clicked.connect(self.lockDoor)

        #open door
        self.btnOpen.clicked.connect(self.openDoor)

        # add staff
        self.btnAddName.clicked.connect(self.addStaff)
        # capture image
        self.btnCapture.clicked.connect(self.captureImage)

        # get data of staff
        self.getNewData()

        # find employee
        self.btnSearch.clicked.connect(self.findData)

        # delete employee
        self.btnDel.clicked.connect(self.delEmployee)

    # update frame for attendance
    def imageUpdateSlot(self, Image):
        self.imgLabel.setPixmap(QPixmap.fromImage(Image))

    def imageUpdateSlot2(self, Image):
        self.imgLabel2.setPixmap(QPixmap.fromImage(Image))  

    def tabChange(self):
        index = self.Attendance.currentIndex()
        if(index == 1):
            self.isTab1Enable = True
            self.Worker1.ImageUpdate.connect(self.imageUpdateSlot2)
        else:
            if(self.isTab1Enable):
                self.isTab1Enable = False
                self.Worker1.ImageUpdate.disconnect(self.imageUpdateSlot2)

    def lockDoor(self):
        self.isLockCl = True

    def openDoor(self):
        self.isOpenCl = True

    # Thêm thông tin thành viên
    def addStaff(self):
        staffName = self.name.text()
        displayName = self.dplName.text()
        if staffName and displayName:
            self.staffName = staffName
            self.displayName = displayName
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Thêm nhân viên thành công bạn hãy chụp ảnh nhân viên")
            msg.setWindowTitle("Thông báo")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Tên nhân viên hoặc tên hiển thị chưa được nhập")
            msg.setWindowTitle("Cảnh báo")
            msg.exec_()

    # chụp ảnh
    def captureImage(self):
        (x,y,w,h) = self.Worker1.face_location
        flag, frame = self.capture.read()
        path = r'images'
        staffName = self.staffName
        displayName = self.displayName
        if flag:
            frame = frame[y:h, x:w]
            if displayName and staffName:
                name = self.displayName.upper() + ".png"
                img_path = os.path.join(path, name)
                cv2.imwrite(img_path, frame)
                writeThread = Thread(target=self.insertData, args=((staffName, displayName.upper()), ))
                writeThread.start()
                time.sleep(1)
                # update preview image
                pixmap = QPixmap(img_path)
                self.previewImgLabel2.setPixmap(pixmap)
                self.previewImgLabel2.setMask(pixmap.mask())
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Thêm nhân viên thành công")
                msg.setWindowTitle("Thành công")
                msg.exec_()
                sfr.add_new_face_encoding(img_path)
                # time.sleep(1)
                self.Attendance.setCurrentIndex(0)
                
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Bạn chưa nhập tên nhân viên")
                msg.setWindowTitle("Cảnh báo")
                msg.exec_()
        # update input text
        self.staffName = None
        self.displayName = None
        self.name.setText("")
        self.dplName.setText("")

        # update preview image
        pixmap = QPixmap(241, 231)
        pixmap.fill(QColor("white"))
        self.previewImgLabel2.setPixmap(pixmap)
        self.previewImgLabel2.setMask(pixmap.mask())
        self.getNewData()

    def insertData(self, args):
        (staffName, displayName) = args
        df = pd.read_csv('member.csv',usecols= ['ID','DISPLAY_NAME','NAME'])
        lastID = df.iloc[-1]['ID']
        lastID = int(lastID) + 1
        data = pd.DataFrame(np.array([(lastID, displayName, staffName)]))
        data.to_csv('member.csv', mode='a', header=False, index=False)

    def getData(self, employeeName):
        employeeName = str(employeeName).upper()
        data = pd.read_csv('member.csv')
        if employeeName != "":
            return data[data['DISPLAY_NAME'].str.contains(employeeName)]
        return data

    def displayData(self, data):
        numRow = 0
        if len(data) != 0:
            numRow = len(data)
        self.tableWidget.setRowCount(numRow)
        for i in range(numRow):
            for j in range(3):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(data.iat[i,j])))

    def findData(self):
        employeeName = self.nameSearch.text()
        data = self.getData(employeeName)
        self.displayData(data)

    def getNewData(self):
        data = self.getData("")
        self.displayData(data)

    def delEmployee(self):
        currentRow = self.tableWidget.currentRow()
        ID = self.tableWidget.item(currentRow, 0).text()
        password, ok = QInputDialog.getText(self,"Nhập password admin để xóa nhân viên", "PASSWORD")
        if ok:
            if password == "12345":
                self.tableWidget.removeRow(currentRow)
                delEmpThread = Thread(target=self.delEmpThread, args=((ID),))
                delEmpThread.start()

    def delEmpThread(self, args):
        (ID) = args
        ID = int(ID)
        df = pd.read_csv('member.csv')
        selectedRow = df.loc[df.ID == ID]
        displayName = selectedRow.iloc[0].DISPLAY_NAME
        imgPath = 'images/' + displayName + '.png'
        os.remove(imgPath)
        df = df.loc[df.ID != ID]
        df.to_csv('employee.csv', header=True, index=False)

# Thread chấm công 
class Worker1(QThread):

    ImageUpdate = pyqtSignal(QImage)

    def __init__(self, mainthread):
        super().__init__()
        self.mainthread = mainthread
        self.face_location = (0,0,0,0)
        self.port = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)

    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(-1)
        self.mainthread.capture = Capture
        while self.ThreadActive:
            ret, frame  = Capture.read()
            isDetected = self.detectFace(frame)
            if isDetected:
                if self.mainthread.isOpenCl:
                    self.port.flushInput()
                    # b"open" -> chuyển sang chuỗi bytes
                    self.port.write(b"open")
                    self.mainthread.isOpenCl = False
                if self.mainthread.isLockCl:
                    self.port.flushInput()
                    self.port.write(b"lock")
                    self.mainthread.isLockCl = False
            if(ret):
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Quay ngược lại nếu camera bị đảo ngược
                # FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)

    def stop(self):
        self.ThreadActive = False
        self.quit()
        self.channel.close()

    def detectFace(self, frame):
        face_locations, face_names = sfr.detect_known_faces(frame)
        if len(face_names) >= 1:
            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                # cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
                self.face_location = (x1, y1, x2, y2)
                
                # set name and time 
                self.mainthread.nameLabel.setText(name)

                # update preview image
                pixmap = QPixmap("images/" + name +".png")
                self.mainthread.previewImgLabel1.setPixmap(pixmap)
                self.mainthread.previewImgLabel1.setMask(pixmap.mask())
            return True
        else:
            # set name and time 
            self.mainthread.nameLabel.setText("Unknown")

            # update preview image
            pixmap = QPixmap(241, 231)
            pixmap.fill(QColor("white"))
            self.mainthread.previewImgLabel1.setPixmap(pixmap)
            self.mainthread.previewImgLabel1.setMask(pixmap.mask())
            return False




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Attendance = QtWidgets.QTabWidget()
    ui = Ui_Attendance()
    ui.setupUi(Attendance)
    Attendance.show()
    sys.exit(app.exec_())
