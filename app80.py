class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def set_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection


c1 = Connection()
c1.set_user('angel')
c1.set_password('1234')
print(c1.user, c1.password)

print('-------------')

c2 = Connection.set_with_auth('angelina', '12345')
print(c2.user, c2.password)
