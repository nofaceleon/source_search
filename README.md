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

![1](https://p.pstatp.com/origin/pgc-image/725d64854eba4f0891b855c2f28ce6ea)



![1](https://p.pstatp.com/origin/pgc-image/f6981808e9c54e7d91af60ec6b41d148)



![1](https://p.pstatp.com/origin/pgc-image/a73dbb9ded8f4d209ffac56029ead03f)



![1](https://p.pstatp.com/origin/pgc-image/346d4c90910b4600a567a73b559a7852)