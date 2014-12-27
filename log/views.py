from django.shortcuts import render
from log.models import Log

def index(request):
    button_list = Log.objects.all()
    context = {'button_list': button_list}
    return render(request, 'log/index.html', context)


