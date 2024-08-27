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
