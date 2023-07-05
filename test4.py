from flask import Flask, jsonify
from random import choice, randint
import requests

app = Flask(__name__)

# Define the route for generating a dummy word
@app.route('/dummy_word')
def generate_dummy_word():
    word_length = randint(1, 20)  # Random word length between 1 and 10
    word = ''.join(choice('ACGT') for _ in range(word_length))
    
        # Save the Latin text to a file
    with open('shahid.txt', 'w') as file:
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
    with open('dummy_words.txt', 'w') as file:
        file.write(lines)

    return jsonify({'message': 'Dummy words generated and saved to dummy_words.txt'})

if __name__ == '__main__':
    app.run()