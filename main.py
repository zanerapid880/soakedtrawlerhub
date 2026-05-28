"""cleaner_62ea52 - Network utility."""
import socket, json
SERVICE_TAG = "cleaner_62ea52"
def get_host_info() -> dict:
    hostname = socket.gethostname()
    try: ip = socket.gethostbyname(hostname)
    except socket.gaierror: ip = "127.0.0.1"
    return {"hostname": hostname, "ip": ip, "service": SERVICE_TAG}
def check_port(host: str, port: int, timeout: float = 1.0) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout): return True
    except (socket.timeout, ConnectionRefusedError, OSError): return False
def main():
    info = get_host_info()
    print(f"[{SERVICE_TAG}] Host info: {json.dumps(info)}")
    for port in [80, 443, 8080]: print(f"[{SERVICE_TAG}] Port {port}: {'open' if check_port('localhost', port) else 'closed'}")
if __name__ == "__main__":
    main()
