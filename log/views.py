from django.shortcuts import render, get_object_or_404
from datetime import datetime
from log.models import Log, Event


def index(request):
    button_list = Log.objects.all()
    context = {'button_list': button_list}
    return render(request, 'log/index.html', context)

def takeAction(request, action_id):
    log = get_object_or_404(Log, event_type=action_id)
    status_msg = "User performed the %s action." % action_id
    event = Event(log = log, time = datetime.now(), data = status_msg)
    event.save()

    button_list = Log.objects.all()
    return render(request, 'log/index.html', {'button_list': button_list, 'status': status_msg})


