from app import db

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer,primary_key=True)
    date_created = db.Column(db.DateTime)
    
    def __init__(self,date_created):
        self.date_created = date_created
    def __repr__(self):
        return "<Data %r>" % str(self.date_created)
