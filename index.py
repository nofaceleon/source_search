import time
from ui.main_ui import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem, QWidget
from core.moviedl import moviedl
from PyQt5.QtCore import QObject, pyqtSignal
from threading import Thread
from ui.about import Ui_Dialog


# 修改ui文件后重新复发布py文件 : pyuic5 -o ./ui/main_ui.py ./ui/main_ui.ui
# 打包exe : pyinstaller -w -F -i icon.ico index.py


# 使用自定义信号去控制页面元素的修改
class mySignal(QObject):
    btnChange = pyqtSignal(str)  # 自定义信号
    statusBarChange = pyqtSignal(str)


# 每一个窗口都是一个类文件
# 版本信息窗口
class dialog_w(Ui_Dialog, QWidget):
    def __init__(self):
        super(dialog_w, self).__init__()
        self.setupUi(self)

# 主程序
class main(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.ms = mySignal()  # 实例化自定义信号
        self.logic()

    # 业务逻辑
    def logic(self):
        self.searchBtn.clicked.connect(self.search)  # 监听点击事件
        self.actionversion.triggered.connect(self.show_about)

        self.ms.btnChange.connect(self.btn_text_change)  # 监听自定义信号
        self.ms.statusBarChange.connect(self.status_bar_text_change)

    # 显示版本信息页面
    def show_about(self):
        # 控制显示, 必须是全局变量才能监听, 否则会闪退
        dialog.show()
        # QMessageBox.information(self, '关于', content, QMessageBox.Ok)

    # 修改按钮文字
    def btn_text_change(self, text):
        self.searchBtn.setText(text)

    # 修改状态文字
    def status_bar_text_change(self, text):
        self.statusbar.showMessage(text)

    # 开始搜索
    def search(self):
        # 不在主线程中执行这个
        keyword = self.movieName.text()  # 获取关键字
        self.ms.btnChange.emit('搜索中')  # 发送自定义信号
        self.ms.statusBarChange.emit(f"【{keyword}】 正在搜索中....")

        # 使用多线程来防止阻塞,影响页面渲染
        def t_run(key):
            md = moviedl()
            start = time.time()
            data = md.run(key)
            end = time.time()
            total_time = '%.2f' % (end - start)
            self.showResult(data)
            self.ms.statusBarChange.emit(f"【{key}】 搜索完成, 共找到 {len(data)} 条数据, 总耗时 {total_time}s")
            self.ms.btnChange.emit('开始搜索')  # 发送自定义信号

        task = Thread(target=t_run, args=(keyword,))  # 线程只有一个参数的时候也必须用元组的方式传递参数
        task.start()

    # 结果展示
    def showResult(self, data):
        self.searchRes.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
        self.searchRes.setRowCount(len(data))
        row = 0
        for i in data:
            self.searchRes.setItem(row, 0, QTableWidgetItem(i['source']))
            self.searchRes.setItem(row, 1, QTableWidgetItem(i['movie_name']))
            self.searchRes.setItem(row, 2, QTableWidgetItem(i['movie_link']))
            row += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = main()  # 主窗口实例化
    ui.show()  # 主窗口展示
    dialog = dialog_w()  # 子窗口只能全局实例化
    sys.exit(app.exec_())
