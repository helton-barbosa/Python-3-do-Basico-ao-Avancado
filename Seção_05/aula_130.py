# method vs @classmethod vs @staticmethod
# method: método de instância, tem acesso ao self
# @classmethod: método de classe, tem acesso ao cls
# @staticmethod: método estático, não tem acesso ao self nem ao cls
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
    def create_with_auth(cls, usuario, senha):
        connection = cls()
        connection.user = usuario
        connection.password = senha
        return connection

    @staticmethod
    def soma(a, b):
        return a + b


con_1 = Connection()
con_1.set_user('Helton')
con_1.set_password('123456')
print(f'Host: {con_1.host}\nUsuário: {con_1.user}\nSenha: {con_1.password}\n')

con_2 = Connection.create_with_auth('Rose', '654321')
print(f'Host: {con_2.host}\nUsuário: {con_2.user}\nSenha: {con_2.password}\n')

print(Connection.soma(10, 20))
