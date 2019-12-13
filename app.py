from flask import Flask, render_template, request

from utils import fizzbuzz

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/result', methods=['POST'])
def result():
    number = request.form.get('number')

    say = fizzbuzz(number)

    return render_template(
        'result.html',
        say=say
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
