import numpy as np

def check(list):
    if np.abs(list).sum() != np.abs(list.sum()):
        return 0
    elif max(np.abs(list)) > 3 or min(np.abs(list)) == 0:
        return 0
    return 1

def solve_first_task(file):
    sum = 0
    for line in file:
        a = np.array([int(x.strip()) for x in line.split()])
        diff = a[1:] - a[:-1]
        sum += check(diff)
    
    return sum

def main():
    data = open("day2/test_data.txt", "r")
    #data = open("day2/example_task1_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
