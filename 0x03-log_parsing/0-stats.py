#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics:"""
import sys
import re


format = r'^(\d{1,3}\.){3}\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.'
format += r'\d+\] \"GET /projects/260 HTTP/1.1\" \d{3} \d{1,4}$'
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

i = 0
metrics = ""
TotalFileSize = 0
try:
    for line in sys.stdin:
        i += 1
        # checks if each line match input
        match = re.match(format, line)
        if match:
            line_split = re.split(r'\s+', line)
            status = int(line_split[-3])
            fileSize = int(line_split[-2])
            TotalFileSize += fileSize
            if status in status_codes:
                status_codes[status] += 1
        if (i == 10):
            i = 0
            status_metrics = [f"{k}: {v}" for k, v in status_codes.items()
                              if v > 0]
            status_metrics = '\n'.join(status_metrics)
            metrics = f"File size: {TotalFileSize}\n{status_metrics}"
            print(metrics)
except KeyboardInterrupt:
    print(metrics)
