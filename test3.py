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




# response = requests.get('http://localhost:5000/dummy_word')
# if response.status_code == 200:
#     data = response.json()
#     word = data['word']
#     print(f"Generated word: {word}")
# else:
#     print("Error occurred while fetching the dummy word.")


if __name__ == '__main__':
    app.run()
