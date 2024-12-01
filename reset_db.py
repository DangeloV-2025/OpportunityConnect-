from app import app
from models import db, Scholarship, FlyIn

# Import the populate scripts
import populate_scholarships
import populate_flyins

with app.app_context():
    # Drop all tables
    db.drop_all()
    print("All tables dropped.")

    # Recreate tables
    db.create_all()
    print("All tables recreated.")

    # Populate the database with scholarship data
    populate_scholarships.populate_scholarships()  # Populate the scholarships
    print("Scholarships populated.")

    # Populate the database with fly-in data
    populate_flyins.populate_flyins()  # Populate the fly-ins
    print("Fly-ins populated.")
