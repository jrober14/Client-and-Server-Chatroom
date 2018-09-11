import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 50000))
s.listen(1)
conn, addr = s.accept()
print(conn)
print(addr)
while True:
    data = conn.recv(1024)


    print(data)
    data = input(": ")
    conn.send(data.encode())

conn.close()
