from flask import Flask, request

app = Flask(__name__)

@app.route('/greet', methods=['GET', 'POST'])
def greet_person():
    name = request.values.get('text')
    return f'Hi {name}!'

app.run(debug=True)