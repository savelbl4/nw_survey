from Exscript.util.start import start
from Exscript import Host, Account
import re

account1 = Account('user', '321')
hosts = [
    Host('ssh://192.168.0.31'),
    Host('ssh://192.168.0.32'),
]

commands = [
    'who am i',
    'ip a',
]

a = []

def do_something(job, host, conn):
    for i in commands:
        conn.execute(i)
        a.append(conn.response)

with open('log.txt','w+') as fp:
    start([account1], hosts, do_something, stdout=fp)

for c in a:
    s = c.split("\r\n")
    # print(s)
    for string in s:
        match = re.search(r'\d.\d.\d.\d', string)
        print(string) if match else ''