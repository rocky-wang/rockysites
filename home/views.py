from django.shortcuts import render
import logging


# Create your views here.
def home_index(request):
    logging.debug('GET type is %s' % type(request.GET))
    return render(request, 'home/base.html')
