# 影视资源搜索工具

软件打包方法

1. 安装依赖

   ```python
   pip3 install -r requirements.txt
   ```

2. 打包exe文件

   ```py
   pyinstaller -w -F -i icon.ico index.py
   ```

3. 如果修改了UI文件, 则需要重新生成

   ```python
   # 主窗口UI
   pyuic5 -o ./ui/main_ui.py ./ui/main_ui.ui
   # 版本信息窗口
   pyuic5 -o ./ui/about.py ./ui/about.ui
   ```



软件运行界面

![1](https://github.com/nofaceleon/source_search/blob/master/screenshots/1.PNG?raw=true)



![1](https://github.com/nofaceleon/source_search/blob/master/screenshots/2.PNG?raw=true)



![1](https://github.com/nofaceleon/source_search/blob/master/screenshots/3.PNG?raw=true)



![1](https://github.com/nofaceleon/source_search/blob/master/screenshots/4.PNG?raw=true)
