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
	#app.run('0.0.0.0', debug=True, port=8100, ssl_context='adhoc')
    #app.run(port='15443', debug=True, ssl_context='adhoc')
	app.run(debug=True)