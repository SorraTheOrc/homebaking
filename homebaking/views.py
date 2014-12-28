from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from beautifulhue.api import Bridge

hue_username = 'homebakingrgardler'
hue_bridge = Bridge(device={'ip':'192.168.1.5'}, user={'name':hue_username})


def index(request):
    response = hue_getSystemData()

    if 'lights' in response:
        msg = 'Connected to the Hub'
        return render(request, 'homebaking/index.html', {'status': msg})
    elif 'error' in response[0]:
        error = response[0]['error']
        if error['type'] == 1:
            return render(request, 'homebaking/hue_connect.html')
        else:
            print 'Unhandled exception when connecting to bridge'
            print error

def connect(request):
    hue_create_config();
    return HttpResponseRedirect('/')

def hue_create_config():
    created = False
    while not created:
        resource = {'user':{'devicetype': 'beautifulhuetest', 'name': hue_username}}
        response = hue_bridge.config.create(resource)['resource']
        if 'error' in response[0]:
            if response[0]['error']['type'] != 101:
                print 'Unhandled error creating configuration on the Hue'
                print response[0]
        else:
            created = True

def hue_getSystemData():
  resource = {'which':'system'}
  return hue_bridge.config.get(resource)['resource']



  
