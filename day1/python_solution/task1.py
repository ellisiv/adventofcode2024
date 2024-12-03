import numpy as np

def solve_first_task(file):
    a = []
    b = []
    
    for line in file:
        split = [x.strip() for x in line.split()]
        a.append(int(split[0]))
        b.append(int(split[1]))
    a = np.array(a)
    b = np.array(b)
    a.sort()
    b.sort()

    return np.abs(b-a).sum()



def main():
    data = open("day1/test_data.txt", "r")
    #data = open("day1/example_task1_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
