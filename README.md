# Omnimam

## Description

Omnimam is a Python script designed to test multiple credentials against different services, such as SSH, FTP, HTTP, and HTTPS. It allows you to test a list of passwords against a specified service to determine if any of them are valid.

## Features

- SSH credential testing
- FTP credential testing
- HTTP credential testing
- HTTPS credential testing

## Requirements

- Python 3.x
- Paramiko library for SSH (`pip install paramiko`)
- Requests library for HTTP and HTTPS (`pip install requests`)

## Usage

python3 omniman.py -u <username> -p <password_list> -d <target_dns> -s <service_type> -e <error_message> -sm <success_message>

Arguments:

    -u, --user: Username for authentication
    -p, --password: File containing a list of passwords
    -d, --dns: IP/Domain of the target
    -s, --service: Type of service to test (ssh, ftp, http, https)
    -e, --error: Error message on login failure (for HTTP and HTTPS)
    -sm, --success: Success message on login success (for HTTP and HTTPS)


Examples

SSH:

python3 omniman.py -u user -p passwords.txt -d target_ip -s ssh

FTP:

python3 omniman.py -u user -p passwords.txt -d target_ip -s ftp

HTTP:

python3 omniman.py -u user -p passwords.txt -d http://target_url/login.php -s http -e "error message" -sm "success message"

HTTPS:

python3 omniman.py -u user -p passwords.txt -d https://target_url/login.php -s https -e "error message" -sm "success message"

Disclaimer

This script is intended for educational purposes only. Misuse of this script can lead to legal consequences. Use responsibly and only on systems you own or have explicit permission to test.
