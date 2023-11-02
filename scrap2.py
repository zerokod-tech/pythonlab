import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('http://news.ycombinator.com/news')
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.find_all('a')
links = soup.select('.titleline')
# votes = soup.select('.score')
subtext = soup.select('.subtext')
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


pprint.pprint(create_custom_hn(links, subtext))
