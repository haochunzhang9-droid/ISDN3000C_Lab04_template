import socket, time, json

HOST = "192.168.127.10"   # RDK-X5 IP
PORT = 65432

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"GET_DATA")
        data = s.recv(4096)
        info = json.loads(data.decode())   # JSON → dict
        print(f"[{info['time']}] CPU: {info['cpu_percent']}% | "
              f"Memory: {info['memory']}% | Disk: {info['disk']}% | "
              f"Platform: {info['platform']}")
    time.sleep(60)

