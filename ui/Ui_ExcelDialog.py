# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/xorg/eric/Sportfest/ui/ExcelDialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(624, 486)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setEnabled(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setEnabled(False)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setEnabled(False)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.vornameEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.vornameEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vornameEdit.sizePolicy().hasHeightForWidth())
        self.vornameEdit.setSizePolicy(sizePolicy)
        self.vornameEdit.setObjectName("vornameEdit")
        self.gridLayout_4.addWidget(self.vornameEdit, 1, 2, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.nameEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameEdit.sizePolicy().hasHeightForWidth())
        self.nameEdit.setSizePolicy(sizePolicy)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout_4.addWidget(self.nameEdit, 0, 2, 1, 1)
        self.geschlechtBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.geschlechtBox.setEnabled(False)
        self.geschlechtBox.setChecked(True)
        self.geschlechtBox.setTristate(False)
        self.geschlechtBox.setObjectName("geschlechtBox")
        self.gridLayout_4.addWidget(self.geschlechtBox, 2, 1, 1, 1)
        self.geschlechtEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.geschlechtEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geschlechtEdit.sizePolicy().hasHeightForWidth())
        self.geschlechtEdit.setSizePolicy(sizePolicy)
        self.geschlechtEdit.setObjectName("geschlechtEdit")
        self.gridLayout_4.addWidget(self.geschlechtEdit, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setEnabled(False)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 1)
        self.klasseBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.klasseBox.setEnabled(False)
        self.klasseBox.setChecked(True)
        self.klasseBox.setObjectName("klasseBox")
        self.gridLayout_4.addWidget(self.klasseBox, 3, 1, 1, 1)
        self.klasseEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.klasseEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.klasseEdit.sizePolicy().hasHeightForWidth())
        self.klasseEdit.setSizePolicy(sizePolicy)
        self.klasseEdit.setObjectName("klasseEdit")
        self.gridLayout_4.addWidget(self.klasseEdit, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.createNew = QtWidgets.QPushButton(self.groupBox_3)
        self.createNew.setEnabled(False)
        self.createNew.setObjectName("createNew")
        self.gridLayout_3.addWidget(self.createNew, 0, 0, 1, 1)
        self.addInto = QtWidgets.QPushButton(self.groupBox_3)
        self.addInto.setEnabled(False)
        self.addInto.setObjectName("addInto")
        self.gridLayout_3.addWidget(self.addInto, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 4, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.excelOpen = QtWidgets.QPushButton(self.groupBox)
        self.excelOpen.setObjectName("excelOpen")
        self.gridLayout_2.addWidget(self.excelOpen, 0, 0, 1, 1)
        self.excelPath = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.excelPath.sizePolicy().hasHeightForWidth())
        self.excelPath.setSizePolicy(sizePolicy)
        self.excelPath.setObjectName("excelPath")
        self.gridLayout_2.addWidget(self.excelPath, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.sheetCombo = QtWidgets.QComboBox(self.groupBox_4)
        self.sheetCombo.setEnabled(False)
        self.sheetCombo.setObjectName("sheetCombo")
        self.gridLayout_5.addWidget(self.sheetCombo, 0, 0, 1, 1)
        self.openSheet = QtWidgets.QPushButton(self.groupBox_4)
        self.openSheet.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openSheet.sizePolicy().hasHeightForWidth())
        self.openSheet.setSizePolicy(sizePolicy)
        self.openSheet.setObjectName("openSheet")
        self.gridLayout_5.addWidget(self.openSheet, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 1, 0, 1, 2)
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setEnabled(False)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.allRows = QtWidgets.QRadioButton(self.groupBox_5)
        self.allRows.setEnabled(False)
        self.allRows.setChecked(True)
        self.allRows.setObjectName("allRows")
        self.gridLayout_6.addWidget(self.allRows, 0, 0, 1, 2)
        self.areaRows = QtWidgets.QRadioButton(self.groupBox_5)
        self.areaRows.setEnabled(False)
        self.areaRows.setObjectName("areaRows")
        self.gridLayout_6.addWidget(self.areaRows, 1, 0, 1, 2)
        self.rowMin = QtWidgets.QSpinBox(self.groupBox_5)
        self.rowMin.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rowMin.sizePolicy().hasHeightForWidth())
        self.rowMin.setSizePolicy(sizePolicy)
        self.rowMin.setMinimumSize(QtCore.QSize(0, 20))
        self.rowMin.setMinimum(1)
        self.rowMin.setMaximum(999)
        self.rowMin.setObjectName("rowMin")
        self.gridLayout_6.addWidget(self.rowMin, 2, 0, 1, 1)
        self.rowMax = QtWidgets.QSpinBox(self.groupBox_5)
        self.rowMax.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rowMax.sizePolicy().hasHeightForWidth())
        self.rowMax.setSizePolicy(sizePolicy)
        self.rowMax.setMinimumSize(QtCore.QSize(0, 20))
        self.rowMax.setMinimum(2)
        self.rowMax.setMaximum(999)
        self.rowMax.setObjectName("rowMax")
        self.gridLayout_6.addWidget(self.rowMax, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_5, 2, 1, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_6.setEnabled(False)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.vornamePreview = QtWidgets.QLineEdit(self.groupBox_6)
        self.vornamePreview.setEnabled(False)
        self.vornamePreview.setReadOnly(True)
        self.vornamePreview.setObjectName("vornamePreview")
        self.gridLayout_7.addWidget(self.vornamePreview, 1, 0, 1, 1)
        self.geschlechtPreview = QtWidgets.QLineEdit(self.groupBox_6)
        self.geschlechtPreview.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geschlechtPreview.sizePolicy().hasHeightForWidth())
        self.geschlechtPreview.setSizePolicy(sizePolicy)
        self.geschlechtPreview.setMinimumSize(QtCore.QSize(12, 0))
        self.geschlechtPreview.setBaseSize(QtCore.QSize(0, 0))
        self.geschlechtPreview.setMaxLength(1)
        self.geschlechtPreview.setReadOnly(True)
        self.geschlechtPreview.setObjectName("geschlechtPreview")
        self.gridLayout_7.addWidget(self.geschlechtPreview, 1, 2, 1, 1)
        self.klassePreview = QtWidgets.QLineEdit(self.groupBox_6)
        self.klassePreview.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.klassePreview.sizePolicy().hasHeightForWidth())
        self.klassePreview.setSizePolicy(sizePolicy)
        self.klassePreview.setMinimumSize(QtCore.QSize(12, 0))
        self.klassePreview.setReadOnly(True)
        self.klassePreview.setObjectName("klassePreview")
        self.gridLayout_7.addWidget(self.klassePreview, 1, 3, 1, 1)
        self.nachnamePreview = QtWidgets.QLineEdit(self.groupBox_6)
        self.nachnamePreview.setEnabled(False)
        self.nachnamePreview.setReadOnly(True)
        self.nachnamePreview.setObjectName("nachnamePreview")
        self.gridLayout_7.addWidget(self.nachnamePreview, 1, 1, 1, 1)
        self.vornameLabel = QtWidgets.QLabel(self.groupBox_6)
        self.vornameLabel.setEnabled(False)
        self.vornameLabel.setObjectName("vornameLabel")
        self.gridLayout_7.addWidget(self.vornameLabel, 0, 0, 1, 1)
        self.nachnameLabel = QtWidgets.QLabel(self.groupBox_6)
        self.nachnameLabel.setEnabled(False)
        self.nachnameLabel.setObjectName("nachnameLabel")
        self.gridLayout_7.addWidget(self.nachnameLabel, 0, 1, 1, 1)
        self.geschlechtLabel = QtWidgets.QLabel(self.groupBox_6)
        self.geschlechtLabel.setEnabled(False)
        self.geschlechtLabel.setObjectName("geschlechtLabel")
        self.gridLayout_7.addWidget(self.geschlechtLabel, 0, 2, 1, 1)
        self.klasseLabel = QtWidgets.QLabel(self.groupBox_6)
        self.klasseLabel.setEnabled(False)
        self.klasseLabel.setObjectName("klasseLabel")
        self.gridLayout_7.addWidget(self.klasseLabel, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox_6, 3, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.excelOpen, self.sheetCombo)
        Dialog.setTabOrder(self.sheetCombo, self.openSheet)
        Dialog.setTabOrder(self.openSheet, self.geschlechtBox)
        Dialog.setTabOrder(self.geschlechtBox, self.klasseBox)
        Dialog.setTabOrder(self.klasseBox, self.nameEdit)
        Dialog.setTabOrder(self.nameEdit, self.vornameEdit)
        Dialog.setTabOrder(self.vornameEdit, self.geschlechtEdit)
        Dialog.setTabOrder(self.geschlechtEdit, self.klasseEdit)
        Dialog.setTabOrder(self.klasseEdit, self.createNew)
        Dialog.setTabOrder(self.createNew, self.addInto)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Aus Excel-Tabelle importieren - FFSportfest"))
        self.groupBox_2.setTitle(_translate("Dialog", "Schritt 3a: Spalten auswählen"))
        self.label_2.setText(_translate("Dialog", "Nachnamen:"))
        self.label_4.setText(_translate("Dialog", "Geschlecht:"))
        self.label_3.setText(_translate("Dialog", "Vornamen:"))
        self.vornameEdit.setToolTip(_translate("Dialog", "<html><head/><body><p>Geben Sie die Spalte ein, in welchem sich die Vornamen befinden (z.B: B)</p></body></html>"))
        self.vornameEdit.setPlaceholderText(_translate("Dialog", "B"))
        self.nameEdit.setToolTip(_translate("Dialog", "<html><head/><body><p>Geben Sie die Spalte ein, in welchem sich die Nachnamen befinden (z.B: A)</p></body></html>"))
        self.nameEdit.setPlaceholderText(_translate("Dialog", "A"))
        self.geschlechtBox.setToolTip(_translate("Dialog", "<html><head/><body><p>Gibt an ob das Geschlecht in der Tabelle vorhanden ist.</p><p><br/></p><p>Ist das <span style=\" font-weight:600;\">Auswahlfeld aktiviert</span>, wird das Geschlecht <span style=\" font-weight:600;\">aus der angegebenen Spalte</span> aus der Tabelle <span style=\" font-weight:600;\">übernommen.</span></p><p>Ist das <span style=\" font-weight:600;\">Auswahlfeld nicht aktiviert</span>, wird das <span style=\" font-weight:600;\">angegebene Geschlecht </span>(M/W)<span style=\" font-weight:600;\"> für alle Schüler</span> eingetragen (und kann später geändert werden).</p></body></html>"))
        self.geschlechtBox.setText(_translate("Dialog", "Vorhanden"))
        self.geschlechtEdit.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Wenn Geschlecht vorhanden aktiviert:</span></p><p>Geben Sie die Spalte ein, in welchem sich das Geschlecht der Schüler befindet.</p><p><span style=\" font-weight:600;\">Wenn Geschlecht vorhanden nicht aktiviert:</span></p><p>Geben Sie das Geschlecht für alle Schüler ein (M = Männlich, W = Weiblich)</p></body></html>"))
        self.geschlechtEdit.setPlaceholderText(_translate("Dialog", "C"))
        self.label_5.setText(_translate("Dialog", "Klasse:"))
        self.klasseBox.setToolTip(_translate("Dialog", "<html><head/><body><p>Gibt an ob die Klasse in der Tabelle vorhanden ist.</p><p><br/></p><p>Ist das <span style=\" font-weight:600;\">Auswahlfeld aktiviert</span>, wird die Klasse <span style=\" font-weight:600;\">aus der angegebenen Spalte</span> aus der Tabelle <span style=\" font-weight:600;\">übernommen.</span></p><p>Ist das <span style=\" font-weight:600;\">Auswahlfeld nicht aktiviert</span>, werden <span style=\" font-weight:600;\">alle Schüler in eine Klasse</span> eingefügt.</p></body></html>"))
        self.klasseBox.setText(_translate("Dialog", "Vorhanden"))
        self.klasseEdit.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Wenn Klasse vorhanden aktiviert:</span></p><p>Geben Sie die Spalte ein, in welcher sich die Klassen der Schüler befinden. Die Klassen müssen im Format X.X (z.B. <span style=\" font-style:italic;\">5.1</span>) sein.</p><p><span style=\" font-weight:600;\">Wenn Klasse vorhanden nicht aktiviert:</span></p><p>Geben Sie die Klasse für alle Schüler ein (z.B. 5.3)</p></body></html>"))
        self.klasseEdit.setPlaceholderText(_translate("Dialog", "D"))
        self.groupBox_3.setTitle(_translate("Dialog", "Schritt 5: Daten speichern"))
        self.createNew.setToolTip(_translate("Dialog", "<html><head/><body><p>Erstellt aus den Schülern der Excel-Tabelle eine neue Datenbank.</p></body></html>"))
        self.createNew.setText(_translate("Dialog", "Als neue Datenbank speichern"))
        self.addInto.setToolTip(_translate("Dialog", "<html><head/><body><p>Fügt die Schüler aus der Excel-Tabelle in eine existierende Datenbank ein. Sollte ein Schüler schon existieren wird er <span style=\" font-weight:600;\">nicht</span> überschrieben, es kann also zu Duplikaten kommen. Sie sollten die Datenbank anschließend darauf untersuchen.</p></body></html>"))
        self.addInto.setText(_translate("Dialog", "Eine Klasse in vorh. Datenbank einfügen"))
        self.groupBox.setTitle(_translate("Dialog", "Schritt 1: Excel-Tabelle öffnen"))
        self.excelOpen.setText(_translate("Dialog", "Datei öffnen..."))
        self.excelPath.setText(_translate("Dialog", "Keine ausgewählt..."))
        self.groupBox_4.setTitle(_translate("Dialog", "Schritt 2: Arbeitsblatt auswählen"))
        self.openSheet.setText(_translate("Dialog", "Öffnen"))
        self.groupBox_5.setTitle(_translate("Dialog", "Schritt 3b: Zeilen auswählen"))
        self.allRows.setText(_translate("Dialog", "Alle Zeilen"))
        self.areaRows.setText(_translate("Dialog", "Bereich:"))
        self.rowMin.setPrefix(_translate("Dialog", "von "))
        self.rowMax.setPrefix(_translate("Dialog", "bis "))
        self.groupBox_6.setTitle(_translate("Dialog", "Schritt 4: Vorschau (1. Element lt. gewählten Spalten/Zeilen)"))
        self.vornameLabel.setText(_translate("Dialog", "Vorname:"))
        self.nachnameLabel.setText(_translate("Dialog", "Nachname:"))
        self.geschlechtLabel.setText(_translate("Dialog", "Geschlecht:"))
        self.klasseLabel.setText(_translate("Dialog", "Klasse:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

