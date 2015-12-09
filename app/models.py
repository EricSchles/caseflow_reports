from app import db

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer,primary_key=True)
    date_created = db.Column(db.DateTime)
    name = db.Column(db.String(400))
    email = db.Column(db.String(500))
    
    def __init__(self,date_created,name,email):
        self.date_created = date_created
        self.name = name
        self.email = email
    def __repr__(self):
        return "<Data %r>" % str(self.name)
