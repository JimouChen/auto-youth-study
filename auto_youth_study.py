import requests
import json

youth_study_headers = {
    'X-Litemall-Token': '',
    'X-Litemall-IdentiFication': 'young',
    'User-Agent': 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.28(0x18001c2d) NetType/4G Language/zh_CN',
    'Content-Type': 'application/x-www-form-urlencoded',
}


def save_history(token, chapter_id):
    url = 'https://youthstudy.12355.net/apih5/api/young/course/chapter/saveHistory'
    headers = youth_study_headers
    headers['X-Litemall-Token'] = token
    data = 'chapterId=' + str(chapter_id)
    response = requests.post(url=url, headers=headers, data=data)
    res = json.loads(response.text)
    return res


def get_chapter_id():
    url = 'https://youthstudy.12355.net/apih5/api/young/chapter/new'
    response = requests.get(url=url, headers=youth_study_headers)
    res = json.loads(response.text)
    print('最新一期：', res['data']['entity']['name'])
    return res['data']['entity']['id']


def get_token(sign):
    url = 'https://youthstudy.12355.net/apih5/api/user/get'
    data = sign
    response = requests.post(url=url, headers=youth_study_headers, data=data)
    res = json.loads(response.text)
    return res['data']['entity']['token']


def get_sign(mid):
    url = 'https://tuanapi.12355.net/questionnaire/getYouthLearningUrl?mid=' + str(mid)
    response = requests.get(url=url, headers=youth_study_headers)
    res = json.loads(response.text)
    return res['youthLearningUrl'].split('?')[1]


if __name__ == '__main__':
    mid = 'xxxxxxx'
    try:
        print(mid, ' 开始发送请求')
        sign = get_sign(mid)
        token = get_token(sign)
        cid = get_chapter_id()
        res = save_history(token, cid)
        if res['errno'] == 0:
            print('观看记录成功保存，程序结束')
        else:
            print('保存失败')
            print(res['errmsg'])
    except:
        print('异常，请检查你的mid值是否有效')
