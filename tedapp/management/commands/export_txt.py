from django.core.management.base import BaseCommand

from tedapp.models import FarsiTed



def export_txt():
    outF = open("output.txt", "w")
    for link in FarsiTed.objects.filter(link__isnull=False):
        lines = []
        outF.write(link.link)
        outF.write("\n")
    outF.close()


class Command(BaseCommand):
    def handle(self, **options):
        export_txt()
