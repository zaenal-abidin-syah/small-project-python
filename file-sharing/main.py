# for implementing the HTTP Web servers
import http.server
# provides access to the BSD socket interface
import socket
# a framework for network servers
import socketserver
# to display a Web-based documents to users
import webbrowser
# to generate qrcode
import pyqrcode
from pyqrcode import QRCode
# convert into png format
import png
# to access operating system control
import os


# assigning the appropriate port value
PORT = 8011
# this finds the name of the computer user

# uncomment if use desktop
# os.environ['zaens']

 
# changing the directory to access the files desktop
# with the help of os module
# desktop = os.path.join(os.path.join(os.environ['zaens']),
                      #  'OneDrive')

# comment if not used manual directory
# dir = os.path.join('/home', 'USERPROFILE')
dir = os.path.join('/home', 'zaens')
# dir = os.path

# print(desktop)
# print(dir)

# os.chdir(desktop)
os.chdir(dir)

# creating a http request
Handler = http.server.SimpleHTTPRequestHandler
# returns, host name of the system under
# which Python interpreter is executed
hostname = socket.gethostname()

# finding the IP address of the PC

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# print(s)
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
print(IP)
link = IP

# converts the IP address into a Qrcode
url = pyqrcode.create(link)
# saves the Qrcode inform of svg
url.svg("myqr.svg", scale=8)
# opens the Qrcode image in the web browser
webbrowser.open('myqr.svg')


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print("Type this in your Browser", IP)
    print("or Use the QRCode")
    httpd.serve_forever()


