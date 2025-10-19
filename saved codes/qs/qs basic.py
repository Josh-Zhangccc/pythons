import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QPushButton, QLabel, QVBoxLayout, QWidget)
app = QApplication(sys.argv)
#QApplication是主程序，argv在帮助我传递信号
window=QMainWindow()
window.setWindowTitle('qs basic')
window.setGeometry(100,100,400,400)#在在100，100的位置创建一个400x100的窗口
window.show()

sys.exit(app.exec())
#exec一直在循环，检测用户的动作（事件）‘发动机’，exit保证退出程序‘遏制器’