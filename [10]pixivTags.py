# +--------------------------------------------------------------+
# | Size         | 2.94 KiB                                      |
# |--------------------------------------------------------------|
# | Gzipped      | 1.1 KiB                                       |
# |--------------------------------------------------------------|
# | Created      | August 6th 2020, 14:29:05                     |
# |--------------------------------------------------------------|
# | Changed      | August 10th 2020, 14:09:19                    |
# +--------------------------------------------------------------+


import requests
import pandas as pd
import matplotlib.pyplot as plt


class PixivTags(object):
    # 使用面向对象编程主要是因为不同函数之间的变量更方便操作
    def __init__(self, mode='daily', pageNum=10):
        if mode == 'daily':
            self.rootUrl = 'https://www.pixiv.net/ranking.php?mode=daily&content=illust&p='
            self.dir = 'Pixiv/day/'
        elif mode == 'weekly':
            self.rootUrl = 'https://www.pixiv.net/ranking.php?mode=weekly&content=illust&p='
            self.dir = 'Pixiv/week/'
        elif mode == 'monthly':
            self.rootUrl = 'https://www.pixiv.net/ranking.php?mode=monthly&content=illust&p='
            self.dir = 'Pixiv/month/'
        self.pageNum = pageNum
        self.main()  # 放在__init__的末尾

    def getIdLi(self):
        # inout:None output:包含多个整数pid的列表——self.idLi
        self.idLi = []
        for i in range(1, self.pageNum+1):
            re = requests.get(self.rootUrl+str(i)+'&format=json')
            for i in re.json()['contents']:
                self.idLi.append([i['illust_id'], i['tags']])
        # print(self.idLi)
        print(f'共有{len(self.idLi)}个作品')

    def getTagDict(self):
        self.tagDict = {}
        for artWork in self.idLi:
            for tag in artWork[1]:
                try:
                    self.tagDict[tag] += 1
                except:
                    self.tagDict[tag] = 1

    def getTagLi(self):
        self.tagNameLi = list(self.tagDict)
        self.tagScoreLi = list(self.tagDict.values())
        self.tagLi = []
        for i, j in enumerate(self.tagNameLi):
            self.tagLi.append([j, self.tagScoreLi[i]])

    def dictToSe(self):
        data = pd.Series(self.tagDict)
        data = data.sort_values(ascending=False)
        self.data = data

    def showData(self):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        plt.bar(self.data.index[:10], self.data.values[:10])
        plt.title('今日P站人气tag前十')
        plt.show()

    def main(self):
        self.getIdLi()
        self.getTagDict()
        self.dictToSe()
        self.showData()


if __name__ == "__main__":
    p = PixivTags()
