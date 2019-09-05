# Python-study
#파이썬#장고

### Django server

1. 가상환경을 구성하여 다른 개발환경과 겹치지 않게 구성한뒤 실행을한다. 명령어는 `python -m venv myvenv`로 myvenv라는 환경을 구성하였다

2. `myvenv/Scripts/activate`를 실행시키면 가상환경이 실행된다

3. `(myvenv)`라는 가상환경이 켜진것을 볼수 있다.

4. 장고설치전에 파이프를 최신버전으로 업데이트 `python -m pip install --upgrade pip`

5. `pip install django`로 django 최신버전으로 설치

6. `python manage.py runserver`로 서버를 열면 `http://127.0.0.1:8000/`의 서버가 열려있다.