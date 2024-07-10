
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:

    def _log(self, msg):
        raise NotImplementedError('Subclass must implement abstract method')

    def log_error(self, msg):
        return self._log(f'[ERROR] {msg}')

    def log_warning(self, msg):
        return self._log(f'[WARNING] {msg}')


class LogFileMixin(Log):

    def _log(self, msg):
        msg_formatada = f' {msg}, ({self.__class__.__name__})'
        with open(LOG_FILE, 'a', encoding='utf-8') as file:
            file.write(msg_formatada)
            file.write('\n')


class LogPrintMixin(Log):

    def _log(self, msg):
        print(f' {msg}, ({self.__class__.__name__})')


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Hello, world!')
    lp.log_warning('Hello, world!')

    lf = LogFileMixin()
    lf.log_error('Bye, world!')
    lf.log_warning('Bye, world!')
