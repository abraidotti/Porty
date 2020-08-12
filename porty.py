#!/usr/bin/python

import argparse
import ipaddress
import socket
from datetime import datetime


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", required=True,
                        help="specify target IPv4 address")
    options = parser.parse_args()

    if not options.target:
        parser.error(
            "Please specify a target IP. Use --help for more information.")

    try:
        if ipaddress.ip_address(options.target):
            return options
    except ValueError:
        parser.error(
            "Please specify a valid IPv4 address. Use --help for more information.")


options = get_arguments()
target_IP = options.target

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def scanner(port):
    try:
        sock.connect((target_IP, port))
        return True
    except:
        return False


def scan():
    ports = []

    for portNumber in range(1, 1000):
        if scanner(portNumber):
            port = {
                "port": portNumber,
                "open": True
            }
            ports.append(dict(port))

    return ports


start = datetime.now()
ports = scan()
end = datetime.now()
total = {"scan_time": (end-start).total_seconds()}
result = {
            "ports" : ports,
            "total": total
        }

print("Result: ", result)
