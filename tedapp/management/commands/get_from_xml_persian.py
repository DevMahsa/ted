
from django.core.management.base import BaseCommand

from tedapp.models import FarsiTed


def get_xml():
    xml_path = '/Users/mahsagolchian/Desktop/TED-talks-grouped-by-event-in-high-quality.fa.metalink'

    try:
        from xml.dom import minidom
        xmldoc = minidom.parse(xml_path)
        itemlist = xmldoc.getElementsByTagName('url')
        # print(len(itemlist))
        #str(xmldoc.getElementsByTagName('url')[node].toxml()).split('<url type="http">')[1].split('</url>')[0]

        for node in range(1,len(itemlist)):

            try:
                link = \
                str(xmldoc.getElementsByTagName('url')[node].toxml()).split('<url type="http">')[1].split('</url>')[0]

                if not link:
                    continue
            except IndexError:
                pass

            if not FarsiTed.objects.filter(link=link).exists():
                   farsi = FarsiTed(link=link)
                   farsi.save()





    except Exception as error:

        print(error)


class Command(BaseCommand):
    def handle(self, **options):
        get_xml()
