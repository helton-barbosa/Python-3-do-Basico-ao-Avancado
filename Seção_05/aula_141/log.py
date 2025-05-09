# Abstração
class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o mátdodo log')

    def log_error(self, msg):
        return self._log(f'Error: {msg} --> {self.__class__.__name__}')

    def log_success(self, msg):
        return self._log(f'Sucess: {msg} --> {self.__class__.__name__}')


class LogFileMixing(Log):
    def _log(self, msg):
        print(msg)


class LogPrintMixing(Log):
    def _log(self, msg):
        print(msg)


if __name__ == '__main__':
    lf = LogFileMixing()
    lp = LogPrintMixing()
    lf.log_error('Teste')
    lp.log_success('Teste')
