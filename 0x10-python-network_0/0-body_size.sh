#!/bin/bash
# This script takes in a URL, sends a request, and displays the size of the body of the response

# Sending a GET request to the specified URL, using curl in silent mode (-s) and writing the output to a temporary file (-o)
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
