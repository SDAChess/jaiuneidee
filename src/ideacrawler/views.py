from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('ideacrawler/crawler.html')
    context = {}
    return HttpResponse(template.render(context, request))


def idea(request, idea_id):
    #template = loader.get_template('ideacrawler/index.html')
    #context = {}
    #return HttpResponse(template.render(context, request))
    pass


def submit(request):
    template = loader.get_template('ideacrawler/submit.html')
    context = {}
    return HttpResponse(template.render(context, request))
