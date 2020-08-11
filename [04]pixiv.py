# +--------------------------------------------------------------+
# | Size         | 4.81 KiB                                      |
# |--------------------------------------------------------------|
# | Gzipped      | 1.76 KiB                                      |
# |--------------------------------------------------------------|
# | Created      | July 19th 2020, 18:21:16                      |
# |--------------------------------------------------------------|
# | Changed      | August 4th 2020, 10:04:30                     |
# +--------------------------------------------------------------+

from logging import log
import requests
import os
import threading
import logging

class Pixiv:
    # 使用面向对象编程主要是因为不同函数之间的变量更方便操作
    def __init__(self, mode='daily', pageNum=3, tags=[], logger=logging.Logger(__name__)):
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
        self.tags = tags
        self.main()  # 放在__init__的末尾
        return None

    def getIdLi(self):
        # inout:None output:包含多个整数pid的列表——self.idLi
        self.idLi = []
        for i in range(1, self.pageNum+1):
            re = requests.get(self.rootUrl+str(i)+'&format=json')
            for i in re.json()['contents']:
                self.idLi.append([i['illust_id'], i['tags']])
        # print(self.idLi)
        print(f'共有{len(self.idLi)}个作品')

    def getImgUrl(self, id):
        # input:一个pid out:这个pid原图url的列表(可能有多个元素)
        artWorkUrl = f'https://www.pixiv.net/ajax/illust/{id}/pages?lang=zh'
        anImgLi = []
        anImgLi.append(id)
        re = requests.get(artWorkUrl)
        for i in re.json()['body']:
            anImgLi.append(i['urls']['original'])
        # print(anImgLi)
        return anImgLi

    def creatFolder(self):
        # 先把文件加创建了再放文件
        if not os.path.exists('Pixiv'):
            os.mkdir('Pixiv')
        if not os.path.exists('Pixiv/day'):
            os.mkdir('Pixiv/day')
        if not os.path.exists('Pixiv/week'):
            os.mkdir('Pixiv/week')
        if not os.path.exists('Pixiv/month'):
            os.mkdir('Pixiv/month')
        print('文件夹已部署......')

    def downloadImg(self, anImgLi, num=0):
        # 下载图片
        for i in anImgLi[1:]:
            fileName = self.dir + str(num)+'_' + i[57:]
            headers = {}
            headers['referer'] = f'https://www.pixiv.net/artworks/{anImgLi[0]}'
            re = requests.get(i, headers=headers)
            print(f'正在下载:{fileName}')
            logger.info(f'{fileName} has downloaded.')
            with open(fileName, 'wb') as f:
                f.write(re.content)

    def thred(self, artWork, num):
        anImgLi = self.getImgUrl(artWork[0])
        self.downloadImg(anImgLi, num)

    def main(self):
        # 主函数
        self.creatFolder()
        self.getIdLi()
        num = 1
        if len(self.tags) != 0:
            # 当有tag传入，判断是否有包含其中任意tag的作品
            for artWork in self.idLi:
                wb = False
                for i in artWork[1]:
                    if wb:
                        break
                    for o in self.tags:
                        if i == o:
                            wb = True
                            td = threading.Thread(
                                target=self.thred, args=(artWork, num))
                            td.start()
                            num += 1
                            break
        else:
            for artWork in self.idLi:
                # 简单多线程
                td = threading.Thread(target=self.thred, args=(artWork, num))
                td.start()
                num += 1


if __name__ == "__main__":
    logging.basicConfig(
                    level    = logging.DEBUG,              # 定义输出到文件的log级别，                                                            
                    format   = '%(asctime)s  [%(filename)s] : %(levelname)s  %(message)s',    # 定义输出log的格式
                    datefmt  = '%Y-%m-%d %A %H:%M:%S',                                     # 时间
                    filename = './out/Pixiv.log',                # log文件名
                    filemode = 'w')                        # 写入模式“w”或“a”

    logger = logging.getLogger(__name__)

    # 使用时文件会默认保存在文件根目录下Pixiv文件夹中
    os.chdir('out/')
    # 爬取的作品数=pageNum*50
    # mode[日排行:daily 周排行:weekly 月排行:monthly]
    # 目前只支持日文原文标签,只要作品符合标签之一就下载

    tags = {'东方': '東方', '东方project': '東方Project', '芙兰朵露・斯卡蕾特': 'フランドール・スカーレット'}
    p = Pixiv(mode='daily', pageNum=10, tags=(tags['东方'], tags['东方project']))
    # p = Pixiv(mode='daily', pageNum=3)
