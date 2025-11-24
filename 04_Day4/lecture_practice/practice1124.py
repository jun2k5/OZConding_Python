
#a = {} X # 셋 선언할 시 {}는 사용불가능. 딕셔너리로 인식

# a = {1, 2, 3, 4, 5, 5, 5}
# print(type(a))
# print(a) #중복된 5가 제거됨

#=============================
# a = {1,2,3,4}
# b = {3,4,5,6}

# print(f"교집합 (AND): {a&b}")
# print(f"합집합 (OR): {a|b}")
# print(f"차집합 (NOT): {a-b}")
# print(f"대칭 차집합 (XOR): {a^b}")

#=============================

# print(hash("test")) # test문자열을 hash 암호화처리
# print(hash("test"))
# #hash table
# A | B |
# hash_Number | "test"

# 딕셔너리가 이 구조와 동일함
#=============================

# set 탐색

# a = {1,2,3,4,5}
# print(hash(5))
# print("존재함")

# hash(5)하면 값이 존재하는지 없는지 바로 탐색가능
#=============================

# list 탑색

# li = {1,2,3,4}

# if 1 in li:
#     print("1 존재")

# for i in li:
#     if 1 == i:
#         print("1 존재")

#=============================

# 딕셔너리 = Hash Map
# 키값을 hash처리했을 때, 그 주소에 밸류값을 저장하여
# 키-밸류 쌍을 완성시킬 수 있음.
#=============================

# my_dict = {
#     "key":1,
#     "key2":2,
#     "key3":3,
#     "key":4
# }

# print(my_dict["key"])

# 딕셔너리는 내부적으로 해쉬테이블 자료구조를 사용하기때문에
# 해쉬값의 중복이 불가능하다.
# 때문에 값의 중복을 허용하지 않는다.
#=============================

# user = {
#     "name" : "Alice",
#     "age" : 25
# }

# print(f"이름 조회 : {user.get('name')}")
# print(f"이름 조회 : {user['name']}")

# print(f"이름 조회(에러방지) : {user.get('job', "기본값")}")
# # print(f"이름 조회 : {user['job']}")
# #에러 발생, job이 없기때문에 KeyError: 'job' 발생.

# user["no-field"] = "kkk" #원치않는 요소 추가가 될 수 있음.
# user.update({"age": 26, "city": "Seoul"}) # 
# print(user)

#값을 가져올때는 get을 많이 쓴다.

#result = user.pop("job")
#print(user, result)
#지우면서 값반환, 즉 값 꺼내기

# user.setdefault("kkk", "99")
# print(user)
# #추가와 동시에 기본값 설정

# print(type(user.keys())) # 딕셔너리 keys 타입의 뷰 객체 반환
# print(type(user.items())) # 딕셔너리 items 타입의 뷰 객체 반환

# for key, value in user.items():
#     print(f"{key} : {value}")

# for a in user: #키값을 보여준다. 밑과 같다
#     print(a)

# for a in user.keys(): # 위와 같다.
#     print(a)

#=============================

# dict 컴프리헨션

# squares = { x : x**2 for x in range(1, 6)}
# print(squares)

# prices = {
#     "apple" : 1000,
#     "banana" : 500,
#     "cherry" : 2000
# }

# prices = { item: int(prices * 0.9) for item, price in prices.items()}
# 쇼핑몰의 10퍼 할인 행사를 할 때
# 간단한 컴프리헨션 표현을 사용할 수 있다.
#=============================

# a = [1,2,3,4,5]
# b = [1,2,3,4,5]

# print(id(a))
# print(id(b))
# print(a is b) # 동일성, 두 객체가 동일한가?
# print(a == b) # 동등성, 두 객체가 동등한가?

#=============================

# name = ""
# print(name)

# # 단락평가 short circuit Evaluation
# # 논리 연산자로 단락 평가를,  and or not

# display_name = name or "Anonymous"
# print(display_name)

# print(bool(name)) # 빈값이면 False
# if name:
#     print("test")

#=============================

# if "조건값" : #조건문이 아니면 bool()함수로 강제 형변환 후 판단

# name = ""
# result = name if name else "aa"
# -> result = name or "bb"
# print(result)

# macth문 = switch문

#=============================
# 반복문

# for i in range(start, end, step):
# result : start ~ end - 1, step +

#=============================

# short circuit evaluation
# unpacking
# List Comprension
# f-string
# forced casting
# enumerate
# if - elif - else 문
# for - break - else 문, break없이 끝난 경우 else로 넘어감
# while - else 문
# Clean Coding
# early return
# indent 2 level 이상 자제하기



# fruits = ["apple", "banana", "cherry"]
# # enumerate는 이터러블한 객체가 왔을 때, 인덱스값을 같이 반환한다.
# # 인덱싱이 필요한 리스트를 바로 딕셔너리로 만들 수 있다.
# for idx, fruit in enumerate(fruits):
#     print(f"{idx}번 과일 : {fruit}")

#=============================

##### 클래스와 함수

#함수의 사용이유 : DRY - Don't Repeat Yourself

# Docstring : 함수 정의 바로 아래에 """...""" 설명 붙이기, help로 확인가능
# Type Hints : 파라미터에 대한 타입 명시

# 협업시에 꼭 명시하는 습관 중요

# def analyze_scores(scores: list[int]) -> tuple[float, int]:
#     total = sum(scores)
#     avg = total / len(scores)
#     best = max(scores)
#     return avg, best

# scores = [60,70,80,90,100]
# avg, best = analyze_scores(scores)
# print(f"{avg} {best}")

#=============================
# def no_return(a):
#   if a:
#       return
#     ...
#     #return None
# #리턴이 없으면 기본적으로 None 리턴
# result = no_return()
# print(result)

#=============================

# G: 전역(Global) 스코프(Scope)
# global() nonlocal()
# glo = 1

# def my_fun():
#     global glo
#     glo += 1
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1

# my_fun()
# print(glo)

#=============================
# positional argument : 위치인자
# keyword argument : 키워드 인자

# def my_fun(name, age):
#     print(name)
#     print(age)

# temp = {
#     "name":"alex",
#     "age" : 3
# }

# my_fun(**temp)


#=============================
# short circuit evaluation
# unpacking
# List Comprension
# f-string
# forced casting
# enumerate
# if - elif - else 문
# for - break - else 문, break없이 끝난 경우 else로 넘어감
# while - else 문
# Clean Coding
# early return
# indent 2 level 이상 자제하기

# Docstring : 함수 정의 바로 아래에 """...""" 설명 붙이기, help로 확인가능
# Type Hints : 파라미터에 대한 타입 명시

# G: 전역(Global) 스코프(Scope)
# global() nonlocal()

# positional argument : 위치인자
# keyword argument : 키워드 인자

# scope 범위
# LEGB Local Enclosing Global Bult-in


# 반환값이 여러개일때 (타입이 여러개일 때 ) type1 | type2
# def test(a) -> int | float:
#     if type(a) == int:
#         return a
#     return float





