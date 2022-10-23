#!/usr/bin/python3


def pattern_count(text, pattern):
    """
    Returns the number of times a pattern appears in a text
    """
    count, index = 0, -1
    while True:
        index = text.find(pattern, index + 1)
        if index == -1:
            break
        count += 1
    return count


if __name__ == "__main__":
    with open("./rosalind_ba1a.txt", "r") as file:
        text = file.readline().strip()
        pattern = file.readline().strip()
    solution = pattern_count(text, pattern)
    with open("./solution_ba1a.txt", "w") as file:
        file.write(f"{solution}")
