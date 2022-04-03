from database.dbmanager import DBManager

class UserModel:
    def __init__(
            self,
            db: DBManager,
            _hash: str,
            email: str,
            is_active: bool = False
           ):

        self._db = db
        self._hash = _hash
        self._email = email
        self._values = (self._hash, self._email)
        self._is_active = is_active
    
    def activate(self):
        pass

    def deactivate(self):
        pass

    def in_database(self):
        if self._db.find_by_value('users', 'email', self._email):
            return True
        return False

    def save_to_database(self):
        if not self.in_database():
            if not self._db.find_by_value('users', 'email', self._email):
                self._db.insert('users', *self._values)
            else:
                raise EmailOccupiedException
        else:
            raise UsernameTakenException

    def remove_from_database(self):
        if self.in_database():
            self._db.remove_by_value('users', 'email', self._email)
        

