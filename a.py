import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
import http
import ssl
from bs4 import BeautifulSoup
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
req = Request('https://www.naukri.com/autosar-jobs?k=autosar', headers={'User-Agent': 'Mozilla/5.0'})
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.naukri.com/autosar-jobs?k=autosar")
webpage = urlopen(req, timeout=10).read()
soup = BeautifulSoup(driver.page_source,'html.parser')
job_elems = soup.find_all("article",class_="jobTuple bgWhite br4 mb-8")
print(job_elems)
for ele in job_elems:
    pages = ele.find('a',{"class":"title fw500 ellipsis"})
    print(pages.text)
driver.close()
