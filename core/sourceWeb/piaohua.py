from core import common
from lxml import etree


class piaohua:

    def __init__(self):
        self.source = '飘花电影网'
        self.sort = 4
        # print(f"=====开始搜索: {self.source}=====")
        self.base_url = "https://www.btberry.com/"
        self.search_api = self.base_url + "vodsearch/-------------.html?wd={key}&submit="
        self.headers = {
            'authority': 'www.btberry.com',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.btberry.com/',
            'accept-language': 'zh-CN,zh;q=0.9',
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
        lis = tree.xpath('//ul[@id="searchList"]/li')
        buffer = []
        for i in lis:
            buffer.append({
                'source': self.source,
                'movie_name': i.xpath('./div[@class="thumb"]/a/@title')[0],
                'movie_link': self.base_url + i.xpath('./div[@class="thumb"]/a/@href')[0].lstrip('/'),
                'sort': self.sort
            })

        return buffer
