from flask import Flask,request,jsonify
import json

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    result = num1 + num2
    return jsonify({'result': result})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    result = num1 - num2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
