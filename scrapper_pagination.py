from bs4 import BeautifulSoup
import urllib2



def parse():
    base_url = 'https://www.dineout.co.in/bangalore-restaurants'
    url = '"https://www.dineout.co.in/bangalore-restaurants?search_str="'

    while True:
        html=urllib2.urlopen(url)
        soup = BeautifulSoup(html, 'lxml')

        for article in soup.findAll('article', class_ = 'item'):
            try:
                print('\t' + article.find('h1').find('a').get_text())
                print(article.find('p').get_text() + '\n' + '*'*80)
            except AttributeError as e:
                print(e)

        next_button = soup.find('a', class_='next', href=True)

        if next_button:
            url = base_url + next_button['href']
        else:
            break

parse()
