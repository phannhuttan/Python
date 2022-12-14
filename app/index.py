from flask import render_template, request, redirect
from app import dao, app, login
from flask_login import login_user, logout_user, current_user
from app.decorators import annonymous_user
from app.admin import *




@app.route('/')
def home():
    flights = dao.load_flight()
    return render_template('index.html', flights = flights)



@app.route('/register/',methods=['get', 'post'])
def register():
    err_msg = ''
    if request.method.__eq__('POST'):
        password = request.form['password']
        confirm = request.form['confirm']
        if password.__eq__(confirm):
            try:
                dao.register(name=request.form['name'],
                             username=request.form['username'],
                             password=password)
                return redirect('/login/')
            except:
                err_msg = 'Hệ thống đang có lỗi! Vui lòng quay lại sau!'
        else:
            err_msg = 'Mật khẩu KHÔNG khớp!'

    return render_template('register.html', err_msg=err_msg)




@app.route('/book_flight/')
def book_flight():
    # f = dao.get_flight_by_id(fl_id)
    return render_template('book_flight.html' )



@app.route('/login-admin', methods=['post'])
def admin_login():
    username = request.form['username']
    password = request.form['password']
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)
    return redirect('/admin')

@app.route('/login/', methods=['get', 'post'])
def login_index():

    if request.method.__eq__('POST'):
        username = request.form['username']
        password = request.form['password']
        user = dao.auth_user(username=username, password=password)
        if user:
                login_user(user=user)
                return redirect('/admin')

    return render_template('login.html')


@app.route('/user-login/', methods=['get', 'post'])
@annonymous_user
def login_my_user():
    err=''
    if request.method.__eq__('POST'):
        username = request.form['username']
        password = request.form['password']
        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)
            return redirect('/')


    return render_template('login.html')



@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    app.run(debug=True)

