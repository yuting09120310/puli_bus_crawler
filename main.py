from requests import request
import json

print("請輸入車號+地點")
key = input()
list = key.split(' ')

#使用者陣列長度判斷
if(len(list) > 1):
    num = list[0]
    station = list[1]
else:
    num = list[0]

#資料來源位置
if(num.isdigit()):
    url = 'https://www.taiwanbus.tw/eBUSPage/Query/ws/getRData.ashx?type=4&key=' + num +'01'
else:
    url = 'https://www.taiwanbus.tw/eBUSPage/Query/ws/getRData.ashx?type=4&key=' + num +'1'

#資料回傳
response = request('get', url)

#重新編碼 預設空的為utf8
content = response.content.decode()

#資料轉換成json格式
data = json.loads(content)  

#資料轉換成json後為dict 可用搜尋方式檢查資料
item = data['data']

if (len(list) > 1):
    for i in item:
        if station == i['na']:
            print(i['na'],i['ptime'],"車號:",i['car'])
else:
    for i in item:
        print(i['na'],i['ptime'])