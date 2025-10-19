import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                               QGridLayout, QLabel, QLineEdit, 
                               QPushButton, QTextEdit)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("网格布局示例")
        self.setGeometry(100, 100, 600, 400)
        
        # 创建中心控件和网格布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)
        
        # 创建控件
        name_label = QLabel("姓名:")
        self.name_input = QLineEdit()
        
        email_label = QLabel("邮箱:")
        self.email_input = QLineEdit()
        
        phone_label = QLabel("电话:")
        self.phone_input = QLineEdit()
        
        address_label = QLabel("地址:")
        self.address_input = QTextEdit()
        self.address_input.setMaximumHeight(80)  # 限制高度
        
        submit_button = QPushButton("提交")
        clear_button = QPushButton("清除")
        
        # 将控件添加到网格布局中
        # 格式: addWidget(控件, 行, 列, 行跨度, 列跨度)
        grid_layout.addWidget(name_label, 0, 0)  # 第0行，第0列
        grid_layout.addWidget(self.name_input, 0, 1)  # 第0行，第1列
        
        grid_layout.addWidget(email_label, 1, 0)  # 第1行，第0列
        grid_layout.addWidget(self.email_input, 1, 1)  # 第1行，第1列
        
        grid_layout.addWidget(phone_label, 2, 0)  # 第2行，第0列
        grid_layout.addWidget(self.phone_input, 2, 1)  # 第2行，第1列
        
        grid_layout.addWidget(address_label, 3, 0)  # 第3行，第0列
        grid_layout.addWidget(self.address_input, 3, 1)  # 第3行，第1列
        
        # 按钮放在第4行，跨两列
        grid_layout.addWidget(submit_button, 4, 0, 1, 2)  # 第4行，第0列开始，跨2列
        grid_layout.addWidget(clear_button, 5, 0, 1, 2)   # 第5行，第0列开始，跨2列
        
        # 连接信号与槽
        submit_button.clicked.connect(self.submit_form)
        clear_button.clicked.connect(self.clear_form)
    
    def submit_form(self):
        name = self.name_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()
        address = self.address_input.toPlainText()
        
        print(f"姓名: {name}")
        print(f"邮箱: {email}")
        print(f"电话: {phone}")
        print(f"地址: {address}")
        
        # 这里可以添加表单提交的逻辑
    
    def clear_form(self):
        self.name_input.clear()
        self.email_input.clear()
        self.phone_input.clear()
        self.address_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())