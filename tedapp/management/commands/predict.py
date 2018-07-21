from django.core.management.base import BaseCommand

import http.client
import json
import objectpath
def predict():
    group_id = ['A','B','C','D','E','F','G','H']
    connection = http.client.HTTPConnection('worldcup.sfg.io')
    headers = { 'X-Auth-Token': 'e870239c8ead43bb839f0bd195353ed0', 'X-Response-Control': 'minified' }
    for id in group_id:
        connection.request('GET', '/teams/group_results?group_id='+id, None, headers )
        response = json.loads(connection.getresponse().read().decode())
        tree = objectpath.Tree(response)
        teams= list(tree.execute('$..team'))
        print (teams)


class Command(BaseCommand):
    def handle(self, **options):
        predict()