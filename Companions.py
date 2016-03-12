#coding=utf-8
import sys,time,shutil,os,winsound
from shell import shell
from shell import shellcon
from PyQt4.QtGui import * 
from PyQt4.QtCore import *
from main import *
from link import *
class About_UI(QWidget):  
	def __init__(self,parent=None):
		super(About_UI,self).__init__(parent)
		about_browser_qss_file=open("data/UI/style_sheets/QTextBrowser.txt","r")
		about_browser_qss=about_browser_qss_file.read()
		about_browser_qss_file.close()
		about_close_qss_file=open("data/UI/style_sheets/btn_close.txt","r")
		about_close_qss=about_close_qss_file.read()
		about_close_qss_file.close()
		self.btn_close=QPushButton()
		self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
		self.browser0 = QTextBrowser()
		self.browser1 = QTextBrowser()
		self.browser2 = QTextBrowser()
		self.browser3 = QTextBrowser()
		self.browser4 = QTextBrowser()
		self.btn_close.setStyleSheet(about_close_qss)
		self.browser0.setStyleSheet(about_browser_qss)
		self.browser1.setStyleSheet(about_browser_qss)
		self.browser2.setStyleSheet(about_browser_qss)
		self.browser3.setStyleSheet(about_browser_qss)
		self.browser4.setStyleSheet(about_browser_qss)
		self.btn_close.setParent(self)
		self.browser0.setParent(self)
		self.browser1.setParent(self)
		self.browser2.setParent(self)
		self.browser3.setParent(self)
		self.browser4.setParent(self)
		self.btn_close.setGeometry(230,10,9,9)
		self.browser0.setGeometry(6,2,50,28)
		self.browser1.setGeometry(0,60,250,28)
		self.browser2.setGeometry(0,110,250,28)
		self.browser3.setGeometry(0,160,250,28)
		self.browser4.setGeometry(0,210,250,28)
		self.btn_close.clicked.connect(self.close_clicked)
		self.setWindowTitle(u"关于 - Companions")
		self.browser2.setOpenExternalLinks(True)
		self.browser3.setOpenExternalLinks(True)
		self.browser4.setOpenExternalLinks(True)
		self.browser0.append(u'<p style="font-family:Microsoft Yahei;font:15px;color:#4f5359">关于</p>')
		self.browser1.append(u'<div align=center><p style="font-family:Microsoft Yahei;font:15px">当前版本：1.0.2')
		self.browser2.append(u'<div align=center><p style="font-family:Microsoft Yahei;font:15px"><a style="text-decoration:none;color:#6d9eeb" href="http://www.jackeriss.com/companions.htm">官方网站</a></p></div>')
		self.browser3.append(u'<div align=center><p style="font-family:Microsoft Yahei;font:15px"><a style="text-decoration:none;color:#6d9eeb" href="http://www.jackeriss.com/donate.htm">反馈与支持</a></p></div>')
		self.browser4.append(u'<div align=center><p style="font-family:Microsoft Yahei;font:15px">©2015<a style="text-decoration:none;color:#6d9eeb" href="http://www.jackeriss.com"> Jackeriss</a></p></div>')
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.dragPosition=None
		self.setWindowFlags(Qt.FramelessWindowHint|Qt.SubWindow)
		self.resize(250,300)
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
	def paintEvent(self,event):
		path=QPainterPath()
		painter=QPainter(self)
		painter.setRenderHint(QPainter.Antialiasing, True)
		color=QColor(50, 50, 50, 255)
		alpha=[120,75,45,25,15,10]
		path.addRoundRect(6, 6, self.width()-12, self.height()-12, 2)
		painter.fillPath(path, QBrush(QPixmap("data/UI/images/background.png")))
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
			if self.dragPosition != None:
				if self.dragPosition.y()<55:
					self.move(event.globalPos()-self.dragPosition)
					event.accept()
	def mouseReleaseEvent(self,event):
		self.dragPosition=QPoint(0,100)
		event.accept()
	def close_clicked(self):
		self.close()

