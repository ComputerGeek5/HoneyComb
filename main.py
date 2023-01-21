import http.server as SimpleHTTPServer
import os
from datetime import date
from dotenv import dotenv_values

date_today = date.today()


class WebPot:
    class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            log_file = open(f'/etc/honeycomb/logs/web/{date_today}/log.txt', 'a', 1)
            log_file.write('IP: %s\nDate: [%s]\n%s%s\n\n' % (
                self.client_address[0], self.log_date_time_string(), self.headers, format % args))

    def __init__(self, host, port):
        self.host = host
        self.port = port

        try:
            os.makedirs(f'/etc/honeycomb/logs/web/{date_today}')
        except FileExistsError:
            pass

        web_dir = '/etc/honeycomb/web_bait'
        os.chdir(web_dir)
        handler = self.Handler
        httpd = SimpleHTTPServer.HTTPServer((host, port), handler)
        httpd.serve_forever()


env = dotenv_values('.env')
host = env['IP']
port = int(env['WEB_PORT'])

WebPot(host, port)
