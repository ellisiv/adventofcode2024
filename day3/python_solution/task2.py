import numpy as np

def string_splitter(str):
    summa_summarum=0
    split1 = str.split('mul(')
    for a in split1:
        if a != '':
            if a[0].isdigit():
                split2 = a.split(')')
                if split2[0] != '':
                    b = split2[0]
                    if b[0].isdigit():
                        split3 = b.split(',')
                        if split3[0].isdigit() and split3[1].isdigit():
                            summa_summarum += int(split3[0])*int(split3[1])
    return summa_summarum


def solve_second_task(file):
    summa_summarum = 0
    str = ""
    for line in file:
        addition = line.strip()
        str += addition
    
    split1 = str.split("do()")
    for a in split1:
        if a != '':
            split2 = a.split("don't()")
            if split2[0] != '':
                summa_summarum += string_splitter(split2[0])
    return summa_summarum


def main():
    data = open("day3/test_data.txt", "r")
    #data = open("day3/example_task2_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()