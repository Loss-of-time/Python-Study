# +--------------------------------------------------------------+
# | Size         | 3.08 KiB                                      |
# |--------------------------------------------------------------|
# | Gzipped      | 1.21 KiB                                      |
# |--------------------------------------------------------------|
# | Created      | August 7th 2020, 16:42:54                     |
# |--------------------------------------------------------------|
# | Changed      | August 10th 2020, 16:34:49                    |
# +--------------------------------------------------------------+


import json
import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import pandas as pd


class CovidSpider(object):
    def __init__(self):
        self.url = 'http://ncov.dxy.cn/ncovh5/view/pneumonia'
        self.headers = {'Proxy-Connection': 'keep-alive',
                        'Referer': 'http://ncov.dxy.cn/',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'}
        self.main()

    def WorldDay(self):
        self.names = ['createTime', 'countryType', 'continents', 'provinceId', 'provinceName', 'currentConfirmedCount', 'confirmedCount',
                      'confirmedCountRank', 'suspectedCount', 'curedCount', 'deadCount', 'deadCountRank', 'deadRate', 'deadRateRank', 'countryFullName']
        res = requests.get(self.url, headers=self.headers)
        content = res.content.decode()
        bs = BeautifulSoup(content, 'html5lib')
        jsLi = bs.find_all(id='getListByCountryTypeService2true')
        js = re.findall(r'\[.+\]', jsLi[0].text)[0]
        dicLi = json.loads(js)
        self.dictLi = dicLi

    def getCsv(self):
        cols = []
        for name in self.names:
            col = []
            name = name
            for i in self.dictLi:
                try:
                    col.append(i[name])
                except:
                    col.append('')
            cols.append(col)

        files = []
        for i, name in enumerate(self.names):
            files.append(f'\"{name}\":{cols[i]}')
        files = ','.join(files)
        dataFrame = pd.DataFrame(eval('{'+files+'}'))
        dataFrame.to_csv('out/WD.csv', index=False)

    def showData(self):
        data = pd.read_csv('./out/WD.csv').values
        name = data[:10, 4:5]
        comfirmedCount = data[:10, 6:7]
        shape = name.size
        name.resize(shape)
        comfirmedCount.resize(shape)
        se = pd.Series(comfirmedCount, index=name).sort_values(ascending=False)
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        plt.bar(se.index, se.values)
        plt.show()

    def main(self):
        self.WorldDay()
        self.getCsv()
        self.showData()


if __name__ == "__main__":
    cs = CovidSpider()
