#!/bin/bash
# Send an OPTIONS request to the specified URL and display the allowed methods
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
