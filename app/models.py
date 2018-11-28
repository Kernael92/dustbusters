from . import db


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


class Review:
    
    all_reviews = []

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