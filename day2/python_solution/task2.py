import numpy as np

def check_diff(list):
    if np.abs(list).sum() != np.abs(list.sum()):
        return 0
    elif max(np.abs(list)) > 3 or min(np.abs(list)) == 0:
        return 0
    return 1

def remove_outlier(diff):
    is_positive = np.median(diff) > 0
    mulitiplier = 2 if is_positive else 1
    not_found = True
    i = -1
    while not_found:
        i += 1
        element = ((-1) ** mulitiplier) * diff[i]
        if element < 1 or element > 3:
            not_found = False

    if i == len(diff) - 1:
        return diff[:i]
    diff[i + 1] = diff[i + 1] + diff[i]
    return np.concatenate((diff[ :i], diff[i + 1: ]))


def solve_second_task(file):
    sum = 0
    i = 0
    for line in file:
        a = np.array([int(x.strip()) for x in line.split()])
        diff = a[1:] - a[:-1]
        r = check_diff(diff)
        count = 0
        while r == 0 and count<len(a):
            # diff2 = remove_outlier(diff)
            # r = check_diff(diff2)
            # print("r:", r)
            a_reduced = np.concatenate((a[:count], a[count+1:]))
            diff = a_reduced[1:] - a_reduced[:-1]
            r = check_diff(diff)
            count += 1
        sum += r
        i += 1
    
    return sum


def main():
    data = open("day2/test_data.txt", "r")
    #data = open("day2/example_task1_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
