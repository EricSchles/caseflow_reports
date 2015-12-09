from app import db
from app.models import Data
from datetime import datetime
from random import randint

for i in xrange(50):
    data = Data(datetime(randint(2011,2015),randint(1,10),randint(1,28),1,1))
    db.session.add(data)
    db.session.commit()


