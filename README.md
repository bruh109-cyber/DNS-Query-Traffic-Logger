DNS-Query-Traffic-Logger

# DNS-Query-Traffic-Logger

A Python-based network monitoring tool designed to capture, parse, and log DNS queries and responses across local network interfaces.

---

## Features

- **Real-Time DNS Monitoring:** Captures outgoing and incoming DNS query traffic.
- **Detailed Parsing:** Extracts key packet metadata including source IP, requested hostname, and query types.
- **Structured Logging:** Appends captured network traffic details to local log files for subsequent analysis.

## Tech Stack

- **Language:** Python 3.x
- **Networking Modules:** Standard socket library / `scapy`

## Installation & Setup

1. **Clone the repository:**

   git clone [https://github.com/bruh109-cyber/DNS-Query-Traffic-Logger.git](https://github.com/bruh109-cyber/DNS-Query-Traffic-Logger.git)
   cd DNS-Query-Traffic-Logger

Install dependencies:
  pip install scapy
Usage:
  sudo python Passive DNS Query Traffic Logger.py
Project Structure:
   ├── Passive DNS Query Traffic Logger.py        # Core packet capture and logging engine
   └── README.md        # Documentation
