#!/usr/bin/python3


def frequent_words(dna, k):
    """
    Returns a list of most occuring k-mers in the dna
    """
    frequencies = {}
    max_occurrence = 0
    for kmer in (dna[i : i + k] for i in range(len(dna) - k + 1)):
        frequencies[kmer] = frequencies.get(kmer, 0) + 1
        if frequencies[kmer] > max_occurrence:
            max_occurrence = frequencies[kmer]
    kmers = []
    for item in frequencies.items():
        if item[1] == max_occurrence:
            kmers.append(item[0])
    return kmers


if __name__ == "__main__":
    with open("./rosalind_ba1b.txt", "r") as dataset:
        dna = dataset.readline().rstrip()
        k = int(dataset.readline())
    solution = frequent_words(dna, k)
    with open("./solution_ba1b.txt", "w") as file:
        file.write("\n".join(solution))
