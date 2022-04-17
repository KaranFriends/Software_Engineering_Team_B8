from wsgiref.validate import validator
from flask import Flask, flash, g, redirect, render_template, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_required
from flask_wtf import FlaskForm
from graphviz import render
from flask_bcrypt import bcrypt

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    if g.user:
        return render_template('index.html', user=session['user'])
    return redirect(url_for('index.html'))

# @app.route('/login', methods=['POST','GET'])
# def login():
#     if request.method == 'POST':
#         session.pop('user', None)
#         email = request.form.get("email")
#         password = request.form.get("password")
#         if password == 'aosdksad':
#             session['user'] = request.form['username']
#             flash('Thank you for registering')
#             return redirect(url_for(''))
#         db.session.add(new_user)
#         db.session.commit()
#     elif request.method == 'GET':
#         return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return render_template('index.html')



# @app.route('/register')
# def register():
#     new_user = User(email=email, password=password)
#     return render_template('register.html')

@app.route('/movie_details')
def movie_details():
    return render_template('movie_details.html')

@app.route('/promotions')
def promotions():
    return render_template('promotions.html')

@app.route('/edit_profile')
@login_required
def edit_profile():
    return render_template('edit_profile.html')


# @app.before_request
# def before_request():
#     g.user = None

#     if 'user_id' in session:
#         users
#         user = [x for x in users if x.id == session['user_id']][0]
#         g.user = user

if __name__ == '__main__':
    app.run(debug=True)