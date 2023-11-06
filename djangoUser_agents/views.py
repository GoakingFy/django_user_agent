from django.shortcuts import render
from django_user_agents.utils import get_user_agent
from django.http import HttpResponse

def indexed(req):
    return render(req,"djangoUser_agents/index.html")


def info_agent(req):
    user_agent = get_user_agent(req)
    return render(req,"djangoUser_agents/info.html" , {"info":user_agent})


def get_agent(req):
    user_agent = get_user_agent(req)
    client_ip = req.META.get('REMOTE_ADDR')
    host_name = req.META.get('HTTP_HOST')
    if user_agent.is_mobile:
        info_txt = "Estas usando un telefono movil"
        if user_agent.is_touch_capable:
            info_txt += " Ademas el dispositivo es tactil"
        else:
            info_txt += " El dispositivo no es tactil"

    elif user_agent.is_pc:
        info_txt = f'Estas usando un PC con host {host_name} y ip {client_ip}'
        if user_agent.is_touch_capable:
            info_txt += " Ademas el dispositivo es tactil"
        else:
            info_txt += " ademas el dispositivo no es tactil"
        
    elif user_agent.is_tablet:
        info_txt = f'Estas usando una Tablet con host {host_name} y ip {client_ip}'
        if user_agent.is_touch_capable:
            info_txt += " Ademas el dispositivo es tactil"
        else:
            info_txt += " ademas el dispositivo no es tactil"
       
        
    elif user_agent.is_bot:
        info_txt = f'Estas usando un Bot con host {host_name} y ip {client_ip}'
        if user_agent.is_touch_capable:
            info_txt += " Ademas el dispositivo es tactil"
        else:
            info_txt += " ademas el dispositivo no es tactil"

    return render(req, "djangoUser_agents/info_dispositivo.html" , {"info_txt": info_txt})

