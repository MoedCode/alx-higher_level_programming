#!/bin/bash
# This script sends a JSON POST request to a specified URL with the contents of a JSON file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
