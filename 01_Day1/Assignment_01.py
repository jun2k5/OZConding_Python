
def first_sol(a, b):
    return a + b

def second_sol(bridge, weight):
    return abs(bridge - weight)

def third_sol(wood_line):
    return 4 * wood_line

def fourth_sol(tree_age):
    return tree_age // 4

def fifth_sol(first_num, stone_pw):
    second_num = stone_pw // 10
    third_num = stone_pw % 10 // 3
    return f"{first_num}{second_num}{third_num}"

def sixth_sol(stone_pw):
    return stone_pw**0.5

def seventh_sol(min, wave_num):
    return min * 60 // wave_num

def eighth_sol(a_gravity, time, stone_pw):
    return 0.5 * a_gravity * ( time + (stone_pw % 10) )**2

def final_sol(pw_one, pw_two, pw_three):
    return abs(pw_one - pw_three)

if __name__ == "__main__":
    stone_pw = first_sol(14, 29)
    river_weight = second_sol(50, 68)
    wood_line = stone_pw
    wood_age = third_sol(wood_line)
    river_depth = fourth_sol(172)
    temple_pw = fifth_sol(5, stone_pw)
    cave_pw = sixth_sol(stone_pw)
    avg_wave_term = seventh_sol(5, 20)
    waterfall_height = eighth_sol(9.8, 2, stone_pw)
    spaceship_pw = final_sol(32, 42, 128)

    print("01.Stone Password:", stone_pw)
    print("02.River Weight:", river_weight)
    print("03.Wood Age:", wood_age)
    print("04.River Depth:", river_depth)
    print("05.Temple Password:", temple_pw)
    print("06.Cave Password:", cave_pw)
    print("07.Average Wave Term:", avg_wave_term)
    print("08.Waterfall Height:", waterfall_height)
    print("09.Spaceship Password:", spaceship_pw)