from abc import ABC, abstractmethod


class Notificacao(ABC):

    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool:
        ...


class NotificacaoEmail(Notificacao):

    def enviar(self) -> bool:
        print(f'Enviando email: {self.mensagem}')
        return True


class NotificacaoSMS(Notificacao):

    def enviar(self) -> bool:
        print(f'Enviando SMS: {self.mensagem}')
        return False


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada com sucesso')
    else:
        print('Falha ao enviar notificação')


notificacao_email = NotificacaoEmail('Olá, você foi notificado por email')
notificacao_sms = NotificacaoSMS('Olá, você foi notificado por SMS')


notificar(notificacao_email)
print()
notificar(notificacao_sms)
