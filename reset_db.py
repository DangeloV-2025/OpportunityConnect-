from app import app
from models import db, Scholarship

with app.app_context():
    # Drop all tables
    db.drop_all()
    print("All tables dropped.")
    
    # Recreate tables
    db.create_all()
    print("All tables recreated.")
