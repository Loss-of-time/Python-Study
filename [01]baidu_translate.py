# +--------------------------------------------------------------+
# | Size         | 3.1 KiB                                       |
# |--------------------------------------------------------------|
# | Gzipped      | 1.68 KiB                                      |
# |--------------------------------------------------------------|
# | Created      | June 30th 2020, 09:01:11                      |
# |--------------------------------------------------------------|
# | Changed      | July 17th 2020, 17:37:53                      |
# +--------------------------------------------------------------+

import requests


def word(word):
    headers = {
        'origin': 'https:/fanyi.baidu.com',
        'referer': 'https:/fanyi.baidu.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.56',
        'cookie': 'BAIDUID=9ACB468112906D677C28DD257C7A1207:FG=1; BIDUPSID=9ACB468112906D67B3ED38EF88A0A3A8; PSTM=1587274724; BDSFRCVID=jtIOJeC626Jzcncu9dJhrNzp42B-0cTTH6aIUWxinbGC2nmY9TiaEG0P_x8g0Ku-hD88ogKKBmOTHn8F_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JbAtoKD-JKvJfJjkM4rHqR_Lqxby26nBbg59aJ5nJD_-O4cnh4bhet0pMh5whJ8JteuLonOmQpP-HqTa3n7Eh4D1LN5X2lF8QI5KKl0MLU7Wbb0xyn_VMM3beMnMBMnGamOnanuy3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-XDTO0DaQP; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; ZD_ENTRY=bing; session_name=cn.bing.com; MCITY=-266%3A; BDUSS=FQYWNYbmVGQXhuZTVDcm9YfmJWdng1Rn5POFU0bXZ2WThVZVoyZENoMHRPZXRlRVFBQUFBJCQAAAAAAAAAAAEAAAAUnvtfxOO80rj0sdq1xM31xLMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC2sw14trMNeZ0; Appid=tieba; Cuid=9ACB468112906D677C28DD257C7A1207%3AFG%3D1; Appkey=appkey; Extension-Version=2.2; DeviceType=20; LCS-Header-Version=1; delPer=0; PSINO=2; cflag=13%3A3; session_id=1593158479026; BDRCVFR[en5Q-dJqX6n]=mbxnW11j9Dfmh7GuZR8mvqV; H_PS_PSSID=1424_31669_21112_32139_31254_32045_31847; BDRCVFR[Tp5-T0kH1pb]=mk3SLVN4HKm; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1593478993; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1593478993; __yjsv5_shitong=1.0_7_8747aae165e477349028de12c63db5a5144c_300_1593478992287_110.246.100.175_bf815627; yjs_js_security_passport=a5b3f85d6ada38d0a162c0da128adca899c9940c_1593478993_js',
        'x-requested-with': 'XMLHttpRequest',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'accept-encoding': 'utf-8',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'dnt': '1',
    }

    data = {
        'kw': word
    }

    post_url = 'https://fanyi.baidu.com/sug'
    res = requests.post(post_url, headers=headers, data=data)
    return res.content.decode('unicode_escape')


def main():
    raw = input('请输入要翻译的内容: ')
    content = word(raw)
    print(eval(content)['data'][0]['v'])
    print('\n')


if __name__ == "__main__":
    print('百度单词翻译机by时间的流动 QQ1399651432'+'\n')
    while True:
        try:
            main()
        except:
            print('ERROR')
