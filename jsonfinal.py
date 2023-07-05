from flask import Flask, jsonify
from random import choice, randint

app = Flask(__name__)

# Define the route for generating a dummy word
@app.route('/dummy_word')
def generate_dummy_word():
    word_length = randint(1, 20)  # Random word length between 1 and 20
    word = ''.join(choice('ACGT') for _ in range(word_length))

    # Save the word to a file
    with open('shahid.json', 'w') as file:
        file.write(word)

    return jsonify({'word': word})

# Define the route for generating 100 words in 100 lines and saving them to a text file
@app.route('/dummy_words')
def generate_dummy_words():
    words = []
    for _ in range(100):
        word_length = randint(1, 10)  # Random word length between 1 and 10
        word = ''.join(choice('ACGT') for _ in range(word_length))
        words.append(word)

    lines = '\n'.join(words)

    # Save the lines to a text file
    with open('dummy_words.json', 'w') as file:
        file.write(lines)

    return jsonify({'message': 'Dummy words generated and saved to dummy_words.txt'})

# Define the route for comparing shahid.txt and dummy_words.txt and saving LCS to a text file
@app.route('/compare')
def compare_files():
    # Read the contents of shahid.txt
    with open('shahid.json', 'r') as file:
        shahid_text = file.read().strip()

    # Read the contents of dummy_words.txt
    with open('dummy_words.json', 'r') as file:
        dummy_words_text = file.read().strip()

    # Find the Longest Common Subsequence (LCS)
    lcs = longest_common_subsequence(shahid_text, dummy_words_text)

    # Save LCS to a text file
    with open('lcs.json', 'w') as file:
        file.write(lcs)

    return jsonify({'lcs': lcs})


def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Build the Longest Common Subsequence (LCS) string
    lcs = ''
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs = text1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs


if __name__ == '__main__':
    app.run()
