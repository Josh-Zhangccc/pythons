import sys
import random
import math
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QLabel, QPushButton, QMessageBox)
from PySide6.QtCore import QTimer, Qt, QRectF, QPointF
from PySide6.QtGui import QPainter, QColor, QFont, QKeyEvent

class GameWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFocusPolicy(Qt.StrongFocus)  # 允许接收键盘事件
        
        # 游戏状态
        self.game_active = False
        self.game_over = False
        
        # 玩家设置
        self.player_radius = 15
        self.player_pos = QPointF(400, 300)  # 初始位置在中心
        self.player_speed = 10
        
        # 敌人设置
        self.enemies = []
        self.enemy_radius = 10
        self.enemy_speed = 3
        self.spawn_timer = 0
        self.spawn_interval = 60 # 每60帧生成一个新敌人
        
        # 游戏数据
        self.score = 0
        self.survival_time = 0
        
        # 设置定时器
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_game)
        self.timer.start(16)  # 约60FPS
        
        # 初始化UI
        self.init_ui()
    
    def init_ui(self):
        # 创建游戏信息显示
        self.score_label = QLabel("分数: 0",)
        self.time_label = QLabel("时间: 0")
        self.score_label.setFont(QFont("Arial", 14))
        self.time_label.setFont(QFont("Arial", 14))
        
        # 创建按钮
        self.start_button = QPushButton("开始游戏")
        self.start_button.clicked.connect(self.start_game)
        
        # 布局
        info_layout = QHBoxLayout()
        info_layout.addWidget(self.score_label)
        info_layout.addWidget(self.time_label)
        info_layout.addStretch()
        info_layout.addWidget(self.start_button)
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(info_layout)
        main_layout.addStretch()
        self.setLayout(main_layout)
        
        # 设置窗口大小
        self.setMinimumSize(800, 600)

    
    def start_game(self):
        # 重置游戏状态
        self.game_active = True
        self.game_over = False
        self.player_pos = QPointF(400, 300)
        self.enemies = []
        self.score = 0
        self.survival_time = 0
        self.spawn_timer = 0
        
        # 更新UI
        self.update_labels()
        self.start_button.setEnabled(False)
    
    def update_game(self):
        if not self.game_active or self.game_over:
            return
        
        # 更新生存时间
        self.survival_time += 1/60  # 每秒60帧
        self.update_labels()
        self.spawn_interval=max(10,int(60-self.survival_time*2))
        # 生成新敌人
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_enemy()
            self.spawn_timer = 0
        
        # 移动敌人
        self.move_enemies()
        
        # 检测碰撞
        self.check_collisions()
        
        # 重绘游戏画面
        self.update()
    
    def spawn_enemy(self):
        # 随机选择生成边 (0=上, 1=右, 2=下, 3=左)
        side = random.randint(0, 3)
        
        if side == 0:  # 上边
            x = random.randint(0, self.width())
            y = -self.enemy_radius
            dx = random.uniform(-2, 2)
            dy = random.uniform(0.2, 2)
        elif side == 1:  # 右边
            x = self.width() + self.enemy_radius
            y = random.randint(0, self.height())
            dx = random.uniform(-2, -0.2)
            dy = random.uniform(-2, 2)
        elif side == 2:  # 下边
            x = random.randint(0, self.width())
            y = self.height() + self.enemy_radius
            dx = random.uniform(-2, 2)
            dy = random.uniform(-2, -0.2)
        else:  # 左边
            x = -self.enemy_radius
            y = random.randint(0, self.height())
            dx = random.uniform(0.2, 2)
            dy = random.uniform(-2, 2)
        
        # 标准化方向向量并乘以速度
        length = math.sqrt(dx*dx + dy*dy)
        dx = dx / length * self.enemy_speed
        dy = dy / length * self.enemy_speed
        
        # 添加新敌人
        self.enemies.append({
            'pos': QPointF(x, y),
            'vel': QPointF(dx, dy)
        })
    
    def move_enemies(self):
        for enemy in self.enemies:
            enemy['pos'] += enemy['vel']
            
            # 移除超出屏幕的敌人并增加分数
            if (enemy['pos'].x() < -self.enemy_radius or 
                enemy['pos'].x() > self.width() + self.enemy_radius or
                enemy['pos'].y() < -self.enemy_radius or
                enemy['pos'].y() > self.height() + self.enemy_radius):
                self.enemies.remove(enemy)
                self.score += 1
                self.update_labels()
    
    def check_collisions(self):
        for enemy in self.enemies:
            # 计算玩家与敌人之间的距离
            dx = self.player_pos.x() - enemy['pos'].x()
            dy = self.player_pos.y() - enemy['pos'].y()
            distance = math.sqrt(dx*dx + dy*dy)
            
            # 如果距离小于两球半径之和，则发生碰撞
            if distance < self.player_radius + self.enemy_radius:
                self.game_over = True
                self.show_game_over()
                return
    
    def keyPressEvent(self, event: QKeyEvent):
        if not self.game_active or self.game_over:
            return
        
        # 处理键盘输入
        if event.key() == Qt.Key_Left:
            self.player_pos.setX(max(self.player_radius, self.player_pos.x() - self.player_speed))
        elif event.key() == Qt.Key_Right:
            self.player_pos.setX(min(self.width() - self.player_radius, self.player_pos.x() + self.player_speed))
        elif event.key() == Qt.Key_Up:
            self.player_pos.setY(max(self.player_radius, self.player_pos.y() - self.player_speed))
        elif event.key() == Qt.Key_Down:
            self.player_pos.setY(min(self.height() - self.player_radius, self.player_pos.y() + self.player_speed))
        
        # 重绘画面
        self.update()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 绘制背景
        painter.fillRect(self.rect(), QColor(120,150,52))
        if not self.game_active:
            # 绘制游戏说明
            painter.setFont(QFont("Arial", 16))
            painter.drawText(self.rect(), Qt.AlignCenter, "按「开始游戏」按钮开始游戏\n使用方向键控制白色小球移动")
            return
        
        # 绘制玩家
        painter.setBrush(QColor(255, 255, 255))
        painter.setPen(QColor(0, 0, 0))
        painter.drawEllipse(self.player_pos, self.player_radius, self.player_radius)
        
        # 绘制敌人
        for enemy in self.enemies:
            painter.setBrush(QColor(0, 0, 0))
            painter.setPen(QColor(0, 0, 0))
            painter.drawEllipse(enemy['pos'], self.enemy_radius, self.enemy_radius)
        
        if self.game_over:
            # 绘制游戏结束信息
            painter.setFont(QFont("Arial", 24))
            painter.drawText(self.rect(), Qt.AlignCenter, f"游戏结束!\n存活时间: {self.survival_time:.1f}秒\n得分: {self.score}")
    
    def update_labels(self):
        self.score_label.setText(f"分数: {self.score}")
        self.time_label.setText(f"时间: {self.survival_time:.1f}秒")
    
    def show_game_over(self):
        self.start_button.setEnabled(True)
        QMessageBox.information(self, "游戏结束", 
                               f"游戏结束!\n你存活了 {self.survival_time:.1f} 秒\n得分: {self.score}")

class DodgeBallGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("躲避球游戏")
        self.setGeometry(100, 100, 800, 600)
        
        # 创建游戏部件
        self.game_widget = GameWidget()
        self.setCentralWidget(self.game_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DodgeBallGame()
    window.show()
    sys.exit(app.exec())