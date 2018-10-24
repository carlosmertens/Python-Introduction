""" Wikipedia Web Crawl Case Study

>> Program that will allow us to iterate through the first link on Wikipedia

Requests Library:
allows us to get the source code from a web page

"Beautiful Soup Library:
parses anything you give it, and does the tree traversal stuff for you.
You can tell it 'Find all the links', or 'Find all the links of classexternalLink',
or 'Find all the links whose urls match "foo.com", or 'Find the table heading that's got bold text,
then give me that text.'"

NOTE: Work with the documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""
import requests
from bs4 import BeautifulSoup

# Get the source code from a web page
response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')

# Copy the source code in text to variable html
html = response.text

soup = BeautifulSoup(html, 'html.parser')

print(soup.title)

print(soup.title.name)

print(soup.title.string)
