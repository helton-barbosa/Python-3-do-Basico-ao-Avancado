# Abstração
from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o mátdodo log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Sucess: {msg}')


class LogFileMixing(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} --> {self.__class__.__name__}'
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada + '\n')


class LogPrintMixing(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} --> {self.__class__.__name__}'
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada + '\n')


if __name__ == '__main__':
    lf = LogFileMixing()
    lp = LogPrintMixing()
    lf.log_error('Teste')
    lp.log_success('Teste')
