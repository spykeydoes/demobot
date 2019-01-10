from flask import Flask, request

app = Flask(__name__)

@app.route('/yeet', methods=['GET', 'POST'])
def greet_person():
    name = request.values.get('text')
    return f'Hi Memelord {name}!'

if __name__ == "__main__":
    app.run(debug=True)