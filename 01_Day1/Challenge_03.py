# 도전과제 -고급 level 3

class Challenge03:
    @staticmethod
    def first_sol(width, height, num, area):
        return print(f"Result_01 : {((width * height) - (num * area))* 100}")

    @staticmethod
    def second_sol(books_price, buy, tax):
        return print(f"Result_02 : {books_price * buy * (1 + tax / 100)}")
    
    @staticmethod
    def third_sol(g_width, g_height):
        return g_width * g_height, print(f"Result_03 : {g_width * g_height}")

    @staticmethod
    def third_one_sol(third_result, persent):
        return third_result * (persent / 100), print(f"Result_03-1 : {third_result * (persent / 100)}")

    @staticmethod
    def third_two_sol(third_result, third_one_result, tree_area):
        print(f"Result_03-2 : {(third_result - third_one_result) // tree_area}")

    @staticmethod
    def fourth_sol(kg, m):
        return print(f"Result_04 : {kg // (m ** 2)}")

    @staticmethod   
    def fifth_sol(a, b):
        return print(f"Result_05 : {(a**2 + b**2)**0.5}")

    @staticmethod    
    def sixth_sol(won, plus, period):
        return print(f"Result_06 : {won * plus / 100 * period}")

if __name__ == "__main__":
    print("===========================================")
    print("===============Challenge 03================")
    print("===========================================")
    challenge = Challenge03()
    challenge.first_sol(50, 30, 5, 10)
    challenge.second_sol(12000, 3, 10)
    third_result = challenge.third_sol(20, 15)[0]
    third_one_result = challenge.third_one_sol(third_result, 5)[0]
    challenge.third_two_sol(third_result, third_one_result, 2)
    challenge.fourth_sol(92, 1.8)
    challenge.fifth_sol(13, 9)
    challenge.sixth_sol(25000000, 6.15, 3)

'''
cheers = ["할 수 있다!!!", "16기 화이링!", "공부만이 살길."]
for i in range(5):
    print(cheers[i % len(cheers)])

i = 1, 2, 3, 4, 5
len(cheers) = 3

i = 0 일때,
cheers[0 % 3] -> cheers[0] -> "할 수 있다!!!"

i = 1 일때,
cheers[1 % 3] -> cheers[1] -> "16기 화이링!"

i = 2 일때,
cheers[2 % 3] -> cheers[2] -> "공부만이 살길."

i = 3 일때,
cheers[3 % 3] -> cheers[0] -> "할 수 있다!!!

i = 4 일때,
cheers[4 % 3] -> cheers[1] -> "16기 화이링!"

따라서

result----
할 수 있다!!!
16기 화이링!
공부만이 살길.
할 수 있다!!!
16기 화이링!

'''