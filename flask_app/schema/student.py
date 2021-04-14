from flask_app import ma
from flask_app.model.user import Student


class StudentSchema(ma.ModelSchema):
    class Meta:
        model = Student
        include_fk = True