from flask_login import login_required, current_user
from flask import Flask
from flask import render_template,redirect,url_for,abort
from . import main


@main.route('/')
def index():
    title='Home-Clean club'

    return render_template('index.html',title=title)

@main.route('/about')
def about():
    title='About Us- Clean club'
    return render_template('about.html',title=title)
  
@main.route('/index/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    form = ReviewForm()
    employee = get_employee(id)
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        # Updated review instance
        new_review = Review(employee_id=employee.id,employee_name=title,image_path=employee.poster,employee_review=review,user=current_user)

        # save review method
        new_review.save_review()
        return redirect(url_for('.employee',id = employee.id ))

    title = f'{employee.title} review'
    return render_template('new_review.html',title = title, review_form=form, employee=employee)
