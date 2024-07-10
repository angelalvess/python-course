from abc import ABC, abstractmethod


class Log(ABC):

    @abstractmethod
    def _log(self, msg):
        ...

    def log_error(self, msg):
        return self._log(f'[ERROR] {msg}')

    def log_warning(self, msg):
        return self._log(f'[WARNING] {msg}')


class LogPrintMixin(Log):

    def _log(self, msg):
        print(f' {msg}, ({self.__class__.__name__})')


l1 = LogPrintMixin()
l1.log_error('Hello, world!')
