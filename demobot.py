from flask import Flask , request

app = Flask(__name__)

@app.route('/greet')
def hello_world():
    temp = request.values.get('temp')
    temp = int(temp)
    if temp > 30:
        return "Argh that's hot. That's real hot."
    else:
        return f'My favourite temperature is {temp}!'

app.run()