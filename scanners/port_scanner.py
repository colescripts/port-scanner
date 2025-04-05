import socket
import argparse

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple TCP Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-p", "--ports", required=True, help="Port range (e.g. 20-80)")
    args = parser.parse_args()

    start_port, end_port = map(int, args.ports.split("-"))

    print(f"Scanning {args.target} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        scan_port(args.target, port)
