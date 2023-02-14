import requests

# Define the path of the text file containing API URLs
file_path = 'api_urls.txt'

# Define the path of the text file containing the access token
access_token_path = 'access_token.txt'

# Open the text file and read the URLs into a list
with open(file_path, 'r') as f:
    api_urls = f.read().splitlines()

# Check if the list of URLs is empty
if not api_urls:
    print('The api_urls.txt file is empty.')
else:
    # Check if the access token file exists and read the token
    try:
        with open(access_token_path, 'r') as f:
            access_token = f.read().strip()
    except FileNotFoundError:
        access_token = None
        print('The access_token.txt file is missing.')

    # Loop through each API URL and make a GET request
    for i, api_url in enumerate(api_urls):
        try:
            response = requests.get(api_url)
            # Check the response status code and print the status
            if response.status_code == 200:
                print(f'{i + 1}. {api_url} is up and running.')
            else:
                print(f'{i + 1}. {api_url} returned a status code of {response.status_code}.')
                if response.status_code == 100:
                    print(
                        'Continue - The server has received the request headers and that the client should proceed to send the request body.')
                elif response.status_code == 101:
                    print(
                        'Switching Protocols - The server is switching protocols and that the client should switch to the new protocol.')
                elif response.status_code == 102:
                    print(
                        'Processing - The server has received and is processing the request, but no response is available yet.')
                elif response.status_code == 200:
                    print('OK - The request was successful.')
                elif response.status_code == 201:
                    print('Created - The request was successful and that a new resource was created.')
                elif response.status_code == 202:
                    print(
                        'Accepted - The request was accepted for processing, but the processing has not been completed.')
                elif response.status_code == 203:
                    print('Non-Authoritative Information - The response returned is not authoritative.')
                elif response.status_code == 204:
                    print('No Content - The request was successful, but there is no representation to return.')
                elif response.status_code == 205:
                    print(
                        'Reset Content - The server is requesting the client to perform a reload of the current resource.')
                elif response.status_code == 206:
                    print(
                        'Partial Content - The server is delivering only part of the resource due to a range header sent by the client.')
                elif response.status_code == 300:
                    print(
                        'Multiple Choices - Multiple options for the resource from the server. The user-agent must select one of the options.')
                elif response.status_code == 301:
                    print('Moved Permanently - The resource requested has been permanently moved to a new location.')
                elif response.status_code == 302:
                    print('Found - The resource requested has been temporarily moved to a new location.')
                elif response.status_code == 303:
                    print(
                        'See Other - The response to the request can be found under a different URI and should be retrieved using GET.')
                elif response.status_code == 304:
                    print('Not Modified - The resource has not been modified since the last request.')
                elif response.status_code == 305:
                    print(
                        'Use Proxy - The requested resource must be accessed through the proxy given by the location field.')
                elif response.status_code == 306:
                    print('Switch Proxy - No longer used.')
                elif response.status_code == 307:
                    print('Temporary Redirect - The resource requested is temporarily moved to the provided location.')
                elif response.status_code == 308:
                    print('Permanent Redirect - The resource requested is permanently moved to the provided location.')
                elif response.status_code == 400:
                    print('Bad Request - The request cannot be fulfilled due to bad syntax.')
                elif response.status_code == 401:
                    print('Unauthorized - The client must authenticate itself to get the requested response.')
                elif response.status_code == 402:
                    print('Payment Required - This response code is reserved for future use.')
                elif response.status_code == 403:
                    print('Forbidden - The client does not have access rights to the content.')
                elif response.status_code == 404:
                    print('Not Found - The server can not find the requested resource.')
                elif response.status_code == 405:
                    print('Method Not Allowed - The method specified in the request is not allowed for the resource.')
                elif response.status_code == 406:
                    print('Not Acceptable - The server cannot produce a response matching the list of acceptable values defined in the request headers.')
                elif response.status_code == 407:
                    print('Proxy Authentication Required - The client must first authenticate itself with the proxy.')
                elif response.status_code == 408:
                    print('Request Timeout - The server timed out waiting for the request.')
                elif response.status_code == 409:
                    print('Conflict - The request could not be completed due to a conflict with the current state of the target resource.')
                elif response.status_code == 410:
                    print('Gone - The requested resource is no longer available at the server and no forwarding address is known.')
                elif response.status_code == 411:
                    print('Length Required - The server refuses to accept the request without a defined Content-Length.')
                elif response.status_code == 412:
                    print('Precondition Failed - One or more conditions in the request header fields evaluated to false.')
                elif response.status_code == 413:
                    print('Payload Too Large - The server is refusing to process a request because the request payload is too large.')
                elif response.status_code == 414:
                    print('URI Too Long - The server is refusing to service the request because the request-target is too long.')
                elif response.status_code == 415:
                    print('Unsupported Media Type - The server is refusing to service the request because the payload is in a format not supported by this method on the target resource.')
                elif response.status_code == 416:
                    print('Requested Range Not Satisfiable - The client has asked for a portion of the file, but the server cannot supply that portion.')
                elif response.status_code == 417:
                    print('Expectation Failed - The server cannot meet the requirements of the Expect request-header field.')
                elif response.status_code == 418:
                    print('I\'m a teapot - The server refuses to brew coffee because it is a teapot.')
                elif response.status_code == 421:
                    print('Misdirected Request - The request was directed at a server that is not able to produce a response.')
                elif response.status_code == 422:
                    print('Unprocessable Entity - The server understands the content type of the request entity, and the syntax of the request entity is correct, but it was unable to process the contained instructions.')
                elif response.status_code == 423:
                    print('Locked - The source or destination resource of a method is locked.')
                elif response.status_code == 424:
                    print('Failed Dependency - The method could not be performed on the resource because the requested action depended on another action and that action failed.')
                elif response.status_code == 426:
                    print('Upgrade Required - The client should switch to a different protocol such as TLS/1.0, given in the Upgrade header field.')
                elif response.status_code == 428:
                    print('Precondition Required - The origin server requires the request to be conditional.')
                elif response.status_code == 429:
                    print('Too Many Requests - The user has sent too many requests in a given amount of time.')
                elif response.status_code == 431:
                    print('Request Header Fields Too Large - The server is unwilling to process the request because its header fields are too large.')
                elif response.status_code == 451:
                    print('Unavailable For Legal Reasons - The server is denying access to the resource as a consequence of a legal demand.')
                elif response.status_code == 500:
                    print('Internal Server Error - The server encountered an unexpected condition that prevented it from fulfilling the request.')
                elif response.status_code == 501:
                    print('Not Implemented - The server does not support the functionality required to fulfill the request.')
                elif response.status_code == 502:
                    print('Bad Gateway - The server was acting as a gateway or proxy and received an invalid response from the upstream server.')
                elif response.status_code == 503:
                    print('Service Unavailable - The server is currently unable to handle the request due to a temporary overload or scheduled maintenance.')
                elif response.status_code == 504:
                    print('Gateway Timeout - The server was acting as a gateway or proxy and did not receive a timely response from the upstream server.')
                elif response.status_code == 505:
                    print('HTTP Version Not Supported - The server does not support the HTTP protocol version used in the request.')
                elif response.status_code == 506:
                    print('Variant Also Negotiates - Transparent content negotiation for the request results in a circular reference.')
                elif response.status_code == 507:
                    print('Insufficient Storage - The method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request.')
                elif response.status_code == 508:
                    print('Loop Detected - The server detected an infinite loop while processing the request.')
                elif response.status_code == 510:
                    print('Not Extended - The policy for accessing the resource has not been met in the request.')
                elif response.status_code == 511:
                    print('Network Authentication Required - The client needs to authenticate to gain network access.')
                elif response.status_code >= 512:
                    print(f'{response.status_code} - Unknown status code')
                elif response.status_code >= 400:
                    print('The request was unsuccessful. Check the status code description for more information on how to fix it.')
                else:
                    print('The request was unsuccessful.')
        except requests.exceptions.RequestException:
          print(f'{i + 1}. {api_url} is down.')
