import urllib.request
from bs4 import BeautifulSoup

def getTitlesFromAll(amount, rating='all'):
    output = ''
    for i in range(1, amount+1):
        try:
            if rating == 'all':
                html = urllib.request.urlopen('https://habr.com/ru/all/page'+ str(i) +'/').read()
            else:
                html = urllib.request.urlopen('https://habr.com/ru/all/'+ rating +'/page'+ str(i) +'/').read()
        except urllib.error.HTTPError:
            print('Error 404 Not Found')
            break
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.findAll('div', class_ = 'tm-articles-list')
        comps = []
        for item in items:
            comps.append({
                'title': item.find('a', class_ = 'tm-article-snippet__title-link').get_text(strip = True),
                'time': item.find('span', class_= 'tm-article-snippet__datetime-published').get_text(strip = True),
                'link': item.find('a', class_='tm-article-snippet__title-link').get('href'),
                'votes': item.find('span', class_='tm-votes-meter__value tm-votes-meter__value_positive tm-votes-meter__value_appearance-article tm-votes-meter__value_rating').get('title'),
                'views': item.find('span', class_='tm-icon-counter__value').get_text(strip = True)
                
            })
            
            for comp in comps:
                output += (comp['title'] + "\nОпубликовано: " + comp['time'] + "\nПросмотры: " + comp['views'] + "\n" + comp['votes'] + "\nhttps://habr.com" + comp['link'] + "\n" + "\n" + "\n")
    
    return output

def getTitlesFromTop(amount, age='daily'):
    output = ''
    for i in range(1, amount+1):
        try:
            html = urllib.request.urlopen('https://habr.com/ru/top/'+ age +'/page'+ str(i) +'/').read()
        except urllib.error.HTTPError:
            print('Error 404 Not Found')
            break
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.findAll('div', class_ = 'tm-articles-list')
        comps = []
        for item in items:
            comps.append({
                'title': item.find('a', class_ = 'tm-article-snippet__title-link').get_text(strip = True),
                'time': item.find('span', class_= 'tm-article-snippet__datetime-published').get_text(strip = True),
                'link': item.find('a', class_='tm-article-snippet__title-link').get('href'),
                'votes': item.find('span', class_='tm-votes-meter__value tm-votes-meter__value_positive tm-votes-meter__value_appearance-article tm-votes-meter__value_rating').get('title'),
                'views': item.find('span', class_='tm-icon-counter__value').get_text(strip = True)
                
            })
            
            for comp in comps:
                output += (comp['title'] + "\nОпубликовано: " + comp['time'] + "\nПросмотры: " + comp['views'] + "\n" + comp['votes'] + "\nhttps://habr.com" + comp['link'] + "\n" + "\n" + "\n")
            
    return output

    

