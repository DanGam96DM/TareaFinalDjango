from django.shortcuts import render
from django.contrib import messages
from .forms import EventoForm
from eventos.models import Evento, Inscripcion
# Create your views here.
def evento_nuevo(request):
    if request.method == "POST":
        formulario = EventoForm(request.POST)
        if formulario.is_valid():
            evento = Evento.objects.create(nombre=formulario.cleaned_data['nombre'], descripcion=formulario.cleaned_data['descripcion'], fecha=formulario.cleaned_data['fecha'])
            for persona_id in request.POST.getlist('personas'):
                inscripcion = Inscripcion(persona_id=persona_id, evento_id = evento.id)
                inscripcion.save()
            messages.add_message(request, messages.SUCCESS, 'Evento guardado exitosamente')
    else:
        formulario = EventoForm()
    return render(request, 'eventos/evento_nuevo.html', {'formulario': formulario})
