#!/bin/bash
# script that sends a JSON POST
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
