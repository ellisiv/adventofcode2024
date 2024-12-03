
def solve_first_task(file):
    safe_reports = 0
    for line in file:
        numbers = line.split()
        diffs = [int(numbers[i]) - int(numbers[i - 1]) for i in range(1, len(numbers))]
        same_sign = all(el > 0 for el in diffs) or all(el < 0 for el in diffs)
        changes_gradually = all(0 < abs(el) <= 3 for el in diffs)
        safe_reports += same_sign and changes_gradually
    return safe_reports


def main():
    data = open("day2/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
