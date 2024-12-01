from os import makedirs
from sys import argv
from data_downloader import download_and_save_data, get_file_name

task1_content = """
def solve_first_task(file):
    pass


def main():
    data = open("day2/test_data.txt", "r")

    solution = solve_first_task(data)
    print("Solution first task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
"""

task2_content = """
def solve_second_task(file):
    pass


def main():
    data = open("day2/test_data.txt", "r")

    solution = solve_second_task(data)
    print("Solution second task: ", solution)

    data.close()


if __name__ == "__main__":
    main()
"""


def setup_task_file(day, task):
    file_name = "task1.py" if task == 1 else "task2.py"
    content = task1_content if task == 1 else task2_content
    task1_file = open(f"day{day}/python_solution/{file_name}", "w+")
    task1_file.write(content)
    task1_file.close()


def setup_folders_and_files(day: int):
    makedirs(f"day{day}/python_solution", exist_ok=True)
    setup_task_file(day, 1)
    setup_task_file(day, 2)
    open(get_file_name(day, "example_task1"), "w+").close()
    open(get_file_name(day, "example_task2"), "w+").close()


def main():
    day = int(argv[1])
    year = 2024
    setup_folders_and_files(day)
    download_and_save_data(day, year)


if __name__ == "__main__":
    main()
