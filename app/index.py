from app import app, dao
from  flask import render_template
from flask import render_template, request, redirect, session, jsonify
import cloudinary.uploader
from flask_login import login_user, logout_user, current_user




@app.route('/')
def home():
    flights = dao.load_flight()
    return render_template('index.html', flights = flights)



@app.route('/book_flight/')
def book_flight():
    # f = dao.get_flight_by_id(fl_id)
    return render_template('book_flight.html' )

@app.route('/admin/')
def admin():
    return render_template('admin/index.html')

@app.route('/register/')
def register():
    err_msg = ''
    if request.method.__eq__('POST'):
        password = request.form['password']
        confirm = request.form['confirm']
        if password.__eq__(confirm):
            avatar = ''
            if request.files:
                res = cloudinary.uploader.upload(request.files['avatar'])
                avatar = res['secure_url']

            try:
                dao.register(name=request.form['name'],
                             username=request.form['username'],
                             password=password, avatar=avatar)
                return redirect('/login')
            except:
                err_msg = 'Hệ thống đang có lỗi! Vui lòng quay lại sau!'
        else:
            err_msg = 'Mật khẩu KHÔNG khớp!'

    return render_template('register.html', err_msg=err_msg)

@app.route('/login/', methods=['get', 'post'])
def login():
    if request.method.__eq__('POST'):
        username = request.form['username']
        password = request.form['password']
        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)
            return redirect('/')

    return render_template('login.html')


def load_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    app.run(debug=True)

