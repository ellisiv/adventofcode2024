import numpy as np

def string_splitter(str):
    sum=0
    split1 = str.split('mul(')
    for a in split1:
        if a[0].isdigit():
            split2 = a.split(')')
            if split2[0] != '':
                b = split2[0]
                if b[0].isdigit():
                    split3 = b.split(',')
                    if split3[0].isdigit() and split3[1].isdigit():
                        sum += int(split3[0])*int(split3[1])
    return sum


def solve_first_task(file):
    sum = 0
    for line in file:
        sum += string_splitter(line)
    return sum



def main():
    data = open("day3/test_data.txt", "r")
    #data = open("day3/example_task1_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
