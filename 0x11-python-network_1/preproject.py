#!/usr/bin/python3
import urllib.request


def fetch_and_print_response(url, response_file_path, content_file_path):
    # Step 1: Open the URL and get the response
    with urllib.request.urlopen(url) as response:
        # Step 2: Write the response object details to a file
        with open(response_file_path, 'w') as response_file:
            response_file.write(str(response))

        # Step 3: Read the content from the response
        content = response.read()

        # Step 4: Write the content to a separate file
        with open(content_file_path, 'wb') as content_file:
            content_file.write(content)

    # Step 5: Print information about the process
    print(f"Response object details are written to {response_file_path}")
    print(f"Content is written to {content_file_path}")


# Example usage
url_to_fetch = 'http://example.com/'
response_output_file = 'response.txt'
content_output_file = 'content.txt'

# Fetch data and print response object and content to files
fetch_and_print_response(
    url_to_fetch, response_output_file, content_output_file)
