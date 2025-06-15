# Plants vs. Zombies
# Module name: Task_2

from array import *
from itertools import zip_longest

def main():
    print_hi()
    plants_vs_zombies()

def plants_vs_zombies():
    result: str = ''
    # Create an array of zombies.
    zombies = []
    res_zombies = []
    # Create an array of plants.
    plants = []
    res_plants = []
    print('Введіть кількість бійців-зомбі')
    arr_int = zombies
    filling_an_array(zombies)
    print('Введіть кількість бійців-рослин')
    arr_int = plants
    filling_an_array(arr_int)
    # Initial forces zombies and plants
    init_forces_z = counting_forces(zombies)
    init_forces_p = counting_forces(plants)
    fight(zombies, plants, res_zombies, res_plants, int(init_forces_z), int(init_forces_p))
    res_z = counting_forces(res_zombies)
    res_p = counting_forces(res_plants)
    print('Вижило зомбі: ' + str(res_z) + ' (Початкові сили: ' + str(init_forces_z) + ')')
    print('Вижило рослин: ' + str(res_p) + ' (Початкові сили: ' + str(init_forces_p) + ')')
    res = result_fight(res_zombies, res_plants, init_forces_z, init_forces_p, result)
    print('zombies=' + str(zombies) + ' plants=' + str(plants) + '->' + str(res))

def filling_an_array(arr_int):
    # Filling the array with number
    while True:
        user_input = input("Введіть число (або No для виходу): ")
        if (user_input == "No") or (user_input == "no") or (user_input == "NO"):
            break
        arr_int.append(int(user_input))

def counting_forces(arr_int, total=0):
    # Calculating the force
    for i in range(len(arr_int)):
        total = total + int(arr_int[i])
    return  total

def fight(zombies, plants, res_zombies, res_plants, init_forces_z, init_forces_p):
    for z, p in zip_longest(zombies, plants, fillvalue=0):
        if (int(z) > int(p)) or (p == None):
            res_zombies.append(z - p)
            res_plants.append(0)
        elif int(z) == int(p):
            res_zombies.append(0)
            res_plants.append(0)
        elif (int(p) > int(z)) or (z == None):
            res_zombies.append(0)
            res_plants.append(p - z)

def result_fight(res_zombies: object, res_plants: object, init_forces_z, init_forces_p, result: bool) -> bool:
    if counting_forces(res_zombies) > counting_forces(res_plants):
        result: bool = False
    elif counting_forces(res_zombies) < counting_forces(res_plants):
        result: bool = True
    elif counting_forces(res_zombies) == counting_forces(res_plants):
        if init_forces_z > init_forces_p:
            result: bool = False
        else:
            result: bool = True
    return result

def print_hi():
    print(f'Привіт!')

if __name__ == '__main__':
    main()