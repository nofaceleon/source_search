from core import common
from lxml import etree


class subaibai:

    def __init__(self):
        self.source = '素白白影视'
        self.sort = 4
        self.base_url = "https://www.subaibai.com/"
        self.search_api = self.base_url + "?s={key}"
        self.headers = {
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
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
        lis = tree.xpath('//div[@class="bt_img mi_ne_kd search_list"]/ul/li')
        buffer = []
        for i in lis:
            buffer.append({
                'source': self.source,
                'movie_name': i.xpath('./h3/a/text()')[0],
                'movie_link': i.xpath('./h3/a/@href')[0],
                'sort': self.sort
            })
        return buffer
