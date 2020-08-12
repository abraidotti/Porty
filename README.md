# Porty

A port scanner

Supply an IP and get a list of open ports.

**Note: Get consent by default. Not everyone wants their machines' ports scanned.**

## Table of Contents

[Requirements](##Requirements)  
[Installation](##Installation)  
[Configuration](##Configuration)  
[Execution](##Execution)  
[Contribution](##Contribution)  

## Requirements

- Python 3

- Pip and the `scapy` library

- a target IP

## Installation

```bash
git clone https://github.com/abraidotti/Porty
cd Porty
```

## Configuration

None

## Execution

Make sure to specify an IPv4 with no CIDR block.

```bash
python3 porty.py --target 192.168.0.1
```

## Contribution

If you'd like to contribute, file a pull request or github issue to discuss.
