#  Fast Multi-threaded Port Scanner

A powerful and fast network reconnaissance tool written in Python using Object-Oriented Programming (OOP) and multi-threading.

##  Features
- **High Speed**: Utilizes `ThreadPoolExecutor` for concurrent scanning (250+ threads).
- **Banner Grabbing**: Attempts to retrieve service versions and banners.
- **Service Detection**: Automatically identifies common services via `socket`.
- **User-Friendly CLI**: Features a clean ASCII-art interface and flexible scanning modes.
- **Robust Logic**: Handles domain names, IP addresses, and provides error handling for network interruptions.

##  Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/nazar-TAR/PortScanner.git](https://github.com/nazar-TAR/PortScanner.git)
2. Navigate to the project folder:
   ```bash 
   cd PortScanner

## Usage

1. Run the main script:
   ```bash 
   python main.py
### Scanning Modes:
* Default: Scans standard ports (1-1024).
* Full: Comprehensive scan of all 65,535 ports.
* Custom: Specify your own range.

## Technical Details
* Language: Python 3.x
* Concurrency: Threading (I/O bound optimization)
* Architecture: Modular OOP design

_"Every open port is a story waiting to be told ;)"_