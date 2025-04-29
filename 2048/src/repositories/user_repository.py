from database_connection import get_database_connection
from entities.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
        self._cursor = connection.cursor()

    def find_all(self):
        self._cursor.execute("SELECT * FROM users")

        rows = self._cursor.fetchall()

        return [User(row["username"], row["hiscore"]) for row in rows]
    
    def find_by_username(self, username):
        self._cursor.execute("SELECT * FROM users WHERE username = ?", [username])
        user = self._cursor.fetchone()

        if user is not None:
            return User(user["username"], user["hiscore"])
        else:
            return False
    
    def create_user(self, user: User):
        username = user.get_username()
        hiscore = user.get_hiscore()
        self._cursor.execute("INSERT INTO users VALUES(?, ?)", [username, int(hiscore)])
        self._connection.commit()

    def update_hiscore(self, user: User):
        username = user.get_username()
        hiscore = user.get_hiscore()
        self._cursor.execute("UPDATE users SET hiscore = ? WHERE username = ?", (int(hiscore), username))
        self._connection.commit()
