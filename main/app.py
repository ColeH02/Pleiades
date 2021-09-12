from flask import Flask, render_template, Response, request, redirect, url_for
from train import run_through_model
from zodiacSign import zodiac_sign

app = Flask(__name__)


@app.route('/')
def local_website():
    return render_template('index.html')


@app.route('/success/<name>')
def success(name):
    return f'welcome {name}'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form

        zodiac = zodiac_sign(user['month'], user['day'])

        ALQ_dict = {'zodiac': zodiac}
        keys = ['sex', 'sexorient', 'degree', 'sociability', 'acqmark']
        for key in keys:
            ALQ_dict[key] = user[key]

        ALQ = run_through_model(ALQ_dict)

        return redirect(url_for('success', name=ALQ))
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
