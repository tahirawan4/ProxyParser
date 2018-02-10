from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe

from parser.models import ZipInfo


def index(request):
    return render_to_response('index.html', {'content': mark_safe(ZipInfo.objects.filter(zipcode='73442').first().response)})
