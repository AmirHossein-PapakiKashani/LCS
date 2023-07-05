def find_lcs(seq1, seq2):
    m = len(seq1)
    n = len(seq2)

    # Create a table to store the lengths of LCS
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    # Retrieve the LCS from the table
    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if seq1[i - 1] == seq2[j - 1]:
            lcs = seq1[i - 1] + lcs
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs


def find_relevant_dna(file1, file2):
    with open(file1, 'r') as f1:
        seq1 = f1.read().strip()

    relevant_dna = ""
    exact_match_found = False

    with open(file2, 'r') as f2:
        lines = f2.readlines()

        for line in lines:
            seq2 = line.strip()
            n = len(seq2)

            if seq1 == seq2:
                exact_match_found = True
                relevant_dna = seq2
                break

            lcs = find_lcs(seq1, seq2)
            if len(lcs) > len(relevant_dna):
                relevant_dna = seq2

    with open("output.txt", 'w') as output_file:
        for line in lines:
            seq2 = line.strip()
            n = len(seq2)
            lcs = find_lcs(seq1, seq2)
            output_file.write(f"{seq1}\t{seq2}\t{lcs}\n")

    if exact_match_found:
        print(relevant_dna)
        print("Exact match found in the second file.")
    else:
        print("No exact match found.")
        print("Most relevant DNA sequence:", relevant_dna)


# Usage
find_relevant_dna("file1.txt", "file2.txt")
