from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QApplication)
from PyQt5 import QtGui
import cv2
import numpy as np
import sys
import os
import FeatureSelectorProject.FeatureSelector.gui as gui
#import FeatureSelection

QApplication.setApplicationName('FeatureSelector')
QApplication.setApplicationVersion('0.1')

Ui_MainWindow = gui.Ui_MainWindow

class MyApp(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Feature Selector")
        self.connectButtons()

    def connectButtons(self):
        self.btnSelectArea.clicked.connect(self.buttonsTest)

    def buttonsTest(self):
        print('apertadooooo')