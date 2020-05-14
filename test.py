import sqlite3

answer = []
conn = sqlite3.connect("messanger.db")
cur = conn.cursor()
cur.execute(f"SELECT id FROM dialogs WHERE user_id = {1} and user2_id = {2}")
dialog = cur.fetchall()
if dialog:
    cur.execute(f"SELECT * FROM messages WHERE dialog_id = {dialog[0][0]}")
    history = cur.fetchall()
    if history:
        for messange in history:
            mess = {
                "user_id": messange[1],
                "message": messange[2],
                "attachment": messange[3],
                "time": messange[4],
            }
            answer.append(mess)
    print(history)
else:
    answer = None
conn.commit()
conn.close()
print({'messages': answer})
