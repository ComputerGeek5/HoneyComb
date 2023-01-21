from web import WebPot
from ftp import FtpPot
from dotenv import dotenv_values
import threading

env = dotenv_values('.env')
host = env['IP']

web_port = int(env['WEB_PORT'])
web_pot = threading.Thread(None, WebPot(host, web_port).run)
web_pot.start()

ftp_port = int(env['FTP_PORT'])
ftp_pot = threading.Thread(None, FtpPot(host, ftp_port).run)
ftp_pot.start()
