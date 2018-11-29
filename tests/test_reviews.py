from app.models import Review,Employer
from app import db


def setUp(self):
        self.employer_Hassib = Employer(name = 'hassib',password = 'password', email = 'i@ms.com')
        self.new_review = Review(employee_id=12345,employee_name='Review for employees',image_path="default.jpg",employee_review='This employee very trustworthy',user = self.user_Hassib )


def tearDown(self):
        Review.query.delete()
        Employer.query.delete()