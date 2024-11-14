from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, EditProfileForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Введены неверные данные')
    return render_template('login.html', form=form, title='Login')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html')

#обработчик маршрута для редактирования профиля
@app.route("/account/edit", methods=["GET", "POST"])
@login_required
def edit_account():
    form = EditProfileForm()
    if form.validate_on_submit():
        # Обновляем имя пользователя и email
        current_user.username = form.username.data
        current_user.email = form.email.data

        # Если введен новый пароль, хешируем и обновляем его
        if form.password.data:
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            current_user.password = hashed_password

        db.session.commit()
        flash("Ваш профиль был обновлен", "success")
        return redirect(url_for("account"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template("edit_account.html", form=form)




# def edit_account():
#     form = EditProfileForm()
#     if form.validate_on_submit():
#         current_user.username = form.username.data
#         current_user.email = form.email.data
#         current_user.set_password(form.password.data)  # предполагается, что у вас есть метод set_password
#         db.session.commit()
#         flash("Ваш профиль был обновлен", "success")
#         #db.session.refresh(current_user)  # Обновляем объект current_user
#         return redirect(url_for("account"))
#     elif request.method == "GET":
#         form.username.data = current_user.username
#         form.email.data = current_user.email
#     return render_template("edit_account.html", form=form)
