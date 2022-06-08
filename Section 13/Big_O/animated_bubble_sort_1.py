import colorama

CLEAR_SCREEN = '\u001b[2J'
START_OF_LINE = '\u001b[1G'
CLEAR_LINE = f'{START_OF_LINE}\u001b[0K'
PREVIOUS_LINE = colorama.Cursor.UP(1)
HIDE_CURSOR = '\u001b[?25l'


def format_data(data, position=None):
    result = "[ "
    inverse = False
    for index, val in enumerate(data):
        if (position is not None) and (position == index):
            result += colorama.Back.LIGHTYELLOW_EX
            inverse = True
        result += f"{val}"
        if (position is not None) and (index == position + 1) and inverse:
            result += colorama.Back.RESET
            inverse = False
        result += " "

    result += "]"
    return result


def bubble_sort(data: list) -> None:
    """Sorts a list in place."""
    n = len(data)
    comparison_count = 0

    for i in range(n - 1):
        print(f"i = {i}. Starting inner loop with {format_data(data)}")
        print(end="")
        for j in range(n - 1 - i):
            print(f"{CLEAR_LINE}j = {j}, {format_data(data, j)}", end="")
            comparison_count += 1
            if data[j] > data[j + 1]:
                print(f"\t{colorama.Fore.RED}"
                      f"Swapping {data[j]} and {data[j + 1]}"
                      f"{colorama.Fore.RESET}", end="")
                data[j], data[j + 1] = data[j + 1], data[j]
                input(f"{PREVIOUS_LINE}")
            print(f"{CLEAR_LINE}j = {j}, {format_data(data, j)}", end="")

            # Pause
            input(f"{PREVIOUS_LINE}")

        print(f"End of pass {i}.  `data` is now {format_data(data)}")
    print(f"comparison_count is {comparison_count}")


colorama.init()

numbers = [3, 2, 4, 1, 5, 7, 6]
# numbers = [7, 6, 5, 4, 3, 2, 1]

print(f"{CLEAR_SCREEN}{HIDE_CURSOR}Sorting {format_data(numbers)}")
bubble_sort(numbers)
print(f"The sorted data is {format_data(numbers)}")

colorama.deinit()
