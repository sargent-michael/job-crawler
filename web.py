#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen
from colorama import Fore


def get_description(url):
    try:
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        article = soup.find("article", "cms-content").get_text()
        print(article)
    except:
        print(Fore.RED + f"Cannot access: {url}\n" + Fore.RESET)
    
def main():
    url = "https://jobs.paloaltonetworks.com/en/jobs/?search=network+security+researcher&country=United+States&pagesize=20#results"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    for links in soup.find_all('a', {"class":"stretched-link"}):
        print("-"*50)
        job_link = 'https://jobs.paloaltonetworks.com' + links['href']
        print("Job Title: {} \nLink: {} ".format(links.get_text(), job_link))
        print("-"*50)
        get_description(job_link)

if __name__ == "__main__":
    main()