#!/usr/bin/env python3
"""
Network Monitor - A Python-based network monitoring and reconnaissance tool.

Provides utilities for network troubleshooting including ping, DNS lookup,
port scanning, and traceroute functionality.
"""

import sys
import argparse
from modules.ping import ping_host
from modules.dns_lookup import dns_lookup, reverse_dns
from modules.port_scanner import port_scan
from modules.traceroute import traceroute
from modules.utils import print_banner, print_error, print_success


def main():
    """
    Main entry point for the Network Monitor application.
    """
    parser = argparse.ArgumentParser(
        description='Network Monitor - Network troubleshooting and reconnaissance tool',
        epilog='Examples:\n'
               '  python network_monitor.py ping example.com\n'
               '  python network_monitor.py dns example.com\n'
               '  python network_monitor.py scan example.com -p 1-1000\n'
               '  python network_monitor.py traceroute example.com',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Ping subcommand
    ping_parser = subparsers.add_parser('ping', help='Test host reachability')
    ping_parser.add_argument('host', help='Host to ping')
    ping_parser.add_argument('-c', '--count', type=int, default=4, help='Number of packets (default: 4)')
    ping_parser.add_argument('-t', '--timeout', type=int, default=5, help='Timeout in seconds (default: 5)')

    # DNS subcommand
    dns_parser = subparsers.add_parser('dns', help='Perform DNS lookup')
    dns_parser.add_argument('host', help='Domain or IP address')
    dns_parser.add_argument('-r', '--reverse', action='store_true', help='Perform reverse DNS lookup')

    # Port Scanner subcommand
    scan_parser = subparsers.add_parser('scan', help='Scan ports on a host')
    scan_parser.add_argument('host', help='Host to scan')
    scan_parser.add_argument('-p', '--ports', default='1-1000', help='Port range to scan (default: 1-1000)')
    scan_parser.add_argument('-t', '--timeout', type=float, default=1.0, help='Connection timeout (default: 1.0s)')

    # Traceroute subcommand
    trace_parser = subparsers.add_parser('traceroute', help='Trace route to a host')
    trace_parser.add_argument('host', help='Host to trace route to')
    trace_parser.add_argument('-m', '--maxhops', type=int, default=30, help='Maximum hops (default: 30)')
    trace_parser.add_argument('-t', '--timeout', type=int, default=5, help='Timeout in seconds (default: 5)')

    args = parser.parse_args()

    print_banner()

    try:
        if args.command == 'ping':
            ping_host(args.host, args.count, args.timeout)
        elif args.command == 'dns':
            if args.reverse:
                reverse_dns(args.host)
            else:
                dns_lookup(args.host)
        elif args.command == 'scan':
            port_scan(args.host, args.ports, args.timeout)
        elif args.command == 'traceroute':
            traceroute(args.host, args.maxhops, args.timeout)
        else:
            parser.print_help()
    except KeyboardInterrupt:
        print_error('\nOperation cancelled by user')
        sys.exit(1)
    except Exception as e:
        print_error(f'Error: {str(e)}')
        sys.exit(1)


if __name__ == '__main__':
    main()
