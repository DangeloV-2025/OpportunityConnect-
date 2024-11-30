from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Scholarship(db.Model):
    __tablename__ = 'scholarships'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.String(50))
    deadline = db.Column(db.String(50))
    description = db.Column(db.Text)
    apply_link = db.Column(db.String(200))

    def __repr__(self):
        return f'<Scholarship {self.name}>'
