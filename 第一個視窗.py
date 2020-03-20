import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 創建一個視窗
    w = QWidget()
    # 設置視窗尺寸
    w.resize(400, 200)
    # 移動視窗
    w.move(300, 300)
    # 設置視窗名稱
    w.setWindowTitle('第一個桌面應用')
    # 顯示視窗
    w.show()
    # 進入程序並通過exit函數確保安全離開
    sys.exit(app.exec())
