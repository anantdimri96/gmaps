import urllib2
from bs4 import BeautifulSoup




page_num = 0
http_status_okay = True
while http_status_okay:
    page_num = page_num + 1
    time.sleep(2)#delay time requests are sent so we don't get kicked by server
    url2 = "https://www.propertypal.com/property-to-rent/newtownabbey/page-{0}".format(i)
    page2=requests.get(url2)

    # continue if we get a 200 response code
    if page2.status_code is 200:
        http_status_okay = True
    else:
        http_status_okay = False


url="https://www.dineout.co.in/bangalore-restaurants?search_str="
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

links =set()
rating= set()
locations=set()
name=set()
results = soup.find_all("div", {"class":"location"})
name_results=


for result in results:
    locations.add(result.text)


all_links=soup.find_all("a")
for link in all_links:
    links.add(link.get("href"))

# all_span=soup.find_all("a")
# for span in all_span:
#     rating.add(span.get("span"))

a=soup.span
