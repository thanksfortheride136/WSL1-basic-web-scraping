import requests
from bs4 import BeautifulSoup
import codecs
import re

eastchester_scrape = requests.get("https://www.eufsdk12.org/domain/76") # Send a GET request to the website
soup = BeautifulSoup(eastchester_scrape.text, "html.parser") # Parse the HTML content
email_elements = soup.findAll("li", class_="staffemail") # Find all 'li' elements with the class 'staffemail'
decoded_emails = [] # This will hold the decoded email addresses

# Loop through each element
for element in email_elements:
    script = element.find('script').string if element.find('script') else None # Extract the script tag content
    # If the script tag is found
    if script:
        matches = re.findall(r"swrot13\('([^']+)'\)", script) # Use regular expression to find the encoded email within the script tag
        # If a match is found, decode it with ROT13
        if matches:
            encoded_email = matches[0]
            decoded_email = codecs.decode(encoded_email, 'rot_13')
            decoded_emails.append(decoded_email) # Add the decoded email to the list

for email in decoded_emails: # Print out all the decoded emails
    print(email)