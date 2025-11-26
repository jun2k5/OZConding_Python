#함수 심화, 클래스, 예외처리
#===========================
#booting
#은양체제의 실행
#주기억장치, 보조기억장치
#주기억장치 = RAM, ROM / 휘발성, 비휘발성
#보조기억장치 = HDD, SDD
#
#booting = 보조기억장치의 OS -> RAM

#======================

# 가변인자 : *args, **kwargs
# *args = 배열, 집합 / 포지셔널 알규먼트 / Positional arguments
# **kwargs = 딕셔너리 / 키워드 알규먼트 / keyword arguments

# def test(*args):
#     for a in args:
#         print(a)
    
# arg = ["a", "b", "c"]

# test(*arg)

#=======================
# 고차 함수 : 함수를 인자로 받는 함수
# 콜백 함수

# 절차지향 / 객체지향 / 함수지향

# First Class Object / First Class Citizen

# 클로저와 데코레이터 ( Closure / Decorator )

# map, filter, reduce 함수

#=====================================
#재귀 함수 : Recursive function

#========================
#람다 표현식 : Anonymous Functioon

# pairs: list[tuple[int, str]] = [(2, "two"),(3, "three"),(4, "four"), (1, "one")]

# print(pairs)
# pairs.sort(key=lambda u : u[1])
# print(pairs)
# pairs.sort()
# print(pairs)
#===============================
#이터레이터 /  제너레이터
#Iterator / Generator

# __iter__() : 객체 자신 호출 / 초기화할때 사용
# __next__() : 다음 이터레이터 실행


# 제너레이터 : yield로 상태를 유지하는 함수 << 메모리적으로 매우 효율적임
# 일반적인 함수가 값을 반환(return)하고 종료되는 것과 달리,
# 제너레이터 함수는 값을 산출(return)하고 실행 상태를 일시 정지(suspand)한다.

#===========================
# 타입 어노테이션, 타입 힌트

#Any : 모든 것
#Optional[type] : 
#Union[X, Y] : 
#Tuple[T1, T2, ...] : 
# Literal, TypeVar, Generic 등등

# def greet(name:str, age:int) -> str:
#     return f"{name} {age}"

# print(greet.__annotations__)

#=============================

#클래스
#Class vs Object vs Instance

#클래스에서 오브젝트(현실의 객체)를 정의하고 인스턴스(실제 객체)를 생성한다.

#파이썬에서는 클래스를 정의할때 Camel_Case를 사용한다.
# duner method = magic method

#클래스의 인스턴스는 모두가 같은 값을 가진다
#따라서 == 연산이나 is 연산은 True가 나온다.

#클래스 변수는 모든 인스턴스가 공유한다.

#인스턴스 변수는 인스턴스마다 개별적으로 가진다.

#가변 객체를 클래스 변수로 두는 것은 주의해야한다.

# class Dog:
#     val = "abcd"

# a = Dog()
# b = Dog()

# a.val = "asd"
# # 문자열이 불변객체라 클래스변수가 인스턴스 변수로 바뀐다.
# # 때문에 클래스 변수의 주소값을 잃어버려 클래스 변수에 접근할 수 없게된다.

# print(Dog.val) # abcd
# print(a.val) # asd
# print(b.val) # abcd

#==============================

#클래스 상속
# 리스코프 치환

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print("a")

# class Dog(Animal):
#     def speak(self):    # 메서드 오버라이딩
#         print("b")

# class Cat(Animal):
#     def speak(self):    # 메서드 오버라이딩
#         print("c")

#상속받은 클래스는 __init__을 작성하지 않아도 자동으로 생성된다.

# 다형성(polymorphism), 다양성
# 객체지향프로그래밍 OOP (Object-Oriented Programming)
#

# def make_animal_speak_once(animal: Animal):
#     animal.speak()

# animals = {
#     Dog("b"),
#     Cat("c"),
#     Animal("a")
# }

# for i in animals:
#     make_animal_speak_once(i)


#----다중상속----
#JAVA랑 C#은 다중상속을 지원하지않는다.

# class S:
#     def swim(self):


# 다이아몬드 이슈 : 다른 부모클래스들이 같은 이름의 메서드를 가질때,
# 오버라이딩에 문제가 발생, 다른 언어들이 다중상속을 지원하지 않는이유
# 파이썬은 다이아몬드 이슈를 우선순위로 해결했다.
# Left -> right



#=======================================

# 예외처리



#co-routine



