from flask import Flask, render_template, Response, request, redirect, url_for
from train import run_through_model
from zodiacSign import zodiac_sign
from utils import add_to_database, closest

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
        #Update database and get dataframe of current database
        df = add_to_database(user, zodiac, ALQ)
        list_of_ALQs = df["ALQ"].tolist()
        match_ALQ = closest(list_of_ALQs, ALQ)
        index_ALQ = list_of_ALQs.index(match_ALQ)
        match_name = df.at[index_ALQ, "Name"]
        phone_num = df.at[index_ALQ, "Phone"]
        insta_hand = df.at[index_ALQ, "Insta"]
        zodiac_match = df.at[index_ALQ, "zodiac"]

        list_to_return = [match_name, phone_num, insta_hand, zodiac_match]

        return redirect(url_for('success', zodiac = zodiac))
    else:
        return render_template('login.html')


@app.route('/match', methods=['POST', 'GET'])
def match():
    if request.method == 'POST':
        user = request.form
    return redirect(url_for('match', name=user))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
