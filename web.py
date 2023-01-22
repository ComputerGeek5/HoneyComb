import http.server as SimpleHTTPServer
import os
from datetime import date, datetime
from colorama import Fore


class WebPot:
    class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            date_today = date.today()
            now = datetime.now()

            try:
                os.makedirs(f'/etc/honeycomb/logs/web/{date_today}/ips')
            except FileExistsError:
                pass

            request = format % args
            print(
                f'{Fore.LIGHTBLUE_EX}[*] {Fore.LIGHTWHITE_EX}HTTP Request: {request} | {self.client_address[0]}:{self.client_address[1]}')

            log_ips = open(f'/etc/honeycomb/logs/web/{date_today}/IPs.log', 'a')
            log_ips.write(f'IP: {self.client_address[0]} | Date: {now.strftime("%Y/%m/%d %H:%M:%S")}\n')
            log_ips.close()

            log_web = open(f'/etc/honeycomb/logs/web/{date_today}/ips/{self.client_address[0].replace(".", "_")}.log',
                           'a',
                           1)
            log_web.write('%s%s\n\n' % (self.headers, request))
            log_web.close()

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        web_dir = '/etc/honeycomb/web_bait'
        os.chdir(web_dir)

        handler = self.Handler
        address = (self.host, self.port)
        server = SimpleHTTPServer.HTTPServer(address, handler)
        server.serve_forever()
