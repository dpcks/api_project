# setup.py 파일이 있으면 pip로 설치 가능하다.
from setuptools import setup

setup(
    name = "myapi", # 이 이름으로 패키지가 설치
    version = "0.0.1", # 릴리즈 넘버.메이저번호.마이너번호
    description = "my api lib",
    url = "https://github.com/dpcks/api_project.git",
    author = "yechany",
    author_email = "jya05064@naver.com",
    packages= ["my_api"],
    install_requires = [
        "requests"
    ]
)