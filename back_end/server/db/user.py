import bcrypt
from server.db import get_db, db_logger


def create_user(email, password):
    if email is None or password is None:
        raise ValueError('Email and password a mandatory fields')

    db_logger.log(f'Trying to create user with email={email}, password={password}')

    hashed_passwd = bcrypt.hashpw(password, bcrypt.gensalt())

    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users(email, password) VALUES (?,?)", (email, hashed_passwd))

    new_user_id = cursor.lastrowid

    db.commit()
    db_logger.log(f'User has been created successfully. New user_id is {new_user_id}')
    return new_user_id


def authenticate_user(email, password):
    [id, stored_email, hashed_password] = find_user(email)

    if stored_email is None:
        raise LookupError('Invalid email or password')

    if bcrypt.hashpw(password, hashed_password) == hashed_password:
        return {'id': id, 'email': stored_email}
    else:
        raise LookupError('Invalid email or password')


def find_user(email):
    if email is None:
        raise ValueError('Email must be provided to find_user method to make a lookup')

    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users WHERE email=?", (email,))

    return cursor.fetchone()


def delete_user(id):
    if id is None:
        raise ValueError('Id must be provided to delete user')

    db = get_db()
    cursor = db.cursor()

    cursor.execute("DELETE FROM users WHERE id=?", (id,))

    db.commit()
    # test comment
    return cursor.fetchone()
