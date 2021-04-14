from flask import request, url_for, render_template
from flask_admin import Admin, AdminIndexView, expose, helpers
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user, login_user
from werkzeug.utils import redirect
from wtforms import validators

from flask_app import app, db
from flask_app.admin.form import LoginForm, RegisterForm
from flask_app.admin.validator import dob_check, phone_check, email_check
from flask_app.model.user import User, Student

# Login manager to handle all login related tasks
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class StudentView(ModelView):
    can_edit = False
    can_delete = False
    form_excluded_columns = ['date_enroll', 'updated_on']
    form_choices = {
        'class_opted': [
            (5, '5th'),
            (6, '6th'),
            (7, '7th'),
            (8, '8th'),
            (9, '9th'),
            (10, '10th')
        ]
    }

    form_args = {
        'name': {
            'label': 'First Name',
            'validators': [validators.required()]
        },
        'dob': {
            'validators': [validators.required(), dob_check]
        },
        'phone_no': {
            'validators': [validators.required(), phone_check]
        },
        'email': {
            'validators': [validators.required(), email_check]
        },
        'class_opted': {
            'validators': [validators.required()]
        },
        'pin': {
            'validators': [validators.required()]
        }
    }

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('admin.login_view', next=request.url))


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # Handle user login
        form = LoginForm(request.form)
        msg = ""
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            if form.validate_login():
                login_user(user)
            else:
                msg = 'Wrong user or password'

        if current_user.is_authenticated:
            return redirect(url_for('.index'))
        return render_template('login/login.html', msg=msg, form=form)

    @expose('/register', methods=["GET", 'POST'])
    def register_view(self):
        form = RegisterForm(request.form)
        msg = ""
        if helpers.validate_form_on_submit(form):
            if form.register_user():
                return redirect(url_for('.login_view'))
            else:
                msg = 'User Already register'

        if current_user.is_authenticated:
            return redirect(url_for('.index'))
        return render_template('login/register.html', msg=msg, form=form)


admin_panel = Admin(app, name='Studiuz', template_mode='bootstrap3', index_view=MyAdminIndexView())
admin_panel.add_view(StudentView(Student, db.session))
