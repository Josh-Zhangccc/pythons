import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                                QTextEdit, QLabel, 
                                QStatusBar,QVBoxLayout,
                                 QToolBar,QFileDialog)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("菜单栏和工具栏示例")
        self.setGeometry(100, 100, 800, 600)
        self.edit=Edit(self)
        self.text=QTextEdit()
        self.setCentralWidget(self.text)#
        self.file_name=QLabel("You haven't select any files")


        layout=QVBoxLayout()
        layout.addWidget(self.file_name)


        #创建状态栏
        self.bar=QStatusBar()
        self.setStatusBar(self.bar)
        self.bar.showMessage('Just do it')

        #创建菜单栏
        self.create_menus()#自定义的函数

        #创建工具栏
        self.create_toolbar()#自定义的函数

    def create_menus(self):
        menu_bar=self.menuBar()#获取菜单，没有就自动创建
        file_menu=menu_bar.addMenu('files')#创建file菜单

        open_action=QAction('open',self)
        open_action.setShortcut('Ctrl+o')
        open_action.triggered.connect(self.edit.open_file)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        ####
        edit_mune=menu_bar.addMenu('edit')

        copy_action=QAction('copy',self)
        copy_action.setShortcut('Fn+Ctrl+c')
        copy_action.triggered.connect(self.edit.copy)
        edit_mune.addAction(copy_action)

        paste_action=QAction('paste',self)
        paste_action.setShortcut('Fn+Ctrl+v')
        paste_action.triggered.connect(self.edit.paste)
        edit_mune.addAction(paste_action)

    def create_toolbar(self):
        toolbar=QToolBar('tools')
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        open_action=QAction('open',self)
        open_action.setShortcut('Ctrl+o')
        open_action.triggered.connect(self.edit.open_file)
        toolbar.addAction(open_action)
        toolbar.addSeparator()
    
class Edit():
    def __init__(self, parent=None):
        self.save=''
        self.file_path=''
        self.broad=[]
        self.parent = parent
    def copy(self):
        self.broad.append(self.save)
        if len(self.broad)>10:
            self.broad=self.broad[-10:]
        else:
            pass
    def paste(self):
        if len(self.broad)!=0:
            return self.broad[-1]
        else:
            pass
    def choice_paste(self,n):
        if len(self.broad)!=0:
            return self.broad[-n]
        else:
            pass
    def open_file(self):
        self.file_path,_=QFileDialog.getOpenFileName(
            self.parent,
            'select file',
            '',#初始目录
            "all the file(*);;text(*.txt);;python file(*.py)")#fliter
        if self.file_path:
            self.save=self.file_path
            self.file_path=''

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec())