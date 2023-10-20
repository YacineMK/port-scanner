import socket

def spider(host):
    for port in range(1, 65535):  
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  
        result = s.connect_ex((host, port))
        if result == 0:
            print("[*] Port {} is open".format(port))  
        s.close()  