from random import *
# print(random()) # 0.0 ~ 1.0미만의 임의의 값 생성
# print(random() * 10) # 0.0 ~ 10.0미민의 임의의 값 생성.
# print(int(random() * 10)) # 0 ~ 10미만의 임의의 값 생성
# print(int(random() * 10)+1) # 1 ~ 10이하의 임의의 값 생성

##### 로또

# print(int(random()*45)+1) # 1부터 45 이하의 임의의 값 생성
# print(int(random()*45)+1) # 1부터 45 이하의 임의의 값 생성

# print(randrange(1,46)) #1부터 46미만까지 임의의 값 생성
# print(randint(1,45)) # 1부터 45 이하의 임의의 값 생성

# Date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 "+ str(Date) +"일로 선정 되었습니다.")
p = "Python is fun"
print(p[2].isupper())
print(p.replace("Python","Java"))
print(p.count("n"))