from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def pages(request):
    context = {}
    try:
        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))
    except:
        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))