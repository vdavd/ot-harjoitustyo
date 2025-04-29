from database_connection import get_database_connection
from entities.user import User

class UserRepository:
    """Class for interfacing with the users-table in the SQLite database.
    """    
    def __init__(self, connection):
        """Class constructor that initiates the database connection.

        Args:
            connection: The database connection object.
        """        
        self._connection = connection
        self._cursor = connection.cursor()

    def find_all(self):
        """Method for fetching all users in the users table.

        Returns:
            List of user objects.
        """        
        self._cursor.execute("SELECT * FROM users")

        rows = self._cursor.fetchall()

        return [User(row["username"], row["hiscore"]) for row in rows]
    
    def find_by_username(self, username):
        """Method for fetching a single user with a given username.

        Args:
            username: Username of the user of interest.

        Returns:
            If user was found, returns user object. Otherwise returns false.
        """        
        self._cursor.execute("SELECT * FROM users WHERE username = ?", [username])
        user = self._cursor.fetchone()

        if user is not None:
            return User(user["username"], user["hiscore"])
        else:
            return False
    
    def create_user(self, user: User):
        """Method for adding a new user to the users-table in the database.

        Args:
            user: User object that will be added to the database.
        """        
        username = user.get_username()
        hiscore = user.get_hiscore()
        self._cursor.execute("INSERT INTO users VALUES(?, ?)", [username, int(hiscore)])
        self._connection.commit()

    def update_hiscore(self, user: User):
        """Method for updating the hiscore of a given user.

        Args:
            user: User object of the user to be updated.
        """        
        username = user.get_username()
        hiscore = user.get_hiscore()
        self._cursor.execute("UPDATE users SET hiscore = ? WHERE username = ?", (int(hiscore), username))
        self._connection.commit()
