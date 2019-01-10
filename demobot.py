from flask import Flask, request

app = Flask(__name__)

@app.route('/greet', methods=['GET', 'POST'])
def hello_world():
    name = request.values.get('text')
    return f'Hi {name}!'

if __name__ == '__main__':
    app.run()