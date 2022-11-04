#!/usr/bin/python3


def clump(genome, k, L, t):
    """
    Returns all kmers forming an (L, t)-clump in the genome
    """

    def is_clumping():
        if len(indices) < t:
            return False
        for i in range(len(indices) - t + 1):
            if indices[i + t - 1] - indices[i] + k <= L:
                return True
        return False

    kmers = {}
    for kmer, pos in ((genome[i : i + k], i) for i in range(len(genome) - k + 1)):
        if kmers.get(kmer) is None:
            kmers[kmer] = []
        kmers[kmer].append(pos)
    frequent_kmers = []
    for kmer, indices in kmers.items():
        if is_clumping():
            frequent_kmers.append(kmer)
    return frequent_kmers


if __name__ == "__main__":
    with open("datasets/rosalind_ba1e.txt", "r") as dataset:
        genome = dataset.readline().strip()
        k, L, t = [int(x) for x in dataset.readline().split()]
    solution = clump(genome, k, L, t)
    with open("solutions/solution_ba1e.txt", "w") as file:
        file.write(" ".join(solution))
