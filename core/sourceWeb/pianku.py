from core import common


class pianku:

    def __init__(self):
        # print("=====开始搜索片库网=====")
        self.source = '片库网'
        self.base_url = "http://www.pianku5.com/"
        self.search_api = self.base_url + "index.php?g=home&m=search&a=api&sid=0&limit=10&wd="
        self.headers = {
            'Connection': 'keep-alive',
            'Accept': 'text/plain, */*; q=0.01',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'http://www.pianku5.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }

    def search_source(self, key):
        # print(f"正在 [{self.source}] 中搜索----->{key}")
        self.search_api = self.search_api + key
        # start = time.time()
        json_data = common.get_html(self.search_api, self.headers, content='json')
        # end = time.time()
        # print(f"{self.source}搜索耗时:{end - start}s")
        return self.handle_data(json_data)

    def handle_data(self, data):
        buffer = []
        if data['status'] == 1:
            movie_datas = data['data']
            for i in movie_datas:
                buffer.append({
                    'source': self.source,
                    'movie_name': i['vod_name'],
                    'movie_link': self.base_url + i['link'].lstrip('/')
                })
        return buffer
