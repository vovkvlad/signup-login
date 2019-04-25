from server.db import get_db, db_logger


def create_user(email, password):
    if email is None or password is None:
        raise ValueError('Email and password a mandatory fields')

    db_logger.log(f'Trying to create user with email={email}, password={password}')
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users(email, password) VALUES (?,?)", (email, password))

    new_user_id = cursor.lastrowid


    db.commit()
    db_logger(f'User has been created successfully. New user_id is {new_user_id}')
    return new_user_id


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
