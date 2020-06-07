from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord


def index(request):
    webpage_list = AccessRecord.objects.all() #.order_by('date')
    # print (webpage_list)
    date_dict = {'access_records': webpage_list}
    return render(request, 'first_app/index.html', context=date_dict)


def newextension(request):
    return HttpResponse('<em> my new extension</em>')


def secondextension(request):
    return HttpResponse('<em> my 2nd extension</em>')
# Create your views here.
