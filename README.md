# Email Project

Python 3.11 에서 테스트 됨.

Required type :service_account GCP credentials.json

# QuickStart

| 파일명                          | 변수명             | 자료형 | 설명                   |  
|------------------------------|-----------------|-----|----------------------|
| main.py                      | CREDENTIAL_PATH | 문자열 | GCP 인증정보가 담긴 json 파일 |
| main.py                      | RECEIVER_EMAIL  | 문자열 | 받는이 이메일주소            |
| main.py                      | CONTENT         | 문자열 | 내용                   |
| utils.email.providers.google | SENDER_EMAIL    | 문자열 | 보낸이 이메일주소            |  

### 실행

```
python main.py
```  
