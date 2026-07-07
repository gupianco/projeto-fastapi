import requests

headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzIiwiZXhwIjoxNzgyMjM3NjcyfQ.lO5Rq1AtX4mRiPdY0LhnZcOCJX89RQNz_cazA9uU2Qs'
}

requisicao = requests.get('http://127.0.0.1:8000/auth/refresh', headers=headers)
print(requisicao)
print(requisicao.json())
