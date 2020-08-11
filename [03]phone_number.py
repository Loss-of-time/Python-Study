# +--------------------------------------------------------------+
# | Size         | 9.95 KiB                                      |
# |--------------------------------------------------------------|
# | Gzipped      | 3.08 KiB                                      |
# |--------------------------------------------------------------|
# | Created      | July 13th 2020, 10:24:48                      |
# |--------------------------------------------------------------|
# | Changed      | August 6th 2020, 19:21:27                     |
# +--------------------------------------------------------------+
# 自动手机号磁场分析器 v1.10.3
# 7/23 因为原来的手机号网站出了问题，临时更换了一个网站，现在勉强能用
# 7/24 找到了一个网站生成大量手机号

import time
import requests


def getPhoneNumber():
    url = 'https://api.uukit.com/phone/generate_batch'
    headers = {'referer': 'https://uutool.cn/phone-generate/',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40'}
    data = {'phone_num': '10000',
            'area': ''}
    re = requests.post(url, headers=headers, data=data)
    re = re.json()['data']['rows']
    re.pop()
    return re


def numSplit(num):
    # 电话号分为两两一组，多出的单独
    li = list(num)
    result = []
    line1 = []
    line2 = []
    if len(num) % 2 == 0:
        length = len(num)
    else:
        length = len(num)-1

    for i in range(int(length/2)):
        bit = ''.join(li[(i*2):(i*2+2)])
        line1.append(bit)
    line1.append(li[-1])
    line2.append(li[0])
    for i in range(int(length/2)):
        bit = ''.join(li[(i*2)+1:(i*2+2)+1])
        line2.append(bit)
    result.append(line1)
    result.append(line2)
    # 结果是一个二元数组，分别为从第一位开始的结果和从第二位开始的结果
    return result


def special(bitLi, btMfDic):
    # 判断5,0,的特殊情况,暂时不考虑重复的数字
    add = 0  # 特殊bit在列表中的序号

    for i in bitLi:
        # 先排除单独的数字
        if len(i) == 1:
            pass
        elif len(i) == 2:
            # 将bit与字典对应，对应不上的就是特殊情况
            try:
                btMfDic[i]
            except:
                li = list(i)
                p = 0
                FoZ = ['x', 'x']
                for i in li:
                    # 判断是5x x5 0x x0 50 05 00 55 八种中哪一种
                    if i == '5':
                        FoZ[p] = '5'
                    if i == '0':
                        FoZ[p] = '0'
                    p += 1
                FoZ = ''.join(FoZ)
                # 在不同情况下,更改此bit，规则被极大的简化了，只要是特殊情况就复制前一位磁场
                newBit = bitLi[add-1]+bitLi[add]
                newBit = list(newBit)

                if FoZ == 'x5' or FoZ == '5x':
                    if add > 0:
                        if len(newBit) == 3:
                            newBit.remove('5')
                        else:
                            newBit.remove('5')
                            newBit.pop(0)
                    else:
                        newBit = bitLi[add]+bitLi[add]
                        newBit = list(newBit)
                        newBit.remove('5')
                        newBit.remove('5')

                if FoZ == '0x' or FoZ == 'x0':
                    if len(newBit) == 3:
                        newBit.pop()
                    else:
                        newBit.pop()
                        newBit.pop()

                if FoZ == '55' or FoZ == '00' or FoZ == '50' or FoZ == '05':
                    if len(newBit) > 3:
                        newBit = bitLi[add-1]
                    else:
                        newBit = '11'

                newBit = ''.join(newBit)
                bitLi[add] = newBit

        add += 1
    return bitLi


def twice(bitLi):
    # 处理重复数字的特殊情况
    p = 0
    for i in bitLi:
        i = list(i)
        if len(i) > 1 and i[0] == i[1] and p > 0:
            bit = bitLi[p-1]+bitLi[p]
            bit = list(bit)
            if len(bit) > 3:
                bit.pop(0)
                bit.pop()
            else:
                bit.pop()
            bitLi[p] = ''.join(bit)
        p += 1

    return bitLi


def operate(bitLi):
    # 传入一条切割好的一维列表，调用上面的函数，并返回结果
    global bitMfdic
    global mfCnDic
    bitLi = special(bitLi, bitMfdic)
    bitLi = twice(bitLi)
    p = 0
    for i in bitLi:
        if len(i) > 1:
            bitLi[p] = bitMfdic[i]
            bitLi[p] = mfCnDic[bitLi[p]]
        p += 1
    return bitLi


def removeEnd0(results):
    # 除去尾号为零的电话号
    p = 0
    for i in results:
        if i[1][-1] == '0':
            results.pop(p)
        p += 1
    return results


def goodThing(results):
    # 去除带凶星的手机号
    badThings = ['五鬼1', '六煞1', '祸害1', '绝命1',
                 '五鬼2', '六煞2', '祸害2', '绝命2',
                 '五鬼3', '六煞3', '祸害3', '绝命3',
                 '五鬼4', '六煞4', '祸害4', '绝命4']
    badLi = []
    # 记录带凶星的说记号的地址
    add = 0
    for result in results:
        bad = False
        for i in result[1:]:
            for o in i:
                if len(o) > 1:
                    for p in badThings:
                        if o == p:
                            bad = True
                            break
        if bad:
            badLi.append(add)
        add += 1
    # 根据地址删除带凶星的说记号，因为从前往后删，每次实际上地址都要往前一位
    deleted = 0
    for i in badLi:
        del results[i-deleted]
        deleted += 1
    return results


def mfUp(results):
    # 只保留磁场上升的电话号
    down = []
    add = 0
    for result in results:
        wantBreak = False
        for bitLi in result[1:]:
            if wantBreak:
                break
            mfLevel = []
            for bit in bitLi:
                if len(bit) > 1:
                    bit = list(bit)
                    mfLevel.append(bit[-1])
            for bit in range(len(mfLevel)-1):
                if mfLevel[bit] > mfLevel[bit+1]:
                    down.append(add)
                    wantBreak = True
                    break
        add += 1
    deleted = 0
    for i in down:
        del results[i-deleted]
        deleted += 1
    return results


def main():
    # 主函数进行各种函数的调用
    resultsT = []
    results = []
    o = 0
    try:
        # for i in range(200):
        ret = getPhoneNumber()
        resultsR = []
        for num in ret:
            result = []
            result.append(num)
            bitLi = numSplit(num)
            for i in bitLi:
                result.append(operate(i))
            resultsR.append(result)
        o = len(resultsR)
        results = removeEnd0(resultsR)
        results = goodThing(results)
        # results = mfUp(results)
        # print(results)
        for result in results:
            resultsT.append(result)
            li = list(result[0])
            right = True
            for i in li:
                if i == '0':
                    right = False
                    break
            if right:
                print(result)
        # print(resultsT)

    except:
        print('error')
    return results, o


if __name__ == "__main__":

    '已废弃的网址,现在使用程序生成https://m.10010.com/mall-mobile/NumList/search,http://api.jubaolh.com/api/mobile/list,http://www.xuanhao.com/pcmobile.php?'

    # bit与磁场好相对应的字典
    bitMfdic = {'13': '11', '31': '11',
                '19': '21', '91': '21',
                '14': '31', '41': '31',
                '11': '41', '22': '41',
                '18': '51', '81': '51',
                '47': '61', '74': '61',
                '17': '71', '71': '71',
                '12': '81', '21': '81',
                '68': '12', '86': '12',
                '78': '22', '87': '22',
                '76': '32', '67': '32',
                '99': '42', '88': '42',
                '79': '52', '97': '52',
                '38': '62', '83': '62',
                '89': '72', '98': '72',
                '69': '82', '96': '82',
                '49': '13', '94': '13',
                '43': '23', '34': '23',
                '93': '33', '39': '33',
                '66': '43', '77': '43',
                '36': '53', '63': '53',
                '29': '63', '92': '63',
                '64': '73', '46': '73',
                '84': '83', '48': '83',
                '27': '14', '72': '14',
                '26': '24', '62': '24',
                '28': '34', '82': '34',
                '44': '44', '33': '44',
                '24': '54', '42': '54',
                '16': '64', '61': '64',
                '32': '74', '23': '74',
                '37': '84', '73': '84',
                }

    # 磁场号与汉语意义相对应的字典
    mfCnDic = {'11': '天医1', '21': '延年1', '31': '生气1', '41': '伏位1', '51': '五鬼1', '61': '六煞1', '71': '祸害1', '81': '绝命1',
               '12': '天医2', '22': '延年2', '32': '生气2', '42': '伏位2', '52': '五鬼2', '62': '六煞2', '72': '祸害2', '82': '绝命2',
               '13': '天医3', '23': '延年3', '33': '生气3', '43': '伏位3', '53': '五鬼3', '63': '六煞3', '73': '祸害3', '83': '绝命3',
               '14': '天医4', '24': '延年4', '34': '生气4', '44': '伏位4', '54': '五鬼4', '64': '六煞4', '74': '祸害4', '84': '绝命4', '00': '|'
               }

    for i in range(10):
        main()
        time.sleep(0.5)
