from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

# class Actor(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name= db.Column(db.String(100), nullable=False , unique= True
#     hiringprice = db.Column(db.String(20))
#     age= db.Column(db.Integer)
#     nationality = db.Column(db.String(50))
#     bestperformance = db.Column(db.String(250))

    # def to_dict(self):
    #     return{
    #         'id': self.id,
    #         'name': self.name,
    #         'hiringprice':self.hiringprice,
    #         'nationality':self.nationality,
    #         'bestperformance': self.bestperformance
    #     }
