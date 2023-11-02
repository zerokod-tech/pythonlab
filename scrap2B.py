import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('http://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

# links#links = soup.find_all('a')
links = soup.select('.titleline')
subtext = soup.select('.subtext')

links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')
# votes = soup.select('.score')

mega_links = links + links2
mega_subtext = subtext + subtext2


# print(soup.body.contents)
# print(soup.find_all('a'))
# print(soup.find('a'))
# print(soup.select('.titleline'))
# print(votes[0])


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
    if len(vote):
        points = int(vote[0].getText().replace(' points', ''))
        # print(points)
        # hn.append(href)
        hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
