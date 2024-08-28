import json
import requests

api_key = '5fff9c2b0fc84cac9155a7c341c5ac03'
def get_users_address(x, y):
    url = 'https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x={longitude}&y={latitude}'.format(longitude=x,
                                                                                                        latitude=y)
    headers = {"Authorization": "KakaoAK " + api_key}
    result = json.loads(str(requests.get(url, headers=headers).text))
    match_first = result['documents'][0]['address_name']
    return str(match_first)

def search_places(query, x, y, radius=5000, size = 10):
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    headers = {
        "Authorization": f"KakaoAK {api_key}"
    }
    params = {
        "query": query,
        "x": x,
        "y": y,
        "radius": radius,
        "size": size
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        places = response.json().get('documents', [])
        results = []
        for idx, place in enumerate(places, start=1):
            place_info = {
                "idx" : idx,
                "name": place.get('place_name', 'N/A'),
                "address_name": place.get('address_name', 'N/A'),
                "road_address_name": place.get('road_address_name', 'N/A')
            }
            results.append(place_info)
        json_output = json.dumps(results, ensure_ascii=False, indent=4)
        #print(json_output)
        return json_output

    else:
        return f"Error: {response.status_code}"

#print(search_places("주유소", 126.93702575685037,37.64151042235078))
# x = "127.027636"
# y = "37.497950"
# print(get_users_address(x, y))
