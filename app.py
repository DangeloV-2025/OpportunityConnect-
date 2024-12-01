from flask import Flask, render_template, request
from models import db, Scholarship, FlyIn

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scholarships.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/scholarships')
def scholarships():
    search_query = request.args.get('search', '')
    if search_query:
        scholarships = Scholarship.query.filter(Scholarship.name.ilike(f'%{search_query}%')).all()
    else:
        scholarships = Scholarship.query.all()  # Call the .all() method
    return render_template('scholarships.html', scholarships=scholarships)


@app.route('/flyins')
def flyins():
    search_query = request.args.get('search', '')
    if search_query:
        flyins = FlyIn.query.filter(FlyIn.name.ilike(f'%{search_query}%')).all()
    else:
        flyins = FlyIn.query.all()  # Call the .all() method
    return render_template('flyins.html', flyins=flyins)




@app.route('/precollege')
def precollege():
    return render_template('precollege.html')

@app.route('/community')
def community():
    return render_template('community.html')

if __name__ == '__main__':
    app.run(debug=True)
