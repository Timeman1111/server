import socket
import threading

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
# conn.sendall(data)




def return_int(value):
    return 1




def initateconnect():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("CONNECTED")
            while True:
                data = conn.recv(1024)
                data = str(data)
                if not data:
                    break
                if data == 'test':
                    conn.sendall(return_int)
                    return
            
            

       
initateconnect()
