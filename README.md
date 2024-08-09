# Port Scanner in Python

## Overview

This is a simple port scanner script written in Python. It scans a specified range of ports on a target IP address to determine which ports are open. It is useful for basic network exploration and security testing.

## Features

- Scans ports in the range 50-85 (configurable).
- Reports open and closed ports.
- Handles exceptions such as connection errors and invalid hostnames.

## Installation

No installation is required. The script uses Python's built-in modules. Ensure you have Python 3.x installed on your system.

## Usage

To use the port scanner, run the script from the command line with the target IP address as an argument:

```bash
python3 scanner.py <target_ip>
