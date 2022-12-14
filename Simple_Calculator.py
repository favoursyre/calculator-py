# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


#I am learning how to create a calculator

from PyQt5 import QtCore, QtGui, QtWidgets


class UI_Calculator(object):
    def setupUi_Calculator(self, calculatorWindow):
        calculatorWindow.setObjectName("calculatorWindow")
        calculatorWindow.resize(360, 550)
        self.centralwidget = QtWidgets.QWidget(calculatorWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 341, 90))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")

        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculatorButton("%"))
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")

        self.divisionButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculatorButton("/")) #This calls the button function
        self.divisionButton.setGeometry(QtCore.QRect(280, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.divisionButton.setFont(font)
        self.divisionButton.setObjectName("divisionButton")

        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.removeButton())
        self.arrowButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")

        self.CButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculatorButton("C"))
        self.CButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.CButton.setFont(font)
        self.CButton.setObjectName("CButton")

        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculatorButton("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")

        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculatorButton("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.nineButton.setFont(font) 
        self.nineButton.setObjectName("nineButton")

        self.multiplicationButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculatorButton("*"))
        self.multiplicationButton.setGeometry(QtCore.QRect(280, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.multiplicationButton.setFont(font)
        self.multiplicationButton.setObjectName("multiplicationButton")

        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculatorButton("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")

        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculatorButton("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")

        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculatorButton("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")

        self.subtractionButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculatorButton("-"))
        self.subtractionButton.setGeometry(QtCore.QRect(280, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.subtractionButton.setFont(font)
        self.subtractionButton.setObjectName("subtractionButton")

        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculatorButton("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")

        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculatorButton("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")

        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculatorButton("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")

        self.additionButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculatorButton("+"))
        self.additionButton.setGeometry(QtCore.QRect(280, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.additionButton.setFont(font)
        self.additionButton.setObjectName("additionButton")

        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculatorButton("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")

        self.plus_minusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.plus_minus_Button())
        self.plus_minusButton.setGeometry(QtCore.QRect(10, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.plus_minusButton.setFont(font)
        self.plus_minusButton.setObjectName("plus_minusButton")

        self.pointButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.dotButton())
        self.pointButton.setGeometry(QtCore.QRect(190, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.pointButton.setFont(font)
        self.pointButton.setObjectName("pointButton")

        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.equalsButton())
        self.equalButton.setGeometry(QtCore.QRect(280, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")

        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.calculatorButton("0"))
        self.zeroButton.setGeometry(QtCore.QRect(100, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")

        calculatorWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(calculatorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 21))
        self.menubar.setObjectName("menubar")
        calculatorWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(calculatorWindow)
        self.statusbar.setObjectName("statusbar")
        calculatorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(calculatorWindow)
        QtCore.QMetaObject.connectSlotsByName(calculatorWindow)

    def equalsButton(self): #This handles the equal button function
        screen = self.outputLabel.text()
            
        try: #This handles any error that might occur 
            if "%" in screen: #This checks if there's % in the screen
                screen = screen[:-1]
                screen = f"{screen} / 100" #This converts the equivalent of percentage and converts it to a string in other to be evaluated
            else:
                pass
            answer = eval(screen) #The evaluate function evaluates the string mathematically and solves it
            self.outputLabel.setText(f"{answer}")
        except:
            self.outputLabel.setText("Math Error")

    def plus_minus_Button(self): #This is a function to handle the plus/minus button
        screen = self.outputLabel.text()
        if "-" in screen:
            self.outputLabel.setText(screen.replace("-", ""))
        else:
            self.outputLabel.setText(f"-{screen}")

    def removeButton(self): #This declares a function for the arrow delete button
        screen = self.outputLabel.text() #This calls whatever is on the screen
        screen = screen[:-1]
        self.outputLabel.setText(screen)

    def dotButton(self): #A function for the dot button
        screen = self.outputLabel.text()
        if screen[-1] == ".": 
            pass
        else:
            self.outputLabel.setText(f"{screen}.")

    def calculatorButton(self, pressed): #This handles the button functions in the calculator
        screen = self.outputLabel.text()
        if pressed == "C":
            self.outputLabel.setText("0")
        else:
            if self.outputLabel.text() == "0": #This checks if 0 is previously in the label and then deletes it
                self.outputLabel.setText("")
            self.outputLabel.setText(f"{self.outputLabel.text()}{pressed}") #This concatenate the previous value with the new value

    def retranslateUi(self, calculatorWindow):
        _translate = QtCore.QCoreApplication.translate
        calculatorWindow.setWindowTitle(_translate("calculatorWindow", "Calculator"))
        self.outputLabel.setText(_translate("calculatorWindow", "0"))
        self.percentButton.setText(_translate("calculatorWindow", "%"))
        self.divisionButton.setText(_translate("calculatorWindow", "/"))
        self.arrowButton.setText(_translate("calculatorWindow", "Del"))
        self.CButton.setText(_translate("calculatorWindow", "C"))
        self.sevenButton.setText(_translate("calculatorWindow", "7"))
        self.nineButton.setText(_translate("calculatorWindow", "9"))
        self.multiplicationButton.setText(_translate("calculatorWindow", "*"))
        self.eightButton.setText(_translate("calculatorWindow", "8"))
        self.fourButton.setText(_translate("calculatorWindow", "4"))
        self.sixButton.setText(_translate("calculatorWindow", "6"))
        self.subtractionButton.setText(_translate("calculatorWindow", "-"))
        self.fiveButton.setText(_translate("calculatorWindow", "5"))
        self.oneButton.setText(_translate("calculatorWindow", "1"))
        self.threeButton.setText(_translate("calculatorWindow", "3"))
        self.additionButton.setText(_translate("calculatorWindow", "+"))
        self.twoButton.setText(_translate("calculatorWindow", "2"))
        self.plus_minusButton.setText(_translate("calculatorWindow", "+/-"))
        self.pointButton.setText(_translate("calculatorWindow", "."))
        self.equalButton.setText(_translate("calculatorWindow", "="))
        self.zeroButton.setText(_translate("calculatorWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calculatorWindow = QtWidgets.QMainWindow()
    ui = UI_Calculator()
    ui.setupUi_Calculator(calculatorWindow)
    calculatorWindow.show()
    app.exec_()
