from database.dbmanager import DBManager

class UserModel:
    def __init__(self, db: DBManager, username: str, _hash: str, email: str):
        self._db = db
        self._username = username
        self._hash = _hash
        self._email = email
        self._values = (self._username, self._hash, self._email)

    def in_database(self):
        if self._db.find_by_value('users', 'username', self._username):
            return True
        return False

    def save_to_database(self):
        if not self.in_database():
            if not self._db.find_by_value('users', 'email', self._username):
                self._db.insert('users', *self._values)
            else:
                raise EmailOccupiedException
        else:
            raise UsernameTakenException

    def remove_from_database(self):
        if self.in_database():
            self._db.remove_by_value('users', 'username', self._username)
        

