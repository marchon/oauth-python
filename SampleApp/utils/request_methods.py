import requests
import configRead
from requests_oauthlib import OAuth1

# POST for qbo sandbox
def post(req_data, access_key, access_sec):
    payload = req_data['payload']
    url = req_data['url']
    tokens = configRead.get_consumer_tokens()
    auth = OAuth1(tokens['consumer_key'], tokens['consumer_sec'], access_key, access_sec)
    headers = {'Accept': 'application/json', 'content-type': 'application/json; charset=utf-8'}
    req = requests.post(url, auth=auth, headers=headers, json=payload)

    req_status_content = {}
    req_status_content['status_code'] = req.status_code
    req_status_content['content'] = req.content
    return req_status_content