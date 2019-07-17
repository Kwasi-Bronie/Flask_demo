from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        Hello World
    </body>
    </html>
    '''

number = 0

@app.route('/ping')
def ping():
    global number
    number += 1
    return 'you are pong ' + str(number)

@app.route('/api')
def api():
    return jsonify({"hello": "there"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
