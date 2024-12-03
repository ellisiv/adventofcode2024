
def solve_first_task(file):
    for line in file:
        line = "x" + line
        mul_ends = line.split("mul(")
        for mul_end in mul_ends[1:]:
            mul_contents = mul_end.split(")")[0]
            if len(mul_contents) == 1:
                continue
            factors = mul_contents.split(",")
            if len(factors) != 2:
                continue
            
    pass


def main():
    data = open("day3/example_task1_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
