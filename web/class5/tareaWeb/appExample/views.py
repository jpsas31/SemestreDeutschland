from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    tabdata=['1','2','3','4']
    tabdata2=['31','52','37','476']
    context = {"list1":tabdata, 'list2':tabdata2}
    # template = loader.get_template("appExample/templates/index.html")
    # return HttpResponse(template.render())
    return render(request, 'appExample/templates/index.html', context)

