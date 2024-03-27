# 1일차
## 프로젝트 세팅

### 1. Github
- 레포지토리 생성
- 로컬에 있는 내 컴퓨터 폴더와 깃헙의 Remote 공간 연결
- git clone 'https://github.com/BE-02-Kimchangkyu/django-youtube.git'

### 2. Docker Hub
- 나의 컴퓨터에 가상환경을 구축 (윈도우, 맥  >> 리눅스 환경구축{MySQL, Python, Redis})
- AccessToken값을 Github 레포지토리에 등록 -> 빌드목적

### 3. 장고 프로젝트 세팅
- requirements.txt  ->  실제 배포할 때 사용
- requirements.dev.txt  -> 개발하고 연습할 때 사용(파이썬 패키지 관리)
- 실전: 패키지 의존성 관리 -> 버전관리, 패키지들 간의 관계 관리

### 4. DRF세팅
 - DJangoRestframework
 - drf-spectacular / swagguer-ui, redoc / requirements.txt 추가
 - docer-compose build

 Streaming - 영상 파일은 어떻게 보낼까? TCP/UDP, 3ways handshake.
 Socket - ws://, Hand Shake 양방향 통신가능해진다, Low Overhead, Frame(웹소켓에서 데이터를 나누는 단위) 
 HTTP의 차이 공부.


# docker-compose up
# docker-compose build
# docker-compose run --rm app sh -c 'python manage.py showmigrations'
# docker-compose run --rm app sh -c 'python manage.py makemigrations'
# docker-compose run --rm app sh -c 'python manage.py migrate'

# docker-compose run --rm app sh -c 'python manage.py comments'
# docker-compose run --rm app sh -c 'python manage.py createsuperuser'
# docker-compose run --rm app sh -c 'python manage.py test users'
# docker-compose run --rm app sh -c 'flake8'
# git add .
# git commit -m ''
# git push -u origin main

# ssh ec2-user@3.35.9.218

# makemigrations (장고한테 알려주는 것)
# migrate (장고가 DB를 찾아가는것)
