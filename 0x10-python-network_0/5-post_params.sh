#!/bin/bash
# script to post to the entered url
CURL -sX POST "email=test@gmail.com&subject=I will always be here for PLD" "$1"
