#!/usr/bin/python3


def number_to_pattern(number, k):
    alphabet = {0: "A", 1: "C", 2: "G", 3: "T"}
    pattern = []
    for i in range(k):
        pattern.append(alphabet[number % 4])
        number = number // 4
    return "".join(pattern[::-1])


if __name__ == "__main__":
    with open("datasets/rosalind_ba1m.txt", "r") as dataset:
        number = int(dataset.readline())
        k = int(dataset.readline())
    solution = number_to_pattern(number, k)
    with open("solutions/solution_ba1m.txt", "w") as file:
        file.write(str(solution))
