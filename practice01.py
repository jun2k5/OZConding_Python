import requests

response = requests.get('https://kream.co.kr/')
print("상태 코드:", response.status_code)
print("HTML 내용 (첫 100자):", response.text[:100])