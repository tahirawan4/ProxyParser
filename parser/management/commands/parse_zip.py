import csv
from django.core.management.base import BaseCommand
import os

from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

from ProxyParser.settings import PROJECT_ROOT
from parser.models import ZipInfo

API_ENDPOINT = 'https://broadbandnow.com/%s/%s?zip=%s'


class Command(BaseCommand):
    help = "Parser"

    def make_request(self, state, city, zip_code, req_proxy):
        url = API_ENDPOINT % (state, city, zip_code)
        request = req_proxy.generate_proxied_request(url)
        if request:
            ZipInfo.objects.create(zipcode=zip_code, response=request.text)
            return True
        else:
            return False

    def handle(self, *args, **options):
        print('Start Parsing')
        req_proxy = RequestProxy()
        file_ = open(os.path.join(PROJECT_ROOT, 'zipcodes.csv'))
        repeat_request_zip = []
        with file_ as csvfile:
            zip_reader = csv.reader(csvfile, delimiter=',')
            for row in zip_reader:
                zip_code = row[0]
                city = row[1]
                state = row[2]
                print('Parse Zip: %s' % zip_code)
                if not self.make_request(state, city, zip_code, req_proxy):
                    repeat_request_zip.append(row)

        for zip_code_info in repeat_request_zip:
            zip_code = zip_code_info[0]
            city = zip_code_info[1]
            state = zip_code_info[2]
            print('Parse Zip: %s' % zip_code)
            self.make_request(state, city, zip_code, req_proxy)
