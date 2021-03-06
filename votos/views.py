# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Count

# Create your views here.
from votos.models import *


def resultado_global(request):
    """
    Generar la vista para devolver el resultado global de la elección.
    Tener en cuenta que tiene que tener:
    Cantidad total de votos por candidato
    Cantidad total de votos nulos
    Porcentaje de cada candidato
    Porcentaje de votos nulos
    Total de votos de la elección
    """
    #TODO TU CODIGO AQUI
    distrito = Distrito.objects.all()
    candidato = Candidato.objects.all()
    return render(request,'global.html', {'distrito' : distrito}, {'candidato' : candidato})


def resultado_distrital(request, id):
    """
    Generar la vista para devolver el resultado distrital de la elección
    Tener en cuenta que tiene que tener:
    Tamaño del padrón
    Porcentaje de votos del distrito (respecto al padron. Ejemplo: Si el distrito tiene 1000 votantes y hay 750 votos, el porcentaje es 75%)
    Total de votos del distrito
    Candidato ganador
    """
    #TODO TU CODIGO AQUI
    distrito = Distrito.objects.all()
    post = Distrito.objects.get(id=id)
    candidato = Candidato.objects.filter(distritro=post)
    return render(request, 'distrital.html', {'distrito' : distrito}, {'post' : post}, {'candidato' : candidato})
