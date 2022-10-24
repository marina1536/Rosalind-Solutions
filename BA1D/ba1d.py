#!/usr/bin/python3


def occurrences(genome, pattern):
    """
    Returns all occurrences of a pattern in a genome
    """
    indices, index = [], -1
    while True:
        index = genome.find(pattern, index + 1)
        if index == -1:
            break
        indices.append(index)
    return indices


if __name__ == "__main__":
    with open("./rosalind_ba1d.txt", "r") as dataset:
        pattern = dataset.readline().rstrip()
        genome = dataset.readline().rstrip()
    solution = occurrences(genome, pattern)
    with open("./solution_ba1d.txt", "w") as file:
        file.write(" ".join(map(str, solution)))
