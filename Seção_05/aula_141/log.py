# Abstração
class Log:
    def log(self, msg):
        raise NotImplementedError('Implemente o mátdodo log')


class LogFileMixing(Log):
    def log(self, msg):
        print(msg)


if __name__ == '__main__':
    l = LogFileMixing()
    l.log('Teste')
