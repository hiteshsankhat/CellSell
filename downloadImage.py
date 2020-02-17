from bs4 import BeautifulSoup as soup
import requests
import shutil


def get_source(link):
    r = requests.get(link)
    if r.status_code == 200:
        return soup(r.text)


def saveImageFile(path, link):
    r = requests.get(link, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        f = open(path, "wb")
        shutil.copyfileobj(r.raw, f)
        f.close()


def getImageTagBrand(html):
    return html.findAll('div', attrs={'class': 'image'})


def getImagesBrand(tags, link):
    for i in tags:
        src = list(list(i.children)[1].children)[0].get('src')
        saveImageFile(src, link+src)
        print(link+src)


def modelImageTag(html):
    return html.findAll('div', attrs={'class': 'brand_box2'})


def getModelImage(tags):
    for i in tags:
        link = list(i.children)[1].get('src')
        fileName = link.split('/')[-1]
        saveImageFile(fileName, link)
        print(fileName)


# link = 'http://quickmobile.co.in/'
# html = get_source(link)
# imageTags = getImageTagBrand(html)
# getImagesBrand(imageTags, link)


oneplusImageLink = 'https://cashsecond.com/sell-Oneplus'
html = get_source(oneplusImageLink)
tags = modelImageTag(html)
getModelImage(tags)

oneplusImageLink = 'https://cashsecond.com/sell-Apple'
html = get_source(oneplusImageLink)
tags = modelImageTag(html)
getModelImage(tags)

