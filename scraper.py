import requests as r
from bs4 import BeautifulSoup



def get_url(interests):
    url = "https://paperswithcode.com/search?q_meta=&q_type=&q={}".format(interests.replace(" ", "+"))
    response = r.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    anchors = soup.find_all("a")
    nxt_url = "https://paperswithcode.com"
    hrefs = []
    for link in anchors:
        try:
            if "/paper/" in link["href"] and "#code" not in link["href"]:
                if nxt_url+link["href"] not in hrefs:
                    hrefs.append(nxt_url+link["href"])
        except:
            continue
    
    return hrefs


hrefs = get_url("magnetic field")    


def get_paras(hrefs):
    paras_of_paper = []
    for link in hrefs:
        print(link)
        r1 = r.get(link)
        soup = BeautifulSoup(r1.text, "html.parser")
        paras = soup.find_all("p")
        paragraph = [para.text for para in paras]
        paras_of_paper.append(paragraph[-1])
    return paras_of_paper


paras = get_paras(hrefs)


def get_paper_pdf_links(hrefs):
    dic = {}
    for i in hrefs:
        url = i
        dict_key = url.split("/")[-1]
        r2 = r.get(url)
        soup = BeautifulSoup(r2.text, "html.parser")
        anchors = soup.find_all("a")
        try:
            anchors = [link["href"] for link in anchors if "pdf" in link["href"]]
            dic[dict_key] = anchors
        except:
            continue
    return dic


pdfs = get_paper_pdf_links(hrefs)