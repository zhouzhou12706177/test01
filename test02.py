import sys
from PyQt4 import QtGui,QtCore

class windowTest(QtGui.QDialog):
    def __init__(self):
        super(windowTest,self).__init__(parent=None)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("rename Func")
        self.setLayout(QtGui.QVBoxLayout())
        #self.setFixedWidth(320)
        #self.setFixedHeight(285)
        self.layout().setAlignment(QtCore.Qt.AlignTop)
        self.layout().setContentsMargins(0,0,0,0)
        
        rename_widget=QtGui.QWidget()
        rename_widget.setLayout(QtGui.QVBoxLayout())
        rename_widget.layout().setContentsMargins(10,10,10,0)
        rename_widget.layout().setSpacing(8)
        rename_widget.setSizePolicy(QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Fixed)
        self.layout().addWidget(rename_widget)
         
        rename_text_layout=QtGui.QHBoxLayout()
        rename_text_layout.setContentsMargins(0,0,0,0)
        rename_text_layout.setSpacing(20)
        
        lineA=mySplitter("RENAME")
        rename_widget.layout().addWidget(lineA)
        
        rename_text_lb =QtGui.QLabel("new name:")
        rename_text_le =QtGui.QLineEdit()
        rename_text_le.setFixedWidth(200)
        rename_text_layout.addWidget(rename_text_lb)
        rename_text_layout.addWidget(rename_text_le)
        rename_widget.layout().addLayout(rename_text_layout)
        
        rename_mult_layout=QtGui.QHBoxLayout()
        rename_mult_layout.setContentsMargins(0,0,0,0)
        
        rename_mult_lb=QtGui.QLabel("Multiples Naming Method:")
        rename_mult_combo=QtGui.QComboBox()
        rename_mult_combo.addItems(['Number (1-9)','Letters (a-z)'])
        rename_mult_combo.setFixedWidth(100)
        
        rename_mult_layout.addWidget(rename_mult_lb)
        rename_mult_layout.addWidget(rename_mult_combo)
        rename_widget.layout().addLayout(rename_mult_layout)
        
        mult_options_layout=QtGui.QHBoxLayout()
        rename_widget.layout().addLayout(mult_options_layout)
        frame_pad_lb=QtGui.QLabel('No. Padding:')
        frame_pad_spin=QtGui.QSpinBox()
        frame_pad_spin.setFixedWidth(40)
        frame_pad_spin.setMinimum(0)
        frame_pad_spin.setMaximum(10)
        
        mult_options_layout.addWidget(frame_pad_lb)
        mult_options_layout.addWidget(frame_pad_spin)
        
        lower_radio=QtGui.QRadioButton('Lowercase')
        upper_radio=QtGui.QRadioButton('Uppercase')
        
        
        fix_layout=QtGui.QHBoxLayout()
        rename_widget.layout().addLayout(fix_layout)
        
        prefix_check=QtGui.QCheckBox('Prefix:')
        # prefix_check.stateChanged.connect()
        prefix_le=QtGui.QLineEdit()
        prefix_le.setEnabled(False)
        
        suffix_check=QtGui.QCheckBox('Suffix:')
        suffix_le=QtGui.QLineEdit()
        suffix_le.setEnabled(False)
        
        fix_layout.addWidget(prefix_check)
        fix_layout.addWidget(prefix_le)
        fix_layout.addSpacerItem(QtGui.QSpacerItem(50,5,QtGui.QSizePolicy.Expanding))
        fix_layout.addWidget(suffix_check)
        fix_layout.addWidget(suffix_le)
        
        previos_layout=QtGui.QHBoxLayout()
        rename_widget.layout().addLayout(previos_layout)
        previos_lb=QtGui.QLabel('e.g.')
        rename_button=QtGui.QPushButton('Rename')
        rename_button.setFixedWidth(60)
        previos_layout.addWidget(previos_lb)
        previos_layout.addWidget(rename_button)
        
        #replace Widget
        
        replace_Widget=QtGui.QWidget()
        replace_Widget.setLayout(QtGui.QVBoxLayout())
        self.layout().addWidget(replace_Widget)
        
        lineB=mySplitter("FIND/REPLACE")
        replace_Widget.layout().addWidget(lineB)
        
        replace_lb=QtGui.QLabel('Find:')
        replace_le=QtGui.QLineEdit()
        with_lb=QtGui.QLabel("replace:")
        with_le=QtGui.QLineEdit()
        
        replace_layout=QtGui.QHBoxLayout()
        replace_layout.addWidget(replace_lb)
        replace_layout.addWidget(replace_le)
        
        with_layout=QtGui.QHBoxLayout()
        with_layout.addWidget(with_lb)
        with_layout.addWidget(with_le)
        
        replace_Widget.layout().addLayout(replace_layout)
        replace_Widget.layout().addLayout(with_layout)
        
        selection_layou=QtGui.QHBoxLayout()
        selection_lb=QtGui.QLabel('Selection Mode:')
        all_radio=QtGui.QRadioButton('All')
        selection_radio=QtGui.QRadioButton('Selected')
        
        selection_layou.addWidget(selection_lb)
        selection_layou.addWidget(all_radio)
        selection_layou.addWidget(selection_radio)
        
        replace_Widget.layout().addLayout(selection_layou)
        
        replace_button_layout=QtGui.QHBoxLayout()
        replace_button_layout.setAlignment(QtCore.Qt.AlignRight)
        replace_button=QtGui.QPushButton('Replace')
        replace_button_layout.addWidget(replace_button)
        
        replace_Widget.layout().addLayout(replace_button_layout)
        
        
        
        
        
        
        
    def on_button(self):
        print "hello"
        #self.setWindowTitle(self.te.toPlainText())
class mySplitter(QtGui.QWidget):
    def __init__(self,text,color=(50,50,50),shadow=True):
        super(mySplitter,self).__init__(parent=None)
        
        self.setMinimumHeight(2)
        self.setLayout(QtGui.QHBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)
        
        first_line=QtGui.QFrame()
        first_line.setFrameStyle(QtGui.QFrame.HLine|QtGui.QFrame.Plain)
        first_line.setMaximumWidth(15)
        # first_line.setMinimumHeight(4)
        # first_line.setLineWidth(4)
        
        main_color="rgba(%s,%s,%s,255)"%(color[0],color[1],color[2])
        shadow_color=""
        if shadow==True:
            shadow_color="rgba(150,150,150,255)"
        
        lineStyleSheet="background-color:%s; \
                                 border-bottom:1px solid %s;"%(main_color,shadow_color)
        first_line.setStyleSheet(lineStyleSheet)
        # main_line.setFixedHeight(5)
        self.layout().addWidget(first_line)
        
        
        font=QtGui.QFont()
        font.setBold(True)
        textSize=QtGui.QFontMetrics(font)
        text_width=textSize.width(text)+6
        text_lb=QtGui.QLabel()
        text_lb.setText(text)
        text_lb.setFont(font)
        text_lb.setMaximumWidth(text_width)
        text_lb.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.layout().addWidget(text_lb)
        
        second_line=QtGui.QFrame()
        second_line.setFrameStyle(QtGui.QFrame.HLine|QtGui.QFrame.Plain)
        second_line.setStyleSheet(lineStyleSheet)
        
        self.layout().addWidget(second_line)
        
        
        
app=QtGui.QApplication(sys.argv) 

win=windowTest()
win.show()
app.exec_()