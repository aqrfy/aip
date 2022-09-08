Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
import  pyfiglet
logo =	pyfiglet.figlet_format('###a bat')
print(X+logo)


import socket as s
host = input ("\033[1;33m a bat : ")
print (f'IP of (host) is {s.gethostbyname(host)}')     