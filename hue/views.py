from django.shortcuts import render
from beautifulhue.api import Bridge

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
        return render(request, 'homebaking/index.html', {'status': 'Unkown group action requested: ' + action_id})

    bridge.group.update(resource)
    return render(request, 'homebaking/index.html', {'status': 'Group action taken'})


