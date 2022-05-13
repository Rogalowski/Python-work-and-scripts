import paramiko

t = paramiko.Transport(("54.72.144.20", 7515))
t.connect(username='kgawda', password=open('/home/kjg/alx_ssh.txt').read().strip())
sesja = t.open_session()
sesja.exec_command('ls -al')

dane = sesja.recv(1024)
while dane:
    print(dane.decode('utf-8'))
    dane = sesja.recv(1024)

# while dane := sesja.recv(1024):
#     print(dane.decode('utf-8'))

sftp = paramiko.SFTPClient.from_transport(t)
print(sftp.open('test.txt').read())
sftp.get('test.txt', 'test_from_remote.txt')
# sftp.put()

t.close()
