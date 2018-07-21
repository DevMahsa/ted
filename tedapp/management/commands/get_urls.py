from django.core.management.base import BaseCommand

from tedapp.models import Url


def get_urls():
    import requests
    from bs4 import BeautifulSoup

    maxpagenum = 78
    try:

        for i in range(1, maxpagenum, 1):
            url = "https://www.ted.com/talks/quick-list?page=" + str(i)
            # url = "https://www.ted.com/talks/quick-list?page=78"
            response = requests.get(url)
            if response:
                soup = BeautifulSoup(response.content, 'html.parser')
                dllist = soup.findAll('ul', attrs={'class': 'quick-list__download'})
                titlelist = soup.findAll('span', attrs={'class': 'l3'})
                events = soup.findAll('div', attrs={'class': 'col-xs-2 event'})
                try:
                    for e in range(len(events)):
                        if len(dllist[e].contents) > 5:
                            event = \
                                str(soup.findAll('div', attrs={'class': 'col-xs-2 event'})[e + 1]).split('?q=')[
                                    1].split(
                                    '">')[0] or None
                            title = str(titlelist[e]).split('<a href="/talks/')[1].split('">')[0] or None
                            low = str(dllist[e].findAll('a')).split('Low')[0].split('<a href="')[1].split('">')[
                                      0] or None
                            medium = str(dllist[e].findAll('a')).split('Low</a>, <a href="')[1].split('">Medium')[
                                         0] or None
                            high = str(dllist[e].findAll('a')).split('Medium')[1].split('<a href="')[1].split('">')[
                                       0] or None
                            fasub = str(dllist[e].findAll('a')).split('Medium')[1].split('<a href="')[1].split('">')[
                                0].split('.mp4')[0].__add__('-fa.mp4?apikey=TEDDOWNLOAD')
                            engsub = str(dllist[e].findAll('a')).split('Medium')[1].split('<a href="')[1].split('">')[
                                0].split('.mp4')[0].__add__('-en.mp4?apikey=TEDDOWNLOAD')
                            if not Url.objects.filter(title=title).exists():
                                url = Url(title=title, event=event, low=low, medium=medium, high=high, fasub=fasub,
                                          engsub=engsub)
                                url.save()
                            else:
                                continue
                        else:
                            continue
                except IndexError:
                    pass

    except Exception as error:

        print(error)


class Command(BaseCommand):
    def handle(self, **options):
        get_urls()
