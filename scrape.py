from bs4 import BeautifulSoup
import requests

HEADERS = ({'User-Agent':
              'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
              'Accept-Language': 'en-US'})

url = "https://play.google.com/store/search?q=dumb%20ways%20to%20die&c=apps"
website = requests.get (url, headers = HEADERS)
soup = BeautifulSoup(website.content, 'lxml')

links = soup.find_all('a', attrs={'class': "Si6A0c Gy4nib"})
links_list = []
rating_list = []

for link in links:
    links_list.append(link['href'])

for link in links_list:
    url_new = "https://play.google.com" + link
    website_new = requests.get (url_new, headers = HEADERS)
    soup_new = BeautifulSoup(website_new.content, "lxml")

    try:
        title = soup_new.find('span', attrs={'class': 'DdYX5'}).string.strip()
        rating = soup_new.find('div', attrs={'class':'TT9eCd'})
        out_rating = rating['aria-label']
        all_words = out_rating.split()
        rating = all_words[1]
        rating_list.append(rating)
       
    except:
        rating = ""

    print (title)

    
rating_list_int = [eval(i) for i in rating_list]
rating_list_int.sort()
the_biggest_raiting = rating_list_int[-1]
str1 = str(the_biggest_raiting)
print ("the biggest raiting is", the_biggest_raiting)
