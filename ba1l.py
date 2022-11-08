#!/usr/bin/python3


def pattern_to_number(pattern):
    """Returns kmer's lexicographic position"""
    if not pattern:
        return 0
    offset = {"A": 0, "C": 1, "G": 2, "T": 3}
    number = 0
    for i, char in enumerate(pattern[::-1]):
        number += 4**i * offset[char]

    return number


if __name__ == "__main__":
    with open("datasets/rosalind_ba1l.txt", "r") as dataset:
        kmer = dataset.readline().strip()
    solution = pattern_to_number(kmer)
    with open("solutions/solution_ba1l.txt", "w") as file:
        file.write(str(solution))
