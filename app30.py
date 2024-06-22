import os

listt = []

while True:

    print('Select an option:')
    option = input('[i]nsert, [l]ist, [d]elete: ')

    if option == 'i':
        os.system('clear')
        valor = input('Insert a value: ')
        listt.append(valor)
        print('Inserting...')
    elif option == 'l':
        os.system('clear')

        if len(listt) == 0:
            print('List is empty')

        for i, value in enumerate(listt):
            print(i, value)

    elif option == 'd':
        index_str = input('Enter the index to delete: ')

        try:
            index = int(index_str)
            del listt[index]
        except:
            print('Invalid index')
    else:
        print('Invalid option')
