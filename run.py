import sys
import 練習1  #.檔案名稱


from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = 練習1.Ui_MainWindow()
    # 向視窗添加控鍵
    ui.setupUi(mainWindow)
    mainWindow.show()#顯示視窗
    sys.exit(app.exec())


