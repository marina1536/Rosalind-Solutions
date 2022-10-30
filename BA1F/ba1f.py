#!/usr/bin/python3


def skew(genome):
    """
    Returns positions in genome with minimum skew
    """
    skew, min = 0, 0
    positions = []
    for i in range(len(genome)):
        nucleotide = genome[i]
        if nucleotide == "G":
            skew += 1
        elif nucleotide == "C":
            skew -= 1
        if skew < min:
            min = skew
            positions = [i + 1]
        elif skew == min:
            positions.append(i + 1)
    return positions


if __name__ == "__main__":
    with open("./rosalind_ba1f.txt", "r") as dataset:
        genome = dataset.readline().strip()
    solution = skew(genome)
    with open("./solution_ba1f.txt", "w") as file:
        file.write(" ".join(map(str, solution)))
