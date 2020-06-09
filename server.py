from flask import Flask, render_template
import socket

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game')
def game():
    return render_template('game.html')


def main():
    app.run(
        debug=True
    )


if __name__ == '__main__':
    main()
