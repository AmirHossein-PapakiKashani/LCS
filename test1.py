from flask import Flask, jsonify
from random import choice, randint

app = Flask(__name__)

# Define the route for generating 100 words in 100 lines
@app.route('/dummy_words')
def generate_dummy_words():
    words = []
    for _ in range(100):
        word_length = randint(1, 10)  # Random word length between 1 and 10
        word = ''.join(choice('ACGT') for _ in range(word_length))
          
        # Save the Latin text to a file
        with open('shahid.txt', 'w') as file:
          file.write(word)

        words.append(word)

    lines = '\n'.join(words)
    return jsonify({'lines': lines})

if __name__ == '__main__':
    app.run()
