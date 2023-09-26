from tables import db, Messages


def insert_message(text, user_name):
    data = Messages(text=str(text), user_name=str(user_name))
    db.add(data)
    db.commit()


def get_all_data_message():
    data = db.query(Messages).all()
    return data


def get_data_message_filter_user(user):
    data = db.query(Messages).filter(Messages.user_name == str(user)).all()
    return data
