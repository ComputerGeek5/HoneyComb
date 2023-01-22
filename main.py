from web import WebPot
from ftp import FtpPot
from telnet import TelnetPot
from dotenv import dotenv_values
import threading

env = dotenv_values('.env')
host = env['IP']

web_port = int(env['WEB_PORT'])
web_pot = threading.Thread(None, WebPot(host, web_port).run)
web_pot.start()

ftp_port = int(env['FTP_PORT'])
ftp_connection_message = env['FTP_CONNECTION_MESSAGE'] + '\n\r'
ftp_bait_message = env['FTP_BAIT_MESSAGE'] + '\n\r'
ftp_pot = threading.Thread(None, FtpPot(host, ftp_port, ftp_connection_message, ftp_bait_message).run)
ftp_pot.start()

telnet_port = int(env['TELNET_PORT'])
telnet_connection_message = env['TELNET_CONNECTION_MESSAGE']
telnet_bait_message = env['TELNET_BAIT_MESSAGE']
telnet_pot = threading.Thread(None, TelnetPot(host, telnet_port, telnet_connection_message, telnet_bait_message).run)
telnet_pot.start()
