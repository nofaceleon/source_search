from core import common


class mypianku:

    def __init__(self):
        self.source = '片库'
        self.sort = 1  # 排序优先级
        self.base_url = "https://www.mypianku.net/"
        self.search_api = self.base_url + "s/ajax.php?q={key}"
        self.headers = {
            'authority': 'www.mypianku.net',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'accept': 'text/plain, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.mypianku.net/',
            'accept-language': 'zh-CN,zh;q=0.9',
        }

    def search_source(self, key):
        self.search_api = self.search_api.format(key=key)

        json_data = common.get_html(self.search_api, self.headers, content='json')

        return self.handle_data(json_data)

    def handle_data(self, data):
        buffer = []
        movie_datas = data['data']
        for i in movie_datas:
            buffer.append({
                'source': self.source,
                'movie_name': i['title'],
                'movie_link': self.base_url + i['url'].lstrip('/').partition('?')[0],
                'sort': self.sort
            })
        return buffer
