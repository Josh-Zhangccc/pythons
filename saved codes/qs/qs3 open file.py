import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QPushButton, QLabel, QVBoxLayout, 
                               QLineEdit,QWidget,QMessageBox,
                               QFileDialog)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('open file')
        self.setGeometry(100,100,400,400)
        
        self.open_btn=QPushButton('open file')
        self.save_btn=QPushButton('save file')
        self.file_name=QLabel("You haven't select any files")

        layout=QVBoxLayout()
        layout.addWidget(self.open_btn)
        layout.addWidget(self.save_btn)
        layout.addWidget(self.file_name)
        container=QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


        self.open_btn.clicked.connect(self.open_file)
        self.save_btn.clicked.connect(self.save_file)

    def open_file(self):
        file_path,_=QFileDialog.getOpenFileName(
            self,
            'select file',
            '',#初始目录
            "all the file(*);;text(*.txt);;python file(*.py)")#fliter
        if file_path:
            self.file_name.setText(f'You selected {file_path}')
    def save_file(self):
        file_path,_=QFileDialog.getSaveFileName(
            self,
            'select file',
            '',
            '')
        if file_path:
            self.file_name.setText(f'Save file into {file_path}')

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())
