# Example of getting information stored in github

import http.client
import json

# -- API information
HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = input('Enter a username: ')
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
user = json.loads(text_json)

# -- Get some data

name = user['name']

print()
print("Name: {}".format(name))

conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT + GITHUB_ID + '/repos', None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
repositories = json.loads(text_json)

# -- Get some data

for i in repositories:
    print('The name of one repository is: ', i['name'])

conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, "/repos/" + GITHUB_ID + '/2018-2019-PNE-practices/contributors', None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()


# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
commits = json.loads(text_json)

# -- Get some data

commits = commits[0]['contributions']

print('The number of commits in 2018-2019-PNE-practices is: ', commits )






