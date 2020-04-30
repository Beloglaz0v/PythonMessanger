import sqlite3


def connect_to_db(func):
    def wrapper(*args):
        conn = sqlite3.connect("messanger.db")
        cur = conn.cursor()
        result = func(*args, cur)
        conn.commit()
        conn.close()
        return result
    return wrapper


@connect_to_db
def select(cur):
    cur.execute(f"SELECT id, login, password FROM users")
    return cur.fetchall()

print(select())