import pandas as pd
import sys
from os import system, name

encryptionkey = pd.read_csv(r"decodekeynew.csv",
                            sep=',', names=['Character', 'Byte'], header=None, skiprows=[0])

df = pd.DataFrame(data=encryptionkey)

df['Character'] = df['Character'].astype(str)
df['Byte'] = df['Byte'].astype(str)

def split(message):
    return [char for char in message]

def code_message(message):
    message_split = split(message)
    coded_message = ""

    for i in range(len(message_split)):
        j = message_split[i]
        try:
            coded_char = encryptionkey.loc[encryptionkey['Character'] == j, 'Byte'].iloc[0]
        except:
            print('Caractere não encontrado!')
            coded_char = '@@@'
        finally:
        	coded_message = coded_message + coded_char
    return coded_message

def decode_message(message):
    new_word = ''
    decoded_message = []

    for i in range(0, len(message), 2):
        j = message[i:i + 2]
        index_nb = df[df.eq(j).any(1)]

        df2 = index_nb['Character'].tolist()

        s = [str(x) for x in df2]

        decoded_message = decoded_message + s

    new_word = ''.join(decoded_message)

    return new_word


def clear():
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 

clear()
while True:
    clear()
    option = str(input('Escolha uma das opções a seguir:\n( E ) para encriptar uma mensagem\n( D ) para decriptar uma mensagem\n( S ) para sair\nOpção: '))
    if option.lower() == 'e':
        clear()
        message = str(input('Digite a mensagem que deseja encriptar:\n'))
        encripted = code_message(message)
        print('Sua mensagem encriptada: %s \n' % encripted)
    elif option.lower() == 'd':
        clear()
        message = str(input('Digite a hash que deseja decriptar:\n'))
        decripted = decode_message(message)
        print('Sua mensagem decriptada: %s \n' % decripted)
    elif option.lower() == 's':
        clear()
        print('Até logo!')
        sys.exit()
    else:
        clear()
        print('Opção não identificada!!!')
    input('Pressione qualquer tecla para voltar ao menu!')