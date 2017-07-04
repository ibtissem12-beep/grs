from PySide import QtCore, QtGui
import sys
sys.path.insert(0, '../gui')
from qt import Ui_MainWindow
from tabRequest import ControlTabRequest


class ControlMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupControlTabs()
        self.setupButtons()
        self.setupIcons()
        self.setupMenuActions()
        self.setupShortcuts()
        self.setWorldmap("worldmap-lq")
    
    def setupControlTabs(self):
        self.CTRequest = ControlTabRequest(self.ui)
    
    def setupButtons(self):
        self.ui.Bcfgsaveas.clicked.connect(self.CTRequest.saveRequestData)
        self.ui.Bcfgload.clicked.connect(self.CTRequest.loadRequestData)
        self.ui.Buncheckall.clicked.connect(self.CTRequest.uncheckAll)
        self.ui.Bcheckall.clicked.connect(self.CTRequest.checkAll)
    
    def setupIcons(self):
        self.iconStart = QtGui.QIcon()
        self.iconStart.addPixmap(QtGui.QPixmap("../img/icon/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.TBstartsdr.setIcon(self.iconStart)
        self.iconPing = QtGui.QIcon()
        self.iconPing.addPixmap(QtGui.QPixmap("../img/icon/ping2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.TBping.setIcon(self.iconPing)
        self.iconSend = QtGui.QIcon()
        self.iconSend.addPixmap(QtGui.QPixmap("../img/icon/antenna3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.TBsend.setIcon(self.iconSend)
    
    def setupMenuActions(self):
        pass
    
    def setupShortcuts(self):
        QtGui.QShortcut(QtGui.QKeySequence("Alt+Return"), self, self.toggleFullScreen, context=self)
        QtGui.QShortcut(QtGui.QKeySequence("F11"), self, self.toggleFullScreen, context=self)
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+E"), self, self.toggleEventLog, context=self)
    
    def toggleFullScreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()
    
    def toggleEventLog(self):
        if self.ui.LEeventlog.isHidden():
            self.ui.LEeventlog.show()
        else:
            self.ui.LEeventlog.hide()
    
    def setWorldmap(self, imgName):
        imgDir = "../img/%s.jpg" % imgName
        pixmap = QtGui.QPixmap(imgDir)
        pixmap = pixmap.scaled(640,360)
        self.ui.Lworldmap.setPixmap(pixmap)