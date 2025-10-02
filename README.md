# ISDN3000C Lab04

**Add your readme information**
# ISDN3000C Lab04 - IoT Gateway

## 📡 Network Setup
- **RDK-X5 (Server)**: 192.168.127.10
- **Laptop (Client)**: 192.168.127.12

The server runs on the RDK-X5 board, and the client runs on the laptop.  
They communicate via TCP sockets over the local network.

---

## 📑 Data Format
We use **JSON** as the data exchange format.  
The server sends system information in the following structure:

```json
{
  "cpu_percent": 0.7,
  "memory": 10.5,
  "disk": 18.1,
  "platform": "Linux-6.1.83-aarch64-with-glibc2.35",
  "time": "Thu Oct  2 10:28:43 2025"
}

group members：SHEN Yuming 20945165

ZHANG Haochun 21147459
