import socket
from concurrent.futures import ThreadPoolExecutor
import time

class PortScanner:
    def __init__(self, target, start_port, end_port, threads=100):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.threads = threads
        self.timeout = 0.5
        self.open_ports = []

    def _check_port(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((self.target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = 'Unknown service'
            self.open_ports.append((port, service))
        s.close()

    def run(self):
        try:
            start_time = time.time()
            print(f'Scanning for {self.target}...\nWaiting!')
            with ThreadPoolExecutor(self.threads) as executor:
                executor.map(self._check_port, range(self.start_port, self.end_port + 1))
            print(f'Scanning is finished! \nTotal time: {time.time() - start_time:.2f}')
        except KeyboardInterrupt:
            print('Scan Stopped')
            print(f'Total time: {time.time() - start_time:.2f}')
        except socket.error:
            print('Problems with Network')
            print(f'Total time: {time.time() - start_time:.2f}')

    def show_results(self):
        self.open_ports.sort()
        for port, service in self.open_ports:
            print(f'Port {port} is open ({service})')