from django.shortcuts import render, get_object_or_404
from beautifulhue.api import Bridge
from datetime import datetime
import json
from log.models import Log, Event

username = 'homebakingrgardler'
bridge = Bridge(device={'ip':'192.168.1.5'}, user={'name': username})

def takeAction(request, group_id, action_id):
    if action_id == 'on':
        resource = {
            'which':group_id,
            'data':{
                'action':{
                    'on':True,
                    'ct':166,
                    'bri':160
                    }
                }
            }
    elif action_id == 'off':
        resource = {
            'which':group_id,
            'data':{
                'action':{
                    'on':False,
                    }
                }
            }
    else:
        description = 'Unkown group action requested: ' + action_id
        log(description)
        return render(request, 'hue/actionFailed.html', {'status': description})

    bridge.group.update(resource)
    description = 'Group ' + group_id + ' turned ' + action_id
    log(description, resource)
    return render(request, 'hue/actionSucceeded.html', {'status': description})

def log(description, resource = {}):
    log = get_object_or_404(Log, event_type='Hue')
    event = Event(log = log, time = datetime.now(), data = description + ' using ' + json.dumps(resource))
    event.save()

