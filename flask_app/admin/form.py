from wtforms import form, fields, validators, ValidationError

from flask_app import db
from flask_app.model.user import User


class LoginForm(form.Form):
    username = fields.StringField(validators=[validators.required()])
    password = fields.StringField(validators=[validators.required()])

    def validate_login(self):
        # Validate user with credentials
        user = self.get_user()

        if user is None:
            return False

        return True

    def get_user(self):
        return User.query.filter(User.username == str(self.username.data), User.password == str(self.password.data)).first()


class RegisterForm(form.Form):
    username = fields.StringField(validators=[validators.required()])
    password = fields.StringField(validators=[validators.required()])

    def register_user(self):
        # Validate user with credentials
        user_existed = self.get_user()

        if user_existed:
            return False
        user = User(username=self.username.data, password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return True

    def get_user(self):
        return User.query.filter(User.username == str(self.username.data)).first()

