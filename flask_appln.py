
from flask import Flask, jsonify, request;

app = Flask(__name__);

@app.route("/", methods=['GET'])
def hello():
    return jsonify({"Greetings":"Hello World"});

@app.route("/", methods=['POST'])
def abc():
    return jsonify({"Finish":"Good Bye!"});

@app.route("/abc/", methods=['GET', 'POST'])
def xyz():
    if request.method=='GET':
        return jsonify({"WELCOME":"Guest"});
    if request.method=='POST':
        return jsonify({"BYE":"Guest"});

@app.route("/cube/abc/xyz/<int:num>", methods=['GET'])
def cube(num):
	return jsonify({ "result" : num*num*num });
    
if __name__ == '__main__':
    app.run(debug=True);
