from requests import get


class DataCatcher:
    def __init__(self):

        self.total = None
        self.non_symptom = None
        self.overseas = None
        self.local = None
        self.updateDate = None
        self.url = 'https://voice.baidu.com/newpneumonia/getv2'
        self.headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
        }

        self.place = input('输入想查询的地区，形如上海-闵行区、江苏-苏州、湖北：')

        if '-' in self.place:
            self.target = 'district'
        else:
            self.target = 'province'

    def get_total(self, a, b):
        self.total = []
        for i in range(len(a)):
            self.total.append(a[i] + b[i])

    def get_resp(self):

        if self.target == 'province':
            params = {
                'from': 'mola - virus',
                'stage': 'publish',
                'target': 'trend',
                'isCaseIn': 1,
                'area': self.place
            }
            resp = get(url=self.url, headers=self.headers, params=params)
            dic = resp.json()['data'][0]['trend']
            self.updateDate = dic['updateDate']
            self.local = dic['list'][-1]['data']
            self.overseas = dic['list'][-2]['data']
            DataCatcher.get_total(self, self.local, self.overseas)

        elif self.target == 'district':
            params = {
                'from': 'mola - virus',
                'stage': 'publish',
                'target': 'trendCity',
                'area': self.place
            }
            resp = get(url=self.url, headers=self.headers, params=params)

            dic = resp.json()['data'][0]['trend']
            self.updateDate = dic['updateDate']
            self.non_symptom = dic['list'][0]['data']
            self.local = dic['list'][-1]['data']
            DataCatcher.get_total(self, self.local, self.non_symptom)
