import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QPushButton, QLabel, QVBoxLayout, 
                               QLineEdit,QWidget,QMessageBox)

class MainWindow(QMainWindow):#继承QMainWindow的属性
    def __init__(self):
        super().__init__()#调用QMainWindow的属性
        self.setWindowTitle('class based window')
        self.setGeometry(200,200,1000,625)
        #self就是在调用QMainWindow
        #接下来放置组件
        self.button=QPushButton('click me',self)
        self.label=QLabel("You haven't click me")
        self.name_input=QLineEdit()
        self.name_input.setPlaceholderText('Please input your name')
        self.submit_button=QPushButton('enter')
        self.greeting_label=QLabel('Hi!,e...your name?')
        
        #布局
        layout=QVBoxLayout()
        layout.addWidget(self.greeting_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        container=QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        #链接按钮与函数（信号和槽）
        self.button.clicked.connect(self.on_cilck_button)
        self.submit_button.clicked.connect(self.on_submit_clicked)
        self.name_input.returnPressed.connect(self.on_submit_clicked)
    def on_cilck_button(self):
        QMessageBox.information(self,'please ingore me','noting series~')
        QMessageBox.warning(self,'Warning',"Don't cilck NO!")
        reply=QMessageBox.question(self,'Question','Do you want to go on?',
                                   QMessageBox.Yes|QMessageBox.No,
                                   QMessageBox.Yes)
        if reply==QMessageBox.Yes:
            self.label.setText("Let's go on!")
        else:
           self.label.setText('You click the me!')
    
    def on_submit_clicked(self):
        name=self.name_input.text()
        self.greeting_label.setText(f'Hi!{name}!')

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())
