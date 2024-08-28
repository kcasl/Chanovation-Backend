import requests

# 서버의 주소와 엔드포인트 설정
url = "http://127.0.0.1:8000/checkdb"

# 보낼 데이터 설정
user_data = {
    "user_id": "sadw12e"  # 실제로 전송할 user_id로 변경하세요
}

# POST 요청 보내기
try:
    response = requests.post(url, json=user_data)

    # 서버 응답 처리
    if response.status_code == 200:
        result = response.json()  # 서버가 True 또는 False를 반환할 것으로 예상됨
        print("DB 체크 결과:", result)
    else:
        print("에러 발생:", response.status_code, response.text)
except requests.exceptions.RequestException as e:
    print("요청 실패:", e)