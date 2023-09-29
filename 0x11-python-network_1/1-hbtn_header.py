#!/usr/bin/python3
"""Script to retrieve a specific header from a URL."""

import sys
from urllib.request import urlopen


def main():
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    with urlopen(url) as response:
        header_value = response.getheader("X-Request-Id")

    print(header_value or "X-Request-Id header not found in the response.")


if __name__ == "__main__":
    main()
