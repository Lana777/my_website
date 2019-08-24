from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home3.html')


if __name__ == '__main__':
    app.run(port=5001, debug=True)