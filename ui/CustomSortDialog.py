# -*- coding: utf-8 -*-

"""
Module implementing CustomSortDialog.
"""

from PyQt5.QtCore import pyqtSlot,  QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QDialog

from .Ui_CustomSortDialog import Ui_Dialog


class CustomSortDialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(CustomSortDialog, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit.setValidator(QRegExpValidator(QRegExp("^([Kk]|[Nn]|[Vv]|[Gg])$")))
        self.lineEdit.textEdited.connect(self.makeupper)
        
    def makeupper(self,  text):
        self.le.setText(text.upper())