class Help_UI(QWidget):  
	def __init__(self,parent=None):
		super(Help_UI,self).__init__(parent)
		help_browser_qss_file=open("data/UI/style_sheets/QTextBrowser.txt","r")
		help_browser_qss=help_browser_qss_file.read()
		help_browser_qss_file.close()
		help_close_qss_file=open("data/UI/style_sheets/btn_close.txt","r")
		help_close_qss=help_close_qss_file.read()
		help_close_qss_file.close()
		help_toolbox_qss_file=open("data/UI/style_sheets/QToolBox.txt","r")
		help_toolbox_qss=help_toolbox_qss_file.read()
		help_toolbox_qss_file.close()
		self.btn_close=QPushButton()
		self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
		self.browser0 = QTextBrowser()
		self.browser1 = QTextBrowser()
		self.browser2 = QTextBrowser()
		self.browser3 = QTextBrowser()
		self.browser4 = QTextBrowser()
		self.browser5 = QTextBrowser()
		self.browser6 = QTextBrowser()
		self.browser7 = QTextBrowser()
		self.browser8 = QTextBrowser()
		self.browser9 = QTextBrowser()
		self.toolbox = QToolBox()
		self.toolbox.setCursor(QCursor(Qt.PointingHandCursor))
		self.toolbox.layout().setSpacing(0)
		self.groupbox1=QGroupBox()
		self.layout1=QVBoxLayout(self.groupbox1) 
		self.layout1.setMargin(12)
		self.layout1.setAlignment(Qt.AlignHCenter)
		self.layout1.addWidget(self.browser1)
		self.layout1.addStretch()
		self.groupbox2=QGroupBox()
		self.layout2=QVBoxLayout(self.groupbox2) 
		self.layout2.setMargin(12)
		self.layout2.setAlignment(Qt.AlignHCenter)
		self.layout2.addWidget(self.browser2)
		self.layout2.addStretch()
		self.groupbox3=QGroupBox()
		self.layout3=QVBoxLayout(self.groupbox3) 
		self.layout3.setMargin(12)
		self.layout3.setAlignment(Qt.AlignHCenter)
		self.layout3.addWidget(self.browser3)
		self.layout3.addStretch()
		self.groupbox4=QGroupBox()
		self.layout4=QVBoxLayout(self.groupbox4) 
		self.layout4.setMargin(12)
		self.layout4.setAlignment(Qt.AlignHCenter)
		self.layout4.addWidget(self.browser4)
		self.layout4.addStretch()
		self.groupbox5=QGroupBox()
		self.layout5=QVBoxLayout(self.groupbox5) 
		self.layout5.setMargin(12)
		self.layout5.setAlignment(Qt.AlignHCenter)
		self.layout5.addWidget(self.browser5)
		self.layout5.addStretch()
		self.groupbox6=QGroupBox()
		self.layout6=QVBoxLayout(self.groupbox6) 
		self.layout6.setMargin(12)
		self.layout6.setAlignment(Qt.AlignHCenter)
		self.layout6.addWidget(self.browser6)
		self.layout6.addStretch()
		self.groupbox7=QGroupBox()
		self.layout7=QVBoxLayout(self.groupbox7) 
		self.layout7.setMargin(12)
		self.layout7.setAlignment(Qt.AlignHCenter)
		self.layout7.addWidget(self.browser7)
		self.layout7.addStretch()
		self.groupbox8=QGroupBox()
		self.layout8=QVBoxLayout(self.groupbox8) 
		self.layout8.setMargin(12)
		self.layout8.setAlignment(Qt.AlignHCenter)
		self.layout8.addWidget(self.browser8)
		self.layout8.addStretch()
		self.groupbox9=QGroupBox()
		self.layout9=QVBoxLayout(self.groupbox9) 
		self.layout9.setMargin(12)
		self.layout9.setAlignment(Qt.AlignHCenter)
		self.layout9.addWidget(self.browser9)
		self.layout9.addStretch()
		self.toolbox.addItem(self.groupbox1,u"初次见面")
		self.toolbox.addItem(self.groupbox2,u"聊天与问答")
		self.toolbox.addItem(self.groupbox3,u"时间和天气")
		self.toolbox.addItem(self.groupbox4,u"计算器")
		self.toolbox.addItem(self.groupbox5,u"词典")
		self.toolbox.addItem(self.groupbox6,u"百科")
		self.toolbox.addItem(self.groupbox7,u"事件提醒")
		self.toolbox.addItem(self.groupbox8,u"定时关机")
		self.toolbox.addItem(self.groupbox9,u"打开软件和网站")
		self.btn_close.setStyleSheet(help_close_qss)
		self.toolbox.setStyleSheet(help_toolbox_qss)
		self.browser0.setStyleSheet(help_browser_qss)
		self.browser1.setStyleSheet(help_browser_qss)
		self.browser2.setStyleSheet(help_browser_qss)
		self.browser3.setStyleSheet(help_browser_qss)
		self.browser4.setStyleSheet(help_browser_qss)
		self.browser5.setStyleSheet(help_browser_qss)
		self.browser6.setStyleSheet(help_browser_qss)
		self.browser7.setStyleSheet(help_browser_qss)
		self.browser8.setStyleSheet(help_browser_qss)
		self.browser9.setStyleSheet(help_browser_qss)
		self.btn_close.setParent(self)
		self.browser0.setParent(self)
		self.toolbox.setParent(self)
		self.btn_close.setGeometry(380,10,9,9)
		self.browser0.setGeometry(6,2,50,28)
		self.toolbox.setGeometry(20,40,360,540)
		self.btn_close.clicked.connect(self.close_clicked)
		self.setWindowTitle(u"帮助 - Companions")
		self.browser0.append(u'<p style="font-family:Microsoft Yahei;font:15px;color:#4f5359">帮助</p>')
		self.browser1.append(u'<p style="font-family:Microsoft Yahei;font:15px;color:#4f5359">基本操作：<br>左键展开窗口，右键收缩窗口。<br>关于主题：<br>不同的角色有不同的特色，还有许多彩蛋等着你去发现哦！</p>')
		self.browser2.append(u'<pre><p style="font-family:Microsoft Yahei;font:15px;color:#4f5359">你可以这样说：<br>你怎么什么都知道？	给我讲个笑话<br>相对论是谁提出的？	内涵图<br>赵本山的老婆是谁？	让我开心一下<br>昆明的邮编是？</p></pre>')
		self.browser3.append(u'<p style="font-family:Microsoft Yahei;font:15px;color:#4f5359">你可以这样说：<br>几点了？<br>后天星期几？<br>天气<br>北京明天有雨吗？</p>')
		self.browser4.append(u'<p style="font-family:Microsoft Yahei;font:15px;color:#4f5359">你可以这样说：<br>3次根号2<br>3的阶乘<br>5的平方等于几？<br>1021*5.21</p>')
		self.browser5.append(u'<p style="font-family:Microsoft Yahei;font:15px;color:#4f5359">直接输入英文单词即可查词：<br>如输入 "transparency"</p>')
		self.browser6.append(u'<p style="font-family:Microsoft Yahei;font:15px;color:#4f5359">你可以这样说：<br>奥巴马<br>星际穿越<br>植物大战僵尸<br>人艰不拆</p>')
		self.browser7.append(u'<p style="font-family:Microsoft Yahei;font:15px;color:#4f5359">你可以这样说：<br>两个半小时后提醒我去开会<br>11:45提醒我吃饭</p>')
		self.browser8.append(u'<p style="font-family:Microsoft Yahei;font:15px;color:#4f5359">你可以这样说：<br>关机、重启、注销、锁定<br>7:40关机<br>八点一刻关闭计算机<br>20分钟后关机</p>')
		self.browser9.append(u'<p style="font-family:Microsoft Yahei;font:15px;color:#4f5359">你可以这样说：<br>C盘<br>打开浏览器<br>磁盘管理器<br>bilibili</p>')
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.dragPosition=None
		self.setWindowFlags(Qt.FramelessWindowHint|Qt.SubWindow)
		self.resize(400,600)
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
	def paintEvent(self,event):
		path=QPainterPath()
		painter=QPainter(self)
		painter.setRenderHint(QPainter.Antialiasing, True)
		color=QColor(0, 0, 0, 255)
		alpha=[120,75,45,25,15,10]
		path.addRoundRect(6, 6, self.width()-12, self.height()-12, 2)
		painter.fillPath(path, QBrush(QPixmap("data/UI/images/update_bg.png")))
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
			if self.dragPosition != None:
				if self.dragPosition.y()<55:
					self.move(event.globalPos()-self.dragPosition)
					event.accept()
	def mouseReleaseEvent(self,event):
		self.dragPosition=QPoint(0,100)
		event.accept()
	def close_clicked(self):
		self.close()
