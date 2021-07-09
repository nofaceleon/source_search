from core import common
from lxml import etree


class idybee():

    def __init__(self):
        self.source = '电影蜜蜂'
        self.search_api = "https://www.idybee.com/?post_type=post&s="
        self.headers = {
            'authority': 'www.idybee.com',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'zh-CN,zh;q=0.9',
        }

    # 开始搜索, 需要统一返回的格式
    def search_source(self, key):
        # print(f"正在 [{self.source}] 中搜索----->{key}")
        self.search_api = self.search_api + key
        # start = time.time()
        html = common.get_html(self.search_api, self.headers)
        # end = time.time()
        # print(f"{self.source}搜索耗时:{end - start}s")
        return self.handle_html(html)
        # print(self.handle_html(html))

    # 处理html, 提取关键信息
    def handle_html(self, html):
        tree = etree.HTML(html)
        lis = tree.xpath('//ul[@id="index_ajax_list"]/li')
        buffer = []
        for i in lis:
            movie_name = i.xpath('./a/@title')[0]
            movie_link = i.xpath('./a/@href')[0]
            buffer.append({
                'source': self.source,
                'movie_name': movie_name,
                'movie_link': movie_link
            })
        return buffer
