import spur


user='user'
host='192.168.0.31'


shell = spur.SshShell(hostname=host, username=user, password="321")
result = shell.run("ping -c6 vk.com".split(" "))
print(result.output.decode("utf-8")) # prints hello