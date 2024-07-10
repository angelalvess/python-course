class MyError(Exception):

    ...


class AnotherError(MyError):
    ...


def levantar_error():
    raise MyError("Erro levantado")


try:
    levantar_error()
except MyError as e:
    print(e)
    exception_ = AnotherError("Re-levantando erro")
    raise exception_ from e
