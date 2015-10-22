from django.shortcuts import render_to_response
from django.shortcuts import render
from Controller import Controller

controller = Controller()

def home(request):

    return render_to_response('core/index.html', {})

def local(request):

    text=controller.meushosts()
    print text
    context = {'texto': 'Hosts locais', 'hosts':text }
    return render(request, 'core/local.html', context)

def remoto(request):

    texto = controller.querohosts()

    context = {'texto': 'Hosts Remoto', 'hosts':texto }
    return render(request, 'core/remoto.html', context)
