# Open API 라이브러리
- 설치방법
```bash
pip install git+https://github.com/dpcks/api_project.git
```

- 사용방법
```python
from my_api import naver_api

search_api(url,client_id,client_secret,params)

translate_api(text,url,client_id,client_secret,source="ko",target="en")
```