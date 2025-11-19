#필수 과제

class Assignment01:
    @staticmethod
    def first_sol(a, b):
        return a + b

    @staticmethod
    def second_sol(bridge, weight):
        return abs(bridge - weight)

    @staticmethod
    def third_sol(wood_line):
        return 4 * wood_line

    @staticmethod
    def fourth_sol(tree_age):
        return tree_age // 4

    @staticmethod
    def fifth_sol(first_num, stone_pw):
        second_num = stone_pw // 10
        third_num = stone_pw % 10 // 3
        return f"{first_num}{second_num}{third_num}"

    @staticmethod
    def sixth_sol(stone_pw):
        return stone_pw**0.5

    @staticmethod
    def seventh_sol(min, wave_num):
        return min * 60 // wave_num

    @staticmethod
    def eighth_sol(a_gravity, time, stone_pw):
        return 0.5 * a_gravity * ( time + (stone_pw % 10) )**2

    @staticmethod
    def final_sol(pw_one, pw_two, pw_three):
        return abs(pw_one - pw_three)

if __name__ == "__main__":
    assignment = Assignment01()
    stone_pw = assignment.first_sol(14, 29)
    river_weight = assignment.second_sol(50, 68)
    wood_line = stone_pw
    wood_age = assignment.third_sol(wood_line)
    river_depth = assignment.fourth_sol(172)
    temple_pw = assignment.fifth_sol(5, stone_pw)
    cave_pw = assignment.sixth_sol(stone_pw)
    avg_wave_term = assignment.seventh_sol(5, 20)
    waterfall_height = assignment.eighth_sol(9.8, 2, stone_pw)
    spaceship_pw = assignment.final_sol(32, 42, 128)

    print("===========================================")
    print("===============Assignment 01===============")
    print("===========================================")
    print("01.Stone Password:", stone_pw)
    print("02.River Weight:", river_weight)
    print("03.Wood Age:", wood_age)
    print("04.River Depth:", river_depth)
    print("05.Temple Password:", temple_pw)
    print("06.Cave Password:", cave_pw)
    print("07.Average Wave Term:", avg_wave_term)
    print("08.Waterfall Height:", waterfall_height)
    print("09.Spaceship Password:", spaceship_pw)