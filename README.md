# API-Chacker
Automated testing is an important part of software development. It allows developers to quickly and efficiently check the functionality of their applications. In this article, we'll show you how to create a Python script to automate testing of API endpoints.

API Endpoint Testing

API endpoint testing is a process that verifies that an API endpoint returns the expected response for a given request. The expected response can be based on the input parameters, the HTTP status code, or the response data. To test an API endpoint, we send a request to it with a specific set of input parameters and check the response it returns.

Python for API Endpoint Testing

Python is a great language for API endpoint testing. It has a wide range of libraries that can be used to send HTTP requests and parse the responses. Some popular Python libraries for sending HTTP requests are requests, httplib2, and urllib3. These libraries provide a simple and intuitive way to send HTTP requests.

Creating the Python Script

To create the Python script, we'll be using the requests library. It is a popular library for sending HTTP requests in Python. Here are the steps to follow:

Step 1: Install the Requests Library

To install the requests library, run the following command in your terminal:

Copy code
pip install requests
Step 2: Define the API Endpoint URLs

Create a file named api_urls.txt in the same directory as the Python script. In this file, list all the API endpoint URLs that you want to test, with each URL on a new line.

ruby
Copy code
https://example.com/api/endpoint1
https://example.com/api/endpoint2
https://example.com/api/endpoint3
Step 3: Define the Access Token

If your API requires an access token, create a file named access_token.txt in the same directory as the Python script. In this file, enter your access token.

Copy code
ABC123DEF456GHI789
Step 4: Write the Python Script

Create a new Python file and name it api_test.py. Copy and paste the following code into the file:

python
Copy code
import requests

# Open the API URLs file and read the URLs
with open('api_urls.txt', 'r') as file:
    api_urls = [line.strip() for line in file if line.strip()]

# If the file is empty, print an error message and exit
if not api_urls:
    print('Error: API URLs file is empty.')
    exit()

# Open the access token file and read the token
try:
    with open('access_token.txt', 'r') as file:
        access_token = file.read().strip()
except FileNotFoundError:
    access_token = None

# Loop through the API URLs
for index, url in enumerate(api_urls, start=1):
    headers = {}
    if access_token:
        headers['Authorization'] = f'Bearer {access_token}'

    # Send the HTTP request and get the response
    response = requests.get(url, headers=headers)

    # Check the HTTP status code
    if response.status_code == 200:
        print(f'{index}. {url}: OK')
    elif response.status_code == 400:
        print(f'{index}. {url}: Bad Request - The server could not understand the request.')
    elif response.status_code == 401:
        print(f'{index}. {url}: Unauthorized - The request requires user authentication.')
    elif response.status_code == 403:
        print(f'{index}. {url}: Forbidden - The server understood the request, but is refusing to fulfill it.')
    elif response.status_code == 404:
        print(f'{index}. {

© Mejbaur Bahar Fagun
🔀 𝐂𝐨𝐧𝐧𝐞𝐜𝐭 𝐖𝐢𝐭𝐡 𝐌𝐞
𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤: https://lnkd.in/dQhnGZTy
𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤 𝐏𝐚𝐠𝐞: https://lnkd.in/gaSKMG2y
LinkedIn: Mejbaur Bahar Fagun | LinkedIn
𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦: https://lnkd.in/gid7Ehku
𝐌𝐞𝐝𝐢𝐮𝐦: https://lnkd.in/gP6V2iQz
𝐆𝐢𝐭𝐡𝐮𝐛: https://github.com/fagunti
𝐘𝐨𝐮𝐓𝐮𝐛𝐞: https://lnkd.in/gg9AY4BE
