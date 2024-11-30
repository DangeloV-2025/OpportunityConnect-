from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scholarships')
def scholarships():
    return render_template('scholarships.html')

@app.route('/fly-ins')
def fly_ins():
    return render_template('fly_ins.html')

@app.route('/precollege')
def precollege():
    return render_template('precollege.html')

@app.route('/community')
def community():
    return render_template('community.html')

if __name__ == '__main__':
    app.run(debug=True)
