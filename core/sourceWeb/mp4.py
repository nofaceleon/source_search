from core import common
from lxml import etree


class mp4:

    def __init__(self):
        self.source = '高清MP4网'
        self.sort = 99
        # print(f"=====开始搜索: {self.source}=====")
        self.base_url = "http://www.mp4ba.cc/"
        self.search_api = self.base_url + "vod-search-name-{key}.html"
        self.headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer': 'http://www.mp4ba.cc/',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }

    def search_source(self, key):
        # print(f"正在 [{self.source}] 中搜索----->{key}")
        self.search_api = self.search_api.format(key=key)
        # start = time.time()
        html = common.get_html(self.search_api, self.headers)
        # end = time.time()
        # print(f"{self.source}搜索耗时:{end - start}s")
        return self.handle_data(html)

    def handle_data(self, html):
        tree = etree.HTML(html)
        lis = tree.xpath('//ul[@class="list-unstyled"]/li')
        buffer = []
        for i in lis:
            buffer.append({
                'source': self.source,
                'movie_name': i.xpath('./h4/a/text()')[0],
                'movie_link': self.base_url + i.xpath('./h4/a/@href')[0].lstrip('/'),
                'sort': self.sort
            })

        return buffer
