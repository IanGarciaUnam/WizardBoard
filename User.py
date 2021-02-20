from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

session=[]
class Teacher(UserMixin):
    """
    Constructor para modelar al usuario-maestro 
    id
    name = name user
    password from wizardboard session
    is_admin (Boolean)
    """

 
    def __init__(self, id, name, password, is_admin=True):
        self.id = id
        self.name = name
        self.password = generate_password_hash(password)
        session.add(password)
        self.is_admin = is_admin

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.email)


class Student(UserMixin):

    def init(self,id, name, password, is_admin=False):
        self.id=id
        self.name=name
        self.password=generate_password_hash(password)
        self.is_admin=is_admin

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def join_session(self):

        if self.password in session:
            #Class.join(self.password)
