from core.sourceWeb import *
import threading


class moviedl():
    # 配置搜索网站
    def source_targs(self):
        """初始化资源搜索网站"""
        source_tags = {
            'pianku': pianku,
            'idybee': idybee,
            # 'mp4': mp4,
            'piaohua': piaohua,
            'subaibai': subaibai,
            'naifei': naifei,
            'yinfans': yinfans,
            'mypianku': mypianku
        }
        return source_tags

    def run(self, keyword):
        results = self.thread_search(keyword, self.source_targs())
        if results:
            return results
        else:
            return []

    def thread_search(self, keyword, source_targs):
        """
        多线程搜索
        :param keyword:
        :param source_targs:
        :return:
        """

        def t_search(obj, keyword, target_src, search_result):
            try:
                result = obj().search_source(keyword)
                search_result.extend(result)
            except Exception as e:
                print(f"无法在{target_src}中搜索{keyword}----> [{repr(e)}]")

        task_pool, search_result = [], []
        for key, obj in source_targs.items():
            # 创建多线程任务
            task = threading.Thread(
                target=t_search,
                args=(obj, keyword, key, search_result)
            )
            task_pool.append(task)
            task.start()  # 启动线程

        for i in task_pool:
            i.join()  # 等待所有线程执行完毕
        return self.source_sort(search_result)

    # 对数据进行排序
    def source_sort(self, data):
        new_data = sorted(data, key=lambda e: e['sort'])
        return new_data
