from base import db


class Messages(db.Model):
    __tablename__ = "Messages"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    user_name = db.Column(db.String)


class User(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)


class DataHead(db.Model):
    __tablename__ = "PartDataHead"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Datetime, default='`now()`')

    Serial_number = db.Column(db.Integer)


class ParameterList(db.Model):
    __tablename__ = "ParameterList"

    id = db.Column(db.Integer, primary_key=True)
    id_Data_head = db.Column(db.Integer, db.ForeignKey('DataHead.id'))
    Actual_value = db.Column(db.Integer)
    Name = db.Column(db.String)


def create_tables():
    db.create_all()
