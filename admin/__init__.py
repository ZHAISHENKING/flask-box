"""
为了防止db循环调用
将db在仅初始化时调用的admin中注册
"""

from flask_admin import Admin, AdminIndexView
from flask_mongoengine import MongoEngine
from flask import Flask, url_for, redirect, render_template, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash

from wtforms import form, fields, validators
from flask_restful import Resource
import flask_login as login
from flask_limiter import Limiter
from flask_wechatpy import Wechat
from flask_limiter.util import get_remote_address
from flask_admin.contrib.mongoengine import ModelView
import redis

r = redis.StrictRedis("localhost", 6379, db=0)
limiter = Limiter(
    key_func=get_remote_address,   # 根据访问者的IP记录访问次数
    # default_limits=["7 per day"]
)
db = MongoEngine()
wechat = Wechat()


class AdminUser(db.Document):

    username = db.StringField(max_length=80, unique=True)
    email = db.StringField(max_length=120)
    password = db.StringField()

    meta = {
        'db_alias': 'mark'
    }
    # Flask-Login integration
    # NOTE: is_authenticated, is_active, and is_anonymous
    # are methods in Flask-Login < 0.3.0
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.password = generate_password_hash(self.password)
        super(AdminUser, self).save(*args, **kwargs)

    def check_password(self, hash, password):
        return check_password_hash(hash, password)

    # Required for administrative interface
    def __unicode__(self):
        return self.username


# Define login and registration forms (for flask-login)
class LoginForm(form.Form):
    username = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return AdminUser.objects(username=self.username.data).first()


class RegistrationForm(form.Form):
    username = fields.StringField(validators=[validators.required()])
    email = fields.StringField()
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        if AdminUser.objects(username=self.username.data):
            raise validators.ValidationError('Duplicate username')


# Create customized model view class
class MyModelView(ModelView):
    column_list = ("username", "email")

    def is_accessible(self):
        return login.current_user.is_authenticated


# Create customized index view class
class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return login.current_user.is_authenticated


# Flask views
# @app.route('/')

class Index(Resource):
    def get(self):
        return make_response(render_template('index.html', user=login.current_user))


class LoginView(Resource):
    def __init__(self):
        self.form = LoginForm(request.form)

    def get(self):
        return make_response(render_template('form.html', form=self.form))

    def post(self):
        if self.form.validate():
            user = self.form.get_user()
            password = request.form.get("password")
            if AdminUser.check_password(AdminUser, user.password, password):
                login.login_user(user)
                return redirect(url_for('api.index'))
        return make_response(render_template('form.html', form=self.form))


class RegisterView(Resource):

    def __init__(self):
        self.form = RegistrationForm(request.form)

    def get(self):
        return make_response(render_template('form.html', form=self.form))

    def post(self):

        if self.form.validate():
            user = AdminUser()

            self.form.populate_obj(user)
            user.save()

            login.login_user(user)
            return redirect(url_for('api.index'))
        return make_response(render_template('form.html', form=self.form))


class LogoutView(Resource):

    def get(self):
        login.logout_user()
        return redirect(url_for('api.index'))


admin = Admin(
    url='/api',
    index_view=MyAdminIndexView(
        url="/api/admin/",
        name="导航栏"
    ),
    name=u"model主页"
)
