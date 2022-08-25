import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 아래에 코드를 기록하세요.
# 코드 실행은 터미널에서 shell을 실행시켜서 해주세요. 
# $ python manage.py shell_plus 

#4. Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `name` 이 봉준호인 데이터를 아래와 같이 출력하는 코드를 작성하세요.
temp = Director.objects.get(name='봉준호')
print('id :', temp.id)
print('name :', temp.name)
print('debut :', temp.debut)
print('country :', temp.country)

#5. Queryset 메소드 `get` 을 활용해서 `Genre` 테이블에서 `title` 이 드라마인 데이터를 아래와 같이 출력하는 코드를 작성하세요.
temp = Genre.objects.get(title='드라마')
print('id :', temp.id)
print('title :', temp.title)

#6. 위 문제에서 찾은 `director` 와 `genre` 와 아래 `힌트 코드`를 활용해서 `Movie` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.
director_ = Director.objects.get(name='봉준호')
genre_ = Genre.objects.get(title='드라마')

movie = Movie()

movie.title = '기생충'
movie.opening_date = '2019-05-30'
movie.running_time = 132
movie.screening = False 
movie.director_id = director_.id
movie.genre_id = genre_.id

movie.save()

#7. `Movie` 테이블에 아래 데이터를 추가하는 코드를 작성하세요.
movies = [
    ("봉준호", "드라마", "괴물", "2006-07-27", 119, False),
    ("봉준호", "SF", "설국열차", "2013-10-30", 125, False),
    ("김한민", "사극", "한산", "2022-07-27", 129, True),
    ("최동훈", "SF", "외계+인", "2022-07-20", 142, False),
    ("이정재", "첩보", "헌트", "2022-08-10", 125, True),
    ("이경규", "액션", "복수혈전", "1992-10-10", 88, False),
    ("한재림", "재난", "비상선언", "2022-08-03", 140, True),
    ("Joseph Kosinski", "액션", "탑건 : 매버릭", "2022-06-22", 130, True),
]

for movie in movies:
    director_ = Director.objects.get(name=movie[0])
    director_id_ = director_.id
    genre_ = Genre.objects.get(title=movie[1])
    genre_id_ = genre_.id
    title_ = movie[2]
    opening_date_ = movie[3]
    running_time_ = movie[4]
    screening_ = movie[5]
    Movie.objects.create(director_id=director_id_, genre_id=genre_id_, title=title_, opening_date=opening_date_, running_time=running_time_, screening=screening_)

#8. `Movie` 테이블의 모든 데이터를 출력하는 코드를 작성하세요.
movies = Movie.objects.all()
for movie in movies:
    print(movie.director, movie.genre, movie.title, movie.opening_date, movie.running_time, movie.screening)

#9. 위 문제에서 조회한 `Director object (n)`  를 활용해서 각 영화의 감독 `name` 을 조회해서 대신 출력하는 코드를 작성하세요.
movies = Movie.objects.all()
for movie in movies:
	print(movie.director.name, movie.genre, movie.title, movie.opening_date, movie.running_time, movie.screening)

#10. 위 문제에서 조회한 `Genre object (n)`  를 활용해서 각 영화의 장르 `title` 을 조회해서 대신 출력하는 코드를 작성하세요.
movies = Movie.objects.all()
for movie in movies:
    print(movie.director.name, movie.genre.title, movie.title, movie.opening_date, movie.running_time, movie.screening)

#11. 영화 데이터들을 `최신 개봉한 영화순`으로 조회해서 출력하는 코드를 작성하세요.
movies = Movie.objects.order_by('-opening_date')
for movie in movies:
    print(movie.director.name, movie.genre.title, movie.title, movie.opening_date, movie.running_time, movie.screening)

#12. 영화 데이터 중 `가장 먼저 개봉한` 영화를 조회해서 출력하는 코드를 작성하세요.
movie = Movie.objects.order_by('opening_date')[0]
print(movie.director.name, movie.genre.title, movie.title, movie.opening_date, movie.running_time, movie.screening)

#13. 영화 데이터 중 현재 `상영 중`인 영화들을 `개봉일 순`으로 조회해서 출력하는 코드를 작성하세요.
movies = Movie.objects.filter(screening=True).order_by('opening_date')
for movie in movies:
    print(movie.director.name, movie.genre.title, movie.title, movie.opening_date, movie.running_time, movie.screening)


