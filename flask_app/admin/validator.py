from datetime import datetime, timedelta
import re

from wtforms import ValidationError


# DOB validator
def dob_check(form, field):
    age_in_days = datetime.now().date() - field.data
    print(age_in_days)
    if age_in_days < timedelta(days=3650):
        raise ValidationError('Age must be greater than 10')


def phone_check(form, field):
    if len(field.data) != 10:
        raise ValidationError("Phone must be 10 number")


def email_check(form, field):
    EMAIL_REGEX = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if not re.search(EMAIL_REGEX, field.data):
        raise ValidationError("Invalid email")
