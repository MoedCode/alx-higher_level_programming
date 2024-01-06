#!/bin/bash
# 5-post_params.sh

# Take the URL as a command-line argument
url=$1

# Use curl to send a POST request with specified parameters
curl -sX POST "$url" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"

# Print the POST parameters for clarity
echo -e "\nPOST params:"
echo -e "    email: test@gmail.com"
echo -e "    subject: I will always be here for PLD"
