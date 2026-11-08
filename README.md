# Python TCP Socket Client-Server Application

A minimal, robust demonstration of bidirectional client-server communication using Python's built-in `socket` library over TCP (Transmission Control Protocol).

---

## Overview

This project contains two primary scripts:

- **`server.py`**: Binds to a local network interface, listens on a designated port, accepts an incoming client connection, receives transmitted byte data, and echoes it back.
- **`client.py`**: Establishes a TCP connection to the host address and port, sends an encoded string message, awaits the server's reply, and terminates gracefully.

---

## Prerequisites

- **Python 3.8+** (No external dependencies or third-party packages required).

---

## File Structure

```text
.
├── server.py       # TCP socket server implementation
├── client.py       # TCP socket client implementation
└── README.md       # Project documentation and guide
```

---

## Getting Started

### 1. Launch the Server

Open a terminal or command prompt window and start the listening server:

```bash
python server.py
```

Expected output:
```text
Server listening on 127.0.0.1:65432...
```

### 2. Run the Client

Open a second terminal window (leaving the server terminal running) and execute the client:

```bash
python client.py
```

Expected output in client terminal:
```text
Connected to server at 127.0.0.1:65432
Received from server: Hello, Server!
```

Expected output in server terminal:
```text
Connected by ('127.0.0.1', 54321)
Received: Hello, Server!
```

---

## Configuration

Both `server.py` and `client.py` expose two primary constants at the top of their respective files:

| Variable | Default Value | Description |
| :--- | :--- | :--- |
| `HOST` | `"127.0.0.1"` | Loopback address (localhost). To allow connections from external devices, set to `"0.0.0.0"` on the server and point the client to the server's local LAN IP. |
| `PORT` | `65432` | Port number. Non-privileged ports range from `1024` to `65535`. |

---

## How It Works

```
+-------------+                     +-------------+
|  client.py  |                     |  server.py  |
+-------------+                     +-------------+
       |                                   |
       |  socket(AF_INET, SOCK_STREAM)     |  socket(AF_INET, SOCK_STREAM)
       |                                   |  bind(HOST, PORT)
       |                                   |  listen()
       |  connect(HOST, PORT) ------------>|  accept()
       |                                   |
       |  sendall("Hello, Server!") ------>|  recv(1024)
       |                                   |
       |  recv(1024) <---------------------|  sendall(data)
       |                                   |
       |  close()                          |  close()
```

1. **`socket.AF_INET`**: Designates IPv4 as the addressing family.
2. **`socket.SOCK_STREAM`**: Specifies TCP as the transport layer protocol (guarantees ordered, reliable delivery).
3. **`SO_REUSEADDR`**: Socket option used on the server to prevent `OSError: [Errno 98] Address already in use` errors during rapid restarts.
4. **Context Managers (`with` blocks)**: Automatically handle clean socket closure and resource cleanup even if unhandled exceptions occur.

---

## Troubleshooting

- **`ConnectionRefusedError: [Errno 111/61] Connection refused`**  
  The client tried to connect before the server was running, or the host/port settings do not match. Start `server.py` first.

- **`OSError: [Errno 98/48] Address already in use`**  
  The target port is currently occupied by another process or a previous socket in the `TIME_WAIT` state. Ensure `SO_REUSEADDR` is set or choose another port number (e.g., `65433`).

- **Firewall Restrictions**  
  If testing across two physical machines over a local network, ensure incoming TCP connections on your chosen port are permitted by your operating system's firewall.
