#!/usr/bin/python3
"""Script to send a POST request to a specified URL with an email address."""

import sys
from urllib.request import urlopen, Request
from urllib.parse import urlencode

def send_post_request(url, email):
    data = {
        "email": email
    }
    url_encoded_data = urlencode(data)
    utf_encoded_data = url_encoded_data.encode("utf-8")
    request_object = Request(url, utf_encoded_data)

    with urlopen(request_object) as response:
        body = response.read()
        encoded_body = body.decode("utf-8")
        return encoded_body

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    response_body = send_post_request(url, email)
    print(response_body)
