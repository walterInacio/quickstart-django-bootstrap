from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from .models import Esportes
from .forms import EsporteForm


def index(request):
    esportes = Esportes.objects.all()
    return render(request, 'index.html', {'esportes': esportes})

def novoEsporte(request):
    if request.method == 'POST':
        form = EsporteForm(request.POST)

        if form.is_valid():
            esporte = form.save(commit=False)
            esporte.save()
            return redirect('/')

    form = EsporteForm()
    return render(request, 'new-esporte.html', {'form': form})

def editEsporte(request, id):
    esporte = get_object_or_404(Esportes, pk=id)
    form = EsporteForm(instance=esporte)

    if(request.method == 'POST'):
        form = EsporteForm(request.POST, instance=esporte)

        if(form.is_valid()):
            esporte.save()
            return redirect('/')
        else:
            return render(reuquest, 'edit-esporte.html', {'form': form, 'esporte': esporte})
    else:
        return render(request, 'edit-esporte.html', {'form': form, 'esporte': esporte})

def deleteEsporte(request, id):
    esporte = get_object_or_404(Esportes, pk=id)
    esporte.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')

    return redirect('/')
