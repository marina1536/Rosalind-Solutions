#!/usr/bin/python3
from ba1g import hamming


def match(kmer, genome, d):
    """
    Returns all approximate occurences of a kmer in a genome with most d mismatched
    """
    positions = []
    k = len(kmer)
    for i in range(len(genome) - k + 1):
        if hamming(kmer, genome[i : i + k]) <= d:
            positions.append(i)
    return positions


if __name__ == "__main__":
    with open("datasets/rosalind_ba1h.txt", "r") as dataset:
        kmer = dataset.readline().strip()
        genome = dataset.readline().strip()
        d = int(dataset.readline())
    solution = match(kmer, genome, d)
    with open("solutions/solution_ba1h.txt", "w") as file:
        file.write(" ".join(map(str, solution)))
