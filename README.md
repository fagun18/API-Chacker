# API-Chacker
Introduction
APIs, or Application Programming Interfaces, are an essential part of modern software development. APIs allow different software applications to communicate with each other and exchange data. When developing an API, it's essential to test it thoroughly to ensure that it's working correctly and returning the expected results. This is where automated testing comes in.
In this article, we'll introduce a Python script that automates the process of testing APIs and checking the status code of each request. This script can be used to quickly and easily test your APIs and ensure that they are up and running smoothly.
Script Overview
The API testing script is a Python script that reads a list of API URLs from a text file, makes a GET request to each URL, and checks the status code of the response. If the API is up and running, the script will print a message saying so. If the API is down or returns an error, the script will print a message with the status code of the response and provide information on what the status code means and how to fix it.
The script is designed to be simple and easy to use, even for those who are new to Python or automated testing. In the following sections, we'll provide a step-by-step guide on how to use the script to test your APIs.
Requirements
To use the API testing script, you'll need the following:
Python 3.x
The requests library

You can install the requests library using pip:
pip install requests
Step 1: Create a Text File with API URLs
The first step in using the API testing script is to create a text file named api_urls.txt. This file should contain a list of API URLs that you want to test, with each URL on a new line.
For example, suppose you want to test the following APIs:
https://api.example.com/v1/users
https://api.example.com/v1/orders
https://api.example.com/v1/products

In that case, your api_urls.txt file should look like this:
https://api.example.com/v1/users
https://api.example.com/v1/orders
https://api.example.com/v1/products
Make sure that the api_urls.txt file is in the same directory as the API testing script.
Step 2: (Optional) Create a Text File with an Access Token
If the APIs you're testing require an access token to access, you'll need to create a text file named access_token.txt. This file should contain the access token that you want to use, with no extra characters or whitespace.
For example, suppose your access token is:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

In that case, your access_token.txt file should look like this:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF
Reading API URLs from a Text File
The first step in automating API testing is to read a list of API URLs from a text file. Here is an example of how to do that using Python:
with open('api_urls.txt') as file:
    api_urls = [line.strip() for line in file if line.strip()]
In this code snippet, we use the built-in open() function to open a file named api_urls.txt. We then use a list comprehension to iterate over each line in the file and strip off any leading or trailing whitespace. We also check if the line is not empty by using the if line.strip() condition. The resulting list of URLs is stored in the api_urls variable.
If the api_urls.txt file is empty, the code above will not produce any results. Therefore, it's a good practice to add a check to ensure that the list of API URLs is not empty. Here's how to do that:
if not api_urls:
    print('The file containing API URLs is empty. Please provide at least one URL.')
    exit()
This code snippet checks if the api_urls list is empty and prints an error message if it is. It then exits the program using the exit() function.
Checking HTTP Status Codes
Once we have the list of API URLs, the next step is to send HTTP requests to each URL and check the HTTP status code returned. Here is an example of how to do that using Python:
import requests

access_token = '<YOUR_ACCESS_TOKEN>' # Replace with your actual access token or use the file reading method shown earlier

for i, url in enumerate(api_urls):
    headers = {'Authorization': f'Bearer {access_token}'} if access_token else {}
    response = requests.get(url, headers=headers)
    status_code = response.status_code

    if status_code == 200:
        print(f'{i+1}. {url} is up and running.')
    elif status_code == 401:
        print(f'{i+1}. {url} is down. Access denied. Please check your access token.')
    elif status_code == 404:
        print(f'{i+1}. {url} is down. Resource not found.')
    else:
        print(f'{i+1}. {url} returned an unexpected status code: {status_code}')
In this code snippet, we first import the requests library, which is a simple HTTP library for Python. We then define an access_token variable, which contains the API access token. You can replace the string with your actual access token or use the file reading method.

© Mejbaur Bahar Fagun
🔀 𝐂𝐨𝐧𝐧𝐞𝐜𝐭 𝐖𝐢𝐭𝐡 𝐌𝐞
𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤: https://lnkd.in/dQhnGZTy
𝐅𝐚𝐜𝐞𝐛𝐨𝐨𝐤 𝐏𝐚𝐠𝐞: https://lnkd.in/gaSKMG2y
LinkedIn: Mejbaur Bahar Fagun | LinkedIn
𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦: https://lnkd.in/gid7Ehku
𝐌𝐞𝐝𝐢𝐮𝐦: https://lnkd.in/gP6V2iQz
𝐆𝐢𝐭𝐡𝐮𝐛: https://github.com/fagunti
𝐘𝐨𝐮𝐓𝐮𝐛𝐞: https://lnkd.in/gg9AY4BE
