# Financial-Portal-Crawler

Author: Taylor Peterson

Purpose: Detecting and exporting info from BYUI financial portal. A re-skin of my BYUI-web-crawler

## Prerequisites

In order to run this software, you will need to have python 10 or greater installed. Using python's installer pip, you will need to install beautiful soup by using the command: pip install beautifulsoup4. You will also need to most likely install request by using the command: pip install requests

Depending on your Operating System (Windows, Linux, Apple), you will need to run this with python in your terminal. It would look something like this: python helpguide_crawler.py inside powershell, commandprompt or the terminal of apple/linux machine. If you have Visual Studio Code editor (or another similar code editor) you can click the play button instead.

## Usage
Run the python file WEBcrawler.py to run all python files together. No arguments are needed/can be used.

## QA's:
Q: Why is this software slightly slow?   A: Initially I really wanted to thread this, but when I threaded these it most likely appeared the the TD domain as a DDOS type attack. In order to look over these html files and get the appropriate information it needs to run at a normal speed without threading.

Q: The site changes drastically, would this still be useful?   A: If the sites change pretty dramatically, there will need to be re-write of a lot of the code, especially in terms of how it would find it's next page
in the site. Hopefully my comments can help 

Q: Why does it give me the error: "File "c:[path to]\helpguide_crawler.py", line 1, in <module>
import requests"    A:   This is because you need to install beautifulsoup4 and request, refer to my prerequisits section above.

Q: What would be the purpose of something like this?   A: My manager wanted the information scraped from these websites to make it easy for an AI to train on. While working on it we realized this has a few different applications such as seeing http protocols, odd locations or re-directs, etc.
