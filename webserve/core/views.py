from django.shortcuts import render_to_response
from django.shortcuts import render
#from . import Controller

#controller = Controller()

def home(request):
    return render_to_response('core/index.html', {})

def local(request):
    context = {'texto': 'Hosts locais', 'hosts':'10.0.0.1'}
    return render(request, 'core/local.html', context)

def remoto(request):
    context = {'texto': 'Hosts Remoto', 'hosts':'10.0.0.1'}
    return render(request, 'core/remoto.html', context)