class Setting_UI(QWidget):
	def __init__(self,parent=None):
		global changed,auto_start,ui_path,setted_theme,current_theme,themes_list,next,previous,theme_id,startup_path
		changed=next=previous=False
		theme_id=0
		startup_path = shell.SHGetPathFromIDList(shell.SHGetSpecialFolderLocation(0,shellcon.CSIDL_STARTUP))
		if os.path.isfile(startup_path+"/Companions.lnk"):
			auto_start=True
		else:
			auto_start=False
		super(Setting_UI,self).__init__(parent)
		setting_close_qss_file=open("data/UI/style_sheets/btn_close.txt","r")
		setting_close_qss=setting_close_qss_file.read()
		setting_close_qss_file.close()
		setting_previous_qss_file=open("data/UI/style_sheets/btn_previous.txt","r")
		setting_previous_qss=setting_previous_qss_file.read()
		setting_previous_qss_file.close()
		setting_next_qss_file=open("data/UI/style_sheets/btn_next.txt","r")
		setting_next_qss=setting_next_qss_file.read()
		setting_next_qss_file.close()
		setting_default_qss_file=open("data/UI/style_sheets/btn_default.txt","r")
		setting_default_qss=setting_default_qss_file.read()
		setting_default_qss_file.close()
		setting_save_qss_file=open("data/UI/style_sheets/btn_save.txt","r")
		setting_save_qss=setting_save_qss_file.read()
		setting_save_qss_file.close()
		setting_cancel_qss_file=open("data/UI/style_sheets/btn_bcancel.txt","r")
		setting_cancel_qss=setting_cancel_qss_file.read()
		setting_cancel_qss_file.close()
		setting_browser_qss_file=open("data/UI/style_sheets/QTextBrowser.txt","r")
		setting_browser_qss=setting_browser_qss_file.read()
		setting_browser_qss_file.close()
		setting_check_qss_file=open("data/UI/style_sheets/QCheckBox.txt","r")
		setting_check_qss=setting_check_qss_file.read()
		setting_check_qss_file.close()
		setting_slider_qss_file=open("data/UI/style_sheets/QSlider.txt","r")
		setting_slider_qss=setting_slider_qss_file.read()
		setting_slider_qss_file.close()
		themes_list=[]
		themes_list1=os.listdir('data/themes')
		for i in range(len(themes_list1)-1,-1,-1):
			themes_list.append(themes_list1[i].decode('gbk'))
		self.theme_pic=QLabel()
		self.btn_close=QPushButton()
		self.btn_previous=QPushButton()
		self.btn_next=QPushButton()
		self.btn_default=QPushButton()
		self.btn_save=QPushButton()
		self.btn_cancel=QPushButton()
		self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
		self.btn_previous.setCursor(QCursor(Qt.PointingHandCursor))
		self.btn_next.setCursor(QCursor(Qt.PointingHandCursor))
		self.btn_default.setCursor(QCursor(Qt.PointingHandCursor))
		self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
		self.btn_cancel.setCursor(QCursor(Qt.PointingHandCursor))
		self.browser0=QTextBrowser()
		self.browser1=QTextBrowser()
		self.browser2=QTextBrowser()
		self.browser3=QTextBrowser()
		self.browser4=QTextBrowser()
		self.check=QCheckBox(u'开机自动运行',self)
		self.check.setCursor(QCursor(Qt.PointingHandCursor))
		self.check.move(110,100)
		self.slider=QSlider(Qt.Horizontal)
		self.slider.setCursor(QCursor(Qt.PointingHandCursor))
		self.slider.setMinimum(40)
		self.slider.setMaximum(400)
		self.slider.setValue(trans)
		self.btn_close.setStyleSheet(setting_close_qss)
		self.btn_previous.setStyleSheet(setting_previous_qss)
		self.btn_next.setStyleSheet(setting_next_qss)
		self.btn_default.setStyleSheet(setting_default_qss)
		self.btn_save.setStyleSheet(setting_save_qss)
		self.btn_cancel.setStyleSheet(setting_cancel_qss)
		self.browser0.setStyleSheet(setting_browser_qss)
		self.browser1.setStyleSheet(setting_browser_qss)
		self.browser2.setStyleSheet(setting_browser_qss)
		self.browser3.setStyleSheet(setting_browser_qss)
		self.browser4.setStyleSheet(setting_browser_qss)
		self.check.setStyleSheet(setting_check_qss)
		self.slider.setStyleSheet(setting_slider_qss)
		self.theme_pic.setParent(self)
		self.btn_close.setParent(self)
		self.btn_previous.setParent(self)
		self.btn_next.setParent(self)
		self.btn_default.setParent(self)
		self.btn_save.setParent(self)
		self.btn_cancel.setParent(self)
		self.browser0.setParent(self)
		self.browser1.setParent(self)
		self.browser2.setParent(self)
		self.browser3.setParent(self)
		self.browser4.setParent(self)
		self.slider.setParent(self)
		self.theme_pic.setGeometry(136,200,128,128)
		self.btn_close.setGeometry(380,10,9,9)
		self.btn_previous.setGeometry(100,260,11,18)
		self.btn_next.setGeometry(289,260,11,18)
		self.btn_default.setGeometry(30,497,70,26)
		self.btn_save.setGeometry(180,495,80,30)
		self.btn_cancel.setGeometry(290,495,80,30)
		self.browser0.setGeometry(6,2,50,28)
		self.browser1.setGeometry(30,50,50,35)
		self.browser2.setGeometry(30,150,50,35)
		self.browser3.setGeometry(30,380,70,35)
		self.browser4.setGeometry(100,330,200,35)
		self.slider.setGeometry(100,420,200,35)
		self.browser0.append(u'<p style="font-family:Microsoft Yahei;font:15px;color:#4f5359">设置</p>')
		self.browser1.append(u'<p style="font-family:Microsoft Yahei;font:18px;color:#4f5359">启动</p>')
		self.browser2.append(u'<p style="font-family:Microsoft Yahei;font:18px;color:#4f5359">主题</p>')
		self.browser3.append(u'<p style="font-family:Microsoft Yahei;font:18px;color:#4f5359">透明度</p>')
		self.btn_previous.setEnabled(previous)
		self.btn_next.setEnabled(next)
		self.btn_save.setEnabled(changed)
		for i in range(0,len(themes_list)):
			if current_theme==themes_list[i]:
				if i==0:
					if len(themes_list)>1:
						previous=False
						next=True
						self.btn_previous.setEnabled(previous)
						self.btn_next.setEnabled(next)
					else:
						previous=False
						next=False
				elif i==len(themes_list)-1:
					if len(themes_list)>1:
						previous=True
						next=False
						self.btn_previous.setEnabled(previous)
						self.btn_next.setEnabled(next)
					else:
						previous=False
						next=False
						self.btn_previous.setEnabled(previous)
						self.btn_next.setEnabled(next)
				else:
					previous=True
					next=True
					self.btn_previous.setEnabled(previous)
					self.btn_next.setEnabled(next)
				theme_id=i
				break
		if len(current_theme)>10:
			theme_name=current_theme[:10]+'...'
		else:
			theme_name=current_theme
		self.browser4.append(u'<div align=center><p style="font-family:Microsoft Yahei;font:15px">%s</p></div>'%theme_name)
		self.theme_pic.setPixmap(QPixmap(ui_path+"cover.png"))
		self.check.setChecked(auto_start)
		self.btn_close.clicked.connect(self.close_clicked)
		self.btn_next.clicked.connect(self.next_clicked)
		self.btn_previous.clicked.connect(self.previous_clicked)
		self.btn_default.clicked.connect(self.default_clicked)
		self.btn_save.clicked.connect(self.save_clicked)
		self.btn_cancel.clicked.connect(self.close_clicked)
		self.slider.valueChanged.connect(self.update_transparency)
		self.check.clicked.connect(self.check_change)
		if self.check.isChecked() != auto_start or current_theme != setted_theme or trans != transparency:
			changed=True
			self.btn_save.setEnabled(changed)
		else:
			changed=False
			self.btn_save.setEnabled(changed)
		self.setWindowTitle(u"设置 - Companions")
		self.icon = QIcon(ui_path+"cover.png")
		self.setWindowIcon(self.icon)
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.dragPosition=None
		self.setWindowFlags(Qt.FramelessWindowHint|Qt.SubWindow)
		self.resize(400,550)
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
	def paintEvent(self,event):
		global ui_path
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
	def update_transparency(self):
		global changed,transparency,trans,auto_start,current_theme,setted_theme
		trans=self.slider.value()
		if self.check.isChecked() != auto_start or current_theme != setted_theme or trans != transparency:
			changed=True
			self.btn_save.setEnabled(changed)
		else:
			changed=False
			self.btn_save.setEnabled(changed)
	def check_change(self):
		global changed,transparency,auto_start,current_theme,setted_theme
		if self.check.isChecked() != auto_start or current_theme != setted_theme or self.slider.value() != transparency:
			changed=True
			self.btn_save.setEnabled(changed)
		else:
			changed=False
			self.btn_save.setEnabled(changed)
	def mousePressEvent(self,event):
		if event.button()==Qt.LeftButton:
			self.dragPosition=event.globalPos()-self.frameGeometry().topLeft()
			event.accept()
	def mouseMoveEvent(self,event):
		if event.buttons() & Qt.LeftButton:
			if self.dragPosition != None:
				if self.dragPosition.y()<50:
					self.move(event.globalPos()-self.dragPosition)
					event.accept()
	def mouseReleaseEvent(self,event):
		self.dragPosition=QPoint(0,100)
		event.accept()
	def close_clicked(self):
		global transparency,auto_start,current_theme,setted_theme
		self.check.setChecked(auto_start)
		current_theme=setted_theme
		current_theme_file=open("data/settings/current_theme.txt","w")
		current_theme_file.write(current_theme.encode("gbk"))
		current_theme_file.close()
		self.slider.setValue(transparency)
		self.close()
	def previous_clicked(self):
		global changed,transparency,auto_start,themes_list,current_theme,setted_theme,ui_path,next,previous,theme_id
		if previous:
			theme_id-=1
			theme_name=current_theme=themes_list[theme_id]
			ui_path="data/themes/"+current_theme+"/images/UI/"
			self.theme_pic.setPixmap(QPixmap(ui_path+"cover.png"))
			self.icon = QIcon(ui_path+"cover.png")
			self.setWindowIcon(self.icon)
			current_theme_file=open("data/settings/current_theme.txt","w")
			current_theme_file.write(current_theme.encode("gbk"))
			current_theme_file.close()
			if len(current_theme)>10:
				theme_name=current_theme[:10]+'...'
			self.browser4.clear()
			self.browser4.append(u'<div align=center>%s</div>'%theme_name)
			if theme_id==0:
				if len(themes_list)>1:
					previous=False
					next=True
					self.btn_previous.setEnabled(previous)
					self.btn_next.setEnabled(next)
				else:
					previous=False
					next=False
					self.btn_previous.setEnabled(previous)
					self.btn_next.setEnabled(next)
			else:
				previous=True
				next=True
				self.btn_previous.setEnabled(previous)
				self.btn_next.setEnabled(next)
			if self.check.isChecked() != auto_start or current_theme != setted_theme or self.slider.value() != transparency:
				changed=True
				self.btn_save.setEnabled(changed)
			else:
				changed=False
				self.btn_save.setEnabled(changed)
	def next_clicked(self):
		global changed,transparency,auto_start,themes_list,current_theme,setted_theme,ui_path,next,previous,theme_id
		if next:
			theme_id+=1
			theme_name=current_theme=themes_list[theme_id]
			ui_path="data/themes/"+current_theme+"/images/UI/"
			self.theme_pic.setPixmap(QPixmap(ui_path+"cover.png"))
			self.icon = QIcon(ui_path+"cover.png")
			self.setWindowIcon(self.icon)
			current_theme_file=open("data/settings/current_theme.txt","w")
			current_theme_file.write(current_theme.encode("gbk"))
			current_theme_file.close()
			if len(current_theme)>10:
				theme_name=current_theme[:10]+'...'
			self.browser4.clear()
			self.browser4.append(u'<div align=center>%s</div>'%theme_name)
			if theme_id==len(themes_list)-1:
				if len(themes_list)>1:
					previous=True
					next=False
					self.btn_previous.setEnabled(previous)
					self.btn_next.setEnabled(next)
				else:
					previous=False
					next=False
					self.btn_previous.setEnabled(previous)
					self.btn_next.setEnabled(next)
			else:
				previous=True
				next=True
				self.btn_previous.setEnabled(previous)
				self.btn_next.setEnabled(next)
			if self.check.isChecked() != auto_start or current_theme != setted_theme or self.slider.value() != transparency:
				changed=True
				self.btn_save.setEnabled(changed)
			else:
				changed=False
				self.btn_save.setEnabled(changed)
	def default_clicked(self):
		global changed,transparency,auto_start,themes_list,current_theme,setted_theme,ui_path,next,previous,theme_id
		self.check.setChecked(True)
		self.slider.setValue(360)
		for i in range(0,len(themes_list)):
			if themes_list[i]==u'御坂10032号':
				theme_id=i
				break
		theme_name=current_theme=themes_list[theme_id]
		ui_path="data/themes/"+current_theme+"/images/UI/"
		self.theme_pic.setPixmap(QPixmap(ui_path+"cover.png"))
		self.icon = QIcon(ui_path+"cover.png")
		self.setWindowIcon(self.icon)
		current_theme_file=open("data/settings/current_theme.txt","w")
		current_theme_file.write(current_theme.encode("gbk"))
		current_theme_file.close()
		if len(current_theme)>10:
			theme_name=current_theme[:10]+'...'
		self.browser4.clear()
		self.browser4.append(u'<div align=center>%s</div>'%theme_name)
		if theme_id==0:
			if len(themes_list)>1:
				previous=False
				next=True
				self.btn_previous.setEnabled(previous)
				self.btn_next.setEnabled(next)
			else:
				previous=False
				next=False
				self.btn_previous.setEnabled(previous)
				self.btn_next.setEnabled(next)
		elif theme_id==len(themes_list)-1:
			if len(themes_list)>1:
				previous=True
				next=False
				self.btn_previous.setEnabled(previous)
				self.btn_next.setEnabled(next)
			else:
				previous=False
				next=False
				self.btn_previous.setEnabled(previous)
				self.btn_next.setEnabled(next)
		else:
			previous=True
			next=True
			self.btn_previous.setEnabled(previous)
			self.btn_next.setEnabled(next)
		if self.check.isChecked() != auto_start or current_theme != setted_theme or self.slider.value() != transparency:
			changed=True
			self.btn_save.setEnabled(changed)
		else:
			changed=False
			self.btn_save.setEnabled(changed)
	def save_clicked(self):
		global changed,current_theme,setted_theme,startup_path
		if changed:
			setted_theme=current_theme
			setted_theme_file=open("data/settings/setted_theme.txt","w")
			setted_theme_file.write(setted_theme.encode("gbk"))
			setted_theme_file.close()
			transparency_file=open("data/settings/transparency.txt","w")
			transparency_file.write(str(self.slider.value()))
			transparency_file.close()
			if self.check.isChecked()==True:	
				set_shortcut()
			else:
				os.remove(shell.SHGetPathFromIDList(shell.SHGetSpecialFolderLocation(0,shellcon.CSIDL_STARTUP))+"/Companions.lnk")
			self.close()

class Play(QThread):
	def __init__(self,parent=None):
		super(Play,self).__init__(parent)
	def run(self):
		global song
		winsound.PlaySound("data/sounds/"+song+".wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
        
class wait_main(QThread):
	trigger = pyqtSignal()
	def __init__(self,parent=None):
		super(wait_main,self).__init__(parent)
	def run(self):
		global text,time_out,current_theme,results,song
		time_out=True
		song=None
		results=main(text)
		results=results.decode("gbk")
		if text=="#":
			results='<p style="font-family:Microsoft Yahei;font:24px">Stuart：好吧...</p>'.decode("utf-8")
		if results[-5:]=='@sing':
			song=str(random.randint(1,2))
			lyric_file=open("data/sounds/"+song+".txt","r")
			lyric=lyric_file.read()
			lyric_file.close()
			href_file=open(style_path+"href.txt","r")
			href=href_file.read()
			href_file.close()
			results='<p style="font-family:Microsoft Yahei;font:24px">'+lyric.replace("\n","<br>")+'<br><a style="text-decoration:none;color:#'+href+'" href="#">别唱了！</a></p>'
			results=results.decode("utf-8")
		time_out=False
		self.trigger.emit()
		
class Companions_UI(QWidget):  
	def __init__(self,parent=None):
		super(Companions_UI,self).__init__(parent)
		global shape1,shape2,shape3,ui_path,style_path,setted_theme,current_theme,transparency,trans
		trans=None
		while 1:
			try:
				good_time_file=open("data/db/good_time.txt","w")
				break
			except:
				pass
		good_time_file.write('0')
		good_time_file.close()
		bad_time_file=open("data/db/bad_time.txt","w")
		bad_time_file.write('0')
		bad_time_file.close()
		dirty_words_time_file=open("data/db/dirty_words_time.txt","w")
		dirty_words_time_file.write('0')
		dirty_words_time_file.close()
		setted_theme_file=open("data/settings/setted_theme.txt","r")
		setted_theme=setted_theme_file.readline().strip("\n").decode("gbk")
		setted_theme_file.close()
		current_theme=setted_theme
		current_theme_file=open("data/settings/current_theme.txt","w")
		current_theme_file.write(current_theme.encode("gbk"))
		current_theme_file.close()
		ui_path="data/themes/"+current_theme+"/images/UI/"
		style_path="data/themes/"+current_theme+"/style_sheets/"
		style_path_file=open("data/settings/style_path.txt","w")
		style_path_file.write(style_path.encode("gbk"))
		style_path_file.close()
		QLineEdit_qss_file=open(style_path+"QLineEdit.txt","r")
		QLineEdit_qss=QLineEdit_qss_file.read()
		QLineEdit_qss_file.close()
		QTextBrowser_qss_file=open(style_path+"QTextBrowser.txt","r")
		QTextBrowser_qss=QTextBrowser_qss_file.read()
		QTextBrowser_qss_file.close()
		vQScrollBar_qss_file=open(style_path+"vQScrollBar.txt","r")
		vQScrollBar_qss=vQScrollBar_qss_file.read()
		vQScrollBar_qss_file.close()
		QMenu_qss_file=open("data/UI/style_sheets/QMenu.txt","r")
		QMenu_qss=QMenu_qss_file.read()
		QMenu_qss_file.close()
		transparency_file=open("data/settings/transparency.txt","r")
		transparency=int(transparency_file.read())
		trans=transparency
		transparency_file.close()
		shape1=True
		shape2=False
		shape3=False
		press_left=0
		press_top=0
		self.wait_thread=wait_main()
		self.wait_thread.trigger.connect(self.after_waiting)
		self.play_thread=Play()
		self.browser = QTextBrowser()
		self.lineedit = QLineEdit(u'')
		self.lineedit.setTextMargins(6,0,6,0)
		self.lineedit.selectAll()
		layout = QVBoxLayout()
		layout.addWidget(self.browser)
		layout.addWidget(self.lineedit)
		self.lineedit.hide()
		self.browser.hide()
		self.setLayout(layout)
		self.lineedit.setStyleSheet(QLineEdit_qss)
		self.browser.setStyleSheet(QTextBrowser_qss)
		self.browser.verticalScrollBar().setStyleSheet(vQScrollBar_qss)
		self.lineedit.setFocus()
		self.browser.setOpenExternalLinks(True)
		self.browser.anchorClicked.connect(self.redo)
		self.browser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.lineedit.returnPressed.connect(self.updateUi_2)
		self.setWindowTitle(u"Companions - "+current_theme)
		self.icon = QIcon(ui_path+"cover.png")
		self.trayIcon = QSystemTrayIcon()
		self.settingAction = QAction(u"设 置", self,triggered=self.setting)
		self.helpAction = QAction(u"帮 助", self,triggered=self.help)
		self.aboutAction = QAction(u"关 于", self,triggered=self.about)
		self.quitAction = QAction(u"退 出", self,triggered=self.exit)
		self.trayIconMenu = QMenu(self)
		self.trayIconMenu.setStyleSheet(QMenu_qss)
		self.trayIconMenu.addAction(self.settingAction)
		self.trayIconMenu.addAction(self.helpAction)
		self.trayIconMenu.addAction(self.aboutAction)
		self.trayIconMenu.addAction(self.quitAction)
		self.trayIcon.setContextMenu(self.trayIconMenu)
		self.trayIcon.setToolTip(u"Companions - "+current_theme)	
		self.setWindowIcon(self.icon)
		self.trayIcon.setIcon(self.icon)
		self.trayIcon.show()
		self.setAttribute(Qt.WA_TranslucentBackground)
		self.dragPosition=None   
		self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.SplashScreen|Qt.X11BypassWindowManagerHint) 
		self.setWindowOpacity(transparency/400.0)  
		self.resize(60,60)
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move(screen.width()-size.width(), screen.height()-size.height()-100)
	def paintEvent(self,event):
		global shape1,shape2,shape3
		path=QPainterPath()
		painter=QPainter(self)
		painter.setRenderHint(QPainter.Antialiasing, True)
		color=QColor(0, 0, 0, 255)
		alpha=[120,75,45,25,15,10]
		if shape1:
			path.addRoundRect(6, 6, self.width()-12, self.height()-12, 10)
			painter.fillPath(path, QBrush(QPixmap(ui_path+"logo.png")))
			for i in range(0,6):
				path=QPainterPath()
				path.addRoundRect(6-i, 6-i, self.width()-(6-i)*2, self.height()-(6-i)*2, 10)
				color.setAlpha(alpha[i])
				painter.setPen(color)
				painter.drawPath(path)
		elif shape2:
			path.addRoundRect(6, 6, self.width()-12, self.height()-12, 10)
			painter.fillPath(path, QBrush(QPixmap(ui_path+"background.png")))
			for i in range(0,6):
				path=QPainterPath()
				path.addRoundRect(6-i, 6-i, self.width()-(6-i)*2, self.height()-(6-i)*2, 10)
				color.setAlpha(alpha[i])
				painter.setPen(color)
				painter.drawPath(path)
		elif shape3:
			path.addRoundRect(6, 6, self.width()-12, self.height()-12, 2)
			painter.fillPath(path, QBrush(QPixmap(ui_path+"background.png")))
			for i in range(0,6):
				path=QPainterPath()
				path.addRoundRect(6-i, 6-i, self.width()-(6-i)*2, self.height()-(6-i)*2, 2)
				color.setAlpha(alpha[i])
				painter.setPen(color)
				painter.drawPath(path)
	def setting(self):
		self.setting_ui = Setting_UI()
		self.setting_ui.slider.valueChanged.connect(self.update_transparency)
		self.setting_ui.btn_previous.clicked.connect(self.change_theme)
		self.setting_ui.btn_next.clicked.connect(self.change_theme)
		self.setting_ui.btn_default.clicked.connect(self.change_theme)
		self.setting_ui.btn_close.clicked.connect(self.change_theme)
		self.setting_ui.btn_cancel.clicked.connect(self.change_theme)
		self.setting_ui.show()
	def help(self):
		self.help_ui = Help_UI()
		self.help_ui.show()
	def about(self):
		self.about_ui = About_UI()
		self.about_ui.show()
	def exit(self):
		for root,dirs,files in os.walk(str(os.getcwd())+"\\cache"):
			for filespath in files:
				path = os.path.join(root,filespath)
				try:
					os.remove(path)
				except:
					pass		
		os.popen("TASKKILL /F /IM reminder.exe")
		self.trayIcon.hide()
		sys.exit()
	def update_transparency(self):
		global trans
		self.setWindowOpacity(trans/400.0)
	def change_theme(self):
		global shape1,shape2,shape3,current_theme,ui_path,style_path
		pre_theme=current_theme
		ui_path="data/themes/"+current_theme+"/images/UI/"
		style_path="data/themes/"+current_theme+"/style_sheets/"
		style_path_file=open("data/settings/style_path.txt","w")
		style_path_file.write(style_path.encode("gbk"))
		style_path_file.close()
		QLineEdit_qss_file=open(style_path+"QLineEdit.txt","r")
		QLineEdit_qss=QLineEdit_qss_file.read()
		QLineEdit_qss_file.close()
		QTextBrowser_qss_file=open(style_path+"QTextBrowser.txt","r")
		QTextBrowser_qss=QTextBrowser_qss_file.read()
		QTextBrowser_qss_file.close()
		vQScrollBar_qss_file=open(style_path+"vQScrollBar.txt","r")
		vQScrollBar_qss=vQScrollBar_qss_file.read()
		vQScrollBar_qss_file.close()
		self.lineedit.setStyleSheet(QLineEdit_qss)
		self.browser.setStyleSheet(QTextBrowser_qss)
		self.browser.verticalScrollBar().setStyleSheet(vQScrollBar_qss)
		p=self.palette()
		if shape1:
			p.setBrush(QPalette.Background, QBrush(QPixmap(ui_path+"logo.png")))
		elif shape2:
			p.setBrush(QPalette.Background, QBrush(QPixmap(ui_path+"background.png")))
		elif shape3:
			p.setBrush(QPalette.Background, QBrush(QPixmap(ui_path+"background.png")))
		self.setPalette(p)
		self.icon = QIcon(ui_path+"cover.png")
		self.setWindowIcon(self.icon)
		self.trayIcon.setIcon(self.icon)
		self.trayIcon.setToolTip(u"Companions - "+current_theme)
	def mousePressEvent(self,event):
		global press_left,press_top
		press_left = self.frameGeometry().left()
		press_top = self.frameGeometry().top()
		if event.button()==Qt.LeftButton:
			self.dragPosition=event.globalPos()-self.frameGeometry().topLeft()
			event.accept()
		if event.button()==Qt.RightButton:
			self.renewUi()
			event.accept()
	def mouseReleaseEvent(self,event):
		if event.button()==Qt.LeftButton and self.frameGeometry().left()==press_left and self.frameGeometry().top()==press_top:
			self.updateUi_1()
			event.accept()
	def mouseMoveEvent(self,event):  
		if event.buttons() & Qt.LeftButton:
			self.move(event.globalPos()-self.dragPosition)  
			event.accept()
	def updateUi_1(self):
		global shape1,shape2
		if shape1:
			shape2=True
			shape1=False
			screen = QDesktopWidget().screenGeometry()
			size = self.geometry()
			self.move(self.frameGeometry().left()-340,self.frameGeometry().top())
			self.lineedit.show()
			self.lineedit.setFocus()
			self.resize(400,60)
	def updateUi_2(self):
		global shape1,shape2,shape3,text,count,style_path
		if shape1:
			shape3=True
			shape1=False
			if self.frameGeometry().top()>=440:
				screen = QDesktopWidget().screenGeometry()
				size = self.geometry()
				self.move(self.frameGeometry().left(),self.frameGeometry().top()-440)
				self.lineedit.show()
				self.browser.show()
				self.lineedit.setFocus()
				self.resize(400,500)
			else:
				self.lineedit.show()
				self.browser.show()
				self.resize(400,500)
		elif shape2:
			count=0
			shape3=True
			shape2=False
			if self.frameGeometry().top()>=440:
				screen = QDesktopWidget().screenGeometry()
				size = self.geometry()
				self.move(self.frameGeometry().left(),self.frameGeometry().top()-440)
				self.browser.show()
				self.resize(400,500)
			else:
				self.browser.show()
				self.resize(400,500)
		text = unicode(self.lineedit.text())
		master_file=open(style_path+"master.txt","r")
		master=master_file.read()
		master_file.close()
		self.browser.append(u'<div align=left></div><p style="font-family:Microsoft Yahei;font:24px;color:#'+master+'">我：'.decode("utf8")+'%s</p>' % text)
		text=text.encode("gbk")
		self.browser.moveCursor(QTextCursor.End)
		self.wait_thread.start()
		count+=1
		self.lineedit.clear()
			
	def renewUi(self):
		global shape1,shape2,shape3
		if shape2:
			self.lineedit.clear()
			screen = QDesktopWidget().screenGeometry()
			size = self.geometry()
			self.move(self.frameGeometry().left()+340,self.frameGeometry().top())
			self.lineedit.hide()
			self.resize(60,60)
			self.resize(60,60)
			shape1=True
			shape2=False
		elif shape3:
			self.browser.clear()
			self.lineedit.clear()
			screen = QDesktopWidget().screenGeometry()
			size = self.geometry()
			self.move(self.frameGeometry().left(),self.frameGeometry().top()+440)
			self.browser.hide()
			self.resize(400,60)
			self.resize(400,60)
			shape2=True
			shape3=False
	def redo(self):
		global count,text,song
		self.browser.moveCursor(QTextCursor.End)
		text1=text.decode("gbk").encode("utf8")
		if text1=="内涵图" or text1=="讲个笑话" or text1=="内涵段子" or text1=="内涵图" or text1=="搞笑图" or text1=="让我开心一下" or text1=="让我高兴一下":
			pass
		else:
			if '关机' in text1 or '关闭计算机' in text1 or '关闭电脑'in text1:
				text1="取消关机"
			elif '重启' in text1 or '重新启动' in text1:
				text1="取消重启"
			elif'注销' in text1:
				text1="取消注销"
			elif '提醒' in text1:
				text1="取消提醒"
			elif "唱首歌" in text1 or "唱个歌" in text1 or "唱歌" in text1 or text1=="#":
				winsound.PlaySound("data/sounds/0.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
				text1="#"
			else:
				if random.randint(0,1)==0:
					text1="内涵图"
				else:
					text1="内涵段子"
		text=text1.decode("utf8").encode("gbk")
		self.browser.append("")
		self.wait_thread.start()
		count+=1
	def after_waiting(self):
		global current_theme,results,song
		if song!=None:
			self.play_thread.start()
		self.browser.append(results)
		self.browser.moveCursor(QTextCursor.End)
			
app=QApplication(sys.argv)
form=Companions_UI()
form.show()
sys.exit(app.exec_())
