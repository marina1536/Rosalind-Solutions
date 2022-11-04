#!/usr/bin/python3


def reverse_complement(pattern):
    """
    Returns a reverse complement of a dna string pattern.
    """
    dict = pattern.maketrans("ATGC", "TACG")
    return pattern.translate(dict)[::-1]


if __name__ == "__main__":
    with open("datasets/rosalind_ba1c.txt", "r") as dataset:
        pattern = dataset.readline().rstrip()
    solution = reverse_complement(pattern)
    with open("solutions/solution_ba1c.txt", "w") as file:
        file.write(solution)
