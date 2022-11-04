#!/usr/bin/python3


def hamming(s1, s2):
    """
    Returns the Hamming distance between strings s1 and s2
    """
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance


if __name__ == "__main__":
    with open("datasets/rosalind_ba1g.txt", "r") as dataset:
        string1 = dataset.readline().strip()
        string2 = dataset.readline().strip()
    solution = hamming(string1, string2)
    with open("solutions/solution_ba1g.txt", "w") as file:
        file.write(str(solution))
