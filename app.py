from flask import Flask, render_template

app = Flask(__name__)


# Define the route for the landing page
@app.route('/')
def landing():
    return render_template('landing.html')

# Scholarships page route
@app.route('/scholarships')
def scholarships():
    return render_template('scholarships.html')


if __name__ == '__main__':
    app.run(debug=True)