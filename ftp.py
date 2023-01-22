import socket
import os
from colorama import Fore
from datetime import date, datetime
from util import remove_control_characters


class FtpPot:
    def __init__(self, host, port, connection_message, bait_message):
        self.host = host
        self.port = port
        self.connection_message = connection_message
        self.bait_message = bait_message

    def run(self):
        global resposta
        date_today = date.today()
        now = datetime.now()
        bytes = 1024

        try:
            os.makedirs(f'/etc/honeycomb/logs/ftp/{date_today}/ips')
        except FileExistsError:
            pass

        ftp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ftp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        address = (self.host, self.port)
        ftp_socket.bind(address)
        ftp_socket.listen(1000)

        client_socket, client_address = ftp_socket.accept()
        client_socket.send(self.connection_message.encode('utf-8'))

        log_ips = open(f'/etc/honeycomb/logs/ftp/{date_today}/IPs.log', 'a')
        log_ips.write(f'IP: {client_address[0]} | Date: {now.strftime("%Y/%m/%d %H:%M:%S")}\n')
        log_ips.close()

        print(
            f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}FTP Activity Detected: {client_address[0]}:{client_address[1]}')

        while True:
            try:
                resposta = client_socket.recv(bytes).decode().strip()
                resposta = remove_control_characters(resposta)

                if resposta:
                    client_socket.send(self.bait_message.encode('utf-8'))

                    print(
                        f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}FTP Command: {resposta} | {client_address[0]}:{client_address[1]}')

                    log_ftp = open(
                        f'/etc/honeycomb/logs/ftp/{date_today}/ips/{client_address[0].replace(".", "_")}_commands.log',
                        'a')
                    log_ftp.write(f'{resposta}\n')
                    log_ftp.close()
                else:
                    print(
                        f'{Fore.LIGHTRED_EX}[-] {Fore.LIGHTWHITE_EX}FTP Connection Closed: {client_address[0]}:{client_address[1]}')

                    ftp_socket.listen(1000)
                    client_socket, client_address = ftp_socket.accept()
                    client_socket.send(self.connection_message.encode('utf-8'))

                    print(
                        f'{Fore.LIGHTGREEN_EX}[+] {Fore.LIGHTWHITE_EX}FTP Activity Detected: {client_address[0]}:{client_address[1]}')

                    log_ips = open(f'/etc/honeycomb/logs/ftp/{date_today}/IPs.log', 'a')
                    log_ips.write(f'{client_address[0]} | Date: {now.strftime("%Y/%m/%d %H:%M:%S")}\n')
                    log_ips.close()
            except:
                pass
