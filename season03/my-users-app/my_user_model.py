import sqlite3
con = sqlite3.connect('sql.db', check_same_thread=False)

class User:
    def create(user_info): # firstname, lastname, age, password, email
        cur = con.cursor()
        cur.execute(
            "INSERT INTO users (firstname, lastname, age, password, email) values (?, ?, ?, ?, ?)",
            (user_info['firstname'], user_info['lastname'], user_info['age'], 
            user_info['password'], user_info['email'],)
        )
        con.commit()
        cur.close()

    def get(user_id):
        cur = con.cursor()
        cur.execute("select * from users where id=:id", {"id": user_id})
        tmp = cur.fetchone()
        cur.close()
        return tmp

    def all():
        cur = con.cursor()
        cur.execute("select * from users")
        tmp = cur.fetchall()
        cur.close()
        return tmp

    def update(user_id, attribute, value):
        cur = con.cursor()
        cur.execute(
            f"update users set `{attribute}`=:value where id=:id", {
                "id": user_id,
                "value": value
            }
        )
        con.commit()
        cur.close()
    
    def destroy(user_id):
        cur = con.cursor()
        cur.execute(f"DELETE FROM users where id=:id", {"id": user_id,})
        con.commit()
        cur.close()
    

    def get_email(email):
        cur = con.cursor()
        cur.execute("select * from users where email=:email", {"email": email})
        tmp = cur.fetchone()
        cur.close()
        return tmp



#User.create({"firstname":"Asd", "lastname":"asd", "age":123, "password":"asd", "email":"asd"})
#print(User.get(1))
#print(User.all())
#User.update(1, "age", 44)
#User.destroy(1)