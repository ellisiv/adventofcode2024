import numpy as np
from collections import Counter

def solve_second_task(file):
    a = []
    b = dict()

    for line in file:
        split = [x.strip() for x in line.split()]
        a.append(int(split[0]))
        key = int(split[1])
        if key in b:
            b[key] = b[key] + 1
        else:
            b[key] = 1

    sum = 0
    for element in a:
        if element in b:
            sum += b[element]*element


    return sum


def main():
    data = open("day1/test_data.txt", "r")
    #data = open("day1/example_task2_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
