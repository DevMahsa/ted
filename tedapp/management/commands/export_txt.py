from django.core.management.base import BaseCommand

from tedapp.models import FarsiTed,Url



def export_txt():
    outF = open("output.txt", "w")
    for link in FarsiTed.objects.filter(link__isnull=False):
        outF.write(link.link)
        outF.write("\n")
    outF.close()
    farsiout=open('farsiout.txt','w')
    for farsi in Url.objects.filter(fasub__isnull=False):
        farsiout.write(farsi.fasub)
        farsiout.write("\n")
    farsiout.close()

class Command(BaseCommand):
    def handle(self, **options):
        export_txt()
