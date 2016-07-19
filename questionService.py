from flask import Flask
from pymongo import MongoClient
import json
from bson import json_util


app = Flask(__name__)

@app.route('/quiz')
def getQuiz():
    client = MongoClient("mongodb://localhost/triviaquiz")
    db = client['triviaquiz']
    quiz = client.triviaquiz.questions.find_one({'name': 'American Trivia'})
    return json.dumps(quiz, default=json_util.default)


if __name__ == '__main__':
    app.run(debug=True)