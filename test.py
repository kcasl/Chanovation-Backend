<<<<<<< HEAD
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
=======
import requests

token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjExYzhiMmRmNGM1NTlkMjhjOWRlNWQ0MTAxNDFiMzBkOWUyYmNlM2IiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vcHJvamVjdC0yNDA4MjUiLCJhdWQiOiJwcm9qZWN0LTI0MDgyNSIsImF1dGhfdGltZSI6MTcyNDc0OTM3MSwidXNlcl9pZCI6IllFeWFiRThMMm9iTHFUdW9iVVZXbFNOWThEcjEiLCJzdWIiOiJZRXlhYkU4TDJvYkxxVHVvYlVWV2xTTlk4RHIxIiwiaWF0IjoxNzI0NzQ5MzcxLCJleHAiOjE3MjQ3NTI5NzEsImVtYWlsIjoidGVzdDEyMzRAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbInRlc3QxMjM0QGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.wRu4CybDf_1n2m8EUW2oDA3Z3syCsE-tGe5u5zUJ8SoiKF4of45c3eNsSQ5oEL7iX3h_ucjZF7XvSL-VT3NFqdFxPmXctKoy6xKXQLhL3b_HaBOcltZv0grjWdqHezbrpcxOObg_4xHllEn_9XkMi9Nbsk9a5Ik8Dn20bdDqaktfADQp3NumFCEJbQMY8aWT2bDZ6uH1PbVs-tkF8JGwFU2KpeL3r1U0bYEJDrENB1p17GEpoh1Q6glEVOD3bny8KkEjnpKInab-Ue9yo5BB3mkczHLJZ3ppnQahv4K33rYUbJvZzE2NcUPOY-jCTX54HD2NgpEnlNA_gj-kcF06mA"

def test_validate_endpoint():
    headers = {
        'authorization':token
    }

    response = requests.post(
        "http://127.0.0.1:8000/token",
        headers=headers
    )

    return response.text


print(test_validate_endpoint())
>>>>>>> b027ece4bda4f85ee8f072698e3700c3c4723b42
