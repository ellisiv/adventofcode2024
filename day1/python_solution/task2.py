
def solve_second_task(file):
    list_of_first_numbers = []
    list_of_second_numbers = []
    for line in file:
        first_number, second_number = line.split()
        list_of_first_numbers.append(int(first_number.strip()))
        list_of_second_numbers.append(int(second_number.strip()))
    solution = 0
    for number in set(list_of_first_numbers):
        solution += (number * list_of_first_numbers.count(number) * list_of_second_numbers.count(number))
    return solution


def main():
    data = open("day1/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
