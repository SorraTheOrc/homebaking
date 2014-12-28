from django.shortcuts import render
from beautifulhue.api import Bridge

username = 'homebakingrgardler'
bridge = Bridge(device={'ip':'192.168.1.5'}, user={'name': username})

def takeAction(request, group_id, action_id):
    resource = {
        'which':0,
        'data':{
            'action':{
                'on':True,
                'ct':166,
                'bri':170
                }
            }
        }
    bridge.group.update(resource)
    return render(request, 'homebaking/index.html', {'status': 'Group action taken'})


