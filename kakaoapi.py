import json
import requests

api_key = '5fff9c2b0fc84cac9155a7c341c5ac03'

def get_users_address(x,y):
    url = 'https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x={longitude}&y={latitude}'.format(longitude=x,latitude=y)
    headers = {"Authorization": "KakaoAK " + api_key}
    result = json.loads(str(requests.get(url, headers=headers).text))
    match_first = result['documents'][0]['address_name']
    return str(match_first)
