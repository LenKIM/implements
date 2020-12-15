import requests
import json
import math
from dateutil.parser import parse as dateutil_parse
import datetime
from datetime import timezone

now_dt = datetime.datetime.now(tz=timezone.utc)

path_Dhkim = "Dhkim.txt"
path_Len = "Len.txt"

with open(path_Dhkim, 'r') as fp:
    data_Dhkim = fp.read().strip()
    
with open(path_Len, 'r') as fp:
    data_Len = fp.read().strip()

def send_to_slack(msg):
    headers = {"Content-type": "application/json;charset=utf-8"}
    base_url = "hoo" + "ks." + "sla" + "ck.com"
    sect1 = "T01DK0B8ZBR"
    sect2 = "B01DWNKD07P"
    sect3 = "nJifTFPtalSFR8GehdqZIQbZ"
    url = f"https://{base_url}/services/{sect1}/{sect2}/{sect3}"

    msg_dict = {"text": msg}
    data = json.dumps(msg_dict).encode("utf-8")
    res = requests.post(url, data=json.dumps(msg_dict), headers=headers)
    return res


def get_diff_hours(time_data):

    then_dt = dateutil_parse(time_data)
    then_dt = then_dt.astimezone(tz=timezone.utc)
    diff_dt = (now_dt - then_dt)
    diff_hours = diff_dt.total_seconds() / 60 / 60
    
    return diff_hours

def calc_penalt(diff_hours, name):
    diff_hours_floor = math.floor(diff_hours)

    if diff_hours_floor == 47:
        message = f"{name}, 벌금까지 1시간 남았습니다"
        send_to_slack(message)
        
    
# diff_Dhkim = get_diff_hours(data_Dhkim)
# # diff_Dhkim = 97.089
# calc_penalt(diff_Dhkim, "@김동혁")

diff_Len = get_diff_hours(data_Len)
# diff_Len = 12.867
calc_penalt(diff_Len, "@김정규")
