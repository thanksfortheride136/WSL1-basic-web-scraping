import requests

server_request = requests.get("http://www.google.com")  #variable that stores a GET request
status_code = server_request.status_code

if(status_code == 200):
    print("Website Contacted")
else:
    print("Website Not Contacted")