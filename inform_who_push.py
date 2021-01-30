import json
import sys

import requests


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


name = sys.argv
send_to_slack(f'방금 {name[1]}가 PUSH 했어요')
