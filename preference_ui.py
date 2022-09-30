import sys
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QListWidget, QFrame,\
QPushButton, QLabel, QLineEdit, QComboBox,\
QHBoxLayout, QVBoxLayout, QStackedLayout, QFormLayout

class Page1(QWidget):
    def __init__(self):
        super(Page1, self).__init__()
        
        self.button = QPushButton('Page1')
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.button)

class Page2(QWidget):
    def __init__(self):        
        super(Page2, self).__init__()
        
        self.font = QFont()
        self.font.setBold(True)
        
        self.vbox = QVBoxLayout()
        self.base()
        self.cutting() 
        
        self.setLayout(self.vbox)
        
    def base(self):
        
        self.plateLabel = QLabel('Base Plate')
        self.plateLabel.setFont(self.font)
        self.vbox.addWidget(self.plateLabel)
        
        flo = QFormLayout()
        self.vbox.addLayout(flo)
        
        thickbox = QLineEdit(self)
        flo.addRow('Thickness (mm)', thickbox)
    
    def cutting(self):
        self.cutLabel = QLabel('Cutting Guide')
        self.cutLabel.setFont(self.font)
        self.vbox.addWidget(self.cutLabel)
        
        flo = QFormLayout()
        self.vbox.addLayout(flo)
        
        thickbox = QLineEdit(self)
        flo.addRow('Cutting Thickness (mm)', thickbox)
        
        wall_thickbox = QLineEdit(self)
        flo.addRow('Wall Thickness (mm)', wall_thickbox)
        
        height_box = QLineEdit(self)
        flo.addRow('Minimum Height (mm)', height_box)
        
        mode_cb = QComboBox(self)
        mode_cb.addItems(['Max-Z', 'Adaptive'])
        flo.addRow('Mode', mode_cb)
        
        end_cb = QComboBox(self)
        end_cb.addItems(['Open', 'Closed'])
        flo.addRow('End Finishing', end_cb)

    
class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.widget1 = QWidget()
        self.widget2 = QWidget()
        self.setCentralWidget(self.widget1)
        
        self.hbox1 = QHBoxLayout()
        self.hbox2 = QHBoxLayout()
        self.vbox = QVBoxLayout()
        
        self.page1 = Page1()
        self.page2 = Page2()
        
        self.left = LeftWindow()
        
        #self.mul_page()
        self.initbutton()
           
        self.hbox1.addWidget(self.left)
        self.hbox1.addWidget(self.page2)
        
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        
        self.widget1.setLayout(self.vbox)
        self.setWindowTitle('Preferences')
        self.setFixedSize(900, 600)
    
    def initbutton(self):
        
        self.applyButton = QPushButton('Apply')
        self.hbox2.addWidget(self.applyButton)
        self.closeButton = QPushButton('Cancel')
        self.closeButton.clicked.connect(self.close)
        self.hbox2.addWidget(self.closeButton)
    
    def mul_page(self):
        
        self.stacked_layout = QStackedLayout()
        self.widget2.setLayout(self.stacked_layout)
        self.stacked_layout.addWidget(self.page1)
        self.stacked_layout.addWidget(self.page2)
        
    def page1_clicked(self):
        self.stacked_layout.setCurrentIndex(0)
        
    def page2_clicked(self):
        self.stacked_layout.setCurrentIndex(1)
        
class LeftWindow(QListWidget):
    
    def __init__(self):
        super(LeftWindow, self).__init__()
        
        self.addItem('General')
        #self.itemClicked.connect()
        self.addItem('Preset')
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()