import time

from ui.main_ui import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem
from core.moviedl import moviedl


class main(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.setupUi(self)
        self.logic()

    # 业务逻辑
    def logic(self):
        self.searchBtn.clicked.connect(self.search)  # 监听点击事件

    # 开始搜索
    def search(self):
        # 不在主线程中执行这个

        # self.movieName.setReadOnly(True)
        keyword = self.movieName.text()  # 获取关键字
        md = moviedl()
        start = time.time()
        data = md.run(keyword)
        end = time.time()
        total_time = '%.2f' % (end - start)
        self.showResult(data)
        self.statusbar.showMessage(f"【{keyword}】 搜索完成, 共找到{len(data)}条数据, 总耗时{total_time}s")
        # if data:
        #     self.statusbar.showMessage(f"【{keyword}】 搜索完成, 共找到{len(data)}条数据 总耗时{total_time}s")
        # else:
        #     self.statusbar.showMessage(f"【{keyword}】 搜索完成, 没有找到任何资源, 总耗时{total_time}s")
        # self.movieName.setReadOnly(False)

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
    ui = main()
    ui.show()
    sys.exit(app.exec_())
