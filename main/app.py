from flask import Flask, render_template, Response, request, redirect, url_for
from train import run_through_model
from zodiacSign import zodiac_sign

app = Flask(__name__)


@app.route('/')
def local_website():
    return render_template('index.html')


@app.route('/success/<zodiac>')
def success(zodiac):
    if zodiac == 'Sagittarius':
        return render_template('sagittarius.html')
    elif zodiac == 'Capricorn':
        return render_template('capricorn.html')
    elif zodiac == 'Aquarius':
        return render_template('aquarius.html')
    elif zodiac == 'Pisces':
        return render_template('pisces.html')
    elif zodiac == 'Aries':
        return render_template('aries.html')
    elif zodiac == 'Taurus':
        return render_template('taurus.html')
    elif zodiac == 'Gemini':
        return render_template('gemini.html')
    elif zodiac == 'Cancer':
        return render_template('cancer.html')
    elif zodiac == 'Leo':
        return render_template('leo.html')
    elif zodiac == 'Virgo':
        return render_template('virgo.html')
    elif zodiac == 'Libra':
        return render_template('libra.html')
    elif zodiac == 'Scorpio':
        return render_template('scorpio.html')

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

        return redirect(url_for('success', zodiac=user['zodiac']))
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
