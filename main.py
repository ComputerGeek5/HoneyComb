import http.server as SimpleHTTPServer
import os
from datetime import date, datetime
import linecache

date_today = date.today()
now = datetime.now()


class WebPot:
    class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            log_file = open(f'/etc/honeycomb/logs/web_{date_today}/log.txt', 'w', 1)
            log_file.write('IP: %s\nDate: [%s]\n%s%s\n\n' % (
                self.client_address[0], self.log_date_time_string(), self.headers, format % args))

    def __init__(self, host, port):
        self.host = host
        self.port = port

        try:
            os.makedirs(f'/etc/honeycomb/logs/web_{date_today}')
        except FileExistsError:
            pass

        web_dir = '/etc/honeycomb/web'
        os.chdir(web_dir)
        handler = self.Handler
        httpd = SimpleHTTPServer.HTTPServer((host, port), handler)
        httpd.serve_forever()


# TODO: We should not rely on indexes
host = linecache.getline('/etc/honeycomb/app.conf', 2).split('=')[1].strip()
port = int(linecache.getline('/etc/honeycomb/app.conf', 5).split('=')[1].strip())

WebPot(host, port)
