from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(913, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(762, 398))
        Form.setBaseSize(QSize(762, 389))
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font1)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font1)

        self.horizontalLayout_4.addWidget(self.lineEdit_4)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font1)

        self.horizontalLayout_4.addWidget(self.pushButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setTabletTracking(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)
        self.pushButton.setContextMenuPolicy(Qt.PreventContextMenu)

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0420\u0435\u0448\u0435\u043d\u0438\u0435 \u0421\u041b\u0410\u0423", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0434\u0430\u0439\u0442\u0435 \u0442\u043e\u0447\u043d\u043e\u0441\u0442\u044c \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u0439:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0434\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0434\u0430\u0439\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u044b\u0445:", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0434\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0435\u043d\u0442\u044b \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0439:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041c\u0435\u0442\u043e\u0434 \u0413\u0430\u0443\u0441\u0430:", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0441\u0447\u0435\u0442", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041c\u0435\u0442\u043e\u0434 \u041a\u0440\u0430\u043c\u0435\u0440\u0430:", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0441\u0447\u0435\u0442", None))
    # retranslateUi

