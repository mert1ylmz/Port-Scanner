import socket
from concurrent.futures import ThreadPoolExecutor

TARGET = "127.0.0.1"
PORT_START = 1
PORT_END = 3000
TIMEOUT = 1

def scan_port(port):
    try:
        #IPv4 ve TCP kullanarak bir bağlantı olutur
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
            s.settimeout(TIMEOUT)

            result = s.connect_ex((TARGET, port))
            if result==0:
                print(f"PORT {port} is OPEN")
    except Exception as e:
        e

def main():
    print(f"Scanning on target {TARGET}")
    print(f"Scanning ports {PORT_START} - {PORT_END}")

    with ThreadPoolExecutor(max_workers=100) as executor:
        ports = range(PORT_START, PORT_END+1)
        executor.map(scan_port, ports)

if __name__ == "__main__":
    main()
