from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def bar():
    return render_template('barchart.html')


if __name__ == '__main__':
    app.run(debug=True)