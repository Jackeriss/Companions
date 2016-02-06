#! /usr/bin/env python
#coding:utf-8
from PyQt4.QtGui import * 
from PyQt4.QtCore import *
import time, sys, os, winsound
os.chdir(os.getcwd().strip("/bin"))
class Sound(QThread):
    def __init__(self,parent=None):
        super(Sound,self).__init__(parent)
    def run(self):
        winsound.PlaySound("data/sounds/bell.wav",winsound.SND_FILENAME)
class Reminder_UI(QWidget):
    def __init__(self,parent=None):
        super(Reminder_UI,self).__init__(parent)
        current_theme_file=open("data/settings/current_theme.txt","r")
        current_theme=current_theme_file.readline().strip("\n").decode("gbk")
        current_theme_file.close()
        reminder_browser_qss_file=open("data/UI/style_sheets/QTextBrowser.txt","r")
        reminder_browser_qss=reminder_browser_qss_file.read()
        reminder_browser_qss_file.close()
        reminder_close_qss_file=open("data/UI/style_sheets/btn_close.txt","r")
        reminder_close_qss=reminder_close_qss_file.read()
        reminder_close_qss_file.close()
        reminder_known_qss_file=open("data/UI/style_sheets/btn_known.txt","r")
        reminder_known_qss=reminder_known_qss_file.read()
        reminder_known_qss_file.close()
        reminder_reminder_file=open("data/db/reminder.txt","r")
        reminder_reminder=reminder_reminder_file.read()
        msg=reminder_reminder.decode("gbk")
        reminder_reminder_file.close()
        ui_path="data/themes/"+current_theme+"/images/UI/"
        self.sound_thread=Sound()
        self.btn_close=QPushButton()
        self.btn_known=QPushButton()
        self.browser0 = QTextBrowser()
        self.browser1 = QTextBrowser()
        self.btn_close.setStyleSheet(reminder_close_qss)
        self.btn_known.setStyleSheet(reminder_known_qss)
        self.browser0.setStyleSheet(reminder_browser_qss)
        self.browser1.setStyleSheet(reminder_browser_qss)
        self.btn_close.setParent(self)
        self.btn_known.setParent(self)
        self.browser0.setParent(self)
        self.browser1.setParent(self)
        self.btn_close.setGeometry(380,10,9,9)
        self.btn_known.setGeometry(160,180,80,30)
        self.browser0.setGeometry(6,2,100,28)
        self.browser1.setGeometry(50,85,300,80)
        self.btn_close.clicked.connect(self.close_clicked)
        self.btn_known.clicked.connect(self.close_clicked)
        self.setWindowTitle(u"事件提醒 - Companions")
        self.icon = QIcon(ui_path+"cover.png")
        self.setWindowIcon(self.icon)
        self.browser0.append(u'<p style="font-family:Microsoft Yahei;font:15px;color:#4f5359">事件提醒</p>')
        self.browser1.append(u'<div align=center><p style="font-family:Microsoft Yahei;font:18px">%s</p></div>'%msg)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.dragPosition=None
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
        transparency_file=open("data/settings/transparency.txt","r")
        transparency=int(transparency_file.read())
        transparency_file.close()
        self.setWindowOpacity(transparency/400.0)
        self.resize(400,250)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
        self.sound_thread.start()
    def paintEvent(self,event):
        path=QPainterPath()
        painter=QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        color=QColor(0, 0, 0, 255)
        alpha=[120,75,45,25,15,10]
        path.addRoundRect(6, 6, self.width()-12, self.height()-12, 2)
        painter.fillPath(path, QBrush(QPixmap("data/ui/images/background.png")))
        for i in range(0,6):
            path=QPainterPath()
            path.addRoundRect(6-i, 6-i, self.width()-(6-i)*2, self.height()-(6-i)*2, 2)
            color.setAlpha(alpha[i])
            painter.setPen(color)
            painter.drawPath(path)
    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton:
            self.dragPosition=event.globalPos()-self.frameGeometry().topLeft()
            event.accept()
    def mouseReleaseEvent(self,event):
        if event.button()==Qt.LeftButton:
            event.accept()
    def mouseMoveEvent(self,event):
        if event.buttons() & Qt.LeftButton:
            if self.dragPosition.x()>35 and self.dragPosition.x()<379 and self.dragPosition.y()<55:
                self.move(event.globalPos()-self.dragPosition)
                event.accept()
    def close_clicked(self):
        sys.exit()
app=QApplication(sys.argv)
form=Reminder_UI()
form.show()
sys.exit(app.exec_())
