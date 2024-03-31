#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one,
the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print
anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""

import sys
import signal
import traceback
from typing import Dict, List


if __name__ == "__main__":
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    total_size = 0
    count = 0

    def print_stats() -> None:
        """Prints the stats of the logs read so far."""
        print("File size: {:d}".format(total_size))
        for key in sorted(status_codes.keys()):
            if status_codes[key]:
                print("{:s}: {:d}".format(key, status_codes[key]))

    def signal_handler(sig, frame) -> None:
        """Handles the SIGINT signal."""
        print_stats()

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            count += 1
            data = line.split(" ")
            if len(data) < 7:
                continue
            status = data[-2]
            size = data[-1]
            if status in status_codes:
                status_codes[status] += 1
            total_size += int(size)
            if count == 10:
                print_stats()
                count = 0
    except KeyboardInterrupt:
        print_stats()
        traceback.print_exc()
        sys.exit(0)
    print_stats()
