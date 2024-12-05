# Form implementation generated from reading ui file 'src/ui/form.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(500, 500)
        mainWindow.setMinimumSize(QtCore.QSize(420, 420))
        font = QtGui.QFont()
        font.setPointSize(10)
        mainWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(parent=mainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.algorithmCombo = QtWidgets.QComboBox(parent=self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.algorithmCombo.sizePolicy().hasHeightForWidth())
        self.algorithmCombo.setSizePolicy(sizePolicy)
        self.algorithmCombo.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.algorithmCombo.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.algorithmCombo.setFrame(True)
        self.algorithmCombo.setObjectName("algorithmCombo")
        self.verticalLayout.addWidget(self.algorithmCombo)
        self.tabWidg = QtWidgets.QTabWidget(parent=self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidg.sizePolicy().hasHeightForWidth())
        self.tabWidg.setSizePolicy(sizePolicy)
        self.tabWidg.setObjectName("tabWidg")
        self.checkWordTab = QtWidgets.QWidget()
        self.checkWordTab.setObjectName("checkWordTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.checkWordTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wordTextInp = QtWidgets.QLineEdit(parent=self.checkWordTab)
        self.wordTextInp.setObjectName("wordTextInp")
        self.horizontalLayout.addWidget(self.wordTextInp)
        self.checkWordBtn = QtWidgets.QPushButton(parent=self.checkWordTab)
        self.checkWordBtn.setObjectName("checkWordBtn")
        self.horizontalLayout.addWidget(self.checkWordBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.turingProtocolTextOutp = QtWidgets.QPlainTextEdit(parent=self.checkWordTab)
        self.turingProtocolTextOutp.setReadOnly(True)
        self.turingProtocolTextOutp.setObjectName("turingProtocolTextOutp")
        self.verticalLayout_2.addWidget(self.turingProtocolTextOutp)
        self.tabWidg.addTab(self.checkWordTab, "")
        self.plotTab = QtWidgets.QWidget()
        self.plotTab.setObjectName("plotTab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.plotTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.plotWidg = PlotWidget(parent=self.plotTab)
        self.plotWidg.setObjectName("plotWidg")
        self.verticalLayout_4.addWidget(self.plotWidg)
        self.startPlottingBtn = QtWidgets.QPushButton(parent=self.plotTab)
        self.startPlottingBtn.setObjectName("startPlottingBtn")
        self.verticalLayout_4.addWidget(self.startPlottingBtn)
        self.tabWidg.addTab(self.plotTab, "")
        self.verticalLayout.addWidget(self.tabWidg)
        mainWindow.setCentralWidget(self.centralWidget)
        self.statusbar = QtWidgets.QStatusBar(parent=mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(parent=mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(parent=self.menuBar)
        self.menu.setObjectName("menu")
        mainWindow.setMenuBar(self.menuBar)
        self.algDevModeAct = QtGui.QAction(parent=mainWindow)
        self.algDevModeAct.setCheckable(True)
        self.algDevModeAct.setObjectName("algDevModeAct")
        self.saveAct = QtGui.QAction(parent=mainWindow)
        self.saveAct.setEnabled(False)
        self.saveAct.setObjectName("saveAct")
        self.menu.addAction(self.algDevModeAct)
        self.menu.addAction(self.saveAct)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(mainWindow)
        self.tabWidg.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Taifia"))
        self.wordTextInp.setPlaceholderText(_translate("mainWindow", "Введите слово для проверки"))
        self.checkWordBtn.setText(_translate("mainWindow", "Проверить"))
        self.turingProtocolTextOutp.setPlaceholderText(_translate("mainWindow", "Здесь будет выводиться протокол работы машины Тьюринга"))
        self.tabWidg.setTabText(self.tabWidg.indexOf(self.checkWordTab), _translate("mainWindow", "Проверка слова на соответствие языку"))
        self.startPlottingBtn.setText(_translate("mainWindow", "Начать построение"))
        self.tabWidg.setTabText(self.tabWidg.indexOf(self.plotTab), _translate("mainWindow", "График временной сложности"))
        self.menu.setTitle(_translate("mainWindow", "Меню"))
        self.algDevModeAct.setText(_translate("mainWindow", "Режим разработки алгоритма МТ"))
        self.saveAct.setText(_translate("mainWindow", "Сохранить протокол"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())