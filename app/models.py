from . import db
from datetime import datetime


class Employer:

    def __init__(self,id,name,estate,category):
        self.id =id
        self.name = name
        self.estate = estate
        self.category = category
       

class Employee(db.Model):

    __tablename__ = 'employees'
    
    id = db.Column(db.Integer,primary_key = True)
    employee = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.employee}'

class Review(db.Model):
    
    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    employee_id = db.Column(db.Integer)
    employee_name = db.Column(db.String)
    image_path = db.Column(db.String)
    employee_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    employer_id = db.Column(db.Integer,db.ForeignKey("employers.id"))

    def __init__(self,employee_id,name,review):
        self.employee_id = employee_id
        self.name = name
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.employee_id == id:
                response.append(review)

        return response