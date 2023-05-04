from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/convert', methods=['GET'])
def convert_get():
    
    celsius = float(request.args.get('celsius'))
    fahrenheit = (celsius * 1.8) + 32
    return jsonify({'fahrenheit': fahrenheit})


@app.route('/convert', methods=['POST'])
def convert_post():
    
    celsius = request.json.get('celsius')
    fahrenheit = (celsius * 1.8) + 32
    return jsonify({'fahrenheit': fahrenheit})


if __name__ == '__main__':
    app.run(debug=True)
