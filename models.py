from exts import db
from uuid import uuid4

class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.String(100), primary_key=True, default=uuid4)
    username = db.Column(db.String(100), nullable=False, unique=True)
    __password = db.Column(db.String(100), nullable=False)
    try_times = db.Column(db.Integer, nullable=False, default=0)
    solved_number = db.Column(db.Integer, nullable=False, default=0)
    total_guess_times = db.Column(db.Integer, nullable=False, default=0)
    
    def get_pwd(self) -> str:
        return self.__password