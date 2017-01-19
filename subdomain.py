import requests
import re

domain = raw_input("Domain name you want to review:")
page = requests.get(domain)

content = str(page.content)

# print "content: ", content # For Testing

subdomain = ""

for i in list(re.finditer('href=', content)):
    end = i.end()

    value = end
    while not content[value] == '"':
        value = value + 1
        subdomain = content[end:value]
    print subdomain  # for Testing
