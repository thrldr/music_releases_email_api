from database.database import DBManager


class User:
    def __init__(self, username: str, _hash: str, email: str):
        self._username = username
        self._hash = _hash
        self._email = email
        self._values = (self._username, self._hash, self._email)

    def in_database(self):
        if DBManager.find_by_value('users', 'username', self._username):
            return True
        return False

    def save_to_database(self):
        if not self.in_database():
            if not DBManager.find_by_value('users', 'email', self._username):
                DBManager.insert('users', *self._values)
            else:
                raise EmailOccupiedException
        else:
            raise UsernameTakenException

    def remove_from_database(self):
        if self.in_database():
            DBManager.remove_by_value('users', 'username', self._username)
        

