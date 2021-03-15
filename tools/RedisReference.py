import requests
from bs4 import BeautifulSoup


def getCatalogue(url):
    res = requests.get(url, stream=True)
    html = BeautifulSoup(res.content, "lxml")
    uls = html.find_all("ul")
    # print(uls[2:21])
    print(len(html.find_all("ul")))

    # print(uls[2])
    catalogue = parseToCatalogue(uls[2])


def parseToCatalogue(html):
    html = BeautifulSoup(html, "lxml")
    for ul in html.find_all("ul"):
        for li in ul.find_all("li"):
            print(li.text)
    return ""


if __name__ == "__main__":
    url = "http://redisdoc.com/index.html"
    getCatalogue(url)