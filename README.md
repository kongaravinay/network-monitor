# Network Monitor

A Python-based network monitoring and reconnaissance tool that provides essential network utilities in a single command-line application.

## Features

- **Ping**: Test host reachability with configurable timeout and packet count
- **DNS Lookup**: Resolve domain names to IP addresses and perform reverse lookups
- **Port Scanner**: Scan for open ports on target hosts with adjustable timeout
- **Traceroute**: Trace the network path to a destination host
- **Colored Output**: Clean and intuitive CLI interface with colored text formatting
- **Error Handling**: Comprehensive error handling and validation
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/kongaravinay/network-monitor.git
cd network-monitor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Commands

```bash
# Display help
python network_monitor.py --help

# Ping a host
python network_monitor.py ping example.com

# DNS lookup
python network_monitor.py dns example.com

# Scan ports on a host
python network_monitor.py scan example.com -p 1-1000

# Traceroute to a destination
python network_monitor.py traceroute example.com
```

## Project Structure

```
network-monitor/
├── network_monitor.py          # Main application entry point
├── modules/
│   ├── __init__.py
│   ├── ping.py                 # Ping functionality
│   ├── dns.py                  # DNS lookup functionality
│   ├── scanner.py              # Port scanner functionality
│   ├── traceroute.py           # Traceroute functionality
│   └── utils.py                # Utility functions
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── LICENSE                     # License information
```

## Requirements

- colorama: For colored terminal output
- click: For command-line interface

## Use Cases

- Network troubleshooting and diagnostics
- Network reconnaissance for security assessments
- Educational tool for learning networking concepts
- System administration tasks

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

MIT License - See LICENSE file for details

## Author

Kongaravinay

## Disclaimer

This tool is provided for educational and authorized network analysis purposes only. Unauthorized access to computer networks is illegal.
