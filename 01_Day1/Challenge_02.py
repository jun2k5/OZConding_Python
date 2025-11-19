# 도전과제 -중급 level 2

class Challenge02:
    @staticmethod
    def first_sol(candy, poket, get):
        return print(f"Result_01 : {candy * poket + get}")

    @staticmethod
    def second_sol(friends, ball, luckyboy, get):
        return print(f"Result_02 : {friends * ball + luckyboy * get}")

    @staticmethod
    def third_sol(students, hour):
        return print(f"Result_03 : {students * hour * 60}")

    @staticmethod
    def fourth_sol(fuel, use, day):
        return print(f"Result_04 : {fuel - (use * day)}")

    @staticmethod
    def fifth_sol(extent):
        return print(f"Result_05 : {extent ** 0.5}")

    @staticmethod
    def sixth_sol(people, scores:list):
        return print(f"Result_06 : {sum(scores) // people}")


if __name__ == "__main__":
    print("===========================================")
    print("===============Challenge 02================")
    print("===========================================")
    challenge = Challenge02()
    challenge.first_sol(5, 3, 3)
    challenge.second_sol(10, 4, 3, 2)
    challenge.third_sol(5, 3)
    challenge.fourth_sol(9, 3, 2)
    challenge.fifth_sol(144)
    challenge.sixth_sol(5, [65, 75, 50, 80, 60])



