# 도전과제 -초급 level 1

class Challenge_01:

    @staticmethod
    def first_sol(apple, box):
        return print(f"Result_01 : {apple * box}")

    @staticmethod
    def second_sol(price, friends, num):
        return print(f"Result_02 : {friends * num * price}")

    @staticmethod
    def third_sol(stations, min):
        return print(f"Result_03 : {stations * min}")

    @staticmethod
    def fourth_sol(books, friends):
        return print(f"Result_04 : {books // friends}")

    @staticmethod
    def fifth_sol(poeple, chocolate):
        return print(f"Result_05 : {chocolate // poeple}")

    @staticmethod
    def sixth_sol(distance):
        return print(f"Result_06 : {distance ** 2}")

if __name__ == "__main__":
    print("===========================================")
    print("===============Challenge 01================")
    print("===========================================")
    challenge = Challenge_01()
    challenge.first_sol(7, 3)
    challenge.second_sol(10000, 4, 4)
    challenge.third_sol(5, 3)
    challenge.fourth_sol(9, 3)
    challenge.fifth_sol(2, 8)
    challenge.sixth_sol(5)