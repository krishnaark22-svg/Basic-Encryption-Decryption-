from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result


@app.route('/encrypt', methods=['POST'])
def encrypt_api():
    data = request.json
    text = data['text']
    shift = int(data['shift'])

    return jsonify({"result": encrypt(text, shift)})


@app.route('/decrypt', methods=['POST'])
def decrypt_api():
    data = request.json
    text = data['text']
    shift = int(data['shift'])

    return jsonify({"result": decrypt(text, shift)})


if __name__ == '__main__':
    app.run(debug=True)
