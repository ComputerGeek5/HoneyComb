import socket
import os
from colorama import Fore
from datetime import date, datetime


class FtpPot:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        global resposta
        date_today = date.today()
        now = datetime.now()
        bytes = 1024

        try:
            os.makedirs(f'/etc/honeycomb/logs/ftp/{date_today}/ips')
        except FileExistsError:
            pass

        try:
            pot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            pot_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            pot_socket.bind((self.host, self.port))

            pot_socket.listen(1000)
            client_socket, client_address = pot_socket.accept()

            log_ips = open(f'/etc/honeycomb/logs/ftp/{date_today}/IPs.log', 'a')
            log_ips.write(f'IP: {client_address[0]} | Date: {now.strftime("%Y/%m/%d %H:%M:%S")}\n')
            log_ips.close()

            print(
                f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}FTP Activity Detected: {client_address[0]}:{client_address[1]}')
            client_socket.send('220 (vsFTPd 2.3.4)\n\r'.encode('utf-8'))
        except:
            pass

        while True:
            try:
                resposta = client_socket.recv(bytes).decode().replace("\n", "").replace("\r", "")

                if resposta:
                    print(
                        f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}FTP Command: {resposta} | {client_address[0]}:{client_address[1]}')

                    users_used_ftp = open(
                        f'/etc/honeycomb/logs/ftp/{date_today}/ips/{client_address[0].replace(".", "_")}.log',
                        'a')
                    users_used_ftp.write(f'{resposta}\n')
                    users_used_ftp.close()
            except:
                pass

            if resposta:
                try:
                    # TODO: It would be nicer if we made this message customizable as well in .env
                    client_socket.send('530 user not found\n\r'.encode('utf-8'))
                except:
                    pass

            if not resposta:
                try:
                    print(
                        f'{Fore.LIGHTRED_EX}[-] {Fore.LIGHTWHITE_EX}FTP Connection Closed: {client_address[0]}:{client_address[1]}')
                    pot_socket.listen(1000)
                    client_socket, client_address = pot_socket.accept()

                    print(
                        f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}FTP Activity Detected: {client_address[0]}:{client_address[1]}')
                    client_socket.send('220 (vsFTPd 3.0.3)\n\r'.encode('utf-8'))

                    log_ips = open(f'/etc/honeycomb/logs/ftp/{date_today}/IPs.log', 'a')
                    log_ips.write(f'IP: {client_address[0]} | Date: {now.strftime("%Y/%m/%d %H:%M:%S")}\n')
                    log_ips.close()

                    if resposta:
                        client_socket.send('530 user not found\n\r'.encode('utf-8'))
                except:
                    pass
