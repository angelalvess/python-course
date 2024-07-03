
import os


def listar(tasks):
    if not tasks:
        print("Nenhuma tarefa cadastrada")
        return

    for task in tasks:
        print(task)


def desfazer(tasks, tasks_refazer):
    if not tasks:
        print("Nenhuma tarefa para desfazer")
        return

    task = tasks.pop()
    tasks_refazer.append(task)


def refazer(tasks, tasks_refazer):
    if not tasks_refazer:
        print("Nenhuma tarefa para refazer")
        return

    task = tasks_refazer.pop()
    tasks.append(task)


def adicionar(task, tasks):
    if not task:
        print("Você precisa adicionar uma tarefa")
        return
    tasks.append(task)


tasks = []
tasks_refazer = []


while True:
    print("Comandos: listar, desfazer e refazer")
    task = input("Digite uma tarafa ou comando: ")

    if task == "listar":
        listar(tasks)
        continue
    elif task == "desfazer":
        desfazer(tasks, tasks_refazer)
        listar(tasks)
        continue
    elif task == "refazer":
        refazer(tasks, tasks_refazer)
        listar(tasks)
        continue
    elif task == "clear":
        os.system("clear")
        continue
    else:
        adicionar(task, tasks)
        listar(tasks)

        continue
