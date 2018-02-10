import csv
from django.core.management.base import BaseCommand
import os

from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

from ProxyParser.settings import PROJECT_ROOT
from parser.models import ZipInfo

FIELD_NAME = 'ctl00$zs$txtZip'
API_ENDPOINT = 'https://broadbandnow.com'


class Command(BaseCommand):
    help = "Parser"

    def make_request(self, zip_code, req_proxy):
        data = {FIELD_NAME: zip_code}
        request = req_proxy.generate_proxied_request(API_ENDPOINT, method='POST', data=data)
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
                print('Parse Zip: %s' % row[0])
                if not self.make_request(row[0], req_proxy):
                    repeat_request_zip.append(row[0])

        for zip_code in repeat_request_zip:
            print('Parse Zip: %s' % zip_code)
            self.make_request(zip_code, req_proxy)
