from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
import random

#

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Database connection

client = MongoClient(
    'mongodb+srv://rahulsuit:suitrahul@cluster0.iqfhxzu.mongodb.net/?retryWrites=true&w=majority')
db = client.cluster0


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def hello_world():
    return "Hello World"


global_response = ""
global_token = ""


@app.route('/postOption', methods=['POST'])
@cross_origin()
def postOption():
    req = request.get_json(force=True)
    print(req)
    id = req["id"]
    # id = random.randint(1, 4)
    # Conditional for checking id
    if id == "1":
        image_url = "https://res.cloudinary.com/spiralyze/image/upload/f_auto,w_auto/BabySignLanguage/DictionaryPages/thank_you.svg"
    elif id == "2":
        print("")
        image_url = "https://res.cloudinary.com/spiralyze/image/upload/f_auto,w_auto/BabySignLanguage/DictionaryPages/please.svg"
    elif id == "3":
        print("")
        image_url = "https://res.cloudinary.com/spiralyze/image/upload/f_auto,w_auto/BabySignLanguage/DictionaryPages/sorry.svg"
    elif id == "4":
        print("")
        image_url = "https://res.cloudinary.com/spiralyze/image/upload/f_auto,w_1414/BabySignLanguage/DictionaryPages/welcome-webp.webp"
    elif id == "5":
        image_url = "https://res.cloudinary.com/spiralyze/image/upload/f_auto,w_auto/BabySignLanguage/DictionaryPages/good.svg"
    else:
        image_url = "https://res.cloudinary.com/spiralyze/image/upload/f_auto,w_auto/BabySignLanguage/DictionaryPages/good.svg"

    if image_url != "Null":
        response = {}
        response['success'] = True
        response['result'] = image_url

        global global_response
        global_response = response

        global global_token
        global_token = req["token"]
        return jsonify(response)
    else:
        response = {}
        response['success'] = False
        response['result'] = image_url
        return jsonify(response)


@app.route('/getOption', methods=['GET'])
@cross_origin()
def getOption():
    response = {}
    response['success'] = True
    images_url = random.choice(["https://res.cloudinary.com/spiralyze/image/upload/f_auto,w_auto/BabySignLanguage/DictionaryPages/thank_you.svg",
                                "https://res.cloudinary.com/spiralyze/image/upload/f_auto,w_auto/BabySignLanguage/DictionaryPages/please.svg",
                                "https://res.cloudinary.com/spiralyze/image/upload/f_auto,w_auto/BabySignLanguage/DictionaryPages/sorry.svg",
                                "https://res.cloudinary.com/spiralyze/image/upload/f_auto,w_1414/BabySignLanguage/DictionaryPages/welcome-webp.webp"])
    return images_url


def insertInDb():
    db.insert_one({"result": global_response, "token": global_token})


if __name__ == '__main__':
    app.run()

