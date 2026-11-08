import socket

HOST = "127.0.0.1"  # Server hostname or IP address
PORT = 65432        # Server port

def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")

        message = "Hello, Server!"
        client_socket.sendall(message.encode("utf-8"))

        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")

if __name__ == "__main__":
    run_client()
