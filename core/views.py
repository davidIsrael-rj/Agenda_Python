from django.shortcuts import render, redirect
from core.models import Evento
# Create your views here.

#def index(request):
 #   return redirect('/agenda/')
def lista_eventos(request):
    #listando apenas um evento
    #evento = Evento.objects.get(id=1)
    # listando todos
    evento = Evento.objects.all()
    #listando tudo por usuario
    #usuario = request.user
    #evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)