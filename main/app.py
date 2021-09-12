from flask import Flask, render_template, Response, request, redirect, url_for

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
        return redirect(url_for('success', name=user))
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
