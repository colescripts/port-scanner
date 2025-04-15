import socket
import argparse
import threading

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
    parser = argparse.ArgumentParser(description="Simple Multithreaded TCP Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP address")
    parser.add_argument("-p", "--ports", required=True, help="Port range (e.g. 20-80)")
    args = parser.parse_args()

    try:
        start_port, end_port = map(int, args.ports.split("-"))
        if start_port < 0 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except:
        print("[-] Invalid port range format. Use: start-end (e.g. 20-80)")
        exit()

    print(f"\nScanning {args.target} from port {start_port} to {end_port} using multithreading...\n")

# added multithreading to speed up the process
    
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(args.target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n[✓] Scan complete.")
