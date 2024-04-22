#!/usr/bin/python3

"""
Log Parsing

Write a script that reads stdin line by
line and computes metrics:

Input format: <IP Address> -
[<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
(if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous
<file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer,
don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order

"""

from sys import stdin
from collections import Counter
from time import sleep
from signal import signal, SIGINT


def print_stats(stats):
    print("File size: {}".format(stats['total_size']))
    for k, v in sorted(stats['status_codes'].items()):
        if v:
            print("{}: {}".format(k, v))


def parse_line(line):
    """Parse a log line and return a tuple
    containing the IP address, date, status code,
    and file size"""
    try:
        ip_address, date, request, status_code, file_size = line.split()
    except ValueError:
        return None

    try:
        status_code = int(status_code)
    except ValueError:
        return None

    try:
        file_size = int(file_size)
    except ValueError:
        return None

    return ip_address, date, status_code, file_size


def main():
    stats = {
        'total_size': 0,
        'status_codes': {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
        }
    }

    signal(SIGINT, lambda s, f: print_stats(stats))

    for line in stdin:
        parsed_line = parse_line(line)

        if not parsed_line:
            continue
        ip_address, date, status_code, file_size = parsed_line

        stats['total_size'] += file_size
        stats['status_codes'][status_code] += file_size
        if stats['total_size'] % 10 == 0:
            print_stats(stats)
            sleep(1)

            for k in stats['status_codes']:
                stats['status_codes'][k] = 0

                stats['total_size'] = 0

                print_stats(stats)
                sleep(1)


if __name__ == "__main__":
    main()
