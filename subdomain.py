import requests
import re

#Usage for domains: https://example.com

domain = raw_input("Domain name you want to review:")
page = requests.get(domain)

content = str(page.content)

# If you want to print content of domain for testing, you can delete the # symbol in the line below.
#print "content: ", content

subdomain = ""

for i in list(re.finditer('href=', content)):
    obj = i.obj()
    value = obj
    while not content[value] == '"':
        value = value + 1
        subdomain = content[obj:value]
        
#print subdomain and check the results.
    print subdomain